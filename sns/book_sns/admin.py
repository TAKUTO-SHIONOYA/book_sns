from django.contrib import admin
from .models import Already_book, Not_Yet_Read_Book,Response,User
# Register your models here.
admin.site.register(Already_book)
admin.site.register(Not_Yet_Read_Book)
admin.site.register(Response)
admin.site.register(User)
