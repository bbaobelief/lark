from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class BaseModel(models.Model):
    """
    基础信息
    """
    name = models.CharField(u'标题', max_length=100)
    description = models.TextField(u'描述', max_length=1000000, blank=True, null=True)
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=u'创建人')
    enabled = models.BooleanField(u'启用', default=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return u'{0}'.format(self.name)


class WorkFlow(BaseModel):
    """
    工作流
    """
    flowchart = models.FileField(u'流程图', upload_to='flowchart', blank=True)
    restricted = models.BooleanField(u'限制查看', default=False, help_text=u'只允许工单关联人员查看工单')

    class Meta:
        verbose_name = '工作流'
        verbose_name_plural = '工作流'


class State(BaseModel):
    """
    状态
    """
    TYPE_CHOICE = (
        (0, u'普通'),
        (1, u'初始'),
        (2, u'结束')
    )

    workflow = models.ForeignKey(WorkFlow, verbose_name=u'工作流', on_delete=models.CASCADE)
    type_id = models.IntegerField(u'状态类型', choices=TYPE_CHOICE, default=0)
    owner = models.ForeignKey(AUTH_USER_MODEL, verbose_name=u"负责人", on_delete=models.CASCADE,
                              related_name='owner_state', help_text=u'工单的主审核人')
    trackers = models.ManyToManyField(AUTH_USER_MODEL, verbose_name=u'关注人', related_name='tracker_state', blank=True,
                                      default=None)

    class Meta:
        verbose_name = '工作流状态'
        verbose_name_plural = '工作流状态'


class Transition(BaseModel):
    """
    流转
    """
    TYPE_CHOICE = (
        (0, u'普通流转'),
        (1, u'定时流转')
    )

    workflow = models.ForeignKey(WorkFlow, verbose_name=u'工作流', on_delete=models.CASCADE)
    type_id = models.IntegerField(choices=TYPE_CHOICE, default=0, verbose_name=u'流转类型')
    timer = models.IntegerField(u'定时器', default=0, help_text=u'流转类型设置为定时器流转时生效,单位秒')
    last_state = models.ForeignKey(State, verbose_name=u'上个状态', on_delete=models.CASCADE,
                                   related_name='last_state_transition')
    next_state = models.ForeignKey(State, verbose_name=u'下个状态', on_delete=models.CASCADE,
                                   related_name='next_state_transition')
    alert_text = models.CharField('弹窗提示', max_length=100, default='', blank=True)

    class Meta:
        verbose_name = '工作流流转'
        verbose_name_plural = '工作流流转'
