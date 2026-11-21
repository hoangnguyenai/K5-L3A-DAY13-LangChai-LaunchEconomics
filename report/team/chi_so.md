# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Tỉ lệ yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng số yêu cầu | 994 / 1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | (41 sửa + 7 bỏ) / 177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm tín hiệu lỗi lọt đến khách | Đếm yêu cầu có `mo_lai_trong_7_ngay = 1`, chia tổng số yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng | Tỉ lệ yêu cầu được mở bằng trợ lý | Số yêu cầu đủ điều kiện thuộc nhóm can thiệp có ít nhất một lần nhân viên mở trợ lý, chia tổng số yêu cầu đủ điều kiện đã phân vào nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số yêu cầu hoàn phí đã kiểm tra có số tiền thực hoàn khác số tiền đúng theo chính sách, chia tổng số yêu cầu hoàn phí đã kiểm tra | Không cần tính |

Ba tỉ lệ trên mô tả đợt chạy thử giả lập 1.200 yêu cầu. Đợt chạy thử thiếu đối chứng. Baseline 70% là giả định riêng của nhiệm vụ D để tính cỡ mẫu. Trong hai loại `noi_dia` và `hang_nang`, tỉ lệ mở lại quan sát được là 39 / 982 = **3,97%** để TV2 tham khảo khi đặt ngưỡng.

Đối chiếu trên [CSV yêu cầu](../../src/logix_requests.csv). Mỗi hàng là một yêu cầu. Đếm các hàng thỏa điều kiện trong cột công thức rồi lấy tử số chia mẫu số, nhân 100 và làm tròn hai chữ số thập phân.

## Danh sách event

Mỗi event mang `request_id`, `trace_id` và thời điểm theo UTC. Hệ thống tạo `trace_id` gốc khi nhận yêu cầu, kể cả ở nhóm đối chứng. Agent ghi thêm `run_trace_id` cho từng lần chạy. Với CSV hiện có, dùng `request_id` để nối bảng yêu cầu với các lần chạy.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống yêu cầu hoàn phí | `request_id`, `trace_id`, `created_at`, `loai`, `staff_id`, `arm`, `eligible` | Khi tạo yêu cầu và ghi nhận phân nhóm |
| `refund_input_validated` | Cổng tiếp nhận hoàn phí | `request_id`, `trace_id`, `field`, `valid`, `failure_reason` | Sau mỗi lượt kiểm tra đầu vào |
| `staff_assistant_opened` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `opened_at` | Khi nhân viên mở trợ lý cho yêu cầu |
| `agent_run_completed` | Agent | `request_id`, `trace_id`, `run_trace_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lần chạy, gồm cả lần lỗi |
| `staff_review_decision` | Giao diện CSKH | `request_id`, `trace_id`, `decision` (`giu`, `sua`, `bo`), `review_minutes` | Khi chốt quyết định xem lại |
| `staff_rework_completed` | Giao diện CSKH | `request_id`, `trace_id`, `reason`, `rework_minutes` | Khi nhân viên xử lý lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id`, `idempotency_key`, `refund_vnd`, `status` | Sau mỗi lần ghi sổ, kể cả lỗi |
| `refund_status_notified` | Dịch vụ thông báo | `request_id`, `trace_id`, `status`, `sent_at` | Khi gửi trạng thái hoàn tiền cho khách |
| `handoff_to_staff` | Hệ thống định tuyến | `request_id`, `trace_id`, `reason`, `missing_fields` | Khi chuyển yêu cầu cho CSKH |
| `ticket_closed` | Hệ thống ticket | `request_id`, `trace_id`, `closed_at` | Khi ticket chuyển sang đã đóng |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `trace_id`, `reopened_at`, `reason` | Khi ticket mở lại |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `trace_id`, `checked_at`, `actual_refund_vnd`, `expected_refund_vnd`, `policy_version`, `applied_rate_version`, `expected_rate_version` | Khi hoàn tất kiểm tra mẫu hằng tuần |

### Event dùng để tính từng chỉ số

- **Chính** dùng `refund_request_created`, `ticket_closed` và `ticket_reopened`. Từ lần đóng đầu, kiểm thời gian từ lúc tạo đến lúc đóng ≤ 24 giờ và có lượt mở lại trong 7 ngày sau đóng hay không. Chốt mẫu sau khi hết cửa sổ theo dõi.
- **Bỏ qua gợi ý** dùng `staff_review_decision`. Mỗi yêu cầu đã xem lại tính một lần theo quyết định chốt.
- **Mở lại trong 7 ngày** dùng `refund_request_created`, `ticket_closed` và `ticket_reopened`. Đếm yêu cầu có ít nhất một lần mở lại trong 7 ngày sau lần đóng đầu, chia tổng số yêu cầu trong đoàn hệ đã theo dõi đủ.
- **Mở trợ lý** dùng `refund_request_created` để lấy mẫu số theo `eligible` và `arm`, rồi nối `staff_assistant_opened` theo `request_id`. Một yêu cầu có ít nhất một lượt mở được tính một lần.
- **Hoàn sai tiền** dùng `audit_sample_checked`. Đếm mỗi yêu cầu đã kiểm tra một lần, dùng kết quả kiểm tra chốt để so hai trường số tiền.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | B1: gấp đôi số ca làm lại tăng chi phí mỗi việc thành công 51,77%, lên 6.786,90 đ (simulated). | Tỉ lệ làm lại > 7% trong một tuần. Mẫu trong phạm vi có 48/982 = 4,89%. | Rà 20 trace làm lại hoặc toàn bộ nếu ít hơn. Áp dụng luật thu hẹp trong YAML khi chạm ngưỡng chi phí. | PM trợ lý hoàn phí |
| Duy trì xem lại 100% yêu cầu có gợi ý | B4: 11.742,79 đ/việc nếu làm lại 9 phút/ca và 12.414,50 đ nếu 15,3 phút/ca, với 5 phút xem lại (simulated). | Tỉ lệ yêu cầu có gợi ý được xem lại và số phút mỗi lượt, qua lần chạy thành công và `staff_review_decision`. Theo dõi mốc 4,80 phút xem lại (simulated). | Đo phút thực tế từ tuần đầu. Thử giảm từng bậc xem lại khi chỉ số mở lại và đối soát sổ cái đạt ngưỡng. | Trưởng nhóm CSKH |
