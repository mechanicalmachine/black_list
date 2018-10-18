from django.contrib import admin
from operation.models import BlackList


admin.site.site_header = 'Черный список телефонов'


def add_to_black_list(modeladmin, request, queryset):
    queryset.update(status='a')


def exclude_from_black_list(modeladmin, request, queryset):
    queryset.update(status='n')


add_to_black_list.short_description = "Добавить в черный список"
exclude_from_black_list.short_description = "Исключить из черного списка"


@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ('value', 'added_date', 'added_by', 'reason', 'status')
    list_filter = ('added_date', )
    ordering = ['added_date']
    actions = [add_to_black_list, exclude_from_black_list]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
