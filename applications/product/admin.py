from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.product.models import Product, ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]
    list_display = ('title', 'in_stock', 'quantity', 'image')
    list_editable = ('in_stock', 'quantity')
    search_fields = ('title', 'quantity')
    list_filter = ('quantity', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="20" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Product, ProductAdminDisplay)
