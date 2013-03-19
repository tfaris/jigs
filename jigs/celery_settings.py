from settings import DATABASES, TIME_ZONE

import djcelery
djcelery.setup_loader()
BROKER_URL = "django://"
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
BROKER_HOST = DATABASES['default']['HOST']
BROKER_PORT = DATABASES['default']['PORT']
DATABASE_USER = BROKER_USER = DATABASES['default']['USER']
DATABASE_PASSWORD = BROKER_PASSWORD = DATABASES['default']['PASSWORD']
DATABASE_ENGINE = DATABASES['default']['ENGINE']
DATABASE_NAME = DATABASES['default']['NAME']
CELERY_RESULT_DBURI = DATABASES['default']
CELERY_TIMEZONE = TIME_ZONE
CELERY_IMPORTS = ("puzzle.tasks",)

from celery.schedules import crontab, timedelta
CELERYBEAT_SCHEDULE = {
    "save_sessions": {
        "task": "puzzle.tasks.save_cached_sessions",
        "schedule": timedelta(minutes=1),
    }
}
