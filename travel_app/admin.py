from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TravelPackage, BlogPost, Testimonial, ContactMessage

@admin.register(TravelPackage)
class TravelPackageAdmin(ModelAdmin):
    list_display = ('title', 'destination', 'price', 'created_at')
    search_fields = ('title', 'destination')

@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('customer_name', 'rating')

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email')
