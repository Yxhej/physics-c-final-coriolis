from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle(radius=2)  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}")
        f = Tex("F")

        self.play(Create(circle.shift(LEFT)), run_time=2)  # show the circle on screen
        self.wait()
        self.play(Create(circle.center()), run_time=1)
        self.wait()
        self.play(Transform(circle.shift(RIGHT), f, replace_mobject_with_target_in_scene=True), run_time=2)
        self.wait()
        self.play(Transform(f, t2.shift_onto_screen()), run_time=4)

class DrawCarousel(Scene):
    def construct(self):
        CAROUSEL_HEIGHT = 2
        CAROUSEL_WIDTH = 6

        base = Ellipse(height=CAROUSEL_HEIGHT, width=CAROUSEL_WIDTH)
        arrow2 = Arc(radius=1, angle=PI/2)
        omega = MathTex("\omega")

        arrow2.shift(DOWN).shift(RIGHT);
        omega.align_to(arrow2).shift(3 * RIGHT)
        base.shift(DOWN)
    
        base.set_fill(RED, opacity = 0.65)

        arrow2.stretch_to_fit_height(CAROUSEL_HEIGHT / 2)
        arrow2.stretch_to_fit_width(CAROUSEL_WIDTH / 2)
        arrow2.scale_to_fit_height(CAROUSEL_HEIGHT / 2 * 1.5)
        arrow2.add_tip()

        center = base.get_center;
        

        self.play(Create(base), Create(arrow2), Create(omega))
        self.wait()
        # self.play(movement.rotate(PI))
        # self.play(Create(arrow2))