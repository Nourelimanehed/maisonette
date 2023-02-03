# Generated by Django 4.1.6 on 2023-02-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('adresse', models.TextField()),
                ('nemuro', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='localisation',
            old_name='Commune',
            new_name='commune',
        ),
        migrations.RenameField(
            model_name='localisation',
            old_name='Wilaya',
            new_name='wilaya',
        ),
        migrations.AddField(
            model_name='localisation',
            name='adresse',
            field=models.CharField(default='', max_length=100),
        ),
    ]