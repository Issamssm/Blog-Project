# Generated by Django 4.1.7 on 2023-04-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_categry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categry',
            field=models.CharField(choices=[('programming', 'programming'), ('Ethical Hacking', 'Ethical Hacking'), ('Marketing', 'Marketing'), ('Auther', 'Auther')], default='Another', max_length=50, null=True),
        ),
    ]