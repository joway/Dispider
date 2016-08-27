from project.constants import ValidDomainModels


class ProjectService(object):
    @classmethod
    def gen_project_options(cls, project):
        options = {
            'rules': project.rules,
            'payload': project.payload,
            'process_type': project.process_type,
            'method': project.http_method,
            'headers': project.headers,
            'cookies': project.cookies
        }
        if project.valid_domain_model == ValidDomainModels.HOSTNAME:
            options['valid_link_regex'] = \
                (project.valid_domain_regex + project.valid_path_regex) \
                % project.entry_url
        elif project.valid_domain_model == ValidDomainModels.EXTENSIVE:
            options['valid_link_regex'] = \
                (project.valid_domain_regex + project.valid_path_regex) \
                % project.entry_url
        elif project.valid_domain_model == ValidDomainModels.ALL:
            options['valid_link_regex'] = \
                (project.valid_domain_regex + project.valid_path_regex) \
                % project.entry_url
        return options
