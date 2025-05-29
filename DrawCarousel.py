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

        arrow2.align_to(top_base, RIGHT)
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

        self.wait()
        self.play(Rotate(angle_carousel, rate_func=smoothererstep))
        self.play(Transform(angle_carousel, top_carousel, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        self.play(Create(arrow2), Create(omega))

        self.play(Rotate(top_carousel, angle=3*TAU, run_time=10, rate_func=linear))
