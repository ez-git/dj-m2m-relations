from django.contrib import admin
# from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def formset(self):
        # for form in self.forms: # В form.cleaned_data будет словарь с
        # данными # каждой отдельной формы, которые вы можете проверить
        # form.cleaned_data # вызовом исключения ValidationError можно
        # указать админке о наличие ошибки # таким образом объект не будет
        # сохранен, # а пользователю выведется соответствующее сообщение об
        # ошибке raise ValidationError('Тут всегда ошибка')

        # вызываем базовый код переопределяемого метода
        return super().formset()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
