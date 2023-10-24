from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название компании')

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'id_company': self.pk})


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

    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    company_name = models.ManyToManyField(Company, verbose_name='Компания')
    status = models.BooleanField(choices=BOOL_CHOICES, default=True, verbose_name='Статус')

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class ReferenceEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='ФИО')
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT, verbose_name='Справка')
    date_start = models.DateField(verbose_name='Дата получения справки')
    date_end = models.DateField(verbose_name='Дата окончания справки')

    class Meta:
        ordering = ['employee']
        verbose_name = 'Справка сотрудника'
        verbose_name_plural = 'Справки сотрудников'

    def __str__(self):
        return str(self.employee)

    def range_date(self):
        return f"С {self.date_start.strftime('%d.%m.%y')} по {self.date_end.strftime('%d.%m.%y')}"

