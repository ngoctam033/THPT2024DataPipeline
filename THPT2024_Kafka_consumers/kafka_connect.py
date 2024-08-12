from confluent_kafka import Consumer
import requests
import json

def connect_to_kafka(topics):
        # Cấu hình Kafka Consumer
        conf = {
            'bootstrap.servers': 'kafka-1:9093',  # Địa chỉ broker
            'group.id': 'django-consumer-group',  # Group ID cho consumer
            'auto.offset.reset': 'earliest',  # Đọc từ đầu nếu chưa có offset
        }

        consumer = Consumer(conf)
        consumer.subscribe(topics)  # Đăng ký các topics
        return consumer

def send_data_to_api(url, data):
    headers = {
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        if response.status_code == 201:
            print('Data sent successfully:', response.json())
        else:
            print(f'Failed to send data. Status code: {response.status_code}')
            
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


