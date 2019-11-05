import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weWanted_u.settings")

import django
django.setup()

from company.models import Companies
from job.models     import Jobs, Categories, Tags, JobsToTags

def categorise() :

#    JobsToTags.objects.create(
#            jobs_id = 21,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 21,
#            tags_id = 17
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 21,
#            tags_id = 18
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 21,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 22,
#            tags_id = 1
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 22,
#            tags_id = 2
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 22,
#            tags_id = 3
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 22,
#            tags_id = 4
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 23,
#            tags_id = 16,
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 23,
#            tags_id = 17,
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 23,
#            tags_id = 18
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 24,
#            tags_id = 16,
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 24,
#            tags_id = 16,
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 25,
#            tags_id = 16
#        ).save()
#    JobsToTags.objects.create(
#            jobs_id = 25,
#            tags_id = 17
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 25,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 26,
#            tags_id = 16
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 27,
#            tags_id = 18
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 28,
#            tags_id = 16
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 28,
#            tags_id = 17
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 28,
#            tags_id = 18
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 29,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 29,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 30,
#            tags_id = 16
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 30,
#            tags_id = 17,
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 30,
#            tags_id = 18
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 30,
#            tags_id = 3
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 31,
#            tags_id = 16
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 31,
#            tags_id = 17
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 32,
#            tags_id = 15
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 32,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 32,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 33,
#            tags_id = 15
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 33,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 33,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 34,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 34,
#            tags_id = 17
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 34,
#            tags_id = 20
#        ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 35,
#            tags_id = 16
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 35,
#            tags_id = 20
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 16
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 23
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 24
#            ).save()
#
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 25
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 26
#            ).save()
#    JobsToTags.objects.create(
#            jobs_id = 36,
#            tags_id = 27
#            ).save()
#
 
    JobsToTags.objects.create(
            jobs_id = 36,
            tags_id = 28
            ).save()

    JobsToTags.objects.create(
            jobs_id = 37,
            tags_id = 17
            ).save()
    JobsToTags.objects.create(
            jobs_id = 37,
            tags_id = 23
            ).save()

    JobsToTags.objects.create(
            jobs_id = 37,
            tags_id = 24
            ).save()
    JobsToTags.objects.create(
            jobs_id = 37,
            tags_id = 22
            ).save()
    JobsToTags.objects.create(
            jobs_id = 37,
            tags_id = 17
            ).save()


    JobsToTags.objects.create(
            jobs_id = 38,
            tags_id = 16
            ).save()
    JobsToTags.objects.create(
            jobs_id = 38,
            tags_id = 17
            ).save()
    JobsToTags.objects.create(
            jobs_id = 38,
            tags_id = 18
            ).save()

    JobsToTags.objects.create(
            jobs_id = 40,
            tags_id = 15
            ).save()
    JobsToTags.objects.create(
            jobs_id = 40,
            tags_id = 16
            ).save()
    JobsToTags.objects.create(
            jobs_id = 40,
            tags_id = 20
            ).save()

 
    JobsToTags.objects.create(
            jobs_id = 41,
            tags_id = 17
            ).save()
    JobsToTags.objects.create(
            jobs_id = 41,
            tags_id = 25
            ).save()

if __name__ == '__main__' :
    categorise()
