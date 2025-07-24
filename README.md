# 🏡 Real Estate Data Crawler And Visualization - Hanoi, Vietnam

## 📖 Mô tả dự án
Trong bối cảnh giá bất động sản ở Việt Nam tăng cao, việc có một góc nhìn tổng quan về giá và các thông tin quan trọng khác về giá nhà tại Hà Nội và Việt Nam là vô cùng cần thiết. Nhằm đám ứng nhu cầu cần thiết này, dự án này sẽ thu thập dữ liệu mới nhất được cập nhật hàng tuần từ trang web nhatot.com từ đó phân tích và đưa ra những góc nhìn tổng quan nhất về giá, diện tích, số lượng giao bán hàng tuần.

## 🎯 Mục tiêu

- Crawl dữ liệu bất động sản từ nhatot.com (đường dẫn, giá, giá/m2, diện tích, loại hình nhà ở, vị trí,...)
- Làm sạch và chuẩn hóa dữ liệu.
- Phân tích xu hướng giá, khu vực, loại hình bất động sản
- Trực quan hóa trên Power BI phục vụ báo cáo hoặc ra quyết định đầu tư

## 📅 Quy trình thực hiện dự án
1. Sử dụng Selenium và BeautifullSoup4 để thu thập dữ liệu bất động sản mới nhất từ trang web nhatot.com. Dữ liệu được tổ chức và lưu trữ ở dạng file .csv
2. Sử dụng Pandas để làm sạch và chuẩn hóa dữ liệu. Các thông tin không cần thiết hoặc sinh ra do quá trình trích xuất dữ liệu sẽ bị loại bỏ, các thông tin cần thiết được điều chỉnh để phù hợp cho việc trực quan hóa. Dữ liệu tiếp tục được lưu trong file .csv
3. Cuối cùng là sử dụng PowerBi để trực quan hóa dữ liệu và đưa ra các kết luận và phân tích về giá bất động sản ở Hà Nội
<img width="978" height="451" alt="image" src="https://github.com/user-attachments/assets/d4c0070c-737a-49bd-a2a7-db9a0fb6f304" />

## 📊 Báo cáo 
- Xem chi tiết báo cáo tại đây:https://app.powerbi.com/groups/me/reports/15b15d08-2ffc-4d3f-915f-ea7b46500dc8?ctid=152f0603-a666-48c3-a925-56738149905a&pbi_source=linkShare
<img width="1292" height="786" alt="image" src="https://github.com/user-attachments/assets/aaeb56f1-2302-4f3e-9b7e-afc99be715d2" />


## 📂 Cấu trúc thư mục
```bash
Viet Nam Real Estate Crawler/
├── data/                # Chứa file dữ liệu gốc và dữ liệu đã xử lý
├── notebooks/           # Jupyter Notebooks (crawl, xử lý, phân tích)
├── powerbi/             # File .pbix cho Power BI
├── src/                 # Mã nguồn Python (các script crawl, xử lý)
├── README.md            # File mô tả dự án
├── requirements.txt     # Danh sách thư viện cần cài

