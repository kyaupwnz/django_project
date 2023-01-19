# Generated by Django 4.1.5 on 2023-01-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('category_name', models.CharField(max_length=50)),
                ('unit_price', models.IntegerField()),
                ('date_of_creation', models.DateField(auto_now=True)),
                ('date_of_last_changes', models.DateTimeField()),
            ],
        ),
    ]
