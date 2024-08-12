// Hàm để lấy dữ liệu điểm từ API và hiển thị chúng trong bảng
async function fetchAndDisplayScores() {
    try {
        // Gọi API để lấy dữ liệu điểm
        const response = await fetch('http://localhost:8000/api/all-scores/');  // Thay thế '/api/scores' bằng URL thực tế của API
        const scores = await response.json();

        // Tìm bảng trong tài liệu HTML
        const tableBody = document.getElementById('scores-table-body');

        // Xóa tất cả các hàng hiện tại trong bảng (nếu có)
        tableBody.innerHTML = '';

        // Lặp qua từng phần tử trong mảng scores để tạo các hàng bảng
        scores.forEach(score => {
            const row = document.createElement('tr');

            // Tạo các ô bảng (td) và thêm dữ liệu
            const scoreIdCell = document.createElement('td');
            scoreIdCell.textContent = score.score_id;

            const studentCell = document.createElement('td');
            studentCell.textContent = score.student;

            const subjectCell = document.createElement('td');
            subjectCell.textContent = score.subject;

            const scoreCell = document.createElement('td');
            scoreCell.textContent = score.score;

            // Thêm các ô vào hàng
            row.appendChild(scoreIdCell);
            row.appendChild(studentCell);
            row.appendChild(subjectCell);
            row.appendChild(scoreCell);

            // Thêm hàng vào bảng
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Lỗi khi lấy dữ liệu điểm:', error);
    }
}

// Gọi hàm fetchAndDisplayScores khi trang đã tải
document.addEventListener('DOMContentLoaded', fetchAndDisplayScores);
