import pyglet
import time

t = time.time()
ball_image = pyglet.image.load('bg.png')
ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)








class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__()

        self.label = pyglet.text.Label('Hello, world!')

        self.x = 1

    def on_draw(self):
        self.clear()
        self.x += 1
        ball.draw()


        pyglet.text.Label(f'Hello, world!+{self.x}    {"--- %s seconds ---" % (time.time() - t)}').draw()


if __name__ == '__main__':
    window = HelloWorldWindow()
    pyglet.app.run()
