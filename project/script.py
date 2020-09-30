import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
"""
You can insert os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") before the django.setup() line.
"""

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n):

    for entry in range(n):

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__=='__main__':
    print("database")
    populate(20)
    print("complate")





