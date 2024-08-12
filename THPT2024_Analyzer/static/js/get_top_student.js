// Function to call the API and display the chart
async function fetchAndDisplayChart() {
    try {
        // URL của API
        const apiUrl = 'http://localhost:8000/api/median_score/';

        // Gọi API và lấy dữ liệu
        const response = await fetch(apiUrl);

        // Kiểm tra nếu phản hồi thành công
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Chuyển đổi dữ liệu phản hồi thành JSON
        const data = await response.json();

        // Lấy chuỗi base64 của biểu đồ từ phản hồi
        const chartBase64 = data.chart;

        // Tạo một thẻ img để hiển thị biểu đồ
        const imgElement = document.createElement('img');
        imgElement.src = `data:image/png;base64, ${chartBase64}`;
        imgElement.alt = 'Top Students Chart';

        // Thêm CSS để giới hạn kích thước của ảnh vừa với container
        imgElement.style.maxWidth = '100%';  // Đảm bảo ảnh không vượt quá chiều rộng của vùng chứa
        imgElement.style.height = 'auto';    // Giữ nguyên tỷ lệ khung hình của ảnh

        // Xóa biểu đồ cũ (nếu có) trước khi thêm biểu đồ mới
        const chartContainer = document.getElementById('chart-container');
        chartContainer.innerHTML = ''; // Xóa nội dung cũ
        chartContainer.appendChild(imgElement); // Thêm biểu đồ mới

    } catch (error) {
        console.error('Error fetching or displaying chart:', error);
    }
}

// Gọi hàm để lấy dữ liệu và hiển thị biểu đồ mỗi giây
setInterval(fetchAndDisplayChart, 2000); // 2000 milliseconds = 1 giây