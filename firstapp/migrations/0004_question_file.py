from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20161111_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='file',
            field=models.FileField(blank='true', upload_to='uploads'),
        ),
    ]
