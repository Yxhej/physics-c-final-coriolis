from manim import *
from math import *

class Introduction(Scene):
    def construct(self):        
        floor = Circle(radius=2).set_fill(RED).set_opacity(0.6)
        force = Tex("Understanding the Coriolis Effect").shift(UP)
        arrow = Line(start=LEFT, end=RIGHT).add_tip()            
                    
        coriolis_effect = Tex("Coriolis Effect")
        coriolis_force = Tex("Coriolis Force").shift(1.5*DOWN)
        coriolis_force_eq = Tex("Coriolis Force Equation").shift(0.5*DOWN)
        
        self.add(force)
        self.wait(0.5)
        
        self.play(ReplacementTransform(force, coriolis_effect))
        
        coriolis_effect.generate_target()
        coriolis_effect.target.shift(1.5*UP)
        
        arrow = Line(UP, DOWN).add_tip()
        
        self.play(MoveToTarget(coriolis_effect))
        self.wait(1)
        self.play(FadeIn(arrow))
        self.play(FadeIn(coriolis_force))
        
        wow = VGroup(coriolis_effect, coriolis_force, arrow)
        
        coriolis_force.generate_target()
        coriolis_force.target.shift(0.75*UP)
        
        self.play(ReplacementTransform(wow, coriolis_force), MoveToTarget(coriolis_force))
        self.wait()
        
        ##### equation #######
        eq = MathTex(
            r"\vec{F}_{\text{cor}}", "=", r"-2m", r"(", r"\vec{\Omega}", r"\times", r"\vec{v}", r")",
            font_size=60
        ).shift(UP)

        eq.set_color_by_tex(r"\vec{v}", GREEN)
        eq.set_color_by_tex(r"m", YELLOW)
        eq.set_color_by_tex(r"\vec{F}_{\text{cor}}", RED)
        eq.set_color_by_tex(r"\vec{\Omega}", BLUE)

        labels = VGroup(
            Text("Coriolis Force", font_size=28, color=RED).next_to(eq[0], DOWN),
            Text("Mass", font_size=28, color=YELLOW).next_to(eq[2], DOWN),
            Text("Earth's Angular Velocity", font_size=28, color=BLUE).next_to(eq[4], UP),
            Text("Object Velocity", font_size=28, color=GREEN).next_to(eq[6], DOWN),
        )

        self.play(ReplacementTransform(coriolis_force, coriolis_force_eq), Write(eq), Write(labels))
        self.wait(1)
