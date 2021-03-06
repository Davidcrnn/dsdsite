# Generated by Django 2.2 on 2020-01-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('message', models.TextField()),
                ('Objet', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='images/')),
                ('image1', models.FileField(blank=True, null=True, upload_to='images/')),
                ('image2', models.FileField(blank=True, null=True, upload_to='images/')),
                ('image3', models.FileField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Vitrine', 'Site Vitrine'), ('Catalogue', 'Site Catalogue'), ('Blog', 'Site blog'), ('Ecommerce', 'Site e-commerce')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('projet', 'Projet'), ('production', 'En ligne'), ('developpement', 'En développement'), ('refonte', 'Refonte du site')], max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('year', models.IntegerField(default=2019)),
            ],
        ),
    ]
