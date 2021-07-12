import pygame
import random
import time

from pygame.constants import MOUSEBUTTONUP

pers = [0]
diced = [0]
turn = [0]
lastdice = 0
b = [101, 102, 103, 104]
g = [101, 102, 103, 104]
y = [101, 102, 103, 104]
r = [101, 102, 103, 104]
together = [b, g, y, r]
lim = [40, 10, 20, 30]

class ApplyPos:
    faor_listxy = [[0],[0],[0],[0]]
    try:
        clickables = [((faor_listxy[0]).collidepoint(pygame.mouse.get_pos())),((faor_listxy[1]).collidepoint(pygame.mouse.get_pos())),
                      ((faor_listxy[2]).collidepoint(pygame.mouse.get_pos())),((faor_listxy[3]).collidepoint(pygame.mouse.get_pos()))]
    except AttributeError:
        pass

class Dice:
    dice_list = ['dataelipse\dices\dices1.png','dataelipse\dices\dices2.png','dataelipse\dices\dices3.png','dataelipse\dices\dices4.png','dataelipse\dices\dices5.png','dataelipse\dices\dices6.png']

class Color:
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    red = (255,0,0)
    white = (255,255,255)
    black = (0,0,0)

class Spots:
    blue_seat = [[847,55],[847,142],[935,55],[935,142]]
    green_seat = [[847,844],[847,933],[935,844],[935,933]]
    yellow_seat = [[58,844],[58,933],[146,844],[146,933]]
    red_seat = [[58,55],[58,142],[145,55],[146,142]]
    seat_set = [blue_seat,green_seat,yellow_seat,red_seat]

    blue_goal = [[496,143],[496,231],[496,319],[496,407]]
    green_goal = [[847,493],[760,493],[671,493],[584,493]]
    yellow_goal = [[496,844],[496,757],[496,669],[496,580]]
    red_goal = [[146,493],[233,493],[320,493],[409,493]]
    goal_set = [blue_goal,green_goal,yellow_goal,red_goal]

    color_set = [Color.blue,Color.green,Color.yellow,Color.red]
    on_row = [[585,55],[585,143],[585,231],[585,319],[585,407],[673,407],[761,407],[849,407],[937,407],[937,495],
              [937,583],[849,583],[761,583],[673,583],[585,583],[585,671],[585,759],[585,847],[585,933],[497,933],
              [409,933],[409,847],[409,759],[409,671],[409,583],[320,583],[233,583],[146,583],[58,583],[58,495],
              [58,407],[146,407],[233,407],[320,407],[409,407],[409,319],[409,231],[409,143],[409,55],[497,55]]

class Roll:
    def __init__(self, col : int, screen):
        self.col = col
        self.c = together[col]
        self.screen = screen
        self.d = diced[0]


def is3rolls():
        count = 0
        for i in R1.c:
            if i > 100:
                count += 1
            elif i < 0 and R1.someinfront(R1.c[i]):
                count += 1
            else:
                count -= count
        if count == 4:
            return True
        else:   
            return False

def roll():
        diced[0] = random.randint(1,6)

def dicerollanimation():
        times = [0.2,0.4,0.7,1.1]
        diceslist = [0,1,2,3,4,5]
        templastdice = 0
        for i in range(4):
            templist = []
            for f in diceslist:
                if f != templastdice:
                    templist.append(f)
            b = int(random.choice(templist))
            templastdice -= templastdice + b
            image = Dice.dice_list[b]
            dice_image = pygame.image.load(image).convert_alpha()
            screen.blit(dice_image,[458,456])
            pygame.display.update()
            time.sleep(times[i])


def awaitmove():
    picked = 0
    while True:
        click1 = ApplyPos.clickables[0]
        click2 = ApplyPos.clickables[1]
        click3 = ApplyPos.clickables[2]
        click4 = ApplyPos.clickables[3]
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP and click1 == 1:
            break
        elif ev.type == pygame.MOUSEBUTTONUP and click2 == 1:
            picked = 1
            break
        elif ev.type == pygame.MOUSEBUTTONUP and click3 == 1:
            picked = 2
            break
        if ev.type == pygame.MOUSEBUTTONUP and click4 == 1:
            picked = 3
            break
    pers[0] = picked
    if not check_for_even():
        return
    apply_to_board()

def even_possible():
        count = 0
        for i in range(4):
            if not check_for_even():
                count += 1
        if count == 4:
            return False
        return True

def awaitdice():
    ev = pygame.event.wait()
    while True:
        rectan = pygame.Rect((458,456),(74,74))
        clickdice = rectan.collidepoint(pygame.mouse.get_pos())
        if ev.type == pygame.MOUSEBUTTONUP and clickdice == 1:
            break
    dicerollanimation()
    roll()
    img = Dice.dice_list[diced-1]
    dice_end = pygame.image.load(img).convert_alpha()
    clickdice = dice_end.collidepoint(pygame.mouse.get_pos())
    screen.blit(dice_end,[458,456])
    if not even_possible():
        return
    awaitmove()
    return

def do3rolls():
        count = 0
        for i in range(3):
            while awaitdice() == 6:
                count += 1
            if count > 0:
                break

