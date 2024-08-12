# Sử dụng image Python chính thức
FROM python:3.12-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép mã nguồn vào container
COPY . .

# Cài đặt các phụ thuộc cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Khởi chạy ứng dụng
CMD ["python", "run_consumers.py"]