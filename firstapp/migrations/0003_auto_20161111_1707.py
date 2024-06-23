from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_question_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(blank='true', upload_to='uploads'),
        ),
        migrations.AlterModelTable(
            name='question',
            table='firstapp_question',
        ),
    ]
