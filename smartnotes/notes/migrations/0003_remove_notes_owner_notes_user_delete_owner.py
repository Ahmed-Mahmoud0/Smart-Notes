# Generated by Django 4.1.2 on 2022-10-15 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0002_alter_notes_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='owner',
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]