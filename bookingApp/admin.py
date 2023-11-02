from django.contrib import admin
from .models import Booking ,Course,categories
# Register your models here.
admin.site.register(Booking)
admin.site.register(Course)
admin .site.register(categories)