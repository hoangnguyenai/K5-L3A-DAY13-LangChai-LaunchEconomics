# Phân công Lab 13 · LangChai

**Mục tiêu** Hoàn thành hồ sơ launch v0 và bảo vệ kế hoạch pilot trợ lý hoàn phí LogiX-VN tại Gate 2a.

Đây là phương án cho **ba thành viên**. Nhóm ghép vai kiểm số và viết code CP4 cho TV2 để giữ đủ bốn vai trong [TEAM.md](TEAM.md). [Hướng dẫn nộp](SUBMISSION.md) ghi quy mô chuẩn 4 người. Nếu coach chưa xác nhận nhóm 3 người, TV1 phụ trách xác nhận trước khi nộp.

| Thành viên | Vai trò trong lab | Phụ trách chính | Kiểm chéo |
| --- | --- | --- | --- |
| **TV1 · Đặng Long Nhật** | Viết code trước giờ giải lao | A–B, rủi ro kinh tế E2, tích hợp và push | Tính lại một kết quả cỡ mẫu D1, đối chiếu phạm vi và ngưỡng chi phí |
| **TV2 · Điền họ tên trong TEAM.md** | Kiểm số, gắn nhãn 1, viết code sau giờ giải lao | D1–D3, kế hoạch pilot và phần trình bày thiết kế pilot | Tính tay một kết quả A2, kiểm khả năng đo của các chỉ số |
| **TV3 · Nguyễn Lâm Hoàng** | Gắn nhãn 2 kiêm giữ hồ sơ | Tổng hợp C, chỉ số và event E1, hồ sơ E3, báo cáo nhóm | Kiểm nhãn giả lập, chạy lại code và kiểm file YAML trên máy thứ hai |

## Tiến độ và bàn giao

Các giờ dưới đây theo lịch mẫu 14:00–18:00 GMT+7. Nếu coach đổi lịch, nhóm giữ thứ tự checkpoint và dời mốc bàn giao tương ứng.

### 14:00–14:10 · Chuẩn bị

- **TV1** điền thông tin nhóm, thành viên và vai trong `TEAM.md`. Cả nhóm cài Python theo [hướng dẫn chạy lab](src/README.md) và đọc [quy định](RULES.md).
- **TV2** kiểm tra cách đọc CSV, gồm `keep_default_na=False` khi đọc bảng yêu cầu. **TV3** mở các mẫu trong `report/team/` và chuẩn bị bố cục một trang của hồ sơ launch.

### CP1 · 14:10–14:53 · A — Mô hình chi phí

- **TV1** làm A1–A4 trong `src/lab13.py` và điền phần A trong `report/team/bang_chi_phi.md`. Chạy A1 đến khi cả ba phép thử đạt **1,20 · 1,25 · 1,25** rồi tính A2, tách bốn loại yêu cầu ở A3 và cộng chi phí cố định ở hai mức khối lượng trong A4.
- **TV2** tính tay một kết quả A2 và ghi cách tính. Kiểm tử số có chi phí từ mọi lần chạy, kể cả lần lỗi, mẫu số chỉ đếm yêu cầu `thanh_cong`. Đối chiếu với mức tự làm **12.000 đ/yêu cầu**.
- **TV3** chuẩn bị E1 bằng cách xác định công thức, tử số, mẫu số và cột dữ liệu của ba chỉ số. **Bàn giao 14:53** TV1 gửi A2 đủ 9 dòng, A3 đủ 4 loại và so sánh A4 ở hai mức khối lượng. TV3 cập nhật hồ sơ launch theo số đã kiểm.

### CP2 · 14:53–15:20 · B — Độ nhạy

