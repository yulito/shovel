import os
import random
import time
import platform

limpiar = ""
sistema = platform.system()
if format(sistema) == "Windows":
        limpiar = "cls"
else:
        limpiar = "clear"
        
#figuras
t=chr(127998)
diam=chr(128313)
cala=chr(128128)

#bade del juego (tablero)
base=[[t,t,t,t],[t,t,t,t],[t,t,t,t],[t,t,t,t]]
v1=[["f","f","v","f"],["v","f","f","v"],["f","v","f","f"],["v","f","f","f"]]
v2=[["v","v","f","f"],["f","f","f","v"],["v","f","f","f"],["f","f","f","v"]]
v3=[["f","f","f","f"],["f","f","v","f"],["v","v","f","f"],["f","f","v","v"]]
v4=[["f","f","f","v"],["f","v","v","f"],["f","f","f","v"],["f","v","f","f"]]

#metiendo las versiones de matriz en un arreglo
arr=[v1,v2,v3,v4]
i=5
n=0

os.system(limpiar)

def reseteo():
	for z in range(4):
		for j in range(4):
			base[z][j]=t

def inicio():
	print("\033[1;35m"+"Bienvenido a SHOVEL")
	print("\033[1;34m"+"*******************\n")
	print("\033[1;36m"+"Tu mision es desenterrar \nlos 5 diamantes escondidos.\n"+"\033[0m")
	print("*) Escribe \"s\" para ingresar o \"x\" para salir.")


def tierra():
	print("***** VIDAS "+"\033[1;31m"+str(i)+"\033[0m"+" *****\n")
	print("   A "," B "," C "," D")
	print("1)"+base[0][0]+"  "+base[0][1]+"  "+base[0][2]+"  "+base[0][3])
	print("2)"+base[1][0]+"  "+base[1][1]+"  "+base[1][2]+"  "+base[1][3])
	print("3)"+base[2][0]+"  "+base[2][1]+"  "+base[2][2]+"  "+base[2][3])
	print("4)"+base[3][0]+"  "+base[3][1]+"  "+base[3][2]+"  "+base[3][3])

def perder(val):
	bool = 1
	if val == 0:
		bool = 0
	return bool

def ganar(g):
	cant = 1
	if g == 5:
		cant = 0
	return cant

while True:
	os.system(limpiar)
	inicio()
	opcion = input(">")
	if opcion =="s":
		os.system(limpiar)
		rn=random.randint(0,3)
		v=arr[rn]
		while True:
			tierra()
			c =0
			letra=input("Letra > ")
			if letra == "a" or letra == "b" or letra == "c" or letra == "d":
				if letra == "a":
					c=0
				elif letra == "b":
					c=1
				elif letra == "c":
					c=2
				else:
					c=3
				try:
					nro=int(input("Nro > "))
					nro = nro-1
					if nro >=0 and nro < 4:
						if v[nro][c]=="v":
							n+=1
							base[nro][c]=diam
							res = ganar(n)
							if res ==0:
								os.system(limpiar)
								tierra()
								print("\033[1;33m"+"*******************")
								print("\033[1;33m"+"** HAS GANADO!!! **")
								print("\033[1;33"+"*******************\n"+"\033[0m")
								time.sleep(4)
								reseteo()
								i=5
								n=0
								break
							else:
								os.system(limpiar)
						else:
							base[nro][c]=cala
							i-=1
							resp = perder(i)
							if resp == 0:
								os.system(limpiar)
								tierra()
								print("\033[1;31m"+"+++++++++++++++++++")
								print("\033[1;31m"+"+++ HAS PERDIDO +++")
								print("\033[1;31m"+"+++++++++++++++++++\n"+"\033[0m")
								time.sleep(4)
								reseteo()
								i=5
								n=0
								break
							else:
								os.system(limpiar)
					else:
						os.system(limpiar)
						print("-- Error de digito --\n")
				except:
					os.system(limpiar)
					print("-- Error de digito --\n")
			else:
				os.system(limpiar)
				print("-- Error de digito --\n")
	elif opcion == "x":
		break
	else:
		print("-- Error de digito --\n")
