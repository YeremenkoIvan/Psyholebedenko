# Generated by Django 4.2.2 on 2023-07-02 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('thumbnail_text', models.CharField(blank=True, max_length=512)),
                ('main_text', models.CharField(blank=True, max_length=10000)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('online', models.BooleanField(default=False)),
                ('zoom_link', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(through='event.Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]
