from django.apps import AppConfig
from django.db import OperationalError, ProgrammingError


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


    def ready(self):
        from .management.commands.delete_blog_post_periodic_task import create_periodic_task
        try:
            create_periodic_task()
        except (OperationalError, ProgrammingError):
            # Database tables might not exist yet (e.g., before migrate)
            pass
