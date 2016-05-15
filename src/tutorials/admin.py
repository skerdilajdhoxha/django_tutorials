from django.contrib import admin
from .models import Tutorial, Video, TutorialDetail, Category


# class VideoInline(admin.TabularInline):
#     model = Video
#     max_num = 10


class TutorialDetailInline(admin.TabularInline):
    model = TutorialDetail
    max_num = 50


class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    list_display_links = ['title']
    search_fields = ['title', 'author', 'category']
    list_per_page = 20
    list_filter = ['title']
    view_on_site = True
    prepopulated_fields = {"slug": ("title",)}
    inlines = [TutorialDetailInline]

admin.site.register(Tutorial, TutorialAdmin)


class TutorialDetailAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_per_page = 50
    list_filter = ['name']
    view_on_site = True

admin.site.register(TutorialDetail, TutorialDetailAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'tutorialdetail']
    list_display_links = ['title']
    search_fields = ['title', 'tutorialdetail']
    list_per_page = 20
    list_filter = ['title', 'tutorialdetail']
    view_on_site = True
    #prepopulated_fields = {"slug": ("title",)}

admin.site.register(Video, VideoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 20
    list_filter = ['title']
    view_on_site = True
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


