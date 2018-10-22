import datetime
from django.contrib import admin, messages
from operation.models import PhonesList


admin.site.site_header = 'Черный список телефонов'


def exclude_from_black_list(modeladmin, request, queryset):
    queryset.filter(status=True).update(
        status=False,
        excluded_date=datetime.datetime.now(),
        excluded_by=request.user
    )


exclude_from_black_list.short_description = "Исключить из черного списка"


class StatusCategoryListFilter(admin.SimpleListFilter):
    title = 'Статус'
    parameter_name = 'status_category'

    def lookups(self, request, model_admin):
        return (
            ('in_blacklist', 'Только телефоны в черном списке'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'in_blacklist':
            return queryset.filter(status=True)


@admin.register(PhonesList)
class PhonesListAdmin(admin.ModelAdmin):
    list_display = ('phone', 'added_date', 'added_by', 'reason',
                    'status', 'excluded_date', 'excluded_by')
    list_filter = (StatusCategoryListFilter, )
    ordering = ['added_date']
    actions = [exclude_from_black_list]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not PhonesList.objects.filter(phone=obj.phone, status=True).first():
            obj.status = True
            if not obj.pk:
                obj.added_by = request.user
            super().save_model(request, obj, form, change)
        else:
            response = "Номер {} был добавлен ранее".format(obj.phone)
            messages.set_level(request, messages.ERROR)
            messages.error(request, response)
