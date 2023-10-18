# Generated by Django 4.2.6 on 2023-10-18 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО сотрудника')),
                ('status', models.BooleanField(choices=[(True, 'Работает'), (False, 'Уволен')], default=True, verbose_name='Статус сотрудника')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование справки')),
            ],
            options={
                'verbose_name': 'Справка',
                'verbose_name_plural': 'Справки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ReferenceEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Дата регистрации справки')),
                ('date_end', models.DateField(verbose_name='Дата окончания справки')),
                ('status', models.BooleanField(choices=[(True, 'Активна'), (False, 'Просрочена')], default=True, verbose_name='Статус сотрудника')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference.employee', verbose_name='ФИО сотрудника')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference.reference', verbose_name='Справка')),
            ],
            options={
                'verbose_name': 'Справка сотрудника',
                'verbose_name_plural': 'Справки сотрудников',
                'ordering': ['employee'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='name_reference',
            field=models.ManyToManyField(to='reference.reference', verbose_name='Справка'),
        ),
    ]
