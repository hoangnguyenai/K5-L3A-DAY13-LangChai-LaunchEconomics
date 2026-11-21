# Source code

Chạy trong thư mục `src/` với Python 3.10 trở lên và môi trường đã cài pandas và statsmodels:

```text
python lab13.py
```

Chương trình dùng pandas để đọc hai CSV giả lập và in kết quả A1–A4, B1–B4, D1 và E1. Các ô trống trong cột `quyet_dinh_xem_lai` được giữ là chuỗi rỗng.

| File | Nội dung |
| --- | --- |
| `lab13.py` | Tính chi phí, độ nhạy, cỡ mẫu và chỉ số |
| `lab13_starter.py` | Mã khởi đầu để đối chiếu |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu |
| `requirements.txt` | Thư viện của lab, gồm pandas, statsmodels và PyYAML |

Để kiểm kế hoạch pilot bằng PyYAML từ `src/`:

```text
python -c "from pathlib import Path; import yaml; yaml.safe_load(Path('../report/team/pilot_plan.yaml').read_text(encoding='utf-8-sig'))"
```

Xem [dữ liệu và công thức](../docs/du_lieu_va_cong_thuc.md) để đối chiếu kết quả.
