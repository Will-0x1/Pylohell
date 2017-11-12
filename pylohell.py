import argparse

print("""
\033[32m██████╗ ██╗   ██╗██╗      ██████╗ \033[0;0m\033[31m██╗  ██╗███████╗██╗     ██╗     \033[0;0m     
\033[32m██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗\033[0;0m\033[31m██║  ██║██╔════╝██║     ██║     \033[0;0m
\033[32m██████╔╝ ╚████╔╝ ██║     ██║   ██║\033[0;0m\033[31m███████║█████╗  ██║     ██║     \033[0;0m
\033[32m██╔═══╝   ╚██╔╝  ██║     ██║   ██║\033[0;0m\033[31m██╔══██║██╔══╝  ██║     ██║     \033[0;0m
\033[32m██║        ██║   ███████╗╚██████╔╝\033[0;0m\033[31m██║  ██║███████╗███████╗███████╗\033[0;0m
""")
def Argumentos():
	global args
parser = argparse.ArgumentParser()
parser.add_argument("-e", dest="exploit", action="store", help="define o exploit que você irá usar!", required=False)
args = parser.parse_args()
pr = str(input("Escolha Uma Opção: "))
if pr == str('pyl'):
	print("Hello")
