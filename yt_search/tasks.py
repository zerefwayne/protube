from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta

logger = get_task_logger(__name__)


@periodic_task(run_every=(timedelta(seconds=2)), name="add_two_numbers", ignore_result=True)
def add_two_numbers():
    print("Hellooo!")
    logger.info("Adding two numbers", 5, 10)
    return 15

