from django.contrib import admin

# Register your models here.

from .models import Country, State, District , City, Person




admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Person)
