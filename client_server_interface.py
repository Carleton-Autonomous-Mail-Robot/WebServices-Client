import requests


class Interface:

	def __init__(self):
		self._tmp = ''

	def send(self,status,msg,id):
		res = requests.post('http://127.0.0.1:5000/inbox', data = {'status':status,'ID':id, 'msg':msg})

		print(res.text)




