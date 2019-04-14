# Generated by Django 2.1.7 on 2019-04-14 16:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_modify', models.PositiveIntegerField(default=0, verbose_name='Quantitat modificada')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='None', max_length=16)),
                ('departament_type', models.CharField(default='None', max_length=16)),
                ('departament', models.CharField(default='None', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(default='None', max_length=16)),
                ('model', models.CharField(default='None', max_length=32)),
                ('Descripció', models.CharField(default='None', max_length=64)),
                ('Tipo_producto', models.CharField(default='None', max_length=64)),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantitat')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product', to='warehouseapp.Category', verbose_name='Categoria producte')),
            ],
        ),
        migrations.AddField(
            model_name='catalogchange',
            name='category_id_change',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product_change', to='warehouseapp.Category', verbose_name='Categoria producte'),
        ),
        migrations.AddField(
            model_name='catalogchange',
            name='product_id_change',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_id_change', to='warehouseapp.Product', verbose_name='Producte'),
        ),
        migrations.AlterUniqueTogether(
            name='catalogchange',
            unique_together={('product_id_change', 'category_id_change')},
        ),
    ]
