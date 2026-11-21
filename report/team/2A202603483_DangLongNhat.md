# Báo cáo cá nhân · Đặng Long Nhật · 2A202603483

## 1. Thông tin thành viên

- Họ tên: Đặng Long Nhật
- MSSV: 2A202603483
- Email: nhatlong12cc@gmail.com
- Vai trò: TV1 · Phụ trách A/B, soạn E2 và bàn giao kết quả.

## 2. Phần việc phụ trách

- A1–A4: mô hình chi phí, phân tích theo loại yêu cầu và chi phí cố định.
- B1–B4: độ nhạy, giới hạn lượt chạy và kịch bản xem lại toàn bộ.
- E2: rủi ro kinh tế để TV3 ghép vào `chi_so.md`.

## 3. Đóng góp cụ thể

- Chạy A/B trên dữ liệu lab và đăng kết quả vào `bang_chi_phi.md`.
- Đối chiếu 978 việc thành công với CPS 4.471,97 đ (`simulated`).
- Soạn hai rủi ro E2 về tỷ lệ làm lại và thời gian xem lại.

## 4. Bằng chứng

- Chạy `python lab13.py` tại `src/`, nhận `Ba phép thử đáp án biết trước: ĐẠT` và kết quả đến B4.
- Bảng chi phí của nhóm được cập nhật tại commit `3d273f0`.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT để gợi ý code và kiểm công thức. Tôi tự chạy chương trình trong Windows PowerShell và đối chiếu kết quả trước khi đăng bảng.

## 6. Tự đánh giá

- Giới hạn 2 lượt có tổng chi phí hệ thống thấp nhất, 6.901.220,23 đ (`simulated`). Giới hạn 1 lượt cho CPS thấp nhất, 4.110,99 đ (`simulated`).
- Kịch bản xem lại toàn bộ ở B4 có thể vượt 12.000 đ khi thời gian làm lại khoảng 15,30 phút/ca (`simulated`). Đây là rủi ro cần đo trong pilot.
