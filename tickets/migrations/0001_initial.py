from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Тақырып")),
                ("description", models.TextField(verbose_name="Сипаттама")),
                ("priority", models.CharField(choices=[("low", "Төмен"), ("medium", "Орташа"), ("high", "Жоғары")], default="medium", max_length=10, verbose_name="Басымдық")),
                ("status", models.CharField(choices=[("new", "Жаңа"), ("in_progress", "Орындалуда"), ("done", "Дайын")], default="new", max_length=15, verbose_name="Мәртебе")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Құрылған уақыты")),
            ],
            options={
                "verbose_name": "Өтінім",
                "verbose_name_plural": "Өтінімдер",
                "ordering": ["-created_at"],
            },
        ),
    ]
