# Generated by Django 5.0 on 2023-12-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='recordings/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('camera', models.FileField(blank=True, null=True, upload_to='camera/')),
            ],
        ),
    ]