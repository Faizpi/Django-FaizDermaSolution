from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_choice_id_alter_question_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.FileField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
