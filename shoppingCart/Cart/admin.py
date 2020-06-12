from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display= ('user', 'profile_image', 'phone', 'dob', 'usr_type', 'address')
admin.site.register(UserProfile, UserProfileAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'productImage', 'productCoast', 'productDesc')
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display= ('user', 'product', 'productCoast', 'count', 'checkOut')
admin.site.register(Cart, CartAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display= ('code', 'discount',)
admin.site.register(Coupon, CouponAdmin)
