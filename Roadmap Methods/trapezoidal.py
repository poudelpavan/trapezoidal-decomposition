'''
Created on Feb 11, 2017

@author: Pavan
'''

import pygame

pygame.init()

obstacle = pygame.Rect(180, 200, 300, 200)
obstacle1 = pygame.Rect(600, 300, 10, 200)
obstacle2 = pygame.Rect(400, 490, 200, 10)

image_source = pygame.image.load('robot.bmp')
image_dest = pygame.image.load('dest.bmp')

font = pygame.font.SysFont("comicsansms", 12, bold=True)
font1 = pygame.font.SysFont("verdana", 14, bold=True)

c1 = font.render("C1", True, (128, 128, 128))
c2 = font.render("C2", True, (128, 128, 128))
c3 = font.render("C3", True, (128, 128, 128))
c4 = font.render("C4", True, (128, 128, 128))
c5 = font.render("C5", True, (128, 128, 128))
c6 = font.render("C6", True, (128, 128, 128))
c7 = font.render("C7", True, (128, 128, 128))
c8 = font.render("C8", True, (128, 128, 128))
c9 = font.render("C9", True, (128, 128, 128))
c10 = font.render("C10", True, (128, 128, 128))
c11 = font.render("C11", True, (128, 128, 128))


textSuccess = font.render(
    "GREAT! Robot Successfully reached to the destination.", True, (0, 128, 0))
textFailure = font.render(
    "SORRY! Robot could not reach to destination.", True, (128, 0, 0))
textTitle = font1.render(
    "ROBOTIC MOTION PLANNING: Trapezoidal Decomposition Method", True, (0, 0, 0))

cc1 = cc2 = cc3 = cc4 = cc5 = cc6 = cc7 = cc8 = cc9 = cc10 = cc11 = 0
path_c = []


