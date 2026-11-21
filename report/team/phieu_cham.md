# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

## Phiếu duyệt chéo tại lớp

- Nhóm chấm: LangChai.
- Nhóm được chấm: ABCD
- Điểm C6 / C7 / C8: **10/10 · 5/10 · 10/10**. Tổng: **25/30**.
- **Quyết định đề xuất: Go có điều kiện.** Bổ sung nhãn `simulated` ở cột thay đổi B1 và chốt ngưỡng dừng riêng cho hàng nặng trước khi mở pilot. Trong mẫu, tỷ lệ mở lại của hàng nặng là **13/158 = 8,23%**, trong khi tỷ lệ gộp nội địa và hàng nặng là **39/982 = 3,97%**. [Chỉ số an toàn của ABCD](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/aa1a075f1170a9364ac2d402e07302a43b9d4027/report/team/chi_so.md)
- **Câu hỏi cho đội trình:** Nếu tỷ lệ mở lại của hàng nặng vượt **6%** nhưng tỷ lệ gộp vẫn dưới ngưỡng, nhóm sẽ tạm dừng riêng hàng nặng theo quy tắc nào và ai có quyền quyết định?
- **Trả lời gợi ý:** Tính riêng cho hàng nặng trên các ca đã đủ 7 ngày theo dõi. Nếu tỷ lệ vượt **6%** trong 3 ngày kiểm tra liên tiếp, Giám đốc vận hành tạm dừng trợ lý cho hàng nặng trong **30 phút** và chuyển các ca này về CSKH. Đây là điều kiện đề xuất bổ sung vào kế hoạch pilot.

## Chấm thử hồ sơ LangChai

[Hồ sơ launch LangChai](ho_so_launch_v0.md)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện phù hợp với chi phí biến đổi thấp ở phạm vi chọn và rủi ro xem lại 100% có thể lên 12.414,50 đ/việc (simulated). Điều kiện mở pilot yêu cầu đo phút thực tế và xét ngưỡng an toàn trước khi giảm xem lại. [B4](bang_chi_phi.md) |
| C7 · Số giả lập và phạm vi | Thiếu nhãn và mở cho mọi yêu cầu | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Chi phí có phút giả lập được đánh dấu. Chọn nội địa (0,225×) và hàng nặng (0,685×); quốc tế ở 1,876× và đối tác ở 0,851×, có điều khoản riêng (simulated). [A3](bang_chi_phi.md) |
| C8 · Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng cùng thời gian, 20 nhân viên mỗi nhóm và luật dừng cụ thể. Chưa có lưu lượng quan sát theo nhân viên để kiểm tra mức 299 yêu cầu/người trong kỳ đo và 859 yêu cầu hiệu dụng mỗi nhóm. [Kế hoạch pilot](pilot_plan.yaml) |
| **Tổng chấm thử** | | | | **25 / 30** | |

**Đề xuất chấm thử:** Go có điều kiện.

**Lý do:** Trước khi mở pilot, xác nhận đủ lưu lượng theo từng nhân viên, kiểm thử chống hoàn trùng và xác nhận event cho hai nhóm. Trong pilot, dùng số phút đo thực tế để đánh giá ngưỡng hòa vốn 4,80 phút xem lại ở kịch bản làm lại 15,3 phút/ca (simulated).

**Câu hỏi luyện bảo vệ:** Nếu tới ngày chốt kỳ đo mà một nhóm chưa đạt 859 yêu cầu hiệu dụng, đội sẽ xử lý thế nào?

**Trả lời dự kiến:** Kiểm lại cỡ mẫu hiệu dụng dựa trên phân bố yêu cầu theo nhân viên. Nếu còn thiếu, Giám đốc vận hành duyệt kéo dài kỳ đo, giữ phân nhóm và theo dõi đủ 7 ngày sau khi đóng yêu cầu trước khi kết luận.

## Chấm tham khảo nhóm ABCD

Hồ sơ ABCD · L3A, commit `aa1a075`. [Hồ sơ launch](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/aa1a075f1170a9364ac2d402e07302a43b9d4027/report/team/ho_so_launch_v0.md)

| Tiêu chí | Điểm | Căn cứ |
| --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | 10/10 | Go có điều kiện phù hợp với số liệu. Kịch bản xem lại 100% có thể tốn **12.415 đ/việc thành công** (`simulated`), vượt mốc **12.000 đ**. Nhóm đặt mục tiêu xem lại **≤ 4,80 phút/ca** và đo phút thực tế từ tuần 1. [Hồ sơ launch](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/aa1a075f1170a9364ac2d402e07302a43b9d4027/report/team/ho_so_launch_v0.md) |
| C7 · Số giả lập và phạm vi | 5/10 | Phạm vi chỉ gồm nội địa (**0,22×**) và hàng nặng (**0,69×**); quốc tế ở **1,88×** mốc tự làm (`simulated`). Cột **Thay đổi (%)** ở B1 còn thiếu nhãn `simulated`, ví dụ mức **+51,8%** khi số ca làm lại tăng gấp đôi. Hồ sơ nên ghi thêm lý do loại đối tác khi chi phí là **0,85×** và tỷ lệ thành công **54,4%**. [A3 và B1](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/aa1a075f1170a9364ac2d402e07302a43b9d4027/report/team/bang_chi_phi.md) |
| C8 · Pilot ra được quyết định | 10/10 | Có đối chứng đồng thời, chia ngẫu nhiên **20/20 nhân viên** và đặt mục tiêu **5.980 yêu cầu thô/nhóm**, tương đương **859 hiệu dụng**. Kế hoạch có **4 luật dừng**. Luật mở lại dùng trần **6%** hoặc chênh ít nhất **2 điểm phần trăm** trong **3 ngày kiểm tra liên tiếp**, với Giám đốc vận hành có quyền tắt trong **30 phút**. [Kế hoạch pilot](https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics/blob/aa1a075f1170a9364ac2d402e07302a43b9d4027/report/team/pilot_plan.yaml) |
| **Tổng** | **25/30** | |
