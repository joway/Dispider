from utils.constants import ProcessType, HTTPMethod


class ProjectStatus(object):
    WAIT_FOR_START = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4


PROCESS_TYPE_CHOICES = (
    (ProcessType.CSS_SELECT, 'CSS选择器'),
    (ProcessType.XPATH, 'CSS'),
    (ProcessType.JSON, 'JSON'),
)

HTTP_METHOD_CHOICES = (
    (HTTPMethod.GET, 'GET'),
    (HTTPMethod.POST, 'POST'),
)

PROJECT_STATUS_CHOICES = (
    (ProjectStatus.WAIT_FOR_START, '等待开始'),
    (ProjectStatus.RUNNING, '正在运行'),
    (ProjectStatus.FINISHED, '结束'),
    (ProjectStatus.FAILED, '失败'),
)
