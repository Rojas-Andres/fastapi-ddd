import logging
import multiprocessing
from logging import StreamHandler

bind = "unix:/app/fastapi.sock"
threads = 2
workers = multiprocessing.cpu_count() * 2
worker_class = "uvicorn.workers.UvicornWorker"
accesslog = "-"
errorlog = "-"
loglevel = "info"

logger = logging.getLogger("gunicorn.error")
handler = StreamHandler()
logger.addHandler(handler)
