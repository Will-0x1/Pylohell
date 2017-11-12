import function
import sys

print("""
\033[32m██████╗ ██╗   ██╗██╗      ██████╗ \033[0;0m\033[31m██╗  ██╗███████╗██╗     ██╗     \033[0;0m     
\033[32m██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗\033[0;0m\033[31m██║  ██║██╔════╝██║     ██║     \033[0;0m
\033[32m██████╔╝ ╚████╔╝ ██║     ██║   ██║\033[0;0m\033[31m███████║█████╗  ██║     ██║     \033[0;0m
\033[32m██╔═══╝   ╚██╔╝  ██║     ██║   ██║\033[0;0m\033[31m██╔══██║██╔══╝  ██║     ██║     \033[0;0m
\033[32m██║        ██║   ███████╗╚██████╔╝\033[0;0m\033[31m██║  ██║███████╗███████╗███████╗\033[0;0m
""")
function.Argumentos()

pr = str(input("Escolha Uma Opção: "))  
if pr == str('-pyl'):
	print("""Selecione Qual Exploit Deseja Utilizar
	 MsfVenom - Exploit 	use/exploit/msf
	 Web-Delivery - Exploit use/exploit/web
		""")
	pr2 = str(input("pylohell>> "))
else:
	print("Exploit Não Econtrado")
	sys.exit(0)

if pr2 == str('use/exploit/msf'):
	host  = str(input("Host: "))
	port = int(input("LPORT: "))
	print("""Payloads
			1 - Python
			2 - Windows
			3 - Php
			4 - Android/Apk
			5 - Mac/Os
			6 - Linux
			7 - ASP
			8 - Bash
			9 - Perl
		""")
	pay = str(input("Payload: "))
	print(pay)#FIMt(0)
#Aqui tem o if





#Fim Do IF
if pr2 == str('use/exploit/web'):
	host2  = str(input("Host: "))
	port2 = int(input("LPORT: "))
	print("""Payloads
			1 - Python
			2 - Windows
			3 - Php
		 """)
	pay2 = str(input("Payload: "))
	print(pay2)#FIM
#Aqui tem o if




#Fim Do if
