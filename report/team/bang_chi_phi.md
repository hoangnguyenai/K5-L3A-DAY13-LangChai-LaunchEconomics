# Bảng chi phí · Nhiệm vụ A và B

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25× giá một lượt chạy |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000,00 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,49 | `attempt > 1` | đo từ trace, đã nằm trong token + tool |
| Xem lại | 1.780.000,00 | `phut_xem_lai_simulated` | `simulated` |
| Làm lại | 2.264.000,00 | `phut_lam_lai_simulated` | `simulated` |
| Tổng chi phí | 4.373.585,13 | Token + tool + xem lại + làm lại | `simulated` |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | số việc |
| Chi phí mỗi việc thành công | 4.471,97 | Tổng chi phí / 978 việc thành công | `simulated` |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (Token + tool) / 1.200 yêu cầu | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,28 lần**, từ 4.471,97 đ/việc thành công chia cho 274,65 đ/yêu cầu (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm **51,77%** tổng chi phí, tương ứng 2.264.000 đ (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.695,64 đ | 0,225× |
| hang_nang | 158 | 74,05% | 1,47 | 8.220,73 đ | 0,685× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515,17 đ | 1,876× |
| doi_tac | 68 | 54,41% | 1,88 | 10.214,87 đ | 0,851× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te` có CPS **22.515,17 đ**, bằng **1,876×** mốc 12.000 đ (`simulated`). Lượt 2 có 12/105 lượt `ok` và lượt 3 chỉ có 2/93, nên lợi ích quan sát được của lượt thứ ba rất thấp.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Ngoại suy từ **900 việc thành công trong phạm vi pilot trên 1.200 yêu cầu toàn mẫu**. CPS biến đổi trong phạm vi này là **3.413,90 đ** (`simulated`), với chi phí cố định **40.000.000 đ/tháng**.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185,19 đ | 4.599,09 đ | 0,383× |
| Một nửa khối lượng | 16.875 | 2.370,37 đ | 5.784,27 đ | 0,482× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Khi giảm từ **45.000** xuống **22.500 yêu cầu/tháng**, phần cố định mỗi việc tăng gấp đôi. CPS gồm cố định vẫn dưới 12.000 đ ở cả hai mức, lần lượt **4.599,09 đ** và **5.784,27 đ** (`simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (%) (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723,08 đ | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346,41 đ | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292,01 đ | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.561,95 đ | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.786,90 đ | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.314,50 đ | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.505,71 đ | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237,29 đ | −5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.110,99 đ | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543,12 đ/việc thành công**, tăng **46,31%** so với A2 (`simulated`).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,77%) · 2. Tỉ lệ xem lại (+40,70%) · 3. Lương nhân viên (+23,12%), theo các kịch bản đã thử (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.780,64 đ | 319 | 7.449.780,64 đ | **4.110,99 đ** |
| 2 lần | 4.093.220,23 đ | 234 | **6.901.220,23 đ** | 4.237,29 đ |
| 3 lần | 4.373.585,13 đ | 222 | 7.037.585,13 đ | 4.471,97 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần** cho tổng chi phí hệ thống thấp nhất (**6.901.220,23 đ**, tương đương **5.751,02 đ/yêu cầu**, `simulated`). Giới hạn **1 lần** cho CPS thấp nhất (**4.110,99 đ**, `simulated`) và để lại thêm **85 yêu cầu** cần nhân viên xử lý theo mô hình của lab.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Có **948 yêu cầu xem lại** và **48 ca làm lại**. CPS là **11.742,79 đ** (0,979×, `simulated`) với 9 phút làm lại/ca và **12.414,50 đ** (1,035×, `simulated`) với trung bình dữ liệu khoảng 15,30 phút/ca (`simulated`).
- Kết quả này nói gì về thứ pilot cần học được? Kịch bản 15,30 phút (`simulated`) vượt mốc **12.000 đ**. Mốc hòa vốn là **5,12 phút** xem lại với 9 phút làm lại và **4,80 phút** với trung bình CSV (`simulated`). Pilot cần đo thời gian và tỉ lệ xem lại, đồng thời theo dõi chất lượng xử lý để biết có thể giảm mức xem lại đến đâu.

## Kiểm tay A2 (TV2 · người kiểm số)

Tính độc lập từ hai file CSV, không dùng code của TV1.

| Bước | Cách tính | Kết quả |
| --- | --- | ---: |
| Token | Σ(tokens_in/1000 × 26 + tokens_out/1000 × 130) trên **mọi** 1.624 lần chạy, kể cả status = loi | 245.585 đ |
| Tool | Σ tool_calls × 15 | 84.000 đ |
| Xem lại | Σ phut_xem_lai_simulated × 2.000 | 1.780.000 đ (simulated) |
| Làm lại | Σ phut_lam_lai_simulated × 2.000 | 2.264.000 đ (simulated) |
| Tổng | cộng bốn khoản | 4.373.585 đ (simulated) |
| Số việc thành công | đếm ket_qua == 'thanh_cong' (không chia 1.200) | 978 |
| Chi phí mỗi việc thành công | 4.373.585 ÷ 978 | 4.472 đ (simulated) |

- Lệch so với A2 của TV1: 0% (4.472 đ so với 4.471,97 đ, ngưỡng 2%, chênh lệch `simulated`). Kết luận: khớp.
- So với nhân viên tự làm: (4.373.585 + 222 yêu cầu không thành công × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = 0,49× của 12.000 đ (simulated).
