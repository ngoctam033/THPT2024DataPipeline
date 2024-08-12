from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import FactScores, DimStudents, DimSubjects
from .serializers import FactScoresSerializer
from.backend import get_score_in_subject, generate_bar_chart,calculate_median_in_subject
from django.http import JsonResponse
from django.db import connection

@api_view(['GET'])
def get_all_scores(request):
    scores = FactScores.objects.all()  # Lấy tất cả các bản ghi từ bảng FactScores
    serializer = FactScoresSerializer(scores, many=True)  # Chuyển đổi dữ liệu thành JSON
    return Response(serializer.data)  # Trả về dữ liệu JSON

def index(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_median_score(request):
    try:
            # Lấy tất cả các đối tượng từ model DimSubjects
        all_subjects = DimSubjects.objects.all()
        median_in_subject_dict = {}
        # Duyệt qua từng đối tượng và in ra subject_id
        for subject in all_subjects:            
            # Gọi hàm lấy danh sách top n sinh viên
            top_student = get_score_in_subject(subject.subject_id)
            median_in_subject = calculate_median_in_subject(top_student,subject.subject_id)
                # Lưu kết quả vào từ điển
            median_in_subject_dict[subject.subject_id] = median_in_subject
        bar_chart = generate_bar_chart(median_in_subject_dict)
        # Trả về dữ liệu JSON
        return JsonResponse({'chart': bar_chart})

    except ValueError:
        return JsonResponse({"error": "Invalid input for 'n'. It must be an integer."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
