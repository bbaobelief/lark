# Generated by Django 2.1.5 on 2019-01-25 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(blank=True, max_length=1000000, null=True, verbose_name='描述')),
                ('enabled', models.BooleanField(default=True, verbose_name='启用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('type_id', models.IntegerField(choices=[(0, '普通'), (1, '初始'), (2, '结束')], default=0, verbose_name='状态类型')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_state', to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
                ('trackers', models.ManyToManyField(blank=True, default=None, related_name='tracker_state', to=settings.AUTH_USER_MODEL, verbose_name='关注人')),
            ],
            options={
                'verbose_name': '工作流状态',
                'verbose_name_plural': '工作流状态',
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(blank=True, max_length=1000000, null=True, verbose_name='描述')),
                ('enabled', models.BooleanField(default=True, verbose_name='启用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('type_id', models.IntegerField(choices=[(0, '普通流转'), (1, '定时流转')], default=0, verbose_name='流转类型')),
                ('timer', models.IntegerField(default=0, help_text='流转类型设置为定时器流转时生效,单位秒', verbose_name='定时器')),
                ('alert_text', models.CharField(blank=True, default='', max_length=100, verbose_name='弹窗提示')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('last_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_state_transition', to='workflow.State', verbose_name='上个状态')),
                ('next_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_state_transition', to='workflow.State', verbose_name='下个状态')),
            ],
            options={
                'verbose_name': '工作流流转',
                'verbose_name_plural': '工作流流转',
            },
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(blank=True, max_length=1000000, null=True, verbose_name='描述')),
                ('enabled', models.BooleanField(default=True, verbose_name='启用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('flowchart', models.FileField(blank=True, upload_to='flowchart', verbose_name='流程图')),
                ('restricted', models.BooleanField(default=False, help_text='只允许工单关联人员查看工单', verbose_name='限制查看')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
            },
        ),
        migrations.AddField(
            model_name='transition',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkSheet', verbose_name='工作流'),
        ),
        migrations.AddField(
            model_name='state',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkSheet', verbose_name='工作流'),
        ),
    ]
