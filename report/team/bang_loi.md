# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu bộ nhãn TV2 và TV3

**TV3 · Nguyễn Lâm Hoàng (2A202603448)**

Nhãn TV2 lấy từ cột “Nhãn TV2 chốt” trong [bảng TV2](tv2_nhan_AI_claude.md). Khi tính độ trùng, các nhận xét sau tên loại lỗi được bỏ qua. Nhãn TV3 theo [hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca); căn cứ theo từng mô tả trong [đề bài gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx).

| Ca | Căn cứ | Nhãn TV2 | Nhãn TV3 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Số tài khoản khách nhập thiếu hai chữ số. | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Trợ lý gửi tham số hàng thường cho kiện 28 kg và hoàn thiếu 45.000 đ. | Hệ thống, tool trả về sai | Hệ thống | Có | Hệ thống |
| 3 | Tiền về ví đúng thiết kế, trong khi khách chờ tiền vào tài khoản ngân hàng. | Hệ thống, tiền về đâu phải nói rõ | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | LogiX thiếu dữ liệu chặng do hãng nước ngoài giao. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Kiểm tra mẫu mới phát hiện 14 đơn được hoàn theo giá trước giảm. | Ngầm | Ngầm | Có | Ngầm |
| 6 | Khách chọn nhóm giao trễ cho vấn đề hàng bị vỡ. | Do người dùng nhập sai mục | Do người dùng | Có | Do người dùng |
| 7 | Trợ lý báo hoàn tất dù dịch vụ sổ cái trả 503. | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Trợ lý viện dẫn một điều khoản không có trong chính sách hiện hành. | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Khách nhập mã đơn của sàn vào trường mã vận đơn. | Do người dùng, mã đơn và mã vận đơn là trách nhiệm của người dùng khi họ đặt hàng. | Do người dùng | Có | Do người dùng |
| 10 | Từ chối đúng điều khoản bất khả kháng, trong khi ứng dụng vẫn hiển thị cam kết 24 giờ. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Trợ lý thiếu khả năng xử lý tin nhắn thoại. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Kết quả vẫn đúng nhưng chi phí token của depot tăng gấp 3 lần trong 3 tuần mà không có cảnh báo. | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hoàn phí sản phẩm bảo hiểm của đối tác nằm ngoài phạm vi xử lý. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Khách bấm xác nhận đã nhận tiền trước khi tiền về. | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Trợ lý áp dụng mức hoàn 100% thay cho 50%. Nhân viên phát hiện trước khi gửi. | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Gửi ngay đúng thiết kế nhưng thông báo đến lúc 2:14 sáng. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Bảng giá cũ làm sai tiền của 212 đơn trong 9 ngày mà không có yêu cầu mở lại. | Ngầm | Ngầm | Có | Ngầm |
| 18 | Mức hoàn đúng nhưng thông báo thiếu cách tính khiến khách hiểu là hoàn thiếu. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Đơn 14 tháng vượt cửa sổ truy cập dữ liệu 12 tháng. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Yêu cầu gửi lại phát sinh lần hoàn thứ hai vì thiếu khóa chống trùng. | Hệ thống | Hệ thống | Có | Hệ thống |

**Kết quả đối chiếu TV2–TV3:** Trùng **18/20 ca (90%)**. Hai ca khác nhãn là **ca 3 và ca 8**.

## Hai ca khác nhãn

- **Ca 3 · thống nhất Ngữ cảnh:** Hoàn tiền về ví là hành vi đúng thiết kế. Khách kỳ vọng tiền về tài khoản ngân hàng. Thông báo rõ nơi nhận tiền là biện pháp khắc phục.
- **Ca 8 · thống nhất Hệ thống:** Viện dẫn điều khoản không tồn tại là sai chính sách và nội dung sai xuất hiện trực tiếp trong câu trả lời. Lỗi ngầm chỉ được phát hiện qua kiểm tra sau đó.

## Quy tắc phân biệt các ca dễ lẫn

- **Ca 6 và 9:** Xét dữ liệu hoặc lựa chọn ban đầu của khách. Việc trợ lý có thể hướng dẫn tốt hơn thuộc phần khắc phục.
- **Ca 8 và 15:** Trích dẫn sai có thể kiểm ngay trên chính sách và mức hoàn sai đã bị nhân viên phát hiện. Cả hai vi phạm hành vi mong đợi của hệ thống.
- **Ca 12 và 17:** Kiểm tra định kỳ mới phát hiện bất thường về chi phí hoặc số tiền hoàn. Các ca này thuộc lỗi ngầm.
- **Ca 13 và 18:** Yêu cầu bảo hiểm ngoài khả năng xử lý của trợ lý. Trong ca 18, trợ lý tính được mức hoàn đúng nhưng thông báo thiếu ngữ cảnh để khách hiểu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Tính tỉ lệ `refund_input_validated` có mã vận đơn không hợp lệ trên tổng lượt kiểm tra mã mỗi ngày. Rà khi vượt 2%. | Nhận biết mã đơn của sàn và tra mã vận đơn tương ứng. Nếu tra thất bại, chỉ rõ nơi lấy đúng mã. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Mỗi giờ đối soát `refund_status_notified` có trạng thái “đã hoàn” với bản ghi sổ cái thành công trước thời điểm thông báo và cùng `request_id`. Cảnh báo từ 1 ca lệch. | Chỉ gửi thông báo thành công sau khi sổ cái xác nhận. Nếu hết số lần thử, báo đang xử lý và chuyển CSKH. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Mỗi tuần rà tối đa 10 event `ticket_reopened` có lý do về số tiền. Mở yêu cầu sửa mẫu thông báo khi phát hiện ít nhất 1 ca đúng số tiền nhưng khách hiểu nhầm. | Hiện phí gốc, tỷ lệ và số tiền hoàn trong tin nhắn, ví dụ 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi `handoff_to_staff` do thiếu dữ liệu chặng quốc tế theo ngày. Cảnh báo nếu có ít nhất 1 yêu cầu `eligible=false` vẫn có `agent_run_completed`. | Kiểm phạm vi trước khi gọi trợ lý và chuyển CSKH kèm dữ liệu còn thiếu. | PM trợ lý hoàn phí |
| 17 | Ngầm | Đối chiếu số tiền và phiên bản bảng giá qua `audit_sample_checked` trên tối đa 100 hoàn phí mỗi tuần. Điều tra từ 1 ca dùng bảng giá cũ. | Làm mới bộ nhớ đệm khi bảng giá có hiệu lực, ghi phiên bản vào trace và đối soát các yêu cầu dùng bản cũ. | Kế toán trưởng |
