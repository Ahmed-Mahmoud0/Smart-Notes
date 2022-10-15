# Generated by Django 4.1.2 on 2022-10-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_notes_owner_notes_user_delete_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='is_approved',
            field=models.BooleanField(default=False, help_text='Approve the note if its name is not explicit'),
        ),
    ]