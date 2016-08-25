class ProjectService(object):
    @classmethod
    def gen_project_options(cls, project):
        return {
            'rules': project.rules,
            'payload': project.payload,
            'process_type': project.process_type,
            'method': project.http_method,
            'headers': project.headers,
            'cookies': project.cookies
        }

