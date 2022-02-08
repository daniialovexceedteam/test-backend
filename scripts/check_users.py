import pprint

from django.contrib.auth.models import User

def run():
    pprint(User.objects.all())
    return User.objects.all()
