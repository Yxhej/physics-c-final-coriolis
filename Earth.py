from manim import *

class Earth(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=89 * DEGREES)

        earth = Sphere(radius=2, resolution=(10, 20)).set_fill_by_checkerboard([GREEN, DARK_BLUE])
        circle = Circle(radius=1.5).set_opacity(0)

        self.play(Create(earth), run_time=3)

        # self.begin_ambient_camera_rotation(rate=0.1, about="theta")
        self.wait(2)

        up_arrow = CurvedArrow(start_point=circle.get_right(), end_point=circle.get_left()).set_color(WHITE)

        self.play(Create(up_arrow))

        self.wait(2)
        
        self.stop_ambient_camera_rotation()
