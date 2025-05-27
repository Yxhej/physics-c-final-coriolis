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
        base = Ellipse(height=2, width=6)

        arrow2 = Arc(radius=1, angle=PI/2).stretch_to_fit_height(1.2).stretch_to_fit_width(3.6).add_tip()
        # arrow = ArcBetweenPoints(start=np.array((0.0, -2.1, 0.0)), end=np.array((3.1, -1.0, 0.0))).add_tip()
        # movement = VGroup(base, arrow)


        self.play(Create(base.shift(DOWN)), Create(arrow2))
        self.wait()
        # self.play(movement.rotate(PI))
        # self.play(Create(arrow2))