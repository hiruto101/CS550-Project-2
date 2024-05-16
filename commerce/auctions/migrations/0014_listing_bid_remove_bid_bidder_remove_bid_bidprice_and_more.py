# Generated by Django 5.0.4 on 2024-05-11 07:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_category_id_alter_listing_id_alter_user_id_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bid'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidprice',
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userbid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidprice',
            field=models.IntegerField(default=0),
        ),
    ]