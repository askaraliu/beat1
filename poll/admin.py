from django.contrib import admin
from poll.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','eid','dob','address','email','mob')

admin.site.register(Person,PersonAdmin)
