from django.contrib import admin
from .models import ListChai,ChaiCertificate,ChaiReview,Store

# Register your models here.
# one method
# admin.site.register(ListChai)

# more standard method
class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')


admin.site.register(ListChai,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)


