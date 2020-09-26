from urllib.parse import urlparse

from redis import Redis
from rq import Queue

def redis_connection(url, password):
    parsed_url = urlparse(url)
    return Redis(host=parsed_url.hostname, port=parsed_url.port, password=password)


def redis_queue(url, password, queue_name):
    connection = redis_connection(url, password)
    queue = Queue(
        name=queue_name,
        connection=connection,
        is_async=True
    )
    return queue
