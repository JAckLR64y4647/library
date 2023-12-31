# Generated by Django 4.2.5 on 2023-09-05 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("birth_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("available_copies", models.PositiveIntegerField()),
                ("reserved_copies", models.PositiveIntegerField(default=0)),
                (
                    "penalty_rate",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library.author"
                    ),
                ),
            ],
        ),
    ]
