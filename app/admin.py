from django.contrib import admin
from .models import ItemModel, Package, TourPoint, User, Booking

# Register your models here.
admin.site.register(ItemModel)

admin.site.register(Package)
admin.site.register(TourPoint)

admin.site.register(User)
admin.site.register(Booking)
