from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty
import kivy.utils
import numpy as np



#class GridLayoutExample(GridLayout)

class WidgetsExample(GridLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    mytext = StringProperty("Begin!")


    myothertext=StringProperty("Consternation!")

    count=0
    switch=0


    def on_button_click(self,button):
        if self.switch==0:
            self.count+=1
            button.text="count\n"+str(self.count)
        self.mytext="Hello\n this is the "+str(self.count)+"th click"
        self.cols_minimum[2]= 300

       # self.size = ( * dp(20) + self.myothertext.count() * dp(20))

    def on_toggle_state(self,toggle_button):
        if toggle_button.state=="down":
            print("Off")
            self.switch=0
            self.myothertext="Toggle on to lock counter!"
        #    self.size=(self.mytext.count()*dp(20)+self.myothertext.count()*dp(20))
            toggle_button.text="OFF"
            toggle_button.background_color=(1,0,0,1)
        else:
            print("On")
            self.switch=1
            toggle_button.text="ON"
            self.myothertext="Toggle off to resume counter"
         #   self.size = (self.mytext.count * dp(20) + self.myothertext.count * dp(20))
            toggle_button.background_color=(0,float(208/255),float(209/255),1)



class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        #self.orientation="lr-bt"
        super().__init__(**kwargs)
        for i in range(100):
          size =dp(100)
          b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
          self.add_widget(b)
          

class AnchorLayoutExample(AnchorLayout):
     pass 

class BoxLayoutExample(BoxLayout):
     pass
        
class MainWidget(Widget):
     pass

class TheLabApp(App):
    pass 

TheLabApp().run()