from elastic.services import ElasticService


class PipelineService(object):
    @classmethod
    def pipeline(cls, result):
        # 存储到 elastic search
        ElasticService.index_doc(
            index=result['catalog'], doc_type=result['domain'],
            doc=result['mapping'], doc_id=result['task_id'])
        return result
