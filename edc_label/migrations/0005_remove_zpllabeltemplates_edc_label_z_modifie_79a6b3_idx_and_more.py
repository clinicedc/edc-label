# Generated by Django 4.2.7 on 2023-12-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_label", "0004_alter_zpllabeltemplates_options_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="zpllabeltemplates",
            name="edc_label_z_modifie_79a6b3_idx",
        ),
        migrations.AddIndex(
            model_name="zpllabeltemplates",
            index=models.Index(
                fields=["modified", "created"], name="edc_label_z_modifie_038fe9_idx"
            ),
        ),
    ]