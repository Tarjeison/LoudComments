from typing import List
import hashlib
import kafka_producer

COMMENTS_FILE = "comments.txt"


def save_comments(comments: List[str]):
    comment_file = open(COMMENTS_FILE, "a")
    for comment in comments:
        comment_file.write(hashlib.md5(comment.encode('utf-8')).hexdigest() + "\n")




def get_only_unspoken_comments(comments: List[str]) -> List[str]:
    all_spoken_hash = open(COMMENTS_FILE).read().splitlines()
    unspoken_comments = []
    for comment in comments:
        formatted_comment = format_comment(comment)
        hashed_comment = hashlib.md5(formatted_comment.encode('utf-8')).hexdigest()
        if hashed_comment not in all_spoken_hash:
            print("new comment: " + formatted_comment)
            unspoken_comments.append(formatted_comment)
            kafka_producer.format_and_send_to_kafka(comment)

    return unspoken_comments


def format_comment(comment: str) -> str:
    new_line_split = comment.split("\n")
    return new_line_split[0] + " sier: " + new_line_split[2]


