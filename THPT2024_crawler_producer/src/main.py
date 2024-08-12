from THPT2024DataCrawler import DataCrawler, generate_number_string
from unidecode import unidecode
from selenium.webdriver.common.by import By
import json
import requests

bot = DataCrawler()
bot.open_page('https://diemthi.vnexpress.net/index/detail/sbd/37000001/year/2024')
score_dict = {
    "student_id": '',
    "scores": {}
}
for i in range(20000):
    success = False  # Biến để kiểm tra xem lần thử có thành công không
    attempts = 0     # Biến đếm số lần thử

    while not success and attempts < 5:
        try:
            # Tạo số báo danh
            exam_registration_number = generate_number_string(i + 1)

            # In ra số báo danh
            print('SBD:', exam_registration_number)

            score_dict['student_id'] = exam_registration_number
            #vào đường link để lấy điểm
            bot.open_page('https://diemthi.vnexpress.net/index/detail/sbd/'+ exam_registration_number +'/year/2024')
            # Lấy bảng điểm
            grade_sheet = bot.find_element_by_css('.section-content .section_main .section-body .container .o-detail-thisinh .o-detail-thisinh__diemthi .e-table > tbody')
            if grade_sheet is None:
                print('error: grade sheet not found')
                attempts += 1
                if 'Không tìm thấy kết quả' in bot.driver.find_element(By.TAG_NAME, 'body').text:
                    print('số báo danh', exam_registration_number, 'không tồn tại')
                    score_dict['score'] = 'số báo danh'+ exam_registration_number + 'không tồn tại'
                    break
                continue  # Tiếp tục lặp lại với cùng giá trị i
            # Tạo từ điển để lưu trữ dữ liệu
            # Tạo từ điển để lưu trữ dữ liệu theo cấu trúc mới
            else:
                subject_score_list = grade_sheet.find_elements(By.TAG_NAME, 'tr')

                for element in subject_score_list:
                    subject_score = element.find_elements(By.TAG_NAME, 'td')
                    if len(subject_score) >= 2:
                        Subject =  unidecode(subject_score[0].text.strip())  # Lấy văn bản của môn học
                        Grade = subject_score[1].text.strip()    # Lấy văn bản của điểm số
                        # Thêm vào từ điển
                        # Thêm vào từ điển scores
                        score_dict["scores"][Subject] = Grade

            # Chuyển đổi từ điển thành chuỗi JSON
            json_data = json.dumps(score_dict, ensure_ascii=False, indent=4)
            print(json_data)
            
            # Gửi dữ liệu đến API
            response = requests.post("http://web:8000/api/send-score/", json=score_dict)
            
            # Kiểm tra phản hồi từ server
            if response.status_code == 200:
                print(f'Dữ liệu đã được gửi thành công cho số báo danh {exam_registration_number}.')
            else:
                print(f'Lỗi khi gửi dữ liệu cho số báo danh {exam_registration_number}. Mã lỗi: {response.status_code}')

            # Đánh dấu vòng lặp là thành công
            success = True

        except Exception as e:
            print("error:", e)
            attempts += 1  # Tăng số lần thử nếu gặp lỗi
            # Tiếp tục vòng lặp while, thử lại với cùng giá trị i

    if not success:
        print(f'Không thể lấy dữ liệu cho số báo danh {generate_number_string(i + 1)} sau 5 lần thử.')

bot.close_browser()
print('successfully')
