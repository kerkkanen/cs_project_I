# Generated by Django 4.0.3 on 2022-04-20 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hearts', '0002_alter_account_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciever',
            new_name='receiver',
        ),
    ]