import os
from math import sin, radians, degrees, copysign
import pygame
from pygame.math import Vector2


class Game:
    

    def __init__(self):
        pygame.init()
        global black, white, red, green, blue, bright_red, bright_green, block_color
        # Standard Colors 
        black = (0,0,0)
        white = (255,255,255)
        red = (200,0,0)
        green = (0,200,0)
        blue = (0, 0, 200)
        bright_red = (255,0,0)
        bright_green = (0,255,0)
        block_color = (53,115,255)

        carImg = pygame.image.load('robotCar.png') # Load Images
        gameIcon = pygame.image.load('robotCar.png') # Load Images
        pygame.display.set_icon(gameIcon) # Icone 
        pygame.display.set_caption('Robot Car Simulation') # Screen Title
        width = 1280 # Screen Size
        height = 720 # Screen Size
        self.screen = pygame.display.set_mode((width, height)) # Create the screen
        self.clock = pygame.time.Clock() # Create the clock
        self.ticks = 60
        self.exit = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "robotCar.png")
        car_image = pygame.image.load(image_path)
        car = Car(100, 100)
        ppu = 32

        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:    
                    car.acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:    
                    car.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if car.velocity.x != 0:
                    car.acceleration = copysign(car.max_acceleration, -car.velocity.x)        
            else:
                car.acceleration = 0

            # Limit the acceleration
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))    

            # Limit the steering
            if pressed[pygame.K_RIGHT]:
                car.steering -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 30 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))


            # Logic
            car.update(dt)
            
            # Drawing
            self.screen.fill(black)
            rotated = pygame.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, car.position - (rect.width / 2, rect.height / 2))
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()        


class Car:
    def __init__(self, x, y, angle = 0.0, length = 4, max_steering = 30, max_acceleration = 5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_steering = max_steering
        self.max_acceleration = max_acceleration
        self.max_velocity = 20
        self.brake_deceleration = 10

        self.acceleration = 0.0
        self.steering = 0.0

    # Linear movement
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        # Steering
        # If Steering angle is zero -> angular velocity is zero too
        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt

    # User input

        


def init():
    

   #global screen_width, screen_height, black, white, red, green, bright_red, bright_green, block_color, car_width, window, clock, carImg, gameIcon, TextSurf, TextRect
 
    

    # Car Size
    car_width = 73
    

    # Load Images
    carImg = pygame.image.load('racecar.png')
    gameIcon = pygame.image.load('racecar.png')

    

    pause = False
    #crash = True


def car(x,y):
    window.blit(carImg,(x,y))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()    
    return ans

def game_intro():

    intro = True

    window.fill(white)
    #largeText = pygame.font.SysFont("comicsansms",115)
    #TextSurf, TextRect = text_objects("A bit Racey", largeText)
    #TextRect.center = ((screen_width/2),(screen_height/2))
    #window.blit(TextSurf, TextRect)


def game_loop():
    global pause

    x = (screen_width * 0.45)
    y = (screen_height * 0.7)

    x_change = 0
    y_change = 0

    gameExit = False
 
    while not gameExit:
        if getKey('w'):
            y_change = -0.5
            #return print(x)
        elif getKey('s'):
            y_change = 0.5
            #return print(x) 
        elif getKey('d'):
            x_change = 0.5 
        elif getKey('a'):
            x_change = -0.5
        else:
            x_change = 0
            y_change = 0    


        x += x_change
        y += y_change
        window.fill(white)
        car(x, y)

"""
def main():
    #game_intro()
    game_loop()
    #pygame.quit()
    #quit()
    
    #if getKey('UP'):
    #    return print('Key UP was pressed')
    #if getKey('DOWN'):
    #    return print('Key DOWN was pressed') 
    #if getKey('RIGHT'):
    #    return print('Key RIGHT was pressed') 
    #if getKey('LEFT'):
    #    return print('Key LEFT was pressed')
"""    
"""
    if getKey('w'):
        return print('Key [w] was pressed')
    if getKey('s'):
        return print('Key [s] was pressed') 
    if getKey('a'):
        return print('Key [a] was pressed') 
    if getKey('d'):
        return print('Key [d] was pressed') 
    if getKey('q'):
        return print('Key [q] was pressed') 
    if getKey('e'):
        return print('Key [e] was pressed')

    if getKey('t'):
        return print('Key [t] was pressed')
    if getKey('g'):
        return print('Key [g] was pressed') 
    if getKey('f'):
        return print('Key [f] was pressed') 
    if getKey('h'):
        return print('Key [h] was pressed') 
    if getKey('r'):
        return print('Key [r] was pressed') 
    if getKey('y'):
        return print('Key [y] was pressed')    

    if getKey('i'):
        return print('Key [i] was pressed') 
    if getKey('k'):
        return print('Key [k] was pressed')    
    if getKey('j'):
        return print('Key [j] was pressed') 
    if getKey('l'):
        return print('Key [l] was pressed') 
    if getKey('u'):
        return print('Key [u] was pressed') 
    if getKey('o'):
        return print('Key [o] was pressed')                                                      
"""

if __name__ == '__main__':
    game = Game()
    game.run()
    