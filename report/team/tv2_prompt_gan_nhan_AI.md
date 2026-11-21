Bạn là trợ lý hỗ trợ người gắn nhãn 1 (TV2) trong một bài lab. KHÔNG dùng bất kỳ công cụ nào, KHÔNG đọc file nào. Chỉ suy luận từ nội dung dưới đây.

Nhiệm vụ: gắn mỗi ca trong 20 ca lỗi dưới đây vào đúng MỘT trong năm loại lỗi (theo Google PAIR). Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

Năm loại lỗi:
- Do người dùng: Người dùng nhập sai hoặc chọn sai
- Hệ thống: Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách
- Ngữ cảnh: Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ
- Giới hạn hệ thống: Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được
- Ngầm: Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra

Hai mươi ca lỗi:
1. Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi.
2. Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày.
3. Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn".
4. Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên.
5. Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích.
6. Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn.
7. API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công".
8. Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng.
9. Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì.
10. Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ".
11. Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ".
12. Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy.
13. Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được.
14. Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng.
15. Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi.
16. Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền.
17. Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại.
18. Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu.
19. Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt.
20. Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng.

Trả lời bằng tiếng Việt, đúng một bảng Markdown với các cột:
| Ca | Nhãn | Lý do (một câu, nêu nguyên nhân gốc) | Nhãn thứ hai cân nhắc (nếu có) |

Sau bảng, ghi số ca mỗi loại, và liệt kê các ca bạn thấy khó phân biệt nhất, mỗi ca một câu giải thích vì sao.
