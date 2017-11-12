import argparse

def Argumentos():
	global args
	parser = argparse.ArgumentParser()	
	parser.add_argument("-pyl", dest="exploit", action="store", help="define o exploit que você irá usar!", required=False)
	parser.add_argument("-Host", dest="host", action="store", help="define o seu ip que irá usar!", required=False)
	parser.add_argument("-Lport", dest="port", action="store", help="define a porta que irá usar!", required=False)
	args = parser.parse_args()
