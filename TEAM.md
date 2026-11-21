# Team

## Thông tin nhóm

- Tên nhóm: LangChai
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-LangChai-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- Repo: [LangChai trên GitHub](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics) · Nhánh nộp: main

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Đặng Long Nhật | 2A202603483 | nhatlong12cc@gmail.com | | TV1 · Người viết code A–B |
| 2 | Nguyễn Trường Thành | 2A202603512 | 26ai.thanhnt6@vinuni.edu.vn | Thanhnt-da | TV2 · Kiểm số, gắn nhãn 1 và viết code CP4 |
|   3 | Nguyễn Lâm Hoàng | 2A202603448 | 26ai.hoangnl@vinuni.edu.vn |        | Người gắn nhãn 2 kiêm giữ hồ sơ |

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

- Kiểm tay A2, gắn nhãn 20 ca và xây dựng kế hoạch pilot D1–D3.
- [Báo cáo cá nhân](report/team/2A202603512_NguyenTruongThanh.md) · [Bảng nhãn](report/team/tv2_nhan_AI_claude.md) · [Kế hoạch pilot](report/team/pilot_plan.yaml).
