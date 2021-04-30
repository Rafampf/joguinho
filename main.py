from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from random import sample
from random import random
from random import randint
from random import choice
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '634')

sm = ScreenManager(transition=FadeTransition(duration=0.04))

Builder.load_file("my.kv")






ultimo_score = 0
score_pong = ""
score_chess = ""


#
# class GameOver(Screen):
#     us = NumericProperty(0)
#     pont = "Pontuação: "
#     def on_pre_enter(self, *args):
#         self.us = ultimo_score
#     pass
#
#
#
# class Obstaculo(Image):
#     source = "gordura.png"
#     scored = False
#     gameScreen = None
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.anim = Animation(x= -self.width, duration=3)
#         self.anim.bind(on_complete= self.vanish)
#         self.anim.start(self)
#         self.gameScreen = App.get_running_app().root.get_screen("game")
#
#     def on_x(self, *args):
#         if self.gameScreen:
#             if self.x < self.gameScreen.ids.player.x and not self.scored:
#                 self.gameScreen.score += 0.5
#                 self.scored = True
#
#     def vanish(self, *args):
#         self.gameScreen.remove_widget(self)
#         self.gameScreen.obstaculos.remove(self)
#
#
# class Game(Screen):
#     obstaculos = []
#     score = NumericProperty(0)
#
#     def on_enter(self, *args):
#         Clock.schedule_interval(self.update,1/30)
#         Clock.schedule_interval(self.putObstaculo, 1.4)
#
#     def on_pre_enter(self, *args):
#         self.ids.player.y = self.height/2
#         self.ids.player.speed = 0
#         self.score = 0
#
#     def update(self, *args):
#         global ultimo_score
#         # self.ids.player.speed += -self.height * 2 * 1/30
#         self.ids.player.y += self.ids.player.speed * 1/30
#         if self.ids.player.y > self.height or self.ids.player.y < 0:
#             ultimo_score = self.score
#             self.game0ver()
#         elif self.playerCollided():
#             ultimo_score = self.score
#             self.game0ver()
#
#     def putObstaculo(self, *args):
#         gap = self.height*0.3
#         position = (self.height-gap) * random()
#         width = self.width*0.1
#         obstaculoLow = Obstaculo(x = self.width, height=position, width= width)
#         obstaculoHigh = Obstaculo(x=self.width, y=position + gap, height=self.height -position - gap, width= width)
#         self.add_widget(obstaculoLow, 3)
#         self.obstaculos.append(obstaculoLow)
#         self.add_widget(obstaculoHigh, 3)
#         self.obstaculos.append(obstaculoHigh)
#
#     def game0ver(self):
#         Clock.unschedule(self.update, 1/30)
#         Clock.unschedule(self.putObstaculo, 1)
#         App.get_running_app().root.current = "go"
#         for ob in self.obstaculos:
#             ob.anim.cancel(ob)
#             self.remove_widget(ob)
#         self.obstaculos = []
#
#     def collided(self, wid1, wid2):
#         if wid2.x <= wid1.x + wid1.width and \
#             wid2.x + wid2.width >= wid1.x and \
#             wid2.y <= wid1.y + wid1.height and \
#             wid2.y + wid2.height >= wid1.y:
#             return True
#         return False
#
#     def playerCollided(self):
#         collided = False
#         for obstacle in self.obstaculos:
#             if self.collided(self.ids.player, obstacle):
#                 collided = True
#                 break
#         return collided
#
#
#     def on_touch_down(self, touch):
#         self.ids.player.y = touch.pos[1] - self.ids.player.height/2
#         self.ids.player.x = touch.pos[0] - self.ids.player.width/2
#         # if self.ids.player.speed == 0:
#         #     self.ids.player.speed = self.height*0.7
#         # else:
#         #     self.ids.player.speed = -self.ids.player.speed
#
#     def on_touch_move(self, touch):
#         self.ids.player.y = touch.pos[1] - self.ids.player.height / 2
#         self.ids.player.x = touch.pos[0] - self.ids.player.width / 2
#
#     # def on_touch_up(self, touch):
#     #     self.ids.player.speed = -self.height*0.7
#     pass

