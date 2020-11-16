from threading import Thread

def firstFunction():
    while True:
        for i in range(200):
            print(1000 + i)

def secondFunction():
    while True:
        for i in range(200):
            print(2000000 + i)

t1 = Thread(target = firstFunction)
t2 = Thread(target = secondFunction)

t1.start()
t2.start()

