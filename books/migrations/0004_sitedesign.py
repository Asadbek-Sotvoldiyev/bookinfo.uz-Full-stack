# Generated by Django 5.0.3 on 2024-04-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='site/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
