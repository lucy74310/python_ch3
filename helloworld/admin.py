from django.contrib import admin


# Register your models here.
from helloworld.models import Counter

admin.site.register(Counter)