- **TV1** làm B1–B4. B1 đủ 9 kịch bản, B2 có một cặp thay đổi và xếp hạng ba yếu tố nhạy nhất, B3 so giới hạn 1–3 lần theo cả chi phí hệ thống và chi phí mỗi việc thành công. B4 đối chiếu xem lại 100% với mức tự làm theo hai giả định về thời gian làm lại trong hướng dẫn.
- **TV2** kiểm A/B theo rubric và đọc mẫu `pilot_plan.yaml`. **TV3** tính thử ba chỉ số E1 từ CSV và phác danh sách event. Tách tỷ lệ quan sát trong đợt chạy thử khỏi baseline dùng để tính cỡ mẫu.
- **Bàn giao 15:20** TV1 gửi SHA commit có A/B chạy được, phạm vi đề xuất từ A3–A4, kết quả B3 và B4. TV2 tiếp quản `src/lab13.py` sau giải lao. Trong CP3–CP4, TV1 chuyển các sửa đổi code A/B cho TV2 tích hợp để tránh sửa cùng file.

### CP3 · 15:35–16:08 · C — Gắn nhãn lỗi

- **TV2 và TV3** dùng 8 phút để mỗi người gắn đủ 20 ca theo nguyên nhân gốc trong bản riêng. Lấy ca từ mục “Hai mươi ca lỗi” trong [đề bài gốc](docs/Ngay13_Lab13_De_bai_hoc_vien.docx). Chốt hai bộ nhãn trước khi trao đổi hoặc mở đáp án tham khảo. **TV1** kiểm và chốt bảng A/B trong lúc hai người gắn nhãn.
- **TV3** lưu hai bộ nhãn nguyên gốc trong `report/team/bang_loi.md` và tính số ca trùng trên 20. **TV2 và TV3** chốt nhãn thống nhất, ghi một câu phân biệt cho từng ca bất đồng. Nếu đồng thuận dưới 16/20, ghi định nghĩa đã điều chỉnh và giữ nguyên hai cột nhãn gốc. Sau khi chốt, đối chiếu mục tiêu khớp đáp án ít nhất 16/20.
- **TV3** chốt bảng khắc phục 5 ca, mỗi loại một ca, với cách phát hiện đo được, hành động và một vai trò phụ trách. **TV1** kiểm các dấu hiệu phát hiện, **TV2** chuyển các tín hiệu an toàn liên quan sang phần thiết kế pilot.

### CP4 · 16:08–16:36 · D — Thiết kế pilot

- **TV2** tính đủ năm câu D1 về cỡ mẫu theo yêu cầu, nhân viên, depot và mức chênh 6 điểm trong `src/lab13.py` trước khi chọn đơn vị chia. Ghi D1, năm câu D2 và đánh đổi vào chú thích của `report/team/pilot_plan.yaml`. Tính tỷ lệ mở lại 7 ngày trước khi đặt ngưỡng. Điền kế hoạch có đối chứng cùng thời gian, ngẫu nhiên hóa, giảm ảnh hưởng gián tiếp, ngày quyết định và rollback.
- **TV2** viết ít nhất ba luật dừng cho an toàn, chi phí và mức sử dụng. Mỗi luật có đủ NẾU – TRONG – THÌ – KHÔNG THÌ, ngưỡng, thời hạn và vai trò có quyền dừng. **TV1** kiểm cỡ mẫu hiệu dụng và đánh đổi về mức chênh hoặc số cụm.
- Song song, **TV1** soạn E2 với ít nhất hai rủi ro có số từ bảng độ nhạy, dấu hiệu theo dõi, hành động và vai trò phụ trách. **TV3** tích hợp E2 vào `report/team/chi_so.md`.
- **Bàn giao 16:36** TV2 gửi đơn vị chia, cỡ mẫu mỗi nhóm, đánh đổi và ngưỡng dừng. TV3 đưa vào hồ sơ. Cả nhóm kiểm phạm vi và số liệu khớp giữa A/B, YAML và hồ sơ launch.

### CP5 · 16:36–17:00 · E — Chỉ số và hồ sơ launch

