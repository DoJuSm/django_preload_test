from django.contrib import admin

from .models import MomCat, Kitten

@admin.register(MomCat)
class MomCatAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Kitten)
class MomCatAdmin(admin.ModelAdmin):
    pass


