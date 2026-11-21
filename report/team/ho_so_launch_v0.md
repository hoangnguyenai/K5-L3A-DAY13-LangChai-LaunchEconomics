# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: LangChai · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ toàn mẫu. Trong phạm vi pilot, gồm cố định: 4.599,09 đ ở 45.000 yêu cầu/tháng và 5.784,27 đ ở 22.500 (simulated). [A2/A4](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi số ca làm lại +51,77%, gấp đôi xem lại +40,70%, lương tăng 25% làm chi phí tăng 23,12% (simulated). [B1/B2](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 5.751,02 đ/yêu cầu với giới hạn 2 lần (toàn mẫu, chi phí hệ thống biến đổi) so với 12.000 đ tự làm. Pilot chọn `noi_dia` và `hang_nang`; `quoc_te` và `doi_tac` lần lượt đạt 1,876× và 0,851× mốc tự làm (simulated), với điều khoản riêng ở `doi_tac`. [A3/B3](bang_chi_phi.md) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Quan sát trên dữ liệu giả lập: 82,83% đóng đúng hạn và không mở lại, 27,12% sửa/bỏ sau khi xem lại, 4,25% mở lại trong 7 ngày. [E1](chi_so.md) | Xong, có bằng chứng | Người giữ hồ sơ (TV3) |
| 5 · Bảng lỗi và cách khắc phục | Đối chiếu TV2–TV3 trùng 18/20 ca. Có 5 phương án khắc phục. [C](bang_loi.md) | Chưa | Người gắn nhãn 2 (TV3) |
| 6 · Pilot plan | Phân tầng theo depot, 20 nhân viên mỗi nhóm, mục tiêu 299 yêu cầu/người và 859 hiệu dụng mỗi nhóm. Thiết kế cho mức chênh 6 điểm; ở 5 điểm, power khoảng 64%. [D](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% có thể tốn 12.414,50 đ/việc, vượt 12.000 đ; làm lại gấp đôi làm chi phí tăng 51,77% (simulated). [E2](chi_so.md) | Giả lập | Trưởng nhóm CSKH |

Điều kiện trước khi mở pilot:

- **27/11/2026** — PM trợ lý hoàn phí kiểm đủ hai bộ nhãn cho 20 ca và 5 phương án khắc phục. Kỹ sư trưởng agent kiểm thử gửi lại yêu cầu, với ngưỡng 0 giao dịch hoàn trùng và 0 thông báo thành công thiếu bản ghi sổ cái.
- **27/11/2026** — Giám đốc vận hành kiểm lưu lượng đủ điều kiện theo nhân viên. Mục tiêu 5.980 yêu cầu thô mỗi nhóm trong 14 ngày, khoảng 427 yêu cầu/ngày/nhóm. Duyệt phân nhóm 20/20 và mức chênh thiết kế 6 điểm.
- **30/11/2026** — Trưởng nhóm CSKH kiểm event kết quả ở cả hai nhóm và bật đo phút thực tế. Chỉ giảm mức xem lại theo bậc khi đạt ngưỡng an toàn trong kế hoạch pilot. Ngưỡng hòa vốn B4 là 4,80 phút xem lại ở kịch bản 15,3 phút làm lại (simulated).

**Đề xuất Gate 2a:** Go có điều kiện cho pilot `noi_dia` và `hang_nang`.
