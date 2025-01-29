# Generated by Django 3.2.25 on 2025-01-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='board_images/images/')),
                ('fullname', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('linkedin_url', models.CharField(max_length=255)),
                ('x_url', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Board',
                'ordering': ['created_at'],
            },
        ),
    ]
