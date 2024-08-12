from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from confluent_kafka import Producer
from Analyzer_score.backend import save_score_infor, save_student_infor
import json

producer_conf = {
    'bootstrap.servers': 'kafka-1:9093',  # Thay đổi nếu cần
}

producer = Producer(**producer_conf)

@csrf_exempt
@api_view(['POST'])
def send_score(request):
    data=request.data
    message = json.dumps(data)
    try:
        producer.produce('thpt_2024', value=message)
        producer.flush()
        return Response({'status': 'success', 'message': 'Data sent to Kafka'}, status=status.HTTP_200_OK)
    except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt  # Thêm dòng này để bỏ qua kiểm tra CSRF
@api_view(['POST'])
def save_student_scores(request):
    try:
        data = request.data
        save_score_infor(data)
        save_student_infor(data['student_id'])
        return Response({'status': 'success', 'message': 'Student scores saved successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'status': 'error', 'message': 'Only POST requests are allowed'}, status=status.HTTP_400_BAD_REQUEST)

