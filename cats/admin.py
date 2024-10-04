from django.contrib import admin

from cats.models import Cat, Breed, Grade


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('cat__name', 'grade')
