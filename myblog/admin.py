from django.contrib import admin
from .models import *
from .models import Category
from .models import Tag
from .models import Post
from .models import Keypoints
from .models import Contact,Newsletter



# Register your models here.


class TagTublerInline(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    list_display = ['title', 'date', 'author', 'category', 'status' ,'section']
    list_editable = ['category', 'status', 'section']
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Keypoints)
# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = ['name','email','message','timestamp']
    search_fields = ['name','email','timestamp']

admin.site.register(Contact,ContactAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['fullname','email']

admin.site.register(Newsletter,NewsletterAdmin)