# Generated by Django 3.1.2 on 2020-10-06 10:13

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('maps', models.CharField(max_length=140, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=140)),
                ('opened', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1200, null=True), size=None)),
                ('website', models.CharField(blank=True, max_length=800, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('restLat', models.FloatField()),
                ('restLng', models.FloatField()),
                ('adress', models.CharField(blank=True, max_length=140, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurant')),
                ('review_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StarterPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'StarterPics',
                'verbose_name_plural': 'StarterPics',
            },
        ),
        migrations.CreateModel(
            name='OutsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'OutsidePics',
                'verbose_name_plural': 'OutsidePics',
            },
        ),
        migrations.CreateModel(
            name='MenuPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'MenuPics',
                'verbose_name_plural': 'MenuPics',
            },
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'MainPics',
                'verbose_name_plural': 'MainPics',
            },
        ),
        migrations.CreateModel(
            name='InsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'InsidePics',
                'verbose_name_plural': 'InsidePics',
            },
        ),
        migrations.CreateModel(
            name='DessertPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('restaurant_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.restaurantreview')),
            ],
            options={
                'verbose_name': 'DessertPics',
                'verbose_name_plural': 'DessertPics',
            },
        ),
    ]