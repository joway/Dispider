from utils.elastic import elatic


class PipelineService(object):
    DB_NAME = 'dispider'

    @classmethod
    def pipeline(cls, result):
        # 存储到 elastic search
        cls.save(doc_type=result['proj_id'], doc_id=result['task_id'],
                 doc=result['mapping'])
        return result

    @classmethod
    def save(cls, doc_type, doc_id, doc):
        return elatic.index(index=cls.DB_NAME, doc_type=doc_type, id=doc_id, body=doc)

    @classmethod
    def delete(cls, doc_type, doc_id):
        return elatic.delete(index=cls.DB_NAME, doc_type=doc_type, id=doc_id)

    @classmethod
    def index(cls, doc_type):
        return elatic.index(index=cls.DB_NAME, doc_type=doc_type)
