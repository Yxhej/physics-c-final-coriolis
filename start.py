from manim import *
from math import *

class Start(Scene):
    def construct(self):
        force = Tex("Coriolis force").shift(UP)
        arrow = Line(start=LEFT, end=RIGHT).add_tip()

        self.play(FadeIn(force), run_time=2)
        self.play(FadeIn(arrow.shift(DOWN)), FadeIn(arrow.shift(2*DOWN)))

        
        
