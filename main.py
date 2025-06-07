import pygame
pygame.init()

back = (200, 255, 255) #cor do fundo
mw = pygame.display.set_mode((500,500)) #janela principal com o tamanho 500x500 pixels
mw.fill(back) #preenchimento com a cor de fundo
clock = pygame.time.Clock() #responsável por contar o tempo da aplicação

class Area():
    def __init__(self, x= 0, y= 0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    
    def color(self, new_color): #método para a mudança de cor
        self.fill_color = new_color
    
    def fill(self): #preencher com a nova cor
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def collidepoint(self, x, y): #método para identificar colisões de objetos em movimento
        return self.rect.collidepont(x, y)
    
    def colliderect(self, rect): #método identifica colisões de retângulos estáticos
        return self.rect.colliderect(rect)
    
class Picture(Area):
    def __init__ (self, filename, x= 0, y = 0, width =10, height = 10): #construtor da classe
        Area.__init__(self, x=x, y=y, width=width, height=height, color = None) #construtor da superclasse (classe pai)
        self.image = pygame.image.load(filename)
    
    def draw(self): #desenhar o objeto em determinado ponto do ecrã
        mw.blit(self.image, (self.rect.x, self.rect.y))


racket_x = 200
racket_y = 300

game_over = False

#criar a bola e a plataforma
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)


#criação dos inimigos
start_x = 5
start_y = 5
count = 9 #número de monstros na linha de cima
monsters = [] #uma lista vazia

for j in range(3): #j é o número de linhas
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range(count):
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d) #adicionar os monstros a lista
        x = x + 55 #adicionar a distância entre os monstros
    count -= 1

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_ESC:
                game_over = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_LEFT:
                pass
    for m in monsters:
        m.draw()
    
    platform.draw()
    ball.draw()

    pygame.display.update() #atualização da cena
    clock.tick(40) #taxa de fps
