import requests

def parse() :
    data_main   = requests.get('https://www.wanted.co.kr/api/v4/jobs?1572441251789&country=kr&tag_type_id=669&job_sort=job.latest_order&years=-1&locations=all', timeout=2).json()
    jobs_url    = 'https://www.wanted.co.kr/api/v4/jobs/'
    wanted_jobs_list = data_main['data']

    jobs_url_list = [f"{jobs_url}{job['id']}" for job in wanted_jobs_list]
   
    #data_detail = requests.get(jobs_url_list[0]).json()
    #print(data_detail['job']['company']['name'])
   
    company_info_list = []
    for el in jobs_url_list :
        data_detail = requests.get(el, timeout=2).json()
        company_info_list.append(
            {
                'company_name'  : data_detail["job"]["company"]["name"],
                'main_img'      : data_detail['job']["company_images"][0]["url"],
                'logo_img'      : data_detail['job']['logo_img']['origin'],
                'city'          : data_detail['job']['address']['location'],
                'country'       : data_detail['job']['address']['country'],
                'full_location' : data_detail['job']['address']['full_location'],
                'lat'           : data_detail['job']['address']["geo_location"]['location']['lat'],
                'lng'           : data_detail['job']['address']["geo_location"]['location']['lng'],
            }
        )
    print(company_info_list[0])

            

    
if __name__ == '__main__' :
    parse()    
    



