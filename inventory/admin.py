from django.contrib import admin
from .models import Bike, BikeImage, Enquiry

class BikeImageInline(admin.TabularInline):
    model = BikeImage
    extra = 1

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'year', 'is_available')
    inlines = [BikeImageInline]

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'bike', 'created_at')
