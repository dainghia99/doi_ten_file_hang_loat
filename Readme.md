# Đổi tên thư mục hàng loạt (chuẩn hóa chữ hoa/thường)

Script Python giúp chuẩn hóa hàng loạt **tên thư mục** theo quy tắc viết hoa tiếng Việt, đồng thời **giữ nguyên các từ viết tắt** như `UBND`, `HĐND`, `TTHC`... Phù hợp để dọn dẹp cây thư mục lưu trữ hồ sơ, văn bản có tên đặt không thống nhất (toàn chữ HOA, toàn chữ thường, lộn xộn...).

## Tính năng

- Duyệt **đệ quy** toàn bộ thư mục con trong thư mục gốc.
- 3 chế độ chạy, chọn bằng một con số.
- Chế độ **xem trước** (dry run) để kiểm tra trước khi đổi tên thật.
- Giữ nguyên VIẾT HOA cho danh sách từ viết tắt tùy chỉnh.
- Xử lý đúng việc đổi tên chỉ khác hoa/thường trên Windows (đổi qua tên tạm).
- Không cần cài thêm thư viện, chỉ dùng thư viện chuẩn của Python.

## Yêu cầu

- Python 3.8 trở lên
- Windows, Linux hoặc macOS (script được viết cho Windows nhưng chạy được trên các hệ điều hành khác)

## Cách sử dụng

### 1. Tải script

```bash
git clone https://github.com/<ten-tai-khoan>/<ten-repo>.git
cd <ten-repo>
```

### Lưu ý: Chỉ lưu dự án này vào thư mục `Code` 

### 2. Mở `main.py` và sửa phần cấu hình ở đầu file

```python
ROOT_PATH = r"D:\Duong\Dan\Thu\Muc"   # Thư mục gốc cần xử lý
CHE_DO = 1                            # Chọn chế độ: 1, 2 hoặc 3
GIU_NGUYEN = ["HĐND", "UBND", "TTPVHCC", "TTHC", "CNTT", "TTDVTH"]
```

### 3. Chạy script

```bash
python doi_ten.py
```

## Các chế độ

| `CHE_DO` | Kiểu viết hoa | Hành động | Ví dụ |
|:-------:|---------------|-----------|-------|
| **1** | Viết Hoa Chữ Cái Đầu **Mỗi Từ** | 
| **2** | Chỉ viết hoa chữ cái đầu **của cả tên** | 
| **3** | Viết Hoa Chữ Cái Đầu **Mỗi Từ** |

> Chế độ 2 hiện chỉ xem trước. Muốn đổi tên thật theo kiểu này, sửa trong bảng `CAC_CHE_DO`:
> `2: ("cau", True)` thành `2: ("cau", False)`.

## Quy trình khuyến nghị

1. Đặt `CHE_DO = 1` (hoặc `2`) rồi chạy để **xem trước**. Kết quả có dạng:

   ```
   BÁO CÁO NĂM 2025  -->  Báo Cáo Năm 2025
   họp ubnd xã  -->  Họp UBND Xã
   ```

2. Kiểm tra danh sách. Nếu thiếu từ viết tắt nào cần giữ nguyên chữ hoa, thêm vào `GIU_NGUYEN`.
3. Đặt `CHE_DO = 3` rồi chạy lại để **đổi tên thật**. Kết quả có dạng:

   ```
   Đã đổi: BÁO CÁO NĂM 2025  -->  Báo Cáo Năm 2025
   ```

## Tùy chỉnh danh sách từ viết tắt

Thêm hoặc bớt từ trong `GIU_NGUYEN`. Việc so khớp không phân biệt hoa/thường, và từ khớp sẽ được viết HOA toàn bộ:

```python
GIU_NGUYEN = ["HĐND", "UBND", "MTTQ", "BCH"]   # để [] nếu không cần
```

## Lưu ý quan trọng

- **Sao lưu dữ liệu** hoặc luôn chạy xem trước trước khi đổi tên thật. Chế độ 3 sẽ đổi tên thật và không có chức năng hoàn tác.
- Script **chỉ đổi tên thư mục con** bên trong `ROOT_PATH`. Không đổi tên **tệp tin** và không đổi tên **chính thư mục gốc**.
- Script xử lý từ thư mục **sâu nhất ra ngoài** để việc đổi tên thư mục cha không làm sai đường dẫn của thư mục con.
- Không nên chạy khi có thư mục đang được mở trong Explorer hoặc đang bị phần mềm khác sử dụng, vì Windows có thể từ chối đổi tên. Lỗi sẽ được in ra và script tiếp tục với thư mục kế tiếp.
- Nếu hai thư mục cùng cấp sau khi chuẩn hóa trùng tên nhau (ví dụ `Báo Cáo` và `BÁO CÁO`), việc đổi tên có thể báo lỗi. Hãy kiểm tra ở bước xem trước.

## Cấu trúc repo

```
.
├── doi_ten.py   # Script chính
└── README.md    # Tài liệu hướng dẫn
```