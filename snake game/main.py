import pygame
from pygame.locals import *
import time
import random
size = 20




class Block :
    
    
    
     def __init__(self , parent_screen) :
        self.image = pygame.image.load("rec\images.jpg").convert()
        self.image = pygame.transform.scale(self.image,[20,20])
        self.parent_screen = parent_screen
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size
    
    
    
     def draw (self) :
        
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    
    
    
    
     def move(self) :
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size






class Apple :
    
    
    
    def __init__(self , parent_screen) :
        self.image = pygame.image.load("rec\download.png").convert()
        self.image = pygame.transform.scale(self.image,[20,20])
        self.parent_screen = parent_screen
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size
    
    
    
    
    def draw (self) :
        
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    
    
    
    
    def move(self) :
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size






class AppleB :




    def __init__(self , parent_screen) :
        self.image = pygame.image.load("rec\images(1).jpg").convert()
        self.image = pygame.transform.scale(self.image,[20,20])
        self.parent_screen = parent_screen
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size


    def draw (self) :
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()


    def move(self) :
        self.x = random.randint(0,29)*size
        self.y = random.randint(0,29)*size
            


class Snake :
    
    
    def __init__(self , parent_screen , length , lengthB) :
        self.length = length
        self.lengthB = lengthB
        self.parent_screen = parent_screen
        self.block = pygame.image.load("rec\png-transparent-bricks-block-cube-super-mario-nintendo-pattern-game-mario-bros-smash-video-game.png").convert()
        self.block = pygame.transform.scale(self.block,[20,20])
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'right'
    
    
    def draw(self) : 
        self.parent_screen.fill(( 108, 171, 221 ))
        for i in range(self.length) :
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    
    
    def increase_length(self) :
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    
    
    def increase_lengthB(self) :
        self.lengthB += 5
        self.x.append(-1)
        self.y.append(-1)
        
    
    
    def move_left(self) :
        self.direction = 'left'
    
    
    def move_right(self) :
        self.direction = 'right'
    
    
    def move_up(self) :
        self.direction = 'up' 
    
    
    def move_down(self) :
        self.direction = 'down'
    
    
    def walk(self) :
        for i in range (self.length - 1 , 0 ,-1) :
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]    
        if self.direction == 'up' :
            self.y[0] -= size
        if self.direction == 'down' :
            self.y[0] += size
        if self.direction == 'right' :
            self.x[0] += size
        if self.direction == 'left' :
            self.x[0] -= size 
        
        self.draw()
            


class Game :
    
    
    def __init__(self) :
        pygame.init()
        self.surface = pygame.display.set_mode((600,600))
        self.surface.fill(( 108, 171, 221 ))
        self.snake = Snake(self.surface , 1 , 0)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.block = Block(self.surface)
        self.block.draw()
        self.appleB = AppleB(self.surface)
        self.appleB.draw()
    
    
    def is_collision(self,x1,y1,x2,y2) :
        if x1 >= x2 and x1 < x2 + size :
            if y1 >= y2 and y1 < y2 + size :
                return True
        if x1 < 0 or y1 < 0 or x1 > 600 or y1 > 600 :
            return True

        return False
    
    
    
    def display_score(self) :
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"your score : {self.snake.length + self.snake.lengthB}" , True , (255,255,255))
        self.surface.blit(score , (50 , 10))
    
    
    
    def show_game_over(self) :
        self.surface.fill(( 108, 171, 221 ))
        font = pygame.font.SysFont('arial',30)
        line1 = font.render("Press enter to play again or escape to exit!",True,(255, 198, 89))
        self.surface.blit(line1 , (90,300))
        line2 = font.render("Red Apples = 1   White Apples = 2 ",True,(255, 198, 89))
        self.surface.blit(line2 , (90,350))
        line3 = font.render("Be aware of the blocks!",True,(255, 198, 89))
        self.surface.blit(line3 , (90,400))
        pygame.display.flip()
    
    
    
    def reset(self) :
        self.snake = Snake(self.surface , 1 , 0)
        self.apple = Apple(self.surface)
        self.block = Block(self.surface)
        self.appleB = AppleB(self.surface)
    
    
    
    def play(self) :
        self.snake.walk()
        self.apple.draw()
        self.appleB.draw()
        self.block.draw()
        self.display_score()
        pygame.display.flip()
        
        
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y) :
            self.snake.increase_length()
            self.apple.move()  
            
        
        for i in range (3,self.snake.length) :
            if self.is_collision(self.snake.x[0],self.snake.y[0] ,self.snake.x[i],self.snake.y[i]) :
               raise "Game over"

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.block.x, self.block.y):
            self.block.move()
            raise "Game over"

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.appleB.x, self.appleB.y):
            self.snake.increase_lengthB()
            self.snake.increase_length()
            self.appleB.move()
        
        
        
        
    def run(self):
        pause = False 
        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        running = False 
                    if event.key == K_RETURN :
                        pause = False
                    if not pause :
                        if event.key == K_UP :
                            self.snake.move_up()
                        if event.key == K_DOWN :
                            self.snake.move_down()
                        if event.key == K_RIGHT :
                            self.snake.move_right()
                        if event.key == K_LEFT :
                            self.snake.move_left()
                elif event.type == QUIT : 
                   running = False
            try: 
                if not pause :          
                    self.play()
            except Exception as e :
                self.show_game_over()
                pause = True
                self.reset()
            
            time.sleep(0.2)
   
if __name__ == "__main__" :
    game = Game()
    game.run()
    
             
            
         
 