from django.contrib import admin
import datetime
from django.utils import timezone
from .models import*
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category')
    search_fields = ['name', 'category']
    list_filter = (
        ('author', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page = 30


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    inlines = [
        BookInline,
    ]
    list_per_page = 30