- **TV3** hoàn thiện E1 với ba chỉ số tính thử (chính, sử dụng, an toàn), thêm một chỉ số sử dụng và một chỉ số an toàn. Mỗi chỉ số có công thức và event dùng để tính. Danh sách có ít nhất sáu event, mỗi event có `trace_id`, bên tạo, thuộc tính chính và thời điểm.
- **TV3** chốt `report/team/ho_so_launch_v0.md` trong một trang, đủ bảy mục. Mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và một vai trò phụ trách. Mục dùng cột `_simulated` ghi trạng thái Giả lập. Chỉ mô tả kết quả quan sát của đợt chạy thử.
- **Cả nhóm** chọn Go, Go có điều kiện hoặc No-go theo bằng chứng A–E, nêu cả số bất lợi và cách xử lý. Với Go có điều kiện, ghi vai trò và ngày kiểm tra của từng điều kiện. Với No-go, ghi việc cần làm để quay lại Gate 2a. TV3 gửi hồ sơ lúc **17:00**.

### 17:00–17:45 · Duyệt chéo Gate 2a

- Khi bảo vệ bài nhóm, **TV3** trình bày đề xuất và chỉ số, **TV1** trả lời về chi phí và phạm vi, **TV2** trả lời về đối chứng, cỡ mẫu và luật dừng.
- Khi chấm nhóm được phân, **TV1** chấm đề xuất khớp bằng chứng (C6), **TV3** chấm nhãn giả lập và phạm vi (C7), **TV2** chấm khả năng ra quyết định của pilot (C8). TV3 tổng hợp `report/team/phieu_cham.md` với điểm, lý do có số, quyết định, câu hỏi và câu trả lời thực tế tại buổi duyệt.

### 17:45–18:00 · Chốt và push

- **TV3** hoàn thiện `report/team/group_report.md` (tối đa 2 trang), dẫn bằng chứng A–E và ghi phản hồi thực tế LangChai nhận từ hội đồng. **TV1** cập nhật đóng góp và commit chốt trong `TEAM.md`, tích hợp và push. **TV2** kiểm lại số, đường dẫn và trạng thái hồ sơ.
- **Mỗi người** sao chép `report/team/MSSV_HoTen.md` thành file riêng theo MSSV và họ tên, ví dụ `report/team/20241234_NguyenVanAn.md`, ghi phần việc, bằng chứng, công cụ AI đã dùng và cách tự kiểm tra. Cả ba tự nộp cùng URL repo nhóm trên LMS trước **23h59 GMT+7 ngày lab**, theo [hướng dẫn nộp](SUBMISSION.md).

## Kiểm tra trước khi nộp

- [ ] TV3 chạy `python lab13.py` trong `src/` trên máy thứ hai. A1 in ĐẠT cho cả ba phép thử và chương trình chạy hết A/B/D1.
- [ ] Có đủ sáu file trong `report/team/` gồm `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md` và `phieu_cham.md`. Có thêm `group_report.md`, ba báo cáo cá nhân và `TEAM.md`.
- [ ] Số đối chiếu đạt sai số tối đa 2% theo rubric. Số dẫn xuất từ cột `_simulated` có nhãn `simulated`. Mỗi câu trả lời theo đề tối đa ba dòng và có ít nhất một con số.
- [ ] YAML đọc được bằng `yaml.safe_load`, hết dấu `?` trong trường dữ liệu và có ít nhất ba luật dừng đủ bốn vế.
- [ ] Giữ nguyên hai CSV, bản starter và mẫu báo cáo cá nhân. Rà phạm vi hồ sơ theo quy tắc 5 trong README. Repo mở được cho người chấm, đủ file đã push và cả ba đã nộp link LMS.

## Tài liệu đối chiếu

- [Đề bài và lịch lab](README.md) · [Checkpoint A–E](CHECKPOINTS.md) · [Rubric C1–C8](RUBRIC.md) · [Quy định nộp](SUBMISSION.md)
- [Dữ liệu và công thức](docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn chi tiết](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Cài đặt và chạy](src/README.md)
