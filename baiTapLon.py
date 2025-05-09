from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import schedule

def lay_bai_viet_xa_hoi():
    print("🔄 Đang thu thập bài viết...")

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Mở trang chuyên mục Xã hội
    driver.get("https://dantri.com.vn/xa-hoi.htm")
    time.sleep(2)

    try:
        # Tìm bài viết đầu tiên
        first_article = driver.find_element(By.CSS_SELECTOR, "div.article-thumb > a")
        article_url = first_article.get_attribute("href")
        first_article.click()
        print(f"📄 Đã vào bài viết: {article_url}")
    except Exception as e:
        print("❌ Không tìm thấy bài viết đầu tiên:", e)
        driver.quit()
        return

    time.sleep(2)

    try:
        # Tiêu đề
        title = driver.find_element(By.CSS_SELECTOR, "article > h1").text.strip()

        # Mô tả (nếu có)
        try:
            description = driver.find_element(By.CSS_SELECTOR, "article > h2").text.strip()
        except:
            description = ""

        # Nội dung
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "figcaption > p")
        content = "\n".join([p.text for p in paragraphs if p.text.strip() != ""])

        # Đóng trình duyệt
        driver.quit()

        # Lưu dữ liệu vào CSV
        data = {
            "Tiêu đề": [title],
            "Mô tả": [description],
            "Nội dung": [content]
        }
        df = pd.DataFrame(data)
        output_file = "bai_viet_xa_hoi.csv"
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"✅ Đã lưu vào {output_file}")

    except Exception as e:
        print("❌ Lỗi khi trích xuất nội dung bài viết:", e)
        driver.quit()

# Lên lịch chạy hàng ngày lúc 06:00 sáng
schedule.every().day.at("06:00").do(lay_bai_viet_xa_hoi)

print("🕒 Đang chờ tới 06:00 mỗi ngày để chạy... Nhấn Ctrl+C để dừng.")

while True:
    schedule.run_pending()
    time.sleep(60)
