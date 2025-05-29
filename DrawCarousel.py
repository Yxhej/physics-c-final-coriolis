from manim import *
from math import *

class DrawCarousel(Scene):
    def construct(self):
        CAROUSEL_HEIGHT = 2
        CAROUSEL_WIDTH = 6

        # x^2/3^2 + y^2/1 = 1
        base = Ellipse(height=CAROUSEL_HEIGHT, width=CAROUSEL_WIDTH)
        arrow2 = Arc(radius=1, angle=PI/2)
        omega = MathTex("\omega")
                
        
        base.shift(DOWN)
        arrow2.shift(DOWN).shift(RIGHT)
        omega.align_to(arrow2).shift(3 * RIGHT)
    
        base.set_fill(RED, opacity = 0.25)

        arrow2.stretch_to_fit_height(CAROUSEL_HEIGHT / 2)
        arrow2.stretch_to_fit_width(CAROUSEL_WIDTH / 2)
        arrow2.scale_to_fit_height(CAROUSEL_HEIGHT / 2 * 1.5)
        arrow2.add_tip()

        center = base.get_center
        
        # carousel lines 
        num_sectors = 3 
        angles = [n * (180 / num_sectors) for n in range(num_sectors)]
        end_angles = [180 + angle for angle in angles]

        points = [base.point_at_angle(np.radians(angle)) for angle in angles]
        end_points = [base.point_at_angle(np.radians(angle)) for angle in end_angles]
        
        lines = []
        for i in range(num_sectors):
            start_point = points[i]
            end_point = end_points[i]
            line = Line(start_point, end_point, color=RED)
            lines.append(line)

        carousel = Group(base, *lines)

        self.play(Create(base), Create(lines[1]), Create(lines[0]), Create(lines[2]))
        # self.add(*lines)
        self.wait()
        self.play(Rotate(carousel, axis=np.array((1.0, -1.0, 1.0)), angle=PI/4, rate_functions=not_quite_there))
        self.wait()
        # self.play(movement.rotate(PI))
        # self.play(Create(arrow2))
