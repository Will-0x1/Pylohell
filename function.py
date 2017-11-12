import argparse

def Argumentos():
	global args
	parser = argparse.ArgumentParser()	
	parser.add_argument("-pyl", dest="exploit", action="store", help="define o exploit que você irá usar!", required=False)
	parser.add_argument("-use", dest="payload", action="store", help="define o payload que irá usar!", required=False)
	parser.add_argument("-host", dest="host", action="store", help="define o seu ip que deseja utilizar no payload!", required=False)
	

	args = parser.parse_args()
