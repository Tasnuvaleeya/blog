# Generated by Django 2.0.1 on 2018-01-18 16:55

from django.db import migrations
import django_markup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180118_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_markup.fields.MarkupField(choices=[('none', 'None (no processing)'), ('linebreaks', 'Linebreaks'), ('markdown', 'Markdown'), ('restructuredtext', 'reStructuredText')], max_length=255, verbose_name='markup'),
        ),
    ]