def someinfront(i):
        if int(str(i)[2]) == -4:
            return True
        if not -4 in (-int(str(R1.c[0])[2]),-int(str(R1.c[1])[2]),-int(str(R1.c[2])[2]),-int(str(R1.c[3])[2])):
            return False
        if int(str(i)[2]) == -3:
            return True
        if not -3 in (-int(str(R1.c[0])[2]),-int(str(R1.c[1])[2]),-int(str(R1.c[2])[2]),-int(str(R1.c[3])[2])):
            return False
        if int(str(i)[2]) == -2:
            return True
        if not -2 in (-int(str(R1.c[0])[2]),-int(str(R1.c[1])[2]),-int(str(R1.c[2])[2]),-int(str(R1.c[3])[2])):
            return False
        if int(str(i)[2]) == -1:
                return True
        return False

def check_for_even():
        D = lim[together.index[R1.c]]
        A = (D - R1.c[pers[0]]) + R1.d
        F = together.index[R1.c] * 10
        if R1.c[pers[0]] > 100:
            if not spot_okay(F+1)[0]:
                return False
            return True
        elif R1.c[pers[0]] < 0 and int(str(R1.c[pers[0]] - R1.d)[2]) < 5:
            if not spot_okay(R1.c[pers[0]] - R1.d)[0]:
                return False
            return True
        elif R1.c[pers[0]] <= D and R1.c[pers[0]] + R1.d > D:
            if not spot_okay(-A)[0]:
                return False
            return True
        elif R1.c[pers[0]] > 0 and R1.c[pers[0]] < 41:
            if not spot_okay(A):
                return False
            if (R1.c[pers[0]] + R1.d) < 41 and (R1.c[pers[0]] + R1.d) > 0:
                if not spot_okay(R1.c[pers[0]] + R1.d):
                    return False
            return True
        return False

def bump_spot(n):
        for i in together:
            if i == R1.c:
                continue
            for j in range(4):
                if n == i[j]:
                    r = i.index[j] + 1
                    i[j] == 100 + (together.index[i] * 10) + r
                    return

def spot_okay(n):
        for j in R1.c:
            if n == j:
                return False

def print_color():
        if R1.c == b:
            return "blue"
        elif R1.c == g:
            return "green"
        elif R1.c == y:
            return "yellow"
        elif R1.c == r:
            return "red"

def apply_to_board():
        D = lim[together.index[R1.c]]
        A = (D - R1.c[pers[0]]) + R1.d
        F = together.index[R1.c] * 10
        if R1.c[pers[0]] > 100 and R1.d == 6:
            R1.c[pers[0]] = F+1
            bump_spot(R1.c[pers[0]])
            refresh_display()
            return
        elif R1.c[pers[0]] < 0 and int(str(R1.c[pers[0]] - R1.d)[2]) < 5:
            R1.c[pers[0]] -= R1.d
            refresh_display()
            return 
        elif R1.c[pers[0]] <= D and R1.c[pers[0]] + R1.d > D:
            R1.c[pers[0]] = -A
            bump_spot(R1.c[pers[0]])
            refresh_display()
            return 
        elif R1.c[pers[0]] > 0 and R1.c[pers[0]] < 41:
            if (R1.c[pers[0]] + R1.d) > 40:
                R1.c[pers[0]] = A
            else:
                R1.c[pers[0]] += R1.d
            bump_spot(R1.c[pers[0]])
            refresh_display()
            return

def refresh_display():
        Board = pygame.image.load("dataelipse\prints\Board.png").convert_alpha()
        background_white = pygame.image.load("dataelipse\prints\whiteback.jpg").convert_alpha()
        screen.blit(background_white, [0,0])
        screen.blit(Board, [0,0])
        for s in range(4):
            for i in range(4):
                b = together[s][i]
                if b > 100:
                    n = Spots.seat_set[s][int(str(b)[2])-1]
                elif b < 41 and b > 0:
                    n = Spots.on_row[b-1]
                elif b < 0:
                    n = Spots.goal_set[s][-(b) - 1]
                DERI = pygame.draw.circle(screen, Color.black, n, 22)
                if together.index(together[s]) == turn[0]:
                    ApplyPos.faor_listxy[i] = pygame.Rect(DERI)
                pygame.draw.circle(screen, Spots.color_set[s], n, 20)
        pygame.display.update()


def end(delta):
    for i in together:
        if sum(i) == -10:
            return delta == True
    return delta == False

def change_turn():
    last_turn = turn.pop[0]
    if last_turn < 3:
        turn.append((last_turn+1))
    elif last_turn == 3:
        turn.append(0)    

#GUI change
"""
programIcon = pygame.image.load('dataelipse\icons\setting.png')
pygame.display.set_icon(programIcon)
pygame.init()
screen1 = pygame.display.set_mode((300, 200))
inputed = False
pygame.display.set_caption('Settings')

while not inputed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inputed = True
    screen1.fill(Color.black)
    pygame.display.update()"""

#Game starts
programIcon = pygame.image.load('dataelipse\Icons\maednicon.jpg')
startdice = pygame.image.load('dataelipse\dices\dices3.png')
pygame.display.set_icon(programIcon)
pygame.init()
screen = pygame.display.set_mode((990, 986))
pygame.display.set_caption('Mensch Ärger Dich Nicht')
refresh_display()
screen.blit(startdice,[458,456])

end = False

while not end:
    R1 = Roll(turn[0], screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    if not is3rolls():
        awaitdice()
    else:
        do3rolls()
    change_turn()
    refresh_display()
    end(end)