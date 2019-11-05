import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weWanted_u.settings")

import django
django.setup()

from company.models import Companies
from job.models     import Jobs, Categories, Tags, JobsToTags

def categorise() :

#    JobsToTags.objects.create(
#            jobs_id = 1,
#            tags_id = 3
#        ).save()
    JobsToTags.objects.create(
            jobs_id = 1,
            tags_id = 4
            ).save()
 
    JobsToTags.objects.create(
            jobs_id = 2,
            tags_id = 1
            ).save()
    JobsToTags.objects.create(
            jobs_id = 2,
            tags_id = 2
            ).save()
    JobsToTags.objects.create(
            jobs_id = 2,
            tags_id = 3
            ).save()
    JobsToTags.objects.create(
            jobs_id = 2,
            tags_id = 4
            ).save()
    JobsToTags.objects.create(
            jobs_id = 2,
            tags_id = 9
            ).save()

    JobsToTags.objects.create(
            jobs_id = 3,
            tags_id = 4
            ).save()
    JobsToTags.objects.create(
            jobs_id = 3,
            tags_id = 10,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 3,
            tags_id = 9,
            ).save()


    JobsToTags.objects.create(
            jobs_id = 4,
            tags_id = 9
            ).save()

    JobsToTags.objects.create(
            jobs_id = 5,
            tags_id = 4,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 5,
            tags_id = 10,
            ).save()

    JobsToTags.objects.create(
            jobs_id = 6,
            tags_id = 3
        ).save()
    JobsToTags.objects.create(
            jobs_id = 6,
            tags_id = 4
            ).save()
    JobsToTags.objects.create(
            jobs_id = 6,
            tags_id = 6
            ).save()

    JobsToTags.objects.create(
            jobs_id = 7,
            tags_id = 1
            ).save()
    JobsToTags.objects.create(
            jobs_id = 7,
            tags_id = 2
            ).save()
    JobsToTags.objects.create(
            jobs_id = 7,
            tags_id = 3
            ).save()

    JobsToTags.objects.create(
            jobs_id = 8,
            tags_id = 3
            ).save()
    JobsToTags.objects.create(
            jobs_id = 8,
            tags_id = 5
            ).save()
    JobsToTags.objects.create(
            jobs_id = 8,
            tags_id = 9
            ).save()
    JobsToTags.objects.create(
            jobs_id = 8,
            tags_id = 10
            ).save()

    JobsToTags.objects.create(
            jobs_id = 9,
            tags_id = 11
            ).save()

    JobsToTags.objects.create(
            jobs_id = 10,
            tags_id = 4,
            ).save()

    JobsToTags.objects.create(
            jobs_id = 11,
            tags_id = 4
            ).save()
    JobsToTags.objects.create(
            jobs_id = 11,
            tags_id = 9
            ).save()
    JobsToTags.objects.create(
            jobs_id = 11,
            tags_id = 10
            ).save()

    JobsToTags.objects.create(
            jobs_id = 12,
            tags_id = 4
            ).save()

    JobsToTags.objects.create(
            jobs_id = 13,
            tags_id = 1
            ).save()
    JobsToTags.objects.create(
            jobs_id = 13,
            tags_id = 2
            ).save()
    JobsToTags.objects.create(
            jobs_id = 13,
            tags_id = 3
            ).save()

    JobsToTags.objects.create(
            jobs_id = 15,
            tags_id = 1,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 15,
            tags_id = 3,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 15,
            tags_id = 8
            ).save()

    JobsToTags.objects.create(
            jobs_id = 17,
            tags_id = 1,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 17,
            tags_id = 2,
            ).save()
    JobsToTags.objects.create(
            jobs_id = 17,
            tags_id = 3
        ).save()
    JobsToTags.objects.create(
            jobs_id = 17,
            tags_id = 8
            ).save()

    JobsToTags.objects.create(
            jobs_id = 18,
            tags_id = 1
            ).save()

    JobsToTags.objects.create(
            jobs_id = 18,
            tags_id = 2
            ).save()
    JobsToTags.objects.create(
            jobs_id = 18,
            tags_id = 3
            ).save()
    JobsToTags.objects.create(
            jobs_id = 18,
            tags_id = 10
            ).save()

    JobsToTags.objects.create(
            jobs_id = 19,
            tags_id = 1
            ).save()
    JobsToTags.objects.create(
            jobs_id = 19,
            tags_id = 2
            ).save()
    JobsToTags.objects.create(
            jobs_id = 19,
            tags_id = 3
            ).save()

if __name__ == '__main__' :
    categorise()
