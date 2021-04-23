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
            print(self.parent.ids.pong_ball.velocity)
            sm.current = 'botao'
    pass

class PongPaddle(Image):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_x - self.center_x) / (self.width / 2)
            vel = Vector(vx, -1 * vy)
            if -self.parent.height/75< vel.y < self.parent.height/75:
                vel.y = vel.y*1.05
            if -self.parent.width/33> vel.x or vel.x > self.parent.width/33:
                vel.x = vel.x * 0.8
            ball.velocity = vel.x + (randint(-3, 3) + offset*2) * larguratela/300, vel.y



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
            print(tamanhotela)
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
        self.jogador.center_x = touch.x
        self.jogador.center_y = touch.y
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
        self.ids.score.text = score_pong
    def playar(self):
        global tamanhotela, larguratela
        tamanhotela = self.height
        larguratela = self.width
        sm.current = 'pong'

sm.add_widget(Botao(name= 'botao'))
sm.add_widget(JogoPong(name= 'pong'))
# sm.add_widget(Game(name='game'))
# sm.add_widget(GameOver(name='go'))


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()





