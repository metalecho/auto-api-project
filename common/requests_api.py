import requests
import configparser
import os


config_path = os.getcwd()
file_path = os.path.dirname(config_path)
config_file = file_path + '\\configfile.ini'
conf = configparser.ConfigParser()
conf.read(config_file)

url_head = conf.get('requests_setting','url_head')


class request_method():
    def __init__(self):
        pass

    def auto_get(self,url=None,params=None,headers=None,allow_redirects=True):
        all_url = str(url_head) + str(url)
        print(all_url)
        get_response = requests.get(url=all_url,headers=headers,params=params,allow_redirects=allow_redirects)
        return get_response.url,get_response.text

    def auto_post(self,url=None,data=None,headers=None,allow_redirects=True):
        all_url = str(url_head) + str(url)
        post_response = requests.post(url=all_url, headers=headers, data=data,allow_redirects=allow_redirects)
        return post_response.status_code, post_response.json()



if __name__ == '__main__':
    a = request_method().auto_get(url='/api/user/stu_info',params='stu_name=黑黑',headers='',allow_redirects=False)
    print(a[0])
    print(type(a[1]))
    data = {'username':'niuhanyang','passwd':'aA123456'}
    headers = {'Accept':'*/*'}
    # b = request_method().auto_post(url='/api/user/login',data=data,headers=headers,allow_redirects=False)
    # print(b[0])
    # print(type(b[1]))


