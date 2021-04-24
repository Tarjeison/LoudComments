import json

from kafka import KafkaProducer


def get_kafka_producer():
    return KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         bootstrap_servers='localhost:9092')


def format_and_send_to_kafka(comment):
    comment_split = comment.split("\n")
    json_kafka_message = {'authorName': comment_split[0],
                          'message': comment_split[2],
                          'upvotesCount': comment_split[4],
                          'downvotesCount': comment_split[5]}
    kafka_producer = get_kafka_producer()
    kafka_producer.send('vg_comments', json_kafka_message)
    kafka_producer.flush()
