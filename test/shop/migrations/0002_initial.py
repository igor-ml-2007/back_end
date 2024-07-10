# Generated by Django 5.0.6 on 2024-06-07 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='order'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='productreason',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reason', to='shop.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='producttowhom',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_whom', to='shop.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='productreason',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.reason', verbose_name='reason'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='shop.tags', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='producttowhom',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.towhom', verbose_name='who'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('order', 'product')},
        ),
    ]