# Generated by Django 5.2 on 2025-04-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('raw_text', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
