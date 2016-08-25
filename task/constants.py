class TaskStatus(object):
    WAIT_FOR_START = 1
    RUNNING = 2
    RESTARTING = 3
    FINISHED = 4
    FAILED = 5


TASK_STATUS_CHOICES = (
    (TaskStatus.WAIT_FOR_START, '等待启动'),
    (TaskStatus.RUNNING, '运行中'),
    (TaskStatus.RESTARTING, '重启任务'),
    (TaskStatus.FINISHED, '完成'),
    (TaskStatus.FAILED, '失败'),
)
