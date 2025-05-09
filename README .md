# Dân Trí - Trình Thu Thập Bài Viết Mục Xã Hội

Một script sử dụng Selenium để tự động thu thập bài viết đầu tiên trong chuyên mục **Xã hội** trên trang [https://dantri.com.vn](https://dantri.com.vn), lưu nội dung bài viết vào file CSV.

## 📌 Tính năng

- Tự động mở trang chuyên mục "Xã hội"
- Lấy thông tin tiêu đề, mô tả và nội dung bài viết đầu tiên
- Xuất kết quả ra file `bai_viet_xa_hoi.csv`
- Lên lịch chạy tự động hàng ngày lúc 06:00 sáng

## ⚙️ Yêu cầu hệ thống

- Python 3.7 trở lên
- Google Chrome và ChromeDriver

## 🚀 Cách sử dụng

### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt
