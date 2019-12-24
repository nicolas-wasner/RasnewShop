from django.contrib import admin

# Register your models here.
from app.models import Example, UserForm

admin.site.register(Example)
#admin.site.register(UserForm)