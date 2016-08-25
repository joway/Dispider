from utils.helpers import base62_encode


class PipelineService(object):
    @classmethod
    def pipeline(cls, result):
        # 存储到 elastic search
        proj_hash = base62_encode(result['proj_id'])
        print(proj_hash)
        return result
