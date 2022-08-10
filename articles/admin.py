from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Category, ArticleCategory


class ArticleCategoryInlineFormset(BaseInlineFormSet):
    def clean(self):
        list = []
        for form in self.forms:
            property = form.cleaned_data.get('is_main')
            if property:
                if property in list:
                    raise ValidationError('Два основных раздела')
                list.append(property)
            else:
                list.append(property)
        if not True in list:
            raise ValidationError('Не выбран основной раздел')

        return super().clean()


class ArticleCategoryInline(admin.TabularInline):
    model = ArticleCategory
    formset = ArticleCategoryInlineFormset
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleCategoryInline]
