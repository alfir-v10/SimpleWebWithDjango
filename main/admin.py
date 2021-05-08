from django.contrib import admin

# Register your models here.
from .models import Person
admin.site.register(Person)

from .models import Perform
admin.site.register(Perform)

