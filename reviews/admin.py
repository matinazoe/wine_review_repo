from django.contrib import admin

# Register your models here.
from .models import Repo, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('repo', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Repo)
admin.site.register(Review, ReviewAdmin)