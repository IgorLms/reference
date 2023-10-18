from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название компании')

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование справки')

    class Meta:
        ordering = ['name']
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'

    def __str__(self):
        return self.name


class Employee(models.Model):
    BOOL_CHOICES = ((True, 'Работает'), (False, 'Уволен'))

    full_name = models.CharField(max_length=100, verbose_name='ФИО сотрудника')
    company_name = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Компания')
    status = models.BooleanField(choices=BOOL_CHOICES, default=True, verbose_name='Статус сотрудника')

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class ReferenceEmployee(models.Model):
    BOOL_CHOICES = ((True, 'Активна'), (False, 'Просрочена'))

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='ФИО сотрудника')
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT, verbose_name='Справка')
    date_start = models.DateField(verbose_name='Дата регистрации справки')
    date_end = models.DateField(verbose_name='Дата окончания справки')
    status = models.BooleanField(choices=BOOL_CHOICES, default=True, verbose_name='Статус справки')

    class Meta:
        ordering = ['employee']
        verbose_name = 'Справка сотрудника'
        verbose_name_plural = 'Справки сотрудников'

    def __str__(self):
        return str(self.employee)

