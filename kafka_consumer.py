import json
import text_to_speech
import platform

from kafka import KafkaConsumer


def get_kafka_consumer():
    return KafkaConsumer(group_id='vg_comments_pi', bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))


def run_consumer():
    kafka_consumer = get_kafka_consumer()
    kafka_consumer.subscribe(['vg_comments'])
    for msg in kafka_consumer:
        tts_text = msg.value['authorName'] + ' synes:' + msg.value['message']
        if platform.system() == 'Windows':
            text_to_speech.tts_windows(tts_text)
        else:
            text_to_speech.tts_pi(tts_text)
        print(tts_text)


if __name__ == '__main__':
    run_consumer()
