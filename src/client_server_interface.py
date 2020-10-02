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
	def send(self,status,msg,id):
		res = requests.post('http://127.0.0.1:5000/inbox', data = {'status':status,'ID':id, 'msg':msg})

		return res.txt




