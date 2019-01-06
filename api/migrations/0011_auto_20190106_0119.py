# Generated by Django 2.1.3 on 2019-01-05 19:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20190103_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('menu', models.IntegerField(choices=[(0, 'Main'), (1, 'Secondary')], default=0)),
                ('order', models.IntegerField(default=0)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='tag',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]