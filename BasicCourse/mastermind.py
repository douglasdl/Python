# coding:utf-8

import random
a = random.randint(0, 9)


beat = 0
blow = 0
senha = "3945"
tentativa = input("Tentativa: ")
status = "????"
turn = 0

def printPlay(senha, tentativa):
	print("**********\n*  " + senha + "  *\n**********")
	print("Turn: " + str(turn) + "\tTentativa: " + tentativa)

	print(status)

def checkPlay():
	for n in senha:
	    for t in tentativa:
	        if n == t:
	            #print(t)

while beat < 4:
	turn += 1
checkPlay()
printPlay(senha, tentativa)
print("GAME OVER")