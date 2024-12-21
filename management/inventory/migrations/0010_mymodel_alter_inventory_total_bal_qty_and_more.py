# Generated by Django 5.1.4 on 2024-12-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_customer_options_alter_sale_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='total_bal_qty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email_address',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
