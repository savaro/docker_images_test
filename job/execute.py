import requests


API_ENDPOINT = 'https://api.alauda.cn/v1'

HEADERS = {
    'Content-Type': 'application/json'
}

def register_user():
    print '> Going to create new user'

    url = API_ENDPOINT + '/auth/register'
    data = {
        "username": "chennanfei",
        "password": "111111",
        "realname": "Chen Nanfei",
        "email": "chennanfei2006@163.com"
    }
    response = requests.post(url, json=data, headers=HEADERS)
    print '> Result: status={}, content={}'.format(response.status_code,
                                                   response.content)


def trigger_build():
    print '> Going to trigger new build'

    url = API_ENDPOINT + '/builds'
    data = {
        "namespace": "chennanfei",
        "repo_name": "docker_images_test",
        "tag": "latest"
    }
    response = requests.post(url, json=data, headers=HEADERS)
    print '> Result: status={}, content={}'.format(response.status_code,
                                                   response.content)


def run():
    register_user()
    trigger_build()


run()
