# Báo cáo cá nhân — Nguyễn Lâm Hoàng · 2A202603448

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lâm Hoàng
- MSSV: 2A202603448
- Email: 26ai.hoangnl@vinuni.edu.vn
- Nhóm: LangChai · Lớp L3A
- Vai trò: TV3, người gắn nhãn 2 kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

Phụ trách bảng lỗi ở CP3, đặc tả chỉ số và event E1, tổng hợp hồ sơ launch E3 và báo cáo nhóm. Khi duyệt chéo Gate 2a, TV3 trình bày đề xuất và các chỉ số, chấm tiêu chí C7 về nhãn giả lập và phạm vi, rồi tổng hợp phiếu chấm.

## 3. Đóng góp cụ thể

- **Bảng lỗi (CP3).** Đối chiếu 20 ca cho thấy hai cột TV2 và TV3 trùng 18/20. Nhóm thống nhất ca 3 là Ngữ cảnh và ca 8 là Hệ thống. Bảng có 5 phương án khắc phục với tín hiệu phát hiện và vai trò phụ trách. Ca 7 dùng đối soát thông báo với sổ cái theo `request_id`, cảnh báo từ 1 thông báo báo hoàn thành nhưng thiếu giao dịch thành công. Ca 17 dùng kiểm tra mẫu tối đa 100 yêu cầu hoàn phí mỗi tuần để phát hiện trường hợp dùng bảng giá cũ. [Bảng lỗi](bang_loi.md)
- **Chỉ số và event (E1).** Trong 1.200 yêu cầu giả lập, 994 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (**82,83%**), 48/177 yêu cầu được xem lại bị sửa hoặc bỏ gợi ý (**27,12%**), và 51 yêu cầu mở lại trong 7 ngày (**4,25%**). Hai chỉ số bổ sung đo mức mở trợ lý và tỷ lệ hoàn sai tiền qua kiểm tra mẫu. Đặc tả gồm 12 event có `trace_id` và chỉ rõ event dùng để tính từng chỉ số. [Chỉ số](chi_so.md)
- **Hồ sơ launch (E3).** Hồ sơ một trang đề xuất **Go có điều kiện** cho nội địa và hàng nặng. Với mức xem lại 100%, chi phí có thể lên **12.414,50 đ/việc thành công** (`simulated`), vượt mốc 12.000 đ. Điều kiện mở pilot gồm kiểm thử chống hoàn trùng, kiểm tra lưu lượng cho 20 nhân viên mỗi nhóm và đo thời gian xem lại thực tế. [Hồ sơ launch](ho_so_launch_v0.md)
- **Duyệt chéo (C7).** Bản chấm thử xem xét nhãn `simulated` và lý do chọn phạm vi. Chi phí mỗi việc thành công của nội địa và hàng nặng lần lượt bằng **0,225×** và **0,685×** mốc tự làm, trong khi quốc tế ở **1,876×** (`simulated`). [Phiếu chấm](phieu_cham.md)

## 4. Bằng chứng

- [Kết quả A1–A4, B1–B4 và kiểm tay A2]a (bang_chi_phi.md)
- [Kế hoạch pilot, cỡ mẫu và luật dừng](pilot_plan.yaml)
- [Báo cáo nhóm](group_report.md)
- Lệnh `python lab13.py` chạy đến E1. Ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. [Mã nguồn](../../src/lab13.py)

## 5. Công cụ AI đã dùng

Trợ lý AI được dùng để rà công thức chỉ số và soát sự nhất quán giữa các bảng. Bằng chứng kiểm tra là kết quả chạy `lab13.py` và ba phân số E1 đối chiếu với [CSV yêu cầu](../../src/logix_requests.csv).

## 6. Tự đánh giá

Ba chỉ số E1 có mẫu số cụ thể và có thể tính lại từ dữ liệu. Giới hạn lớn nhất là đợt chạy thử thiếu đối chứng, nên tỷ lệ **82,83%** chỉ mô tả mẫu quan sát. Trong pilot, tỷ lệ mở lại là một tín hiệu an toàn. Kiểm tra mẫu số tiền hoàn giúp phát hiện lỗi khách chưbáo.
