import matplotlib.pyplot as plt
import io
import numpy as np
import base64
from django.forms.models import model_to_dict
def save_student_infor(student_id):
    from .models import DimStudents
    try:
        #thêm student
        DimStudents.objects.raw("INSERT INTO DimStudents (student_id) VALUES (%s)",
                        student_id)
        print('đã thêm id thành công vào database')
    except Exception as e:
        print('save_student_infor',e)

def save_score_infor(data):
    from django.db import transaction
    from .models import FactScores, DimStudents, DimSubjects
    print(data)
    try:
        # Kiểm tra xem 'student_id' và 'scores' có tồn tại trong dữ liệu hay không
        if 'student_id' not in data or 'scores' not in data:
            raise ValueError("Missing required fields: 'student_id' or 'scores'.")

        # Sử dụng giao dịch để đảm bảo tính toàn vẹn dữ liệu
        with transaction.atomic():
            # Lấy hoặc tạo DimStudents
            student, created = DimStudents.objects.get_or_create(student_id=data.get('student_id'))

            # Xử lý và lưu điểm số cho từng môn học
            scores = data.get('scores', {})
            for subject_name, score_value in scores.items():
                # Lấy hoặc tạo DimSubjects
                subject, created = DimSubjects.objects.get_or_create(subject_id=subject_name)

                # Sử dụng update_or_create để tránh trùng lặp và xử lý ràng buộc unique
                FactScores.objects.update_or_create(
                    student_id=student,
                    subject_id=subject,
                    defaults={'score': score_value}
                )

        print("Đã lưu điểm thành công")
    except Exception as e:
        print('save_score_infor', e)

def get_score_in_subject(subject_id):
    from .models import FactScores
    try:
        # Câu lệnh SQL để lấy top n sinh viên có điểm cao nhất trong một môn học cụ thể
        sql_query = """
            SELECT score, score_id
            FROM 
                "Analyzer_score_factscores"
            WHERE 
                subject_id = %s
        """

        # Sử dụng raw() để thực hiện truy vấn SQL
        top_students = FactScores.objects.raw(sql_query, [subject_id])

        # Chuyển đổi kết quả thành danh sách các từ điển
        top_students_list = [
            student.score
            for student in top_students
        ]

        return top_students_list
    except Exception as e:
        return [str(e)]

def generate_bar_chart(data):
    subjects = list(data.keys())
    medians = [float(data[subject]['median']) for subject in subjects]

    # Tạo biểu đồ thanh cho điểm trung vị
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 1, 1)  # Biểu đồ thanh ở trên
    bars = plt.bar(subjects, medians, color='skyblue')
    plt.title('Median Scores of Subjects')
    plt.xlabel('Subjects')
    plt.ylabel('Median Score')
    plt.ylim(0, 10)
    plt.xticks(rotation=45, ha='right')

    # Hiển thị điểm trung vị trên đầu mỗi cột
    for bar, median in zip(bars, medians):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{median}', 
                 ha='center', va='bottom', fontsize=11, color='black')
    
    # Tạo biểu đồ phân phối điểm số
    plt.subplot(2, 1, 2)  # Biểu đồ phân phối ở dưới
    for subject in subjects:
        distribution = data[subject]['distribution']
        ranges = list(distribution.keys())
        counts = list(distribution.values())
        plt.plot(ranges, counts, marker='o', label=subject)

    plt.title('Distribution of Scores Across Subjects')
    plt.xlabel('Score Ranges')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='upper right')
    
    plt.tight_layout()

    # Lưu biểu đồ vào một đối tượng bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Mã hóa hình ảnh dưới dạng base64
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Trả về dữ liệu base64 để gửi đến client
    return image_base64

def calculate_score_distribution(scores, bin_size=1):
    """
    Tính phổ điểm của một danh sách các điểm số.

    Parameters:
    - scores: Danh sách điểm số của sinh viên.
    - bin_size: Kích thước của mỗi nhóm (mặc định là 1).

    Returns:
    - distribution: Một từ điển chứa phổ điểm (key là khoảng điểm, value là số lượng sinh viên trong khoảng đó).
    """
    # Chuyển đổi điểm số thành một mảng numpy
    scores = np.array(scores)

    # Xác định các nhóm điểm
    min_score = int(np.min(scores))
    max_score = int(np.max(scores))
    bins = np.arange(min_score, max_score + bin_size, bin_size)

    # Đếm số lượng sinh viên trong mỗi nhóm
    histogram, bin_edges = np.histogram(scores, bins=bins)

    # Tạo từ điển phổ điểm
    distribution = {}
    for i in range(len(histogram)):
        bin_range = f"{bin_edges[i]}-{bin_edges[i+1]}"
        distribution[bin_range] = histogram[i]

    return distribution

def calculate_median(data):
    """
    Hàm tính trung vị của một danh sách các số.

    Parameters:
    - data: Danh sách các số (list of numbers)

    Returns:
    - median: Trung vị của danh sách
    """
    # Sắp xếp danh sách theo thứ tự tăng dần
    sorted_data = sorted(data)

    # Tính số lượng phần tử trong danh sách
    n = len(sorted_data)

    # Nếu số lượng phần tử là lẻ, trả về phần tử giữa
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        # Nếu số lượng phần tử là chẵn, tính trung bình của hai phần tử giữa
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    return median

def calculate_median_in_subject(data, subject_id):
    distribution = calculate_score_distribution(data, bin_size=1)
    median = calculate_median(data)
        # Tạo từ điển kết quả với subject_id làm key
    result = {
            "median": median,
            "distribution": distribution
    }

    return result
