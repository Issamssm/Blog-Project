# Generated by Django 4.1.7 on 2023-04-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categry',
            field=models.CharField(choices=[('Development', 'Development'), ('Ethical Hacking', 'Ethical Hacking'), ('Marketing', 'Marketing')], default='Development', max_length=50, null=True),
        ),
    ]