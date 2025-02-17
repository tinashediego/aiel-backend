# Generated by Django 3.2.25 on 2025-02-02 17:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchHighlight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Research Highlight')),
                ('content', tinymce.models.HTMLField()),
                ('year', models.PositiveIntegerField(verbose_name='Year of Publication')),
                ('authors', models.TextField(verbose_name='Authors')),
                ('image', models.ImageField(blank=True, null=True, upload_to='research_highlight_images/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Research Highlight',
                'verbose_name_plural': 'Research Highlights',
                'ordering': ['created_at'],
            },
        ),
    ]
