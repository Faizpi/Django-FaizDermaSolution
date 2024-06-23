from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0004_question_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="file",
            field=models.FileField(blank="true", upload_to="files"),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="image",
            field=models.FileField(blank="true", upload_to="images"),
        ),
    ]
