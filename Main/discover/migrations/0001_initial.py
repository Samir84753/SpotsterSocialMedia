# Generated by Django 3.0.8 on 2021-04-01 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_interest', models.CharField(max_length=200)),
                ('interest_icon', models.ImageField(default=True, upload_to='Interest_icon')),
            ],
        ),
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='No Bio....', max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('follow_me', models.ManyToManyField(blank=True, related_name='Follow', to='home.registration')),
                ('following', models.ManyToManyField(blank=True, related_name='Following', to='home.registration')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.registration')),
            ],
        ),
    ]
