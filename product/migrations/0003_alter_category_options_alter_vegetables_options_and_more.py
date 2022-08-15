# Generated by Django 4.0.6 on 2022-08-05 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='vegetables',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='vegetables',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vegetables', to='product.category'),
        ),
    ]