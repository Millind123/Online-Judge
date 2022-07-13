from django.contrib import admin

from .models import Inputs, Problems, Submission

admin.site.register(Problems)
admin.site.register(Inputs)
admin.site.register(Submission)