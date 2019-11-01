import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weWanted_u.settings")

import django
django.setup()

from company.models import Companise


data_main   = requests.get('https://www.wanted.co.kr/api/v4/jobs?1572441251789&country=kr&tag_type_id=669&job_sort=job.latest_order&years=-1&locations=all', timeout=2).json()
jobs_url    = 'https://www.wanted.co.kr/api/v4/jobs/'

wanted_jobs_list = data_main['data']
jobs_url_list = [f"{jobs_url}{job['id']}" for job in wanted_jobs_list]


def company_and_jobs() :
    company_list = []
    unique_company_list = []

    for e in jobs_url_list :
        data_detail = requests.get(e, timeout=2).json()

        company_list.append(data_detail['job']['company']['id'])
        company_list = list(set(company_list))

    for e in jobs_url_list :
        data_detail = requests.get(e, timeout=2).json()
        
        for element in company_list :
            if element == data_detail['job']['company']['id'] :
                try :
                    Companise(
                        company_name  = data_detail["job"]["company"]["name"],
                        main_image    = data_detail['job']["company_images"][0]["url"],
                        logo_image    = data_detail['job']['logo_img']['origin'],
                        city          = data_detail['job']['address']['location'],
                        country       = data_detail['job']['address']['country'],
                        full_location = data_detail['job']['address']['full_location'],
                        lat           = data_detail['job']['address']["geo_location"]['location']['lat'],
                        lng           = data_detail['job']['address']["geo_location"]['location']['lng']
                    ).save()
                    company_list.remove(element)
                    
                except :
                    Companise(
                        company_name  = data_detail["job"]["company"]["name"],
                        main_image    = data_detail['job']["company_images"][0]["url"],
                        logo_image    = data_detail['job']['logo_img']['origin'],
                        city          = data_detail['job']['address']['location'],
                        country       = data_detail['job']['address']['country'],
                        full_location = data_detail['job']['address']['full_location']
                    ).save()
                    company_list.remove(element)

    
if __name__ == '__main__' :
    company_and_jobs()    
