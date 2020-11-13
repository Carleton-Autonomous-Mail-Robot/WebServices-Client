import requests

'''
	Interface class is the border of the system

	Maybe refactored out in the future, and incorporated into client_controller

	@Author Gabriel Ciolac
'''
class Interface:


	def __init__(self):
		self._tmp = ''
	'''
		Forwards a message to server
		@Author Gabriel Ciolac
	'''
	def send(self,status,msg,opperation,id):
		res = requests.post('https://provingrounds.ca/', json = {'status':status,'opperation':opperation,'clientID':id, 'payload':msg})
		print(res.text)
		return res.json()