class JogoPong(Screen):
    def on_pre_enter(self, *args):
        global n_bolas
        n_bolas = 1
        game = self.children[0]
        player1 = game.ids.player_left
        player2 = game.ids.player_right
        ball = game.ids.pong_ball
        ball2 = game.ids.pong_ball2
        player1.size = player2.size = self.width/3, self.height/40
        player1.center_x = player2.center_x = self.width/2
        game.remove_widget(game.ids.pong_ball)
        game.remove_widget(game.ids.pong_ball2)
        ball2.center = self.center
        ball.size = (self.width/11, self.width/11)
        ball2.size = (self.width/11, self.width/11)
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
    pass

    def on_leave(self, *args):
        global n_bolas
        n_bolas = 1
        game = self.children[0]
        player1 = game.ids.player_left
        player2 = game.ids.player_right
        ball = game.ids.pong_ball
        ball2 = game.ids.pong_ball2
        player1.size = player2.size = self.width / 3, self.height / 40
        Clock.unschedule(game.update)
        game.ids.jogador.center_x = game.center_x
        game.ids.jogador.center_y = game.center_y * 0.6
        ball.center = self.center
        ball2.center = self.center
        ball2.velocity = (0,0)
        player2.score = 0
        player1.score = 0





class Player(Image):
    source = "Hgame2.png"
    speed = NumericProperty(0)

    def die_pong(self, ball):
        global score_pong
        if self.collide_widget(ball):
            score_pong = str(self.parent.ids.player_right.score)
            sm.current = 'botao'

    def die_chess(self, ball):
        global score_chess
        score_chess = str(self.parent.score)
        if round(self.x) == round(ball.x) and round(self.y) == round(ball.y):
            if int(self.parent.ids.Lhighscore.text[11:]) < self.parent.score:
                self.parent.ids.Lhighscore.text = 'Highscore: ' + str(self.parent.score)
            self.parent.score = 0
            sm.current = 'botao2'




class PongPaddle(Image):
    score = NumericProperty(0)
    ativo = True
    ultima_bola = None

    def bounce_ball(self, ball):
        if self.collide_widget(ball) and self.ultima_bola != ball:
            self.ativo = True
        if self.collide_widget(ball) and self.ativo:
            if self.ultima_bola == ball:
                self.ativo = False
                Clock.schedule_once(self.backOn, 0.5)
            self.ultima_bola = ball
            vx, vy = ball.velocity
            offset = (ball.center_x - self.center_x) / (self.width / 2)
            vel = Vector(vx, -1 * vy)
            if -self.parent.height/75< vel.y < self.parent.height/75:
                vel.y = vel.y*1.05
            if -self.parent.width/33> vel.x or vel.x > self.parent.width/33:
                vel.x = vel.x * 0.8
            ball.velocity = vel.x + (randint(-3, 3) + offset*2) * larguratela/300, vel.y

    def backOn(self, time=0):
        self.ativo = True



