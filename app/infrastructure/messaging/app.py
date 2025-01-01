from celery import Celery

task_manager = Celery("worker")
task_manager.config_from_object("app.infrastructure.messaging.config")
task_manager.autodiscover_tasks(["app.infrastructure.messaging"])
