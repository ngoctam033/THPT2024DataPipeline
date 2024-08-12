# Sử dụng image Python phiên bản slim để giảm kích thước
FROM python:3.12-slim

# Đặt thư mục làm việc bên trong container
WORKDIR /app

# Sao chép requirements trước để tận dụng cache
COPY requirements.txt /app/

# Cài đặt các thư viện Python cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Cài đặt các gói cần thiết cho Firefox và dọn dẹp
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget gnupg2 unzip bzip2 curl \
                       libnss3 libgconf-2-4 libxi6 libglu1-mesa libxrender1 libxtst6 libxss1 libfontconfig1 \
                       firefox-esr && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Sao chép mã nguồn vào container
COPY src/ /app/src/

# Khởi chạy ứng dụng
CMD ["python", "/app/src/main.py"]
