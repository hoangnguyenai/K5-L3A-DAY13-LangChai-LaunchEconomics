# Báo cáo cá nhân — NguyenTruongThanh-2A202603512

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trường Thành
- MSSV: 2A202603512
- Email: 26ai.thanhnt6@vinuni.edu.vn
- Vai trong nhóm: TV2 · Người kiểm số, người gắn nhãn 1, người viết code sau giờ giải lao (CP4).

## 2. Phần việc phụ trách

- CP1–CP2: kiểm tra cách đọc CSV (`keep_default_na=False`), tính tay độc lập một kết quả A2 để đối chiếu với TV1 và rà bảng A/B theo rubric.
- CP3: gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (5 loại của Google PAIR), gửi TV3 đối chiếu đồng thuận và thống nhất nhãn.
- CP4: tiếp quản `src/lab13.py` để viết phần D1 (cỡ mẫu) và tỉ lệ mở lại 7 ngày; hoàn thiện `report/team/pilot_plan.yaml` (D1–D3, đối chứng, đánh đổi, 3 luật dừng đủ 4 vế, rollback).
- CP5 & Gate 2a: kiểm tra khả năng đo của các chỉ số E1, phụ trách trả lời phần đối chứng/cỡ mẫu/luật dừng khi bảo vệ, và chấm tiêu chí C8 cho nhóm được phân công.

## 3. Đóng góp cụ thể

- Tính tay độc lập A2 từ hai file CSV: token 245.585 đ, tool 84.000 đ, xem lại 1.780.000 đ (`simulated`), làm lại 2.264.000 đ (`simulated`), tổng 4.373.585 đ (`simulated`) / 978 việc thành công = 4.472 đ (`simulated`), khớp 0% sai số so với 4.471,97 đ của TV1; đối chiếu chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× mốc 12.000 đ (`simulated`).
- Gắn nhãn đủ 20 ca lỗi theo 5 loại Google PAIR, có AI hỗ trợ (Claude Opus 5.5, agent mới chỉ nhận 20 ca và 5 định nghĩa, không xem đáp án). Tự rà từng ca và chốt nhãn của mình; khác gợi ý AI ở 2 ca (ca 3 và ca 8). Gửi TV3 (dùng model khác Claude) đối chiếu và ghép vào `report/team/bang_loi.md`.
- Viết phần D1 trong `src/lab13.py`: tính đủ 5 câu cỡ mẫu (chia theo yêu cầu 1.251/nhóm; theo nhân viên m = 75 cần 84 NV > 40 NV; trần 20 NV/nhóm là 1.000 < 1.251; trần 6 depot/nhóm là 300; với MDE +6 điểm cần 859/nhóm, m ≥ 299 yêu cầu/NV, DE = 6,96, power còn ~0,64 nếu tác động thật là +5 điểm) và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25% toàn mẫu; 3,97% phạm vi pilot).
- Hoàn thiện `report/team/pilot_plan.yaml`: chọn chia theo nhân viên (20 + 20, phân tầng theo 12 depot), phạm vi `noi_dia` + `hang_nang`, ghi rõ đánh đổi MDE +6 điểm, viết 3 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ (an toàn, chi phí, sử dụng) và quy trình rollback trong 30 phút.

## 4. Bằng chứng

- Kiểm tay A2 trong `report/team/bang_chi_phi.md` (commit `5c03335`), mục "Kiểm tay A2 (TV2 · người kiểm số)".
- 20 nhãn của người gắn nhãn 1 kèm lý do AI trong `report/team/tv2_nhan_AI_claude.md`, prompt dùng cho AI trong `report/team/tv2_prompt_gan_nhan_AI.md` (commit `991df51`, gộp vào `main` ở `8b69a3d`); TV3 ghép vào `report/team/bang_loi.md`.
- Code D1 và tỉ lệ mở lại 7 ngày trong `src/lab13.py` (commit `ab29e94`), chạy hết từ A1 đến D3 không lỗi (`Ba phép thử đáp án biết trước: ĐẠT`).
- `report/team/pilot_plan.yaml` (commit `cd90764`): đã điền hết dấu `?`, đọc hợp lệ bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, 3 luật dừng đủ 4 vế, không chứa từ bị cấm theo quy tắc 5 của lab.

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini):** kiểm tra tiến độ phân công, hỗ trợ viết code phần D1 trong `src/lab13.py`, rà cấu trúc `report/team/pilot_plan.yaml`.
- **Claude Opus 5.5 (Claude Code):** giải thích đề và vai trò; soát số D1 và file YAML; sửa 2 chỗ trong YAML theo yêu cầu (bỏ ước lượng "~6 tuần" không tính lại được, thêm nhãn `[simulated]` cho dòng `scope`); xử lý xung đột merge ở `bang_chi_phi.md`, tạo nhánh, commit và push theo yêu cầu.
- **Gắn nhãn C (Claude Opus 5.5):** một agent mới chỉ nhận 20 ca và 5 định nghĩa chép nguyên văn từ đề, không dùng công cụ, không đọc file đáp án, gợi ý nhãn kèm lý do (`report/team/tv2_prompt_gan_nhan_AI.md`). Tôi tự rà từng ca và chốt nhãn, khác gợi ý ở ca 3 và ca 8. Theo yêu cầu của TA, TV3 dùng model khác Claude để đối chiếu.
- **Tự kiểm tra:**
  - Tính tay A2 độc lập và so với TV1 (lệch 0%).
  - Chạy lại toàn bộ `src/lab13.py` trong `.venv` trên Windows PowerShell, đối chiếu từng số D1 (1.251; 2,48; 3.103; 1.000; 300; 859; 299; 6,96; 0,64) và tỉ lệ mở lại (4,25% / 3,97%) với hướng dẫn lab.
  - Tự giải tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 299.
  - Chạy `yaml.safe_load`, kiểm tra không còn dấu `?` ngoài chú thích và không có từ bị cấm theo quy tắc 5 của lab.

## 6. Tự đánh giá

- Với 40 nhân viên hiện có, không cách chia theo cụm nào đủ mẫu để phát hiện mức chênh +5 điểm vì trần hiệu dụng `c/ICC` chỉ đạt 1.000 (< 1.251). Việc chấp nhận nâng MDE lên +6 điểm giúp giữ đủ 20 cụm/nhóm và tách được tác động, nhưng cần nêu rõ rủi ro power giảm còn ~0,64 nếu tác động thật chỉ là +5 điểm.
- Tỉ lệ mở lại 7 ngày hiện tại là 3,97% trong phạm vi pilot (4,25% toàn mẫu), nên ngưỡng dừng an toàn phải dựa trên mức chênh với đối chứng (≥ +2 điểm) kèm trần 6%, thay vì đặt ngưỡng tuyệt đối thấp hơn mức nền.
