# Generated by Django 5.1.6 on 2025-02-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Macro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_path', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
