# Báo cáo nhóm

## 1. Thông tin nhóm

- Nhóm LangChai, lớp L3A theo tên repo.
- Vai trò và đóng góp xem trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí xử lý yêu cầu hoàn phí của trợ lý LogiX-VN và chuẩn bị kế hoạch pilot có đối chứng. Nhóm dùng 1.200 yêu cầu và 1.624 lần chạy giả lập để mô tả kết quả chạy thử và xây dựng tiêu chí cho quyết định Gate 2a.

## 3. Giải pháp

- **A–B.** Chi phí mỗi việc thành công là 4.471,97 đ (simulated). Giới hạn 2 lần có chi phí hệ thống biến đổi thấp nhất ở 5.751,02 đ/yêu cầu (simulated). [Bảng chi phí](bang_chi_phi.md)
- **C.** Đối chiếu TV2–TV3 trùng 18/20 ca trước khi thống nhất. Nhóm chốt ca 3 là Ngữ cảnh và ca 8 là Hệ thống. Bảng có 5 phương án khắc phục. [Bảng lỗi](bang_loi.md)
- **D.** Đề xuất chia 20 nhân viên mỗi nhóm, mục tiêu 299 yêu cầu/người để đạt 859 yêu cầu hiệu dụng mỗi nhóm và phát hiện chênh lệch 6 điểm. [Kế hoạch pilot](pilot_plan.yaml)
- **E.** Ba chỉ số tính thử, hai chỉ số đề xuất, 12 event và hai rủi ro kinh tế định lượng. [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md)

## 4. Kết quả

Trong đợt chạy thử giả lập, 994/1.200 yêu cầu (82,83%) đóng trong 24 giờ và không mở lại trong 7 ngày, 48/177 yêu cầu được xem lại (27,12%) bị sửa hoặc bỏ gợi ý, và 51/1.200 yêu cầu (4,25%) mở lại trong 7 ngày. [Công thức và mẫu số](chi_so.md)

Đề xuất Gate 2a là **Go có điều kiện** cho nội địa và hàng nặng. [Hồ sơ launch](ho_so_launch_v0.md)

**Phản hồi từ ABCD.** C8 được **5/10**. Hội đồng ghi nhận đối chứng đồng thời, 20 nhân viên mỗi nhóm và 4 luật dừng. Điểm còn thiếu là lưu lượng đủ điều kiện theo từng nhân viên để xác minh cỡ mẫu hiệu dụng trong 14 ngày. [Phiếu ABCD chấm LangChai](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/31d14c2fcd2491cbc88436ff429fe57469ceedd5/report/team/phieu_cham.md)

## 5. Khó khăn và cách xử lý

Nếu phải xem lại 100% gợi ý, chi phí có thể tăng tới 12.414,50 đ/việc thành công (simulated). Pilot đo phút xem lại và làm lại từ tuần đầu, đồng thời theo dõi mở lại và đối soát hoàn phí. [Kịch bản B4](bang_chi_phi.md#b4--nếu-phải-xem-lại-tất-cả)

Trong mẫu giả lập, 20 nhân viên có từ **39 đến 73** yêu cầu đủ điều kiện. Nếu giữ độ lệch lưu lượng này, **5.980** yêu cầu thô chỉ tương đương **843** hiệu dụng. Mô hình dự phóng cần khoảng **6.900** yêu cầu thô/nhóm để đạt **859** hiệu dụng. Giám đốc vận hành áp dụng điều kiện mở kỳ đo dựa trên lưu lượng của danh sách nhân viên thực tế. [Kế hoạch pilot](pilot_plan.yaml)

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Kết quả chạy thử thiếu nhóm đối chứng. Khi có pilot, cần ghi event giống nhau ở hai nhóm cho các chỉ số kết quả, chờ đủ cửa sổ theo dõi 7 ngày và dùng audit mẫu để phát hiện sai số tiền hoàn.

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../README.md)
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- [Hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
