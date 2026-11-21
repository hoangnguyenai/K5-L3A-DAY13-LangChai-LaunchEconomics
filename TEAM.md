# Team

## Thông tin nhóm

- Tên nhóm: LangChai
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-LangChai-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- Repo: [LangChai trên GitHub](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics) · Nhánh nộp: main

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Đặng Long Nhật | 2A202603483 | nhatlong12cc@gmail.com | Nhatlong2 | TV1 · Người viết code A–B |
| 2 | Nguyễn Trường Thành | 2A202603512 | 26ai.thanhnt6@vinuni.edu.vn | Thanhnt-da | TV2 · Kiểm số, gắn nhãn 1 và viết code CP4 |
| 3 | Nguyễn Lâm Hoàng | 2A202603448 | 26ai.hoangnl@vinuni.edu.vn | hoangnguyenai | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## Đặng Long Nhật-2A202603483

### Phần việc phụ trách

- TV1 · Viết code và chạy A1–A4 (mô hình chi phí) và B1–B4 (phân tích độ nhạy).
- Soạn phần rủi ro kinh tế E2, bàn giao kết quả và kiểm chéo chi phí theo phân công.

### Đóng góp cụ thể

- Triển khai và chạy `python lab13.py` trong `src/`. Cả ba phép thử A1 đạt và chương trình in đủ kết quả đến B4.
- Hoàn thiện bảng chi phí A/B, gồm 978 việc thành công với CPS 4.471,97 đ (`simulated`). Ở B3, giới hạn 2 lượt có tổng chi phí hệ thống thấp nhất, 6.901.220,23 đ (`simulated`).
- Soạn hai rủi ro E2 về tỷ lệ làm lại và chi phí xem lại để TV3 tích hợp.

### Bằng chứng

- [`ae73c6e`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/ae73c6edfdfd83b9cca6db32a2ea4b82d45dd830) · [Code A/B](src/lab13.py) và [báo cáo cá nhân](report/team/2A202603483_DangLongNhat.md).
- [`3d273f0`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/3d273f0eb1b653c8cde88ae84c3cf954d9c3d152) và [`bcf31f0`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/bcf31f099dce9b2aa44cb5effe273ff94eb605ec) · Kết quả A/B và nhãn `simulated` trong [bảng chi phí](report/team/bang_chi_phi.md).

## Nguyễn Lâm Hoàng-2A202603448

### Phần việc phụ trách

- Tổng hợp nhiệm vụ C, phụ trách E1 và E3, giữ hồ sơ launch và tổng hợp báo cáo nhóm.
- Tích hợp E2 từ TV1 và kết quả pilot từ TV2. Phụ trách C7 khi duyệt chéo và kiểm tra hồ sơ trước khi nộp.

### Đóng góp cụ thể

- Chuẩn bị bảng tính thử E1, đặc tả event và cách đối chiếu từng chỉ số. Chuẩn bị bản hồ sơ launch và báo cáo nhóm theo các bằng chứng hiện có.
- Đặc tả 12 event có trace_id, đối chiếu 20 nhãn với TV2, lập bảng 5 phương án khắc phục và tổng hợp hồ sơ một trang.

### Bằng chứng

- [Đặc tả chỉ số](report/team/chi_so.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md) và [báo cáo cá nhân](report/team/2A202603448_NguyenLamHoang.md).

## Nguyễn Trường Thành-2A202603512

### Phần việc phụ trách

- TV2 · Người kiểm số: kiểm cách đọc CSV (`keep_default_na=False`), tính tay độc lập một kết quả A2 và đối chiếu bảng A/B của TV1.
- Người gắn nhãn 1 ở CP3: gắn nhãn 20 ca lỗi theo nguyên nhân gốc, có AI hỗ trợ (Claude Opus 5.5) và cột lý do AI theo yêu cầu của TA.
- Viết code CP4 sau giờ giải lao: D1 (cỡ mẫu) trong `src/lab13.py` và kế hoạch pilot `report/team/pilot_plan.yaml`; trả lời phần đối chứng, cỡ mẫu và luật dừng khi bảo vệ, chấm C8 khi duyệt chéo.

### Đóng góp cụ thể

- Tính tay A2: tổng 4.373.585 đ / 978 việc thành công = 4.472 đ (`simulated`), lệch 0% so với 4.471,97 đ của TV1; chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× mốc 12.000 đ (`simulated`).
- Gắn đủ 20 nhãn, tự rà từng ca và chốt nhãn; khác gợi ý AI ở ca 3 và ca 8. Đối chiếu với TV3 trùng 18/20 ca.
- Viết D1: chia theo yêu cầu 1.251/nhóm; theo nhân viên m = 75 cần 84 NV > 40; trần 20 NV/nhóm là 1.000 và 6 depot/nhóm là 300; MDE +6 điểm cần 859/nhóm, m ≥ 299 yêu cầu/NV, DE 6,96, power ~0,64 nếu tác động thật +5 điểm. Tính tỉ lệ mở lại 7 ngày 4,25% toàn mẫu, 3,97% trong phạm vi pilot.
- Hoàn thiện `pilot_plan.yaml`: chia theo nhân viên 20 + 20 phân tầng theo depot, phạm vi `noi_dia` + `hang_nang`, đánh đổi MDE +6 điểm, luật dừng an toàn, chi phí và sử dụng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, rollback trong 30 phút.

### Bằng chứng

- [`5c03335`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/5c03335) · Mục "Kiểm tay A2" trong [bảng chi phí](report/team/bang_chi_phi.md).
- [`991df51`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/991df51) · [Bảng nhãn TV2](report/team/tv2_nhan_AI_claude.md) và [prompt cho AI](report/team/tv2_prompt_gan_nhan_AI.md).
- [`ab29e94`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/ab29e94) · Code D1 trong [`src/lab13.py`](src/lab13.py).
- [`cd90764`](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/commit/cd90764) · [Kế hoạch pilot](report/team/pilot_plan.yaml).
- [Báo cáo cá nhân](report/team/2A202603512_NguyenTruongThanh.md).
