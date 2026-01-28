import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="tiger28").exists():
    User.objects.create_superuser(
        username="tiger28",
        email="benfrjr@gmail.com",
        password="laohu28"
    )
    print("Superuser created")
else:
    print("Superuser already exists")