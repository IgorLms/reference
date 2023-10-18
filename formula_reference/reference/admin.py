from django.contrib import admin
from .models import Company, Reference, Employee, ReferenceEmployee
from datetime import date


class ReferenceDateEndFilter(admin.SimpleListFilter):
    """
    Фильтрация для справок сотрудников.
    Фильтрация по состоянию просрочена справка или нет на сегодняшнюю дату.
    """

    title = 'Статус справки'
    parameter_name = 'status_date'

    def lookups(self, request, model_admin):
        return [
            ('active', 'Активная'),
            ('overdue', 'Просрочена'),
        ]

    def queryset(self, request, queryset):
        current_date = date.today()
        if self.value() == 'active':
            return queryset.filter(date_end__gte=current_date)
        elif self.value() == 'overdue':
            return queryset.filter(date_end__lt=current_date)


class EmployeeStatusFilter(admin.SimpleListFilter):
    """
    Фильтрация для справок сотрудников.
    Фильтрация по состоянию уволен сотрудник или нет.
    """

    title = 'Статус сотрудника'
    parameter_name = 'status_employee'

    def lookups(self, request, model_admin):
        return [
            ('work', 'Работает'),
            ('fired', 'Уволен'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'work':
            return queryset.filter(employee__status=True)
        elif self.value() == 'fired':
            return queryset.filter(employee__status=False)


@admin.register(ReferenceEmployee)
class ReferenceEmployeeAdmin(admin.ModelAdmin):
    """Справки сотрудников"""

    list_display = ('employee', 'date_of_birth_info', 'company_info', 'reference', 'date_range_info', 'status_info')
    list_per_page = 15
    search_fields = ['employee']
    autocomplete_fields = ['employee']
    list_filter = ['reference__name', 'employee__company_name', ReferenceDateEndFilter, EmployeeStatusFilter]

    @admin.display(description='Дата рождения')
    def date_of_birth_info(self, reference_employee: ReferenceEmployee):
        return reference_employee.employee.date_of_birth

    @admin.display(description='Компания', ordering='employee__company_name')
    def company_info(self, reference_employee: ReferenceEmployee):
        return reference_employee.employee.company_name

    @admin.display(description='Срок справки')
    def date_range_info(self, reference_employee: ReferenceEmployee):
        return f"С {reference_employee.date_start.strftime('%d.%m.%y')} по {reference_employee.date_end.strftime('%d.%m.%y')}"

    @admin.display(description='Статус')
    def status_info(self, reference_employee: ReferenceEmployee):
        return 'Активная' if reference_employee.date_end >= date.today() else 'Просрочена'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Сотрудники"""

    list_display = ('full_name', 'date_of_birth', 'company_name', 'status')
    list_per_page = 15
    search_fields = ['full_name']
    list_filter = ['company_name', 'status']


"""Компании"""
admin.site.register(Company)

"""Справки"""
admin.site.register(Reference)
