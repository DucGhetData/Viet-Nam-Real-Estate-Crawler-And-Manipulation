# Import các thư viện cần thiết
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

print("-   Import thành công các thư viện cần thiết   -")

# Mở trình duyệt và truy cập vào trang web
driver = webdriver.Chrome()
url = 'https://www.nhatot.com/mua-ban-bat-dong-san-ha-noi'
driver.get(url)
print("-   Truy cập trang web bằng Chrome thành công   -")
sleep(3)
# Đợi cho trang web tải xong

# tắt thông báo và quảng cáo trong trang web
sleep(5)
webdriver.ActionChains(driver).double_click().perform()
sleep(3)
notification = driver.find_element(By.CLASS_NAME, 'close-btn')
notification.click()
print("-  Tắt thông báo và quảng cáo thành công  -")

raw_data = []
number_of_pages = 500

# Hàm lấy dữ liệu nhà đất từ trang hiện tại 
def get_house_data(driver, page_number):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Tìm tất cả các blocks chứa bài đăng nhà đất
    house_blocks = soup.find_all('li', itemprop = 'itemListElement')
    print(f"Tổng số bài đăng tìm thấy ở trang {page_number+1}: {len(house_blocks)}")
    
    results = []
    
    for i,block in enumerate(house_blocks):
        # 1. Lấy thẻ a chứa link chính
        link_tag = block.select_one('a[itemprop="item"]')
        
        # Kiểm tra tính hợp lệ
        if not link_tag or not link_tag.has_attr('href'):
            continue
        raw_href = link_tag['href'].strip()
        
        # Lọc bỏ các href không phải bài đăng bất đọng sản
        if not raw_href.startswith('/mua-ban'): 
            continue
        # Ghép url chuẩn
        url = 'https://www.nhatot.com' + raw_href
        
        # 2. Lấy tt loại hình nhà đất, số pòng ngủ, hướng nhà
        type_tag = block.select_one('span.bwq0cbs.tle2ik0')
        property_type = type_tag.text.strip() if type_tag else None
        
        # 3. Lấy tt giá tổng, giá/m2, diện tích(nằm trên cùng 1 dòng)
        price_tags = block.select('span.bfe6oav')
        total_price = price_tags[0].text.strip() if len(price_tags) > 0 else None
        price_per_m2 = price_tags[1].text.strip() if len(price_tags) > 1 else None
        area = price_tags[2].text.strip() if len(price_tags) > 2 else None
        
        # 4. Lấy tt địa chỉ(quận) + thời gian thu thập
        location_tag = block.select_one('span.c1u6gyxh.tx5yyjc')
        location = location_tag.text.strip() if location_tag else None
        time = datetime.now().strftime('%Y-%m-%d')
        
        # Lưu bản ghi vào results
        results.append({
            'url': url,
            'property_type': property_type,
            'total_price': total_price,
            'price_per_m2': price_per_m2,
            'area': area,
            'location': location,
            'date': time
        })
        
    # Trả lại kết quả cuối
    return results

# Chuyển trang bằng cách cuộn và click nút "Next"
for page in range(number_of_pages):
    sleep(3)
    raw_data.extend(get_house_data(driver,page))
    # Cuộn đến khi gặp thẻ div có class 'PtyCategoryDescription_contentWrap__uxtat' để chuyển trang 
    while True:
        driver.execute_script("window.scrollBy(0, 500);")
        sleep(0.5)
        try:
            # Định vị đến vị trí để thanh chuyển trang hiện ra
            paging_div = driver.find_element(By.CLASS_NAME, "PtyCategoryDescription_contentWrap__uxtat")
            if paging_div.is_displayed():
                break
        except NoSuchElementException:
            continue
    sleep(2)
    try:
        # Kiểm tra xem có nút "next" còn hoạt động không
        next_icon = driver.find_element(By.CLASS_NAME, 'Paging_rightIconDisable__G58AE')
        print(f"Trang {page+1} là trang cuối cùng. Dừng vòng lặp.")
        break  # Đã đến trang cuối → không bấm next nữa
        sleep(2)
    except NoSuchElementException:
        try:
            # Nếu không phải disabled → vẫn còn trang sau → bấm next
            next_button = driver.find_element(By.CLASS_NAME, 'Paging_rightIcon__3p8MS')
            next_button.click()
            print(f"-   Hoàn thành thu thập dữ liệu ở trang {page+1}   -")
        except NoSuchElementException:
            print(f"Không tìm thấy nút next ở trang {page+1}. Dừng lại.")
            break

print(f"Số bài đăng hợp lệ: {len(raw_data)}")    

df = pd.DataFrame(raw_data)
save_path = 'F:\\Data Analyst\\Viet Nam Real Estate Crawler\\bat_dong_san.csv'
df.to_csv(save_path, index=False, encoding='utf-8-sig')
print("-   Lưu file thành công vào địa chỉ mong muốn  -")   

