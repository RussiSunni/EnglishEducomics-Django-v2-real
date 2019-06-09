from django.contrib import admin

# Register your models here.
from .models import Stages, Users, UserStages

# Register your models here.


admin.site.register(Stages)
admin.site.register(UserStages)
admin.site.register(Users)