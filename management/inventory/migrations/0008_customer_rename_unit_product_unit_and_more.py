# Generated by Django 5.1.4 on 2024-12-17 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_purchase_total_amt_alter_sale_qty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_mobile', models.CharField(max_length=10)),
                ('customer_address', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Unit',
            new_name='unit',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='customer_mobile',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_mobile',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='sale',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer'),
        ),
    ]
