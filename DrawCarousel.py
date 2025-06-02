from manim import *
from math import *

class DrawCarousel(Scene):
    def construct(self):
        CAROUSEL_HEIGHT = 2
        CAROUSEL_WIDTH = 6

        # x^2/3^2 + y^2/1 = 1
        angled_base = Ellipse(height=CAROUSEL_HEIGHT, width=CAROUSEL_WIDTH)
        top_base = Circle(radius= (CAROUSEL_HEIGHT + CAROUSEL_WIDTH) / 4)
        arrow2 = Arc((CAROUSEL_HEIGHT + CAROUSEL_WIDTH) / 4 + 0.6, angle=PI/2)
        omega = MathTex("\omega")
                
        
        angled_base.shift(DOWN)
    
        angled_base.set_fill(RED, opacity = 0.25)
        top_base.set_fill(RED, opacity = 0.25)

        arrow2.align_to(top_base, RIGHT).shift(RIGHT)
        arrow2.add_tip()
        omega.align_to(arrow2, UP + RIGHT)

        # angle carousel lines 
        num_sectors = 3 
        angles = [n * (180 / num_sectors) for n in range(num_sectors)]
        end_angles = [180 + angle for angle in angles]

        points = [angled_base.point_at_angle(np.radians(angle)) for angle in angles]
        end_points = [angled_base.point_at_angle(np.radians(angle)) for angle in end_angles]
        
        lines = []
        for i in range(num_sectors):
            start_point = points[i]
            end_point = end_points[i]
            line = Line(start_point, end_point, color=RED)
            lines.append(line)

        ########################################################
        angle_carousel = Group(angled_base, *lines)
        self.play(Create(angled_base), Create(lines[1]), Create(lines[0]), Create(lines[2]))
        #########################################################

        # top-down carousel
        angles = [n * (180 / num_sectors) for n in range(num_sectors)]
        end_angles = [180 + angle for angle in angles]

        points = [top_base.point_at_angle(np.radians(angle)) for angle in angles]
        end_points = [top_base.point_at_angle(np.radians(angle)) for angle in end_angles]
        
        lines = []
        for i in range(num_sectors):
            start_point = points[i]
            end_point = end_points[i]
            line = Line(start_point, end_point, color=RED)
            lines.append(line)
        
        top_carousel = Group(top_base, *lines)

        ball = Dot(radius=0.2).set_color(ORANGE)
        ball.align_to(top_base, DOWN)
        
        ball_linear_path = Line(start=ball.get_center(), end=end_points[0], color=ORANGE) #dash_length=0.1, dashed_ratio=0.5)

        # self.wait()
        # self.play(Rotate(angle_carousel, rate_func=smoothererstep))
        self.wait()
        self.play(Transform(angle_carousel, top_carousel, replace_mobject_with_target_in_scene=True))
        self.wait()
        self.play(Create(arrow2), Create(omega), Create(ball))
        self.wait()
        self.play(Rotate(top_carousel, angle=TAU, run_time=3), FadeIn(ball_linear_path), TracedPath(ball.get_center), rate_func=linear)
        