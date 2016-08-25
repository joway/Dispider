from project.models import Project
from project.services import ProjectService
from spider.fetcher.tasks import fetch
from utils.helpers import url_hash


class SchedulerService(object):
    @classmethod
    def scheduling_tasks(cls, proj_id, inter_links: []):
        project = Project.objects.get(id=proj_id)
        options = ProjectService.gen_project_options(project)
        for link in inter_links:
            fetch.delay(options +
                        {
                            'proj_id': proj_id,
                            'task_id': url_hash(link),
                            'url': link,
                        })
