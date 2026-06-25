import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Automatically creates superviewers from .env if they don't exist."

    def handle(self, *args, **options):
        User = get_user_model()
        superusers_env = os.environ.get("SUPERUSERS", "")
        password = os.environ.get("DEFAULT_PASSWORD", "")

        if not superusers_env or not password:
            self.stdout.write(
                self.style.WARNING("SUPERUSERS or DEFAULT_PASSWORD are not set in .env")
            )
            return

        usernames = [name.strip() for name in superusers_env.split(",") if name.strip()]

        for username in usernames:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=f"{username}@example.com",
                    password=password,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Superuser {username} created succesfully.")
                )
            else:
                self.stdout.write(f"Superuser {username} already exists.")
