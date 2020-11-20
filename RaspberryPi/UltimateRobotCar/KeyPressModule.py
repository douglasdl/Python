import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()    
    return ans


def main():
    if getKey('RIGHT'):
        print('Key RIGHT was pressed')
    if getKey('LEFT'):
        print('Key LEFT was pressed')    

if __name__ == '__main__':
    init()
    while True:
        main()