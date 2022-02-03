import vk_api
import requests

token = 'dc3b103e698b4bdf006c09d92b3296c90435943486d2ca23a04a9dda68360695e805f2dcbffdf2c2763aa'

data = requests.get('https://api.vk.com/method/messages.getLongPollServer',
                    params={'access_token': token, 'v' : '5.131'}).json() # получение ответа от сервера

res = data['response']
server = res['server']
key = res['key']
ts = res['ts']

auth = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=3'.format(server=server, key=key, ts=ts)).json()
print(auth)

