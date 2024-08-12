from confluent_kafka import Consumer, KafkaError
from kafka_connect import connect_to_kafka, send_data_to_api
import json
import sys
def start_consumer_for_save_to_database(*args, **kwargs):
        consumer = connect_to_kafka(['thpt_2024'])
        try:
            print('đang chạy consumer_for_save_to_database')
            while True:
                msg = consumer.poll(timeout=10.0)  # Chờ 10 giây để nhận message
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # Cuối partition
                        continue
                    else:
                        sys.stderr.write(f"Error: {msg.error()}")
                        break

                # Giải mã message từ Kafka
                data = json.loads(msg.value().decode('utf-8'))
                send_data_to_api('http://web:8000/api/save-scores/', data)
        finally:
            consumer.close()

# def start_consumer_for_realtime_visualization(*args, **kwargs):

