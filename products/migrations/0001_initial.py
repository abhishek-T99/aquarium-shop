# Generated by Django 3.2.12 on 2022-02-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('additional_info', models.CharField(max_length=20, null=True)),
                ('description', models.TextField()),
                ('product_type', models.CharField(choices=[('fishes', 'fishes'), ('fist tanks', 'fish tanks'), ('fish foods', 'fish foods'), ('decoratives', 'decoratives'), ('heaters', 'heaters'), ('filters', 'filters'), ('lightings', 'lightings'), ('plants', 'plants')], max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]