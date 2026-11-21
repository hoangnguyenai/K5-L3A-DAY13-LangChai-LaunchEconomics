"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py (cần pandas và statsmodels). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import sys
from math import ceil, sqrt
from pathlib import Path
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    if k is None:
        return 1 / p
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT (1,20 · 1,25 · 1,25)')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(
    runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
    he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None,
):
    """Tính chi phí cho tập yêu cầu đang xét."""
    if reqs.empty:
        raise ValueError("Tập yêu cầu rỗng")

    runs = runs.loc[runs["request_id"].isin(reqs["request_id"])]
    if max_lan_chay is not None:
        runs = runs.loc[runs["attempt"] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs["so_lan_chay"] > max_lan_chay
        reqs.loc[vuot_gioi_han, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[
            vuot_gioi_han, ["phut_xem_lai_simulated", "phut_lam_lai_simulated"]
        ] = 0

    tien_token = (runs["tokens_in"] * gia_vao + runs["tokens_out"] * gia_ra) / 1000
    tien_tool = runs["tool_calls"] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    chay_lai = (tien_token + tien_tool).loc[runs["attempt"] > 1].sum()
    xem_lai = reqs["phut_xem_lai_simulated"].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs["phut_lam_lai_simulated"].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int(reqs["ket_qua"].eq("thanh_cong").sum())

    return {
        "token": token,
        "tool": tool,
        "chay_lai": chay_lai,
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": tong / thanh_cong if thanh_cong else float("inf"),
        "hoa_don_moi_yc": (token + tool) / len(reqs),
    }


def co_mau(p1, p2, alpha=0.05, power=0.8):
    normal = NormalDist()
    za = normal.inv_cdf(1 - alpha / 2)
    zb = normal.inv_cdf(power)
    p_gop = (p1 + p2) / 2
    sai_so_gop = sqrt(2 * p_gop * (1 - p_gop))
    sai_so_rieng = sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return ceil(((za * sai_so_gop + zb * sai_so_rieng) / (p2 - p1)) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def in_co_mau():
    print("\nD1 - Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,80; ICC 0,02)")
    p1, p2_5, p2_6 = 0.70, 0.75, 0.76
    alpha, power, icc = 0.05, 0.80, 0.02

    # a) Chia theo yêu cầu
    n_yc_5 = co_mau(p1, p2_5, alpha, power)
    print(f"a) Chia theo yêu cầu (+5 điểm): {n_yc_5:,} yêu cầu/nhóm")

    # b) Theo nhân viên, m = 75
    m_b = 75
    de_b = he_so_thiet_ke(m_b, icc)
    n_nv_b = ceil(n_yc_5 * de_b)
    so_nv_moi_nhom_b = ceil(n_nv_b / m_b)
    print(
        f"b) Theo nhân viên (m={m_b}): DE = {de_b:.2f} | "
        f"{n_nv_b:,} yêu cầu/nhóm → {so_nv_moi_nhom_b} NV/nhóm "
        f"(tổng {so_nv_moi_nhom_b * 2} > 40 NV: không đủ người)"
    )

    # c) 20 nhân viên mỗi nhóm
    c_nv = 20
    tran_nv = c_nv / icc
    print(
        f"c) {c_nv} nhân viên/nhóm: n_hiệu_dụng < c/ICC = {tran_nv:,.0f} "
        f"< {n_yc_5:,} (không đạt cho +5 điểm)"
    )

    # d) 6 depot mỗi nhóm
    c_depot = 6
    tran_depot = c_depot / icc
    print(
        f"d) {c_depot} depot/nhóm: n_hiệu_dụng < c/ICC = {tran_depot:,.0f} "
        f"< {n_yc_5:,} (không đạt)"
    )

    # e) Mức chênh 6 điểm, 20 nhân viên mỗi nhóm
    n_yc_6 = co_mau(p1, p2_6, alpha, power)
    # Giải c_nv * m / (1 + (m - 1) * icc) >= n_yc_6
    m_min_6 = ceil((n_yc_6 * (1 - icc)) / (c_nv - n_yc_6 * icc))
    de_6 = he_so_thiet_ke(m_min_6, icc)
    n_hieu_dung_6 = (c_nv * m_min_6) / de_6
    es_5 = proportion_effectsize(p2_5, p1)
    power_5_tai_n6 = NormalIndPower().power(
        effect_size=es_5, nobs1=n_yc_6, alpha=alpha, ratio=1.0
    )
    print(
        f"e) Mức chênh +6 điểm ({n_yc_6:,}/nhóm), {c_nv} NV/nhóm: "
        f"m >= {m_min_6} yêu cầu/NV | DE = {de_6:.2f} | "
        f"n_hiệu_dụng = {n_hieu_dung_6:,.1f} | "
        f"power nếu tác động thật +5 điểm ≈ {power_5_tai_n6:.2f}"
    )


def in_mo_lai(reqs, reqs_pilot):
    # Tỉ lệ mở lại 7 ngày hiện tại (đầu vào cho luật dừng an toàn ở D3)
    ti_le_mo_lai_all = reqs["mo_lai_trong_7_ngay"].mean()
    so_mo_lai_all = int(reqs["mo_lai_trong_7_ngay"].sum())
    ti_le_mo_lai_pilot = reqs_pilot["mo_lai_trong_7_ngay"].mean()
    so_mo_lai_pilot = int(reqs_pilot["mo_lai_trong_7_ngay"].sum())
    print(
        f"\nD3 - Tỉ lệ mở lại 7 ngày hiện tại: "
        f"toàn mẫu {so_mo_lai_all}/{len(reqs)} ({ti_le_mo_lai_all:.2%}) | "
        f"phạm vi pilot (noi_dia + hang_nang) {so_mo_lai_pilot}/{len(reqs_pilot)} ({ti_le_mo_lai_pilot:.2%})"
    )


def co_mau_hieu_dung(so_yeu_cau, icc):
    tong = sum(so_yeu_cau)
    if tong == 0:
        return 0.0
    de = 1 + icc * (sum(so_ca ** 2 for so_ca in so_yeu_cau) / tong - 1)
    return tong / de


def in_du_bao_luu_luong(reqs, reqs_pilot):
    so_ca = reqs_pilot.groupby("staff_id")["request_id"].nunique()
    ty_trong = so_ca / so_ca.sum()
    icc, n_muc_tieu, so_ngay = 0.02, co_mau(0.70, 0.76), 14
    luu_luong_ngay = 1500 * len(reqs_pilot) / len(reqs) / 2
    bien = 1 - n_muc_tieu * icc * (ty_trong ** 2).sum()
    if bien <= 0:
        print("D2: Cơ cấu cụm trong mẫu có trần hiệu dụng dưới hoặc bằng mục tiêu.")
        return
    tong_can = ceil(n_muc_tieu * (1 - icc) / bien)
    print("\nD2 - Kịch bản lưu lượng theo phân bố nhân viên trong mẫu giả lập")
    print(f"Mẫu: {so_ca.sum()} ca đủ điều kiện, {len(so_ca)} nhân viên, "
          f"min/trung vị/max = {so_ca.min()}/{so_ca.median():g}/{so_ca.max()}")
    for ty_le_tiep_can in (1.0, 0.7):
        du_bao_ngay = luu_luong_ngay * ty_le_tiep_can
        du_bao = ty_trong * du_bao_ngay * so_ngay
        print(f"{ty_le_tiep_can:.0%} lưu lượng: {du_bao.sum():,.2f} ca thô/nhóm, "
              f"{co_mau_hieu_dung(du_bao, icc):,.2f} ca hiệu dụng/nhóm; "
              f"cần ít nhất {ceil(tong_can / du_bao_ngay)} ngày ở cùng tốc độ")
    print(f"Với phân bố mẫu: 5.980 ca thô cho {co_mau_hieu_dung(ty_trong * 5980, icc):.2f} ca hiệu dụng; "
          f"cần {tong_can:,} ca thô để đạt {n_muc_tieu} hiệu dụng mỗi nhóm")


def main():
    src = Path(__file__).parent
    runs = pd.read_csv(src / 'logix_runs.csv')
    reqs = pd.read_csv(src / 'logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('A2 - Chi phí có phút nhân viên mang nhãn simulated')
    for ten, gia_tri in ket_qua.items():
        if ten == 'thanh_cong':
            print(f'{ten:16s} {gia_tri:>14,d}')
        else:
            print(f'{ten:16s} {gia_tri:>14,.2f}')
    print("\nA3 - Theo loại yêu cầu")
    for loai, reqs_loai in reqs.groupby("loai", sort=False):
        kq = mo_hinh(runs, reqs_loai)
        ti_le = kq["thanh_cong"] / len(reqs_loai)
        lan_chay_tb = reqs_loai["so_lan_chay"].mean()
        print(
            f"{loai}: {len(reqs_loai)} yêu cầu | thành công {ti_le:.2%} | "
            f"{lan_chay_tb:.2f} lần/yêu cầu | "
            f"CPS {kq['cps']:,.2f} đ | {kq['cps'] / BASELINE:.3f}×"
        )

    quoc_te_ids = reqs.loc[reqs["loai"].eq("quoc_te"), "request_id"]
    runs_quoc_te = runs.loc[runs["request_id"].isin(quoc_te_ids)]
    for attempt, nhom in runs_quoc_te.groupby("attempt"):
        so_ok = nhom["status"].eq("ok").sum()
        print(f"quoc_te lần {attempt}: {so_ok}/{len(nhom)} ok ({so_ok / len(nhom):.2%})")

    print("\nA4 - Phạm vi noi_dia + hang_nang")
    reqs_pilot = reqs.loc[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    pilot = mo_hinh(runs, reqs_pilot)
    ti_le_viec_pilot_thanh_cong = pilot["thanh_cong"] / len(reqs)
    print(f"Mẫu pilot: {pilot['thanh_cong']}/{len(reqs_pilot)} thành công")
    print(f"CPS biến đổi: {pilot['cps']:,.2f} đ")

    for luu_luong in (45_000, 22_500):
        thanh_cong_thang = luu_luong * ti_le_viec_pilot_thanh_cong
        co_dinh_moi_viec = 40_000_000 / thanh_cong_thang
        cps_ca_co_dinh = pilot["cps"] + co_dinh_moi_viec
        print(
            f"{luu_luong:,} yêu cầu/tháng | {thanh_cong_thang:,.0f} việc thành công | "
            f"cố định {co_dinh_moi_viec:,.2f} đ/việc | "
            f"CPS {cps_ca_co_dinh:,.2f} đ | {cps_ca_co_dinh / BASELINE:.3f}×"
        )
    print("\nB1 - Đổi từng yếu tố")
    cps_goc = ket_qua["cps"]
    kich_ban = [
        ("Giá token ×2", {"gia_vao": 52, "gia_ra": 260}),
        ("Giá token ×0,5", {"gia_vao": 13, "gia_ra": 65}),
        ("Xem lại ×2", {"he_so_xem_lai": 2}),
        ("Xem lại ×0,5", {"he_so_xem_lai": 0.5}),
        ("Làm lại ×2", {"he_so_lam_lai": 2}),
        ("Làm lại ×0,5", {"he_so_lam_lai": 0.5}),
        ("Lương tăng 25%", {"luong_phut": 2500}),
        ("Tối đa 2 lượt", {"max_lan_chay": 2}),
        ("Tối đa 1 lượt", {"max_lan_chay": 1}),
    ]
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        print(f"{ten}: CPS {cps:,.2f} đ | {(cps / cps_goc - 1):+.2%}")

    print("\nB2 - Đổi đồng thời token và xem lại")
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)["cps"]
    print(f"CPS {cps_cap:,.2f} đ | {(cps_cap / cps_goc - 1):+.2%}")

    print("\nB3 - Tổng chi phí hệ thống")
    for gioi_han in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq["thanh_cong"]
        tong_he_thong = kq["tong"] + BASELINE * khong_thanh_cong
        print(
            f"{gioi_han} lượt | trợ lý {kq['tong']:,.2f} đ | "
            f"{khong_thanh_cong} yêu cầu không thành công | "
            f"hệ thống {tong_he_thong:,.2f} đ | CPS {kq['cps']:,.2f} đ | "
            f"{tong_he_thong / len(reqs):,.2f} đ/yêu cầu"
        )

    print("\nB4 - Xem lại 100% trong phạm vi pilot")
    runs_pilot = runs.loc[runs["request_id"].isin(reqs_pilot["request_id"])]
    so_ca_xem_lai = runs_pilot.loc[runs_pilot["status"].eq("ok"), "request_id"].nunique()
    so_ca_lam_lai = reqs_pilot["ket_qua"].eq("lam_lai").sum()
    phut_lam_lai_tb = reqs.loc[
        reqs["ket_qua"].eq("lam_lai"), "phut_lam_lai_simulated"
    ].mean()
    tien_xem_lai = so_ca_xem_lai * 5 * LUONG_PHUT
    print(f"{so_ca_xem_lai} ca xem lại | {so_ca_lam_lai} ca làm lại")

    for phut_lam_lai in (9, phut_lam_lai_tb):
        tien_lam_lai = so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = pilot["token"] + pilot["tool"] + tien_xem_lai + tien_lam_lai
        cps = tong / pilot["thanh_cong"]
        tien_khac = pilot["token"] + pilot["tool"] + tien_lam_lai
        hoa_von = (BASELINE * pilot["thanh_cong"] - tien_khac) / (so_ca_xem_lai * LUONG_PHUT)
        print(f"{phut_lam_lai:.2f} phút làm lại/ca | CPS {cps:,.2f} đ | {cps / BASELINE:.3f}× | "
              f"hòa vốn {hoa_von:.2f} phút xem lại")

    in_co_mau()
    in_du_bao_luu_luong(reqs, reqs_pilot)
    in_mo_lai(reqs, reqs_pilot)

    xem_lai = reqs.loc[reqs["duoc_xem_lai"].eq(1)]
    chinh = (reqs["dong_trong_24h"].eq(1) & reqs["mo_lai_trong_7_ngay"].eq(0)).sum()
    bo_qua = xem_lai["quyet_dinh_xem_lai"].isin(["sua", "bo"]).sum()
    print(f"E1 chinh={chinh}/{len(reqs)}, bo_qua={bo_qua}/{len(xem_lai)}, "
          f"mo_lai={reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)}, "
          f"mo_lai_pilot={reqs_pilot['mo_lai_trong_7_ngay'].sum()}/{len(reqs_pilot)}")


if __name__ == "__main__":
    if not sys.stdout.isatty():
        sys.stdout.reconfigure(encoding="utf-8")
    main()