class PongBall(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    jogador = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    obstaculo1 = ObjectProperty(None)
    obstaculo2 = ObjectProperty(None)
    salvador = Label()
    lbolas = []
    i = 0

    def serve_ball(self, bola=salvador, vel=(0, randint(30, 50)/10)):
        global tamanhotela
        bola.center = self.center
        bola.velocity = (0, randint(30, 50) * tamanhotela / 6340)
        if n_bolas == 1:
            self.add_widget(self.ball)
            self.ball.velocity = (0, randint(30, 50) * tamanhotela / 6340)

        elif n_bolas == 2:
            self.add_widget(self.ball2)
            self.ball2.center = self.center
            self.ball2.velocity = (0, randint(30, 50) * tamanhotela / 6340)

        else:
            bola.size = (bola.width*1.1, bola.height*1.1)
            self.player2.width = self.player2.width*1.1




    def update(self, dt):
        global n_bolas
        bola = self.ball
        bola2 = self.ball2
        bola.move()
        if n_bolas > 1:
            bola2.move()

        self.i += 1
        if self.i % 60 == 0:
            self.player2.score += 1

        # bounce of paddles
        self.player1.bounce_ball(bola)
        self.player2.bounce_ball(bola)
        self.jogador.die_pong(bola)
        self.player1.bounce_ball(bola2)
        self.player2.bounce_ball(bola2)
        self.jogador.die_pong(bola2)
        self.jogador.die_pong(self.player1)
        self.jogador.die_pong(self.player2)
        self.jogador.die_pong(self.obstaculo1)
        self.jogador.die_pong(self.obstaculo2)

        # bounce ball off bottom or top
        if (bola.x < self.x) or (bola.x > self.width - bola.width):
            bola.velocity_x *= -1
        if (bola2.x < self.x) or (bola2.x > self.width - bola2.width):
            bola2.velocity_x *= -1

        if self.ball.y >= self.ball2.y or n_bolas == 1:
            self.bola = self.ball
        elif self.ball.y < self.ball2.y:
            self.bola = self.ball2


        if self.player1.width/2 < self.bola.center_x < self.width - self.player1.width/2:
            self.player1.center_x = self.bola.center_x
        elif self.player1.width/2 > self.bola.center_x:
            self.player1.x = 0
        elif self.bola.center_x > self.width - self.player1.width/2:
            self.player1.x = self.width - self.player1.width

        # went of to a side to score point?
        if self.ball.y > self.top:
            self.player2.score += 1
            n_bolas += 1
            self.serve_ball(self.ball)
        if self.ball.top < self.y:
            self.player1.score += 1
            n_bolas += 1
            self.serve_ball(self.ball)



        if self.ball2.y > self.top:
            self.player2.score += 1
            n_bolas += 1
            self.serve_ball(self.ball2)
        if self.ball2.top < self.y:
            self.player1.score += 1
            n_bolas += 1
            self.serve_ball(self.ball2)


    def on_touch_move(self, touch):
        xL = self.width/3.5
        xA = self.jogador.center_x
        xB = touch.x
        distX = xA - xB
        yL = self.height/8
        yA = self.jogador.center_y
        yB = touch.y
        distY = yA - yB
        if touch.y < self.height/2 and -yL < distY < yL and -xL < distX < xL:
            self.jogador.center = touch.pos
            if touch.x < self.player2.width/2:
                self.player2.x = self.width - self.player2.width

            elif touch.x > self.width - self.player2.width/2:
                self.player2.x = 0

            else:
                self.player2.center_x = self.width - touch.x


class Botao(Screen):
    inicial = "Faça 60 pontos\npara desbloquear\no próximo nível"
    def on_pre_enter(self, *args):
        if score_pong:
            self.ids.pongpont.text = "Pontuação:"
            self.ids.play.text = "Play again"
        else:
            self.ids.pongpont.text = self.inicial
            self.ids.play.text = "Start game"
        self.ids.score.text = score_pong

    def on_leave(self, *args):
        global score_pong
        score_pong = ''
    def playar(self):
        global tamanhotela, larguratela
        tamanhotela = self.height
        larguratela = self.width
        sm.current = 'pong'

class Botao2(Screen):
    inicial = "Faça 60 pontos\npara desbloquear\no próximo nível"

    def on_pre_enter(self, *args):
        if score_chess:
            self.ids.pongpont.text = "Pontuação:"
            self.ids.play.text = "Play again"
        else:
            self.ids.pongpont.text = self.inicial
            self.ids.play.text = "Start game"
        self.ids.score.text = score_chess

    def on_leave(self, *args):
        global score_chess
        score_chess = ''

    def playar(self):
        global tamanhotela, larguratela
        tamanhotela = self.height
        larguratela = self.width
        sm.current = 'chess'
    pass

class Chess(Screen):
    score = NumericProperty(0)
    def on_pre_enter(self, *args):
        h = self.height/2
        w = self.width*1/6
        game = self.children[-1]
        game.jogador = self.ids.player
        game.r1 = self.ids.rook1
        game.r2 = self.ids.rook2
        game.b1 = self.ids.bishop1
        game.b2 = self.ids.bishop2
        game.n1 = self.ids.knight1
        game.n2 = self.ids.knight2
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        self.ids.player.y= h - w*3
        self.casas = game.casas = {
            "a1": [0*w, h - 4*w], "a2": [0*w, h - 3*w], "a3": [0*w, h - 2*w], "a4": [0*w, h - w],
            "a5": [0*w, h], "a6": [0*w, h + w], "a7": [0*w, h + 2*w], "a8": [0*w, h + 3*w],
            "b1": [1*w, h - 4*w], "b2": [1*w, h - 3*w], "b3": [1*w, h - 2*w], "b4": [1*w, h - w],
            "b5": [1*w, h], "b6": [1*w, h + w], "b7": [1*w, h + 2*w], "b8": [1*w, h + 3*w],
            "c1": [2*w, h - 4*w], "c2": [2*w, h - 3*w], "c3": [2*w, h - 2*w], "c4": [2*w, h - w],
            "c5": [2*w, h], "c6": [2*w, h + w], "c7": [2*w, h + 2*w], "c8": [2*w, h + 3*w],
            "d1": [3*w, h - 4*w], "d2": [3*w, h - 3*w], "d3": [3*w, h - 2*w], "d4": [3*w, h - w],
            "d5": [3*w, h], "d6": [3*w, h + w], "d7": [3*w, h + 2*w], "d8": [3*w, h + 3*w],
            "e1": [4*w, h - 4*w], "e2": [4*w, h - 3*w], "e3": [4*w, h - 2*w], "e4": [4*w, h - w],
            "e5": [4*w, h], "e6": [4*w, h + w], "e7": [4*w, h + 2*w], "e8": [4*w, h + 3*w],
            "f1": [5*w, h - 4*w], "f2": [5*w, h - 3*w], "f3": [5*w, h - 2*w], "f4": [5*w, h - w],
            "f5": [5*w, h], "f6": [5*w, h + w], "f7": [5*w, h + 2*w], "f8": [5*w, h + 3*w],
        }
        self.ids.player.pos = game.casas['c1']
        self.ids.rook1.pos = game.casas['a8']
        self.ids.rook2.pos = game.casas['f8']
        self.ids.bishop1.pos = game.casas['c8']
        self.ids.bishop2.pos = game.casas['d8']
        self.ids.knight1.pos = game.casas['b8']
        self.ids.knight2.pos = game.casas['e8']
        self.ids.Lscore.y = h + 4*w
        self.ids.Lhighscore.top = h -5 * w
        game.i = 0
        game.i1 = 0
        game.i2 = 0
        game.slow = 1
        game.k1 = 120
        game.k2 = 240

    @staticmethod
    def cancel_all(widget, *largs):
        if len(largs):
            for animation in list(Animation._instances):
                for x in largs:
                    animation.cancel_property(widget, x)
        else:
            for animation in set(Animation._instances):
                animation.cancel(widget)
    def on_leave(self, *args):
        game = self.children[-1]
        Clock.unschedule(game.update)
        self.cancel_all(self.ids.rook1)
        self.cancel_all(self.ids.rook2)
        self.cancel_all(self.ids.bishop1)
        self.cancel_all(self.ids.bishop2)
        self.cancel_all(self.ids.knight1)
        self.cancel_all(self.ids.knight2)
        self.ids.player.pos = game.casas['c1']
        self.ids.rook1.pos = game.casas['a8']
        self.ids.rook2.pos = game.casas['f8']
        self.ids.bishop1.pos = game.casas['c8']
        self.ids.bishop2.pos = game.casas['d8']
        self.ids.knight1.pos = game.casas['b8']
        self.ids.knight2.pos = game.casas['e8']
        game.i = 0
        game.i1 = 0
        game.i2 = 0
        game.slow = 1
        game.k1 = 120
        game.k2 = 240

class ChessGame(Widget):
    def update(self, dt):
        self.jogador.die_chess(self.r1)
        self.jogador.die_chess(self.r2)
        self.jogador.die_chess(self.b1)
        self.jogador.die_chess(self.b2)
        self.jogador.die_chess(self.n1)
        self.jogador.die_chess(self.n2)
        self.i += 1
        self.i1 += 1
        self.i2 += 1
        if self.i % 45 ==0:
            self.parent.score += 1
        if self.i1 % self.k1 == 0:
            self.i1 = 0
            self.n1.move()
            self.r1.move(1)
            self.b1.move(1)
            if self.k1 >= 90:
                self.k1 -= 1
            if self.slow < 2:
                self.slow = 1.005 * self.slow
        if self.i2 % self.k2 == 0:
            self.i2 = 0
            self.n2.move()
            self.r2.move(2)
            self.b2.move(2)
            if self.k2 > 130:
                self.k2 -= 4

    def move(self, piece, direction='up', times=1, d=1):
        d = d/self.slow
        if direction == 'up':
            anim = Animation(y=piece.y + 1 / 6 * self.width*times,duration=d)
            anim.start(piece)
        elif direction == 'down':
            anim = Animation(y=piece.y - 1 / 6 * self.width*times,duration=d)
            anim.start(piece)
        elif direction == 'right':
            anim = Animation(x=piece.x + 1 / 6 * self.width*times,duration=d)
            anim.start(piece)
        elif direction == 'left':
            anim = Animation(x=piece.x - 1 / 6 * self.width*times,duration=d)
            anim.start(piece)

    def on_touch_move(self, touch):
        xL = self.width / 3.5
        xA = self.jogador.center_x
        xB = touch.x
        distX = xA - xB
        yL = self.height / 8
        yA = self.jogador.center_y
        yB = touch.y
        distY = yA - yB
        if -yL < distY < yL and -xL < distX < xL:
            self.jogador.x = self.qual_casax(touch)
            self.jogador.y = self.qual_casay(touch)

    def qual_casax(self, touch):
        w = self.width*1/6
        xs = [0, w, 2*w, 3*w, 4*w, 5*w, 6*w]
        return min(xs, key=lambda x: abs(x - (touch.x - w/2)))
    def qual_casay(self, touch):
        h = self.height/2
        w = self.width*1/6
        ys = [h - 4*w, h - 3*w, h - 2*w, h - w, h, h + w, h + 2*w, h + 3*w]
        return min(ys, key=lambda x: abs(x - (touch.y - w/2)))

class Bishop(Image):
    def move(self, bishop=1):
        game = self.parent.children[-1]
        jogador = self.parent.ids.player
        distx = self.center_x - jogador.center_x
        disty = self.center_y - jogador.center_y
        w = int(game.width/6)
        if bishop == 1:
            # esquerda baixo
            if 0 <= disty <= distx and distx >= 0:
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'left', int(abs(disty)/w), d)
                game.move(self, 'down', int(abs(disty) / w), d)
            elif disty >= 0 and 0 <= distx <= disty:
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'left', int(abs(distx)/w), d)
                game.move(self, 'down', int(abs(distx) / w), d)
            # esquerda cima
            elif disty <= 0 <= distx and int(abs(distx)) >= int(abs(disty)):
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'left', int(abs(disty)/w), d)
                game.move(self, 'up', int(abs(disty)/w), d)
            elif disty <= 0 <= distx and int(abs(distx)) < int(abs(disty)):
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'left', int(abs(distx)/w), d)
                game.move(self, 'up', int(abs(distx)/w), d)
            # direita cima
            elif distx <= 0 and 0 >= disty >= distx:
                d = randint(8, 10) * int(abs(disty) / w) / 80
                game.move(self, 'right', int(abs(disty)/w), d)
                game.move(self, 'up', int(abs(disty)/w), d)
            elif 0 >= distx > disty and 0 >= disty:
                d = randint(8, 10) * int(abs(disty) / w) / 80
                game.move(self, 'right', int(abs(distx)/w), d)
                game.move(self, 'up', int(abs(distx)/w), d)
            # direita baixo
            elif disty >= 0 >= distx and int(abs(distx)) >= int(abs(disty)):
                d = randint(8, 10)*int(abs(disty)/w)/80
                game.move(self, 'right', int(abs(disty)/w), d)
                game.move(self, 'down', int(abs(disty)/w), d)
            elif disty >= 0 >= distx and int(abs(distx)) < int(abs(disty)):
                d = randint(8, 10)*int(abs(disty)/w)/80
                game.move(self, 'right', int(abs(distx)/w), d)
                game.move(self, 'down', int(abs(distx)/w), d)


        elif bishop == 2:
            # esquerda baixo
            if 0 <= disty <= distx and distx >= 0:
                d = int(abs(distx) / w) / 8
                game.move(self, 'left', int(abs(disty)/w), d*2)
                game.move(self, 'down', int(abs(disty)/w), d*2)
            elif disty >= 0 and 0 <= distx <= disty:
                d = int(abs(distx) / w) / 8
                game.move(self, 'left', int(abs(distx)/w), d*2)
                game.move(self, 'down', int(abs(distx)/w), d*2)
            # esquerda cima
            elif disty <= 0 <= distx and int(abs(distx)) >= int(abs(disty)):
                d = int(abs(distx) / w) / 8
                game.move(self, 'left', int(abs(disty)/w), d*2)
                game.move(self, 'up', int(abs(disty)/w), d*2)
            elif disty <= 0 <= distx and int(abs(distx)) < int(abs(disty)):
                d = int(abs(distx) / w) / 8
                game.move(self, 'left', int(abs(distx)/w), d*2)
                game.move(self, 'up', int(abs(distx)/w), d*2)
            # direita cima
            elif distx <= 0 and 0 >= disty >= distx:
                d = int(abs(distx) / w) / 8
                game.move(self, 'right', int(abs(disty)/w), d*2)
                game.move(self, 'up', int(abs(disty)/w), d*2)
            elif 0 >= distx > disty and 0 >= disty:
                d = int(abs(distx) / w) / 8
                game.move(self, 'right', int(abs(distx)/w), d*2)
                game.move(self, 'up', int(abs(distx)/w), d*2)
            # direita baixo
            elif disty >= 0 >= distx and int(abs(distx)) >= int(abs(disty)):
                d = int(abs(distx) / w) / 8
                game.move(self, 'right', int(abs(disty)/w), d*2)
                game.move(self, 'down', int(abs(disty)/w), d*2)
            elif disty >= 0 >= distx and int(abs(distx)) < int(abs(disty)):
                d = int(abs(distx) / w) / 8
                game.move(self, 'right', int(abs(distx)/w), d*2)
                game.move(self, 'down', int(abs(distx)/w), d*2)
    pass

