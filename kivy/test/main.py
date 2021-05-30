from kivy.app import App
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
#Allows use in kv file
from kivy.properties import BooleanProperty, StringProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

# from kivy.uix.scrollview import ScrollView


#Alternate Method
# class GridLayoutExample(GridLayout):
#     pass
class WidgetsExample(GridLayout):
    num = 0
    count = BooleanProperty(False)
    my_text = StringProperty(str(num))
    text_input_str = StringProperty("Hi")
    # slider_value_txt = StringProperty("Value")
    def on_button_click(self):
        # print("Button Clicked")
        if self.count:
            self.num += 1
            self.my_text = str(self.num)
    def on_toggle_button_state(self, widget):
        # print("Toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count = False
        else:
            widget.text = "ON"
            self.count = True
        return self.count
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
    #def on_slider_value(self, widget):
       # print("Slider Value: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
class StackLayoutExample(StackLayout):
    #Executed first before the code in the kv file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "rl-tb"
        for i in range(1, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


class BoxLayoutExample(BoxLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass
"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Top to bottom layout
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        #Outputs in the order they're added
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       with self.canvas:
           Line(points=(100, 100, 400, 500), width=2)
           Color(0, 1, 0)
           Line(circle=(400, 200, 80), width=2)
           Line(rectangle=(700, 500, 100, 100), width=3)
           self.rect = Rectangle(pos=(400, 200), size=(150, 200))

    def on_button_a_click(self):
        x, y = self.rect.pos
        xs, ys = self.rect.size
        speedX = dp(10)
        diff = self.width - (x + xs)
        if diff < speedX:
            speedX = diff
        x += speedX
        #Cannot mutate tuple, so only way to change
        #tuple is by changing it
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
           self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        #called function every time
        Clock.schedule_interval(self.update, 1/60)
    #calls as window screen changes
    def on_size(self, *args):
        # print("on size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y-self.ball_size/2)
    def update(self, dt):
        # print('update')
        x,y = self.ball.pos
        x += self.vx
        y += self.vy
        if (x + self.ball_size) > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if (y + self.ball_size) > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)

class CanvasExample6(Widget):
    pass
class CanvasExample7(BoxLayout):
    pass

TheLabApp().run()
