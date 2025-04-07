# Generated by Django 4.0.1 on 2022-03-28 14:37

from django.db import migrations, models
import resume_cv.models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeCvCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to=resume_cv.models.resume_cv_directory_path)),
                ('color', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
