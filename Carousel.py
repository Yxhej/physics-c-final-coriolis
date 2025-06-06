from manim import *
from math import *

class DrawCarousel(Scene):
    def construct(self):
        CAROUSEL_HEIGHT = 2
        CAROUSEL_WIDTH = 6

        carousel = Circle(radius=(CAROUSEL_HEIGHT + CAROUSEL_WIDTH) / 4)
        arrow = Arc((CAROUSEL_HEIGHT + CAROUSEL_WIDTH) / 4 + 0.6, angle=PI/2)
        omega = MathTex("\omega")
                
        carousel.set_fill(RED, opacity = 0.25)

        arrow.align_to(carousel, RIGHT).shift(RIGHT)
        arrow.add_tip()
        omega.next_to(arrow, RIGHT).shift(0.01*DOWN)

        # carousel circle lines
        num_sectors = 3 
        
        angles = [n * (180 / num_sectors) for n in range(num_sectors)]
        end_angles = [180 + angle for angle in angles]

        points = [carousel.point_at_angle(np.radians(angle)) for angle in angles]
        end_points = [carousel.point_at_angle(np.radians(angle)) for angle in end_angles]
        
        lines = []

        for i in range(num_sectors):
            start_point = points[i]
            end_point = end_points[i]
            line = Line(start_point, end_point, color=RED).set_opacity(0.8)
            line.set_z_index(1)
            lines.append(line)
        
        top_carousel = Group(carousel, *lines)

        ball = Dot(radius=0.2).set_color(ORANGE)
        ball.align_to(carousel, DOWN)
        
        # i hate this
        ball2 = Dot(radius=0.2).set_color(ORANGE)
        ball2.align_to(carousel, DOWN)
        
        ref_ball_right = Dot(radius=0.2).set_color(WHITE).shift(2.5*RIGHT)
        ref_ball_left = Dot(radius=0.2).set_color(WHITE).shift(2.5*LEFT)
        ref_text = Tex("Rotational\\\\Reference").shift(3.5*LEFT + DOWN)
        
        
        self.play(Create(carousel), Create(lines[1]), Create(lines[0]), Create(lines[2]))
        self.play(Create(arrow), Create(omega), Create(ball2))
        self.wait()
        self.play(Create(ref_ball_right), Create(ref_ball_left), FadeIn(ref_text))
        self.wait(2)
        self.play(FadeOut(ref_text))
        self.wait()
        
        ########## Rotating reference frame, curved deflection
        self.add(TracedPath(ball2.get_bottom, stroke_width=6, dissipating_time=2).set_color(ORANGE))

        rotating = Tex("Rotating Reference Frame").shift(3*UP)
        rotating_references = Group(ref_ball_left, ref_ball_right)
        ball_radial_path = ArcBetweenPoints(start=ball2.get_center(), end=points[0], angle=-TAU/4, color=ORANGE)

        self.play(Create(rotating), run_time=0.8)
        self.play(
            LaggedStart(
                Rotate(rotating_references, angle=TAU, rate_func=linear), 
                MoveAlongPath(ball2, ball_radial_path),
                lag_ratio=0.4,
                run_time=3,
                rate_func=linear),
            Rotate(rotating_references, angle=3*TAU, 
                   rate_func=rate_functions.ease_out_sine, 
                   run_time=2*e))
        
        self.play(FadeOut(ball2), FadeOut(rotating))
        self.remove(ball2)

        self.wait(1.5)
        
        ########## Inertial reference frame, linear
        self.play(FadeIn(ball))
        self.add(TracedPath(ball.get_bottom, stroke_width=6, dissipating_time=2).set_color(ORANGE))
        
        ball_linear_path = Line(start=ball.get_center(), end=points[0], color=ORANGE)
        not_rotating = Tex("Inertial (Non-Rotating) Reference Frame").shift(3*UP)
        
        self.play(Create(not_rotating), run_time=0.8)
        self.play(
            LaggedStart(
                Rotate(top_carousel, angle=PI*1.6, rate_func=linear), 
                MoveAlongPath(ball, ball_linear_path),
                lag_ratio=0.4,
                run_time=3,
                rate_func=linear),
            Rotate(top_carousel, angle=e*PI*1.6, 
                   rate_func=rate_functions.ease_out_sine, 
                   run_time=2*e),
            FadeOut(arrow, omega))
        
        
        why = Text("Why?", font_size=48).shift(3*DOWN)
        
        self.play(SpinInFromNothing(why))
        
        self.wait(2)
        
        # clear all mobjects
        self.play(*[FadeOut(mob)for mob in self.mobjects])      
          
        
        ########## Forces explanation 
        rotating = Tex("Rotating Reference Frame").shift(3*UP)
        rotating_references = Group(ref_ball_left, ref_ball_right)
        
        ball2.move_to(ball_radial_path.get_midpoint())
        repeat_count = 5
        self.play(Create(carousel), Create(lines[1]), Create(lines[0]), Create(lines[2]), Create(arrow), Create(omega), Create(ball2))
        self.play(Create(ref_ball_right), Create(ref_ball_left), Create(ball_radial_path), Create(rotating), run_time=0.8)
        
        
        centrifugal_force = Line(ball_radial_path.get_midpoint(), carousel.point_at_angle(7*TAU/8)).add_tip(tip_width=0.2, tip_length=0.2).set_color(BLUE)
        coriolis_force = Vector([0,1]).set_color(GREEN)
        
        centri = Tex("Centrifugal Force").set_color(BLUE).next_to(centrifugal_force, DOWN, buff=0.75).set_z_index(0)
        coriolis = Tex("Coriolis\\\\Force").set_color(GREEN).next_to(coriolis_force, RIGHT, buff=3.25).set_z_index(0)
        coriolis_force.move_to(ball_radial_path.get_midpoint()).shift(UP*0.5)

        self.play(Create(centrifugal_force), Create(centri))
        self.wait(5)
        self.play(Create(coriolis_force), Create(coriolis))
        self.wait()

        