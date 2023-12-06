from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0
        for form in self.forms:
            if form.cleaned_data != {}:
                main_tag += form.cleaned_data['is_main']
            elif main_tag > 1:
                raise ValidationError('Главный тег должен быть только один!')
                break
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]