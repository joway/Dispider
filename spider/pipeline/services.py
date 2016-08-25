class PipelineService(object):
    def __init__(self):
        pass

    @classmethod
    def pipeline(cls, result):
        # 存储到 elastic search
        cls.callback(result)

    @classmethod
    def callback(cls, result):
        """
        收集后续链接, 并发送回scheduler , 由 scheduler 再分发给fetcher
        若无其余链接, 标记结束, 返回
        """
        print('task id', task_id)
        print(result)
        API = "xxx/callback/proj_id/task_id/"
