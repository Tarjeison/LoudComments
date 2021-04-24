import json

from kafka import KafkaConsumer


def get_kafka_consumer():
    return KafkaConsumer(group_id='vg_comments_1', bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))


def run_consumer():
    kafka_consumer = get_kafka_consumer()
    kafka_consumer.subscribe(['vg_comments'])
    for msg in kafka_consumer:
        print(msg)


if __name__ == '__main__':
    run_consumer()
