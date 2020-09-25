from os import environ
from datetime import datetime
import logging
from random import choice

from rq_scheduler import Scheduler

from app.reviews.generate import log_review
from app.task_queue.redis_helpers import redis_queue


logger = logging.getLogger(__name__)


def start_scheduler(redis_url, redis_password=None, queue_name='job_scheduler_queue'):
    queue = redis_queue(redis_url, redis_password, queue_name)
    scheduler = Scheduler(queue_name=queue.name, connection=queue.connection)

    queue.empty()
    for job in scheduler.get_jobs():
        scheduler.cancel(job)
        logger.info(f"Removed old job {job} from scheduler.")

    # add jobs to scheduler
    job = scheduler.cron(
        cron_string="* * * * *",  # once a minute
        func=log_review,
        args=[datetime.now(), choice(['Alice', 'Bob', 'Carol', 'Dave'])],
        queue_name='basic_queue',
        repeat=None
    )
    logger.info(f"Added job {job}")

if __name__ == "__main__":
    print("about to start")
    url = environ.get('REDIS_URL')
    password = environ.get('REDIS_PASSWORD')  # will be None in development
    print("got env vars")
    start_scheduler(url, password)