class Robot(object):

    def SetCount(self, a):
        if(a == 1):
            global cc1
            cc1 += 1
            path_c.append((150, 150))
        elif(a == 2):
            global cc2
            cc2 += 1
            path_c.append((270, 100))
        elif(a == 3):
            global cc3
            cc3 += 1
            path_c.append((250, 500))
        elif(a == 4):
            global cc4
            cc4 += 1
            path_c.append((400, 160))
        elif(a == 5):
            global cc5
            cc5 += 1
            if(cc5 == 1):
                path_c.append((250, 500))
            elif(cc5 == 2):
                path_c.append((350, 427))
        elif(a == 6):
            global cc6
            cc6 += 1
            path_c.append((400, 380))
        elif(a == 7):
            global cc7
            cc7 += 1
            if(cc7 == 2):
                path_c.append((430, 280))
            else:
                path_c.append((430, 75))
        elif(a == 8):
            global cc8
            cc8 += 1
            path_c.append((570, 160))
        elif(a == 9):
            global cc9
            cc9 += 1
            path_c.append((400, 160))
        elif(a == 10):
            global cc10
            cc10 += 1
            if(cc10 == 1):
                path_c.append((350, 550))
            else:
                path_c.append((350, 550))
                path_c.append((250, 500))
                path_c.append((150, 450))
                path_c.append((75, 375))
        elif(a == 11):
            global cc11
            cc11 += 1
            if(len(path_c) == 1):
                path_c.append((570, 460))
            else:
                path_c.append((685, 160))
                path_c.append((685, 460))
                path_c.append((570, 460))

    def GetCount(self, a):
        if(a == 1):
            return cc1
        elif(a == 2):
            return cc2
        elif(a == 3):
            return cc3
        elif(a == 4):
            return cc4
        elif(a == 5):
            return cc5
        elif(a == 6):
            return cc6
        elif(a == 7):
            return cc7
        elif(a == 8):
            return cc8
        elif(a == 9):
            return cc9
        elif(a == 10):
            return cc10
        elif(a == 11):
            return cc11

    def drawGridLine(self):

        pygame.draw.polygon(
            screen, 0xffff44, ((150, 300), (270, 200), (400, 320), (250, 400)))
        pygame.draw.polygon(
            screen, 0xffff44, ((430, 150), (570, 320), (350, 500), (510, 320)))
        pygame.draw.line(screen, 0xffffff, (150, 0), (150, 600), 2)
        pygame.draw.line(screen, 0xffffff, (250, 400), (250, 600), 2)
        pygame.draw.line(screen, 0xffffff, (270, 0), (270, 200), 2)
        pygame.draw.line(screen, 0xffffff, (350, 345), (350, 600), 2)
        pygame.draw.line(screen, 0xffffff, (400, 0), (400, 442), 2)
        pygame.draw.line(screen, 0xffffff, (430, 0), (430, 408), 2)
        pygame.draw.line(screen, 0xffffff, (570, 0), (570, 600), 2)
        screen.blit(image_source, (start_x, start_y))
        screen.blit(image_dest, (end_x, end_y))
        screen.blit(textTitle, (150, 20))
        screen.blit(c1, (100, 300))
        screen.blit(c2, (200, 150))
        screen.blit(c3, (200, 400))
        screen.blit(c4, (320, 160))
        screen.blit(c5, (300, 390))
        screen.blit(c6, (360, 360))
        screen.blit(c7, (410, 290))
        screen.blit(c8, (500, 220))
        screen.blit(c9, (450, 320))
        screen.blit(c10, (500, 500))
        screen.blit(c11, (620, 300))

    def IsInside(self, x, y, x1, y1, x2, y2, x3, y3):
        sign = (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
        sign1 = ((x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)) <= 0
        sign2 = ((x - x3) * (y2 - y3) - (x2 - x3) * (y - y3)) <= 0
        sign3 = ((x - x1) * (y3 - y1) - (x3 - x1) * (y - y1)) <= 0
        return ((sign1 == sign2) and (sign2 == sign3))

    def IsInsideObstacle(self, x, y):
        a1 = Robot().IsInside(x, y, 150, 300, 270, 200, 400, 320)
        a2 = Robot().IsInside(x, y, 150, 300, 250, 400, 400, 320)
        a3 = Robot().IsInside(x, y, 430, 150, 570, 320, 510, 320)
        a4 = Robot().IsInside(x, y, 350, 500, 570, 320, 510, 320)
        return (a1 or a2 or a3 or a4)

    def CheckBlock(self, x, y):
        if(x <= 0 or y <= 0 or x >= 800 or y >= 600):
            return 0
        elif(x < 150):
            return 1
        elif(x < 250 and y > 300):
            return 3
        elif(x < 270 and y < 300):
            return 2
        elif(x < 350 and y > 345):
            return 5
        elif(x < 400 and y > 320 and y < 500 and Robot().IsInside(x, y, 350, 500, 570, 320, 570, 500) == False):
            return 6
        elif(x < 400 and y < 320):
            return 4
        elif(x < 430 and y < 442 and y < 500 and Robot().IsInside(x, y, 350, 500, 570, 320, 570, 500) == False):
            return 7
        elif(Robot().IsInside(x, y, 430, 150, 510, 320, 430, 408) == True):
            return 9
        elif(x < 570 and y < 320):
            return 8
        elif(x < 570 and y > 320):
            return 10
        elif(x < 800):
            return 11
        else:
            return -1

    def DrawPath(self, screen, start_x, start_y, end_x, end_y):
        size = len(path_c)
        for i in range(0, size - 1):
            pygame.draw.line(screen, 0x0000ff, path_c[i], path_c[i + 1], 2)
        pygame.draw.line(
            screen, 0x0000ff, path_c[size - 1], (end_x, end_y), 2)

    def FindPath(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0
        p = 0

        if(start_x != end_x):
            m = (end_y - start_y) / (end_x - start_x)
        else:
            m = -999

        s_c = Robot().CheckBlock(start_x, start_y)
        d_c = Robot().CheckBlock(end_x, end_y)

        if(s_c == d_c):
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x < end_x):
                        image_x += 1
                        image_y += m
                    elif(image_x > end_x):
                        image_x -= 1
                        image_y -= m
                    else:
                        print(
                            "GREAT! Robot successfully reached to the destination.")
                        success = 1
                else:
                    if(start_y < end_y and image_y <= end_y):
                        image_y += 1
                    elif(start_y > end_y and image_y >= end_y):
                        image_y -= 1
                    else:
                        print(
                            "GREAT! Robot successfully reached to the destination.")
                        success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    Robot.DrawPath(
                        self, screen, start_x, start_y, end_x, end_y)
                    screen.blit(textSuccess, (200, 50))
                    pygame.display.flip()
                    pygame.time.delay(20000)
                    break
                pygame.display.flip()
        elif(s_c == 1):

            if(start_x != 150):
                m = (150 - start_y) / (150 - start_x)
            else:
                m = -999

            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 150):
                        image_x += 1
                        image_y += m
                        intersect_x = image_x
                    else:
                        break
                else:
                    if(start_y < 150 and image_y <= 150):
                        image_y += 1
                    elif(start_y > 150 and image_y >= 150):
                        image_y -= 1
                    else:
                        break

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(1)
            Robot().FindPath(screen, 150, 150, end_x, end_y)
        elif(s_c == 2):
            if(start_x != 270):
                m = (100 - start_y) / (270 - start_x)
            else:
                m = -999

            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 270):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 100 and image_y <= 100):
                        image_y += 1
                    elif(start_y > 100 and image_y >= 100):
                        image_y -= 1
                    else:
                        break

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(2)
            Robot().FindPath(screen, 270, 100, end_x, end_y)
        elif(s_c == 3):
            if(start_x != 250):
                m = (500 - start_y) / (250 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 251):
                        image_x += 1
                        image_y += m
                    else:
                        print("error 2")
                        break
                else:
                    if(start_y < 500 and image_y <= 500):
                        image_y += 1
                    elif(start_y > 500 and image_y >= 500):
                        image_y -= 1
                    else:
                        print("error 1")
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(3)
            Robot().FindPath(screen, 251, 500, end_x, end_y)
        elif(s_c == 4):
            if(start_x != 400):
                m = (160 - start_y) / (400 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 400):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 160 and image_y <= 160):
                        image_y += 1
                    elif(start_y > 160 and image_y >= 160):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(4)
            Robot().FindPath(screen, 400, 160, end_x, end_y)
        elif(s_c == 5 and Robot().GetCount(5) == 0):
            if(start_x != 250):
                m = (500 - start_y) / (250 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x >= 249):
                        image_x -= 1
                        image_y -= m
                    else:
                        print("error 3")
                        break
                else:
                    if(start_y < 500 and image_y <= 500):
                        image_y += 1
                    elif(start_y > 500 and image_y >= 500):
                        image_y -= 1
                    else:
                        print("error 4")
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(5)
            Robot().FindPath(screen, 249, 500, end_x, end_y)
        elif(s_c == 5 and Robot().GetCount(5) == 1):
            if(start_x != 250):
                m = (427 - start_y) / (350 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 350):
                        image_x += 1
                        image_y += m
                    else:
                        print("error 5")
                        break
                else:
                    if(start_y < 427 and image_y <= 427):
                        image_y += 1
                    elif(start_y > 427 and image_y >= 427):
                        image_y -= 1
                    else:
                        print("error 6")
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(5)
            Robot().FindPath(screen, 350, 427, end_x, end_y)
        elif(s_c == 6):
            if(start_x != 400):
                m = (380 - start_y) / (400 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 400):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 380 and image_y <= 380):
                        image_y += 1
                    elif(start_y > 380 and image_y >= 380):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(6)
            Robot().FindPath(screen, 400, 380, end_x, end_y)
        elif(s_c == 7 and Robot().GetCount(7) != 1):
            if(start_x != 430):
                m = (75 - start_y) / (430 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 430):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 75 and image_y <= 75):
                        image_y += 1
                    elif(start_y > 75 and image_y >= 75):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(7)
            Robot().FindPath(screen, 430, 75, end_x, end_y)
        elif(s_c == 7 and Robot().GetCount(7) == 1):
            if(start_x != 430):
                m = (280 - start_y) / (430 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 431):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 280 and image_y <= 280):
                        image_y += 1
                    elif(start_y > 280 and image_y >= 280):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(7)
            Robot().FindPath(screen, 431, 280, end_x, end_y)
        elif(s_c == 8):
            if(start_x != 570):
                m = (160 - start_y) / (570 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x <= 570):
                        image_x += 1
                        image_y += m
                    else:
                        break
                else:
                    if(start_y < 160 and image_y <= 160):
                        image_y += 1
                    elif(start_y > 160 and image_y >= 160):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(8)
            Robot().FindPath(screen, 570, 160, end_x, end_y)
        elif(s_c == 9):
            if(start_x != 400):
                m = (160 - start_y) / (400 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x >= 400):
                        image_x -= 1
                        image_y -= m
                    else:
                        break
                else:
                    if(start_y < 160 and image_y <= 160):
                        image_y += 1
                    elif(start_y > 160 and image_y >= 160):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(9)
            Robot().FindPath(screen, 400, 160, end_x, end_y)
        elif(s_c == 10 and Robot().GetCount(10) == 0):
            if(start_x != 350):
                m = (550 - start_y) / (350 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x >= 348):
                        image_x -= 1
                        image_y -= m
                    else:
                        break
                else:
                    if(start_y < 550 and image_y <= 550):
                        image_y += 1
                    elif(start_y > 550 and image_y >= 550):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(10)
            Robot().FindPath(screen, 349, 550, end_x, end_y)
        elif(s_c == 10 and Robot().GetCount(10) == 1):
            if(start_x != 350):
                m = (550 - start_y) / (350 - start_x)
            else:
                m = -999
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                if(m != -999):
                    if(image_x >= 348):
                        image_x -= 1
                        image_y -= m
                    elif(image_x >= 75):
                        image_x -= 2
                        image_y -= 1
                    else:
                        break
                else:
                    if(start_y < 550 and image_y <= 550):
                        image_y += 1
                    elif(start_y > 550 and image_y >= 550):
                        image_y -= 1
                    else:
                        break
                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(10)
            Robot().FindPath(screen, 75, image_y, end_x, end_y)
        elif(s_c == 11):
            if(start_x == 570 and start_y == 160):
                m = 0
            elif(start_x == 570 and start_y != 160):
                m == -999
            else:
                m = (460 - start_y) / (570 - start_x)

            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)
                if(m == 0):
                    if(image_x <= 685 and image_y < 460):
                        image_x += 2
                    elif(image_y <= 460):
                        image_y += 2
                    elif(image_x >= 568 and image_y >= 460):
                        image_x -= 2
                    else:
                        break
                elif(m == -999):
                    if(start_y < 460 and image_y <= 460):
                        image_y += 1
                    elif(start_y > 460 and image_y >= 460):
                        image_y -= 1
                    else:
                        break
                else:
                    if(image_x >= 568):
                        image_x -= 1
                        image_y -= m
                    else:
                        break

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))
                pygame.display.flip()
            Robot().SetCount(11)
            Robot().FindPath(screen, 569, 460, end_x, end_y)


if __name__ == '__main__':

    print("\n*** ROBOTIC MOTION PLANNING ***")
    print("Trapezoidal Decomposition Method\n")
    print("Working space = 800 * 600")

    start = input("Enter Robot position(x1 y1): ")
    startsplit = start.split()
    if(len(startsplit) < 2):
        print("Invalid Input")
    else:
        start_x = int(startsplit[0])
        start_y = int(startsplit[1])
    end = input("Enter Destination(x2 y2): ")
    endsplit = end.split()
    if(len(endsplit) < 2):
        print("Invalid Input")
    else:
        end_x = int(endsplit[0])
        end_y = int(endsplit[1])

    m = (end_y - start_y) / (end_x - start_x)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(
        "Robotic Motion Planning- Trapezoidal Decomposition", "Implementation")

    if(Robot().IsInsideObstacle(start_x, start_y)):
        print(
            "Invalid Source address, there is obstacle.\nTry again with some other points.")
    elif(Robot().IsInsideObstacle(end_x, end_y)):
        print(
            "Invalid Destination address, there is obstacle.\nTry again with some other points.")
    else:
        path_c.append((start_x, start_y))
        Robot().FindPath(screen, start_x, start_y, end_x, end_y)
