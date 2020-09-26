from os import environ

from rq import Worker

from app.task_queue.redis_helpers import redis_queue


def get_worker(redis_url, redis_password, queue_name="job_scheduler_queue"):
    queue = redis_queue(redis_url, redis_password, queue_name)
    return Worker(
        queues=[queue],
        connection=queue.connection
    )

if __name__ == "__main__":
    url = environ.get("REDIS_URL")
    password = environ.get("REDIS_PASSWORD")
    worker = get_worker(url, password)
    worker.work(with_scheduler=True)