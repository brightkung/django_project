# Generated by Django 3.1.6 on 2021-03-05 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_product_code', models.CharField(max_length=20)),
                ('history_balance', models.IntegerField()),
                ('history_total', models.IntegerField()),
                ('history_date', models.DateField()),
                ('history_user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_name', models.CharField(max_length=50)),
                ('fact_id', models.CharField(max_length=20)),
                ('fact_t', models.TextField()),
                ('fact_a', models.TextField()),
                ('fact_city', models.TextField()),
                ('fact_post', models.CharField(max_length=20)),
                ('fact_email', models.EmailField(max_length=254)),
                ('fact_phone', models.CharField(max_length=20)),
                ('fact_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.TextField()),
                ('identification', models.CharField(max_length=30)),
                ('phone', models.TextField()),
                ('shop_name', models.CharField(max_length=50)),
                ('address_id', models.CharField(max_length=50)),
                ('address_t', models.CharField(max_length=50)),
                ('address_a', models.CharField(max_length=50)),
                ('address_city', models.CharField(max_length=50)),
                ('address_post', models.CharField(max_length=50)),
                ('address_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('product_size', models.CharField(max_length=10)),
                ('product_send_time', models.IntegerField()),
                ('product_cost', models.IntegerField()),
                ('product_selling', models.IntegerField()),
                ('product_balance', models.IntegerField()),
                ('product_image', models.FileField(upload_to='')),
                ('product_desc', models.TextField()),
                ('prodect_status', models.CharField(max_length=50)),
                ('product_fact_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=20)),
                ('product_quantity', models.PositiveIntegerField()),
                ('date_output', models.DateField()),
            ],
        ),
    ]
