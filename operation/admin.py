import datetime
from django.contrib import admin
from operation.models import PhonesList


admin.site.site_header = 'Черный список телефонов'


def exclude_from_black_list(modeladmin, request, queryset):
    queryset.filter(status=True).update(
        status=False,
        excluded_date=datetime.datetime.now(),
        excluded_by=request.user
    )


exclude_from_black_list.short_description = "Исключить из черного списка"


@admin.register(PhonesList)
class PhonesListAdmin(admin.ModelAdmin):
    list_display = ('value', 'added_date', 'added_by', 'reason',
                    'status', 'excluded_date', 'excluded_by')
    list_filter = ('status', )
    ordering = ['added_date']
    actions = [exclude_from_black_list]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if PhonesList.objects.filter(value=obj.value, status=True).first():
            self.message_user(request, "Номер {} был добавлен ранее".format(obj.value))
        else:
            obj.status = True
            if not obj.pk:
                obj.added_by = request.user
            super().save_model(request, obj, form, change)
