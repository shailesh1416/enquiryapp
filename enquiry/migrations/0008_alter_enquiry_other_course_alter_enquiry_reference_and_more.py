# Generated by Django 4.0.5 on 2022-08-04 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0007_alter_enquiry_enquiry_for_alter_enquiry_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='other_course',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='reference',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='specialisation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='whatsapp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_for', models.CharField(max_length=200, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.BigIntegerField(blank=True, null=True)),
                ('enquiry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiry.enquiry')),
            ],
        ),
    ]
