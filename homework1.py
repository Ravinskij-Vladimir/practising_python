from manim import *

class HomeWork1(Scene):
    def construct(self):

        # 1st Figure
        dot = Dot(radius=0.05)
        self.add(dot)

        circ1 = Circle(radius=1, color=RED)
        self.play(GrowFromCenter(circ1))
        
        circ2 = Circle(radius=2, color=RED)
        self.play(GrowFromCenter(circ2))

        
        circ3 = Circle(radius=3, color=RED)
        self.play(GrowFromCenter(circ3))

        self.wait()
        self.play(FadeOut(circ1, circ2, circ3, dot))
        
        # 2nd Figure
        octagon = RegularPolygon(n=8, radius=3)
        self.play(GrowFromCenter(octagon))


        square = Square(side_length=6/np.sqrt(2))
        self.play(FadeIn(square))
        
        inner_circ = Circle(radius=3/np.sqrt(2))
        self.play(Create(inner_circ))

        triangle =  Triangle(radius=3/np.sqrt(2))
        self.play(GrowFromCenter(triangle))
        self.wait()

        self.play(FadeOut(triangle, square, inner_circ, octagon))


        # 3rd Figure
        line1 = Line(2 * (DOWN + LEFT), 2* (LEFT + UP))
        line2 = Line(2 * (DOWN + LEFT), 2 * (DOWN + RIGHT))
        right_triangle = Polygon(2 * (DOWN + LEFT), 2* (LEFT + UP), 2 * (DOWN + RIGHT))
        self.play(FadeIn(right_triangle, shift=UP))
        outer_circle = Circle(radius=2 * np.sqrt(2))
        self.play(Create(outer_circle))
        right_angle = RightAngle(line1, line2)
        self.play(Create(right_angle))
        self.wait()
        self.play(FadeOut(right_angle, right_triangle, outer_circle)) 


        # 4th Figure
        star = Star(n=6, outer_radius=1, start_angle = PI/6)
        self.play(GrowFromCenter(star))
        arc1 = Arc(radius=1, start_angle=PI/6, angle=PI/3)
        self.play(Create(arc1), run_time=0.5)

        arc2 = Arc(radius=1, start_angle=5*PI/6, angle=PI/3)
        self.play(Create(arc2), run_time=0.5)

        arc3 = Arc(radius=1, start_angle=9*PI/6, angle=PI/3)
        self.play(Create(arc3), run_time=0.5)
        self.wait()
        self.play(FadeOut(star, arc1, arc2, arc3))

        # 5th Figure
        circ_0 = Circle(radius=2)
        x_axis = Arrow(3*LEFT, 3 * RIGHT, tip_length=0.1)
        y_axis = Arrow(3*DOWN, 3 * UP, tip_length=0.1)
        self.play(Create(circ_0))
        self.wait(0.5)
        self.play(FadeIn(x_axis, shift=RIGHT, run_time=0.5))
        self.play(FadeIn(y_axis, shift=UP, run_time=0.5))
        curved_arrow = CurvedArrow(2.2 * RIGHT, 2.2 * UP, 
                                   tip_length=0.1)
        self.play(Create(curved_arrow))
        self.wait()
        self.play(FadeOut(circ_0, x_axis, y_axis, curved_arrow))

        # 6th Figure
        line_1 = Line(2*LEFT, 2*RIGHT)
        line_2 = Line(2*LEFT + 2*DOWN, 2*RIGHT + 2*UP)
        angle = Angle(line_1, line_2, radius=0.6)
        self.play(Create(line_1))
        self.play(Create(line_2))
        self.play(Create(angle))
        self.wait()
        self.play(FadeOut(line_1, line_2, angle))
    
        # 7th Figure
        another_right_triangle = Polygon(LEFT + 2* UP, LEFT + DOWN,
                                         DOWN + 3 * RIGHT)
        self.play(Create(another_right_triangle))
        another_inner_circ = Circle(radius=1)
        self.play(GrowFromCenter(another_inner_circ))
        another_dot = Dot(radius=0.05)
        self.play(GrowFromCenter(another_dot))

        one_serif = Line(0.9*LEFT + 1/2 * UP, 1.1*LEFT +  1/2 * UP)
        self.play(FadeIn(one_serif, shift=LEFT, run_time=0.5))

        two_serifs_1 = Line(0.9*DOWN + 0.95*RIGHT, 1.1*DOWN +  0.95*RIGHT)
        two_serifs_2 = Line(0.9*DOWN + 1.05*RIGHT, 1.1*DOWN +  1.05*RIGHT)
        self.play(FadeIn(two_serifs_1, shift=UP, run_time=0.5),
                   FadeIn(two_serifs_2, shift=UP, run_time=0.5))
        self.wait()
        self.play(FadeOut(another_right_triangle, another_inner_circ,
                         another_dot, one_serif, two_serifs_1, two_serifs_2))
        
        # 8th Figure
        another_polygon = RegularPolygon(n=6, radius=2)
        self.play(GrowFromCenter(another_polygon))
        another_dashed_line = DashedLine(3*DOWN, 3*UP)
        self.play(Create(another_dashed_line))

        double_curved_arrow = CurvedDoubleArrow(2*UP + RIGHT, 2*UP + LEFT, 
                                                tip_length=0.1,
                                                radius=2)
        self.play(FadeIn(double_curved_arrow, shift=DOWN))
        self.wait()
        self.play(FadeOut(another_polygon, another_dashed_line, 
                          double_curved_arrow))
        
        # 9th Figure
        rounded_rect = DashedVMobject(RoundedRectangle(width=10, height=6),
                                      num_dashes=75)
        self.play(GrowFromCenter(rounded_rect))
        rounded_triangle = Triangle(radius=1.5).round_corners(radius=0.15).rotate(PI/6)
        self.play(GrowFromCenter(rounded_triangle))
        self.wait()
        self.play(FadeOut(rounded_triangle, rounded_rect))

        spline = CubicBezier(
            3 * LEFT + 3 * DOWN,
            6 * UP,
            3 * RIGHT + 7 * DOWN,
            4 * RIGHT + 3 * UP
        )
        self.play(Create(spline))
        vector = DoubleArrow(3 * LEFT + 3 * DOWN, 4 * RIGHT + 3 * UP,
                       tip_length=0.15)
        self.play(Create(vector))
        self.wait()
        self.play(FadeOut(spline, vector))

        # 10th Figure
        final_circle = Circle(radius=2)
        self.play(Create(final_circle))
        smile = Arc(start_angle = 7*PI/6, angle = 4*PI/6, radius=1.6)
        ellipse = Ellipse(width=1, height=0.5)
        self.play(Create(smile))
        self.wait(0.2)
        self.play(Create(ellipse))
        right_eyebrow = Arc(start_angle = PI/3, angle = PI/3).move_to(UP + RIGHT)
        left_eyebrow = Arc(start_angle = PI/3, angle = PI/3).move_to(UP + LEFT)
        self.play(Create(right_eyebrow))
        self.play(Create(left_eyebrow))
        self.wait()
        self.play(FadeOut(final_circle, smile, ellipse, right_eyebrow, left_eyebrow))