class Rook(Image):
    def move(self, rook=1):
        game = self.parent.children[-1]
        jogador = self.parent.ids.player
        distx = self.center_x - jogador.center_x
        disty = self.center_y - jogador.center_y
        w = int(game.width/6)
        if rook == 1:
            if abs(distx) >= abs(disty) and distx > 0:
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'left', int(abs(distx)/w), d)
            elif abs(distx) >= abs(disty) and distx < 0:
                d = randint(8, 10) * int(abs(distx) / w) / 80
                game.move(self, 'right', int(abs(distx)/w), d)
                print(int(abs(distx)), w, int(abs(distx) / w))
            elif abs(distx) < abs(disty) and disty > 0:
                d = randint(8, 10) * int(abs(disty) / w) / 80
                game.move(self, 'down', int(abs(disty)/w), d)
            elif abs(distx) < abs(disty) and disty < 0:
                d = randint(8, 10)*int(abs(disty)/w)/80
                game.move(self, 'up', int(abs(disty)/w), d)

        elif rook == 2:
            if abs(distx) >= abs(disty) and distx > 0:
                d = int(abs(distx) / w) / 8
                game.move(self, 'left', int(abs(distx)/w), d*2)
            elif abs(distx) >= abs(disty) and distx < 0:
                d = int(abs(distx) / w) / 8
                game.move(self, 'right', int(abs(distx)/w), d*2)
            elif abs(distx) < abs(disty) and disty > 0:
                d = int(abs(disty) / w) / 8
                game.move(self, 'down', int(abs(disty)/w), d*2)
            elif abs(distx) < abs(disty) and disty < 0:
                d = int(abs(disty)/w)/ 8
                game.move(self, 'up', int(abs(disty)/w), d*2)

