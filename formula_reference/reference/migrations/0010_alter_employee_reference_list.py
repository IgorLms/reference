# Generated by Django 4.2.6 on 2023-10-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0009_rename_employee_referenceemployee_employee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='reference_list',
            field=models.ManyToManyField(null=True, to='reference.referenceemployee'),
        ),
    ]
