from django.contrib import admin
from .models import User, Measurement

admin.site.register(User)
admin.site.register(Measurement)