class Knight(Image):
    source = 'cavalo.png'
    def move(self, knight=1):
        game = self.parent.children[-1]
        w = game.width*1/6
        move = choice(self.valid_moves())
        if move == 1:
            self.x = self.x + w
            self.y = self.y + w*2
        if move == 2:
            self.x = self.x + w*2
            self.y = self.y + w
        if move == 3:
            self.x = self.x + w*2
            self.y = self.y - w
        if move == 4:
            self.x = self.x + w
            self.y = self.y - w*2
        if move == 5:
            self.x = self.x - w
            self.y = self.y - w*2
        if move == 6:
            self.x = self.x - w*2
            self.y = self.y - w
        if move == 7:
            self.x = self.x - w*2
            self.y = self.y + w
        if move == 8:
            self.x = self.x - w
            self.y = self.y + w*2

    def valid_moves(self):
        game = self.parent.children[-1]
        h = game.height/2
        w = game.width*1/6
        self.val_moves = []
        ymax = h + 3*w
        ymin = h - 3*w
        xmax = 5*w
        xmin = 0
        if self.y + 2*w <= ymax and self.x + w <= xmax:
            self.val_moves.append(1)
        if self.x + 2*w <= xmax and self.y + w <= ymax:
            self.val_moves.append(2)
        if self.x + 2*w <= xmax and self.y - w >= ymin:
            self.val_moves.append(3)
        if self.y - 2*w >= ymin and self.x + w <= xmax:
            self.val_moves.append(4)
        if self.y - 2*w >= ymin and self.x - w >= xmin:
            self.val_moves.append(5)
        if self.x - 2*w >= xmin and self.y - w >= ymin:
            self.val_moves.append(6)
        if self.x - 2*w >= xmin and self.y + w <= ymax:
            self.val_moves.append(7)
        if self.y + 2*w <= ymax and self.x - w >= xmin:
            self.val_moves.append(8)

        return self.val_moves



    pass



sm.add_widget(Botao2(name='botao2'))
sm.add_widget(Chess(name='chess'))
sm.add_widget(Botao(name='botao'))
sm.add_widget(JogoPong(name='pong'))
# sm.add_widget(Game(name='game'))
# sm.add_widget(GameOver(name='go'))


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()





