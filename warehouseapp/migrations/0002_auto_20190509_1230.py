# Generated by Django 2.1.7 on 2019-05-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='departament',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='departament_type',
            new_name='department_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='marca',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Descripció',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Tipo_producto',
            new_name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='None', max_length=64),
        ),
    ]
