from manim import *

class Earth(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=90 * DEGREES)

        earth = Sphere(radius=2, resolution=(20, 40)).set_fill_by_checkerboard([GREEN, DARK_BLUE])
        self.play(Create(earth), run_time=1.5)

        self.begin_ambient_camera_rotation(rate=0.1, about="theta")

        def create_latitude_arrow(latitude_deg, clockwise=True, swap_ends=False):
            lat_rad = latitude_deg * DEGREES
            r = 2 * np.cos(lat_rad)  # radius
            z = 2 * np.sin(lat_rad)  # vertical position

            # start = r * RIGHT + z * OUT
            # end = r * LEFT + z * OUT

            start = r * LEFT + z * OUT if swap_ends else r*RIGHT + z*OUT
            end = r*RIGHT + z*OUT if swap_ends else r * LEFT + z * OUT

            angle = TAU/4 if clockwise else -TAU/4

            return CurvedArrow(start, end, angle=angle).set_color(WHITE)
        
        self.wait(6)
        self.stop_ambient_camera_rotation()

        arrow_north = create_latitude_arrow(30, clockwise=True, swap_ends=False).scale(0.9)
        arrow_south = create_latitude_arrow(-30, clockwise=False, swap_ends=True).scale(0.9)

        arrow_north.rotate_about_origin(0.5, Z_AXIS)
        arrow_south.rotate_about_origin(0.5, Z_AXIS)

        self.play(Create(arrow_north))
        self.wait(1)

        self.play(Create(arrow_south))

        self.wait(2)
