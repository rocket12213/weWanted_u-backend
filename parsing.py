import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weWanted_u.settings")

import django
django.setup()

from company.models import Companies
from job.models     import Jobs, Categories, Tags

def categorise() :
    Categories(category="front_end").save()
    Categories(category="back_end").save()
    Categories(category="full_stack").save()

    Tags(skill = "HTML").save()
    Tags(skill = "CSS").save()
    Tags(skill = "Javascript").save()
    Tags(skill = "React").save()
    Tags(skill = "React Native").save()
    Tags(skill = "Redux").save()
    Tags(skill = "Typescript").save()
    Tags(skill = "Saas").save()
    Tags(skill = "Angular").save()
    Tags(skill = "Vue").save()
    Tags(skill = "Webpack").save()
    Tags(skill = "RxJS").save()
    Tags(skill = "Next.js").save()
    Tags(skill = "React Hooks").save()
    Tags(skill = "Node.js").save()

    Tags(skill = "phython").save()
    Tags(skill = "django").save()
    Tags(skill = "MySQL").save()
    Tags(skill = "sqllite").save()
    Tags(skill = "AWS").save()
    Tags(skill = "Docker").save()

if __name__ == '__main__' :
    categorise()
