import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    cmd = 'pkill celery'
    subprocess.call(shlex.split(cmd))
    cmd = 'celery worker -l info -A mendelmd -c 2' #-P solo
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        try:
            #autoreload.main(inner_run)
            from django.utils.autoreload import run_with_reloader
            run_with_reloader(restart_celery)
        except ImportError:
            from django.utils import autoreload
            autoreload.main(restart_celery)
        #autoreload.main(restart_celery)
