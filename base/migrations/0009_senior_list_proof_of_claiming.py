# Generated by Django 4.2.7 on 2023-11-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_senior_list_senior_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior_list',
            name='proof_of_claiming',
            field=models.ImageField(blank=True, null=True, upload_to='proof/'),
        ),
    ]
