from manim import *

class ArcCenter(Scene):
    def construct(self):
        arc = Arc(arc_center=LEFT, radius=2)
        self.play(GrowFromCenter(arc))
        self.wait()

        circle = Circle(arc_center=2 * RIGHT)
        self.play(GrowFromCenter(circle))
        self.wait()

        dot = Dot(point=5 * RIGHT + 3.5 * UP)
        self.play(GrowFromCenter(dot))
        self.wait()

        curved_double_arrow = CurvedDoubleArrow(
            ORIGIN, 5 * RIGHT + 3.3 * UP,
            arc_center = 3 * RIGHT,
            tip_length=0.2
        )
        self.play(GrowFromCenter(curved_double_arrow))
        self.wait()


class MoveToMethod(Scene):
    def construct(self):
        star = Star().move_to(RIGHT)
        star_1 = Star()

        self.play(Create(star), Create(star_1))
        self.wait()

        rect = Rectangle(width=0.85).shift(RIGHT)
        self.play(FadeIn(rect))
        self.wait()
        
        rect2 = rect.copy().shift(RIGHT)
        self.play(FadeIn(rect2))
        self.wait()
        self.play(FadeOut(star, shift=UP, run_time=0.8),
                  FadeOut(star_1, shift=UP, run_time=0.8),
                  FadeOut(rect, shift=UP, run_time=0.8),
                  FadeOut(rect2, shift=UP, run_time=0.8))
        

class BetterShiftThanMove(Scene):
    def construct(self):
        ellipse = Ellipse().shift(UP + 3 * RIGHT)
        self.play(GrowFromCenter(ellipse))
        self.wait()

        circ = Circle().move_to(ellipse)
        self.play(FadeIn(circ))
        self.wait()

class ToEdgeMethod(Scene):
    def construct(self):
        square_1 = Square().to_edge(UP)
        self.play(Create(square_1))
        self.wait()

        square_2 = Square().to_edge(LEFT)
        self.play(Create(square_2))
        self.wait()

        square_3 = Square().to_edge(DOWN, buff=0.5)
        self.play(Create(square_3))
        self.wait()

        square_4 = Square().to_edge(RIGHT, buff=1.2)
        self.play(Create(square_4))
        self.wait()

        square_5 = Square().shift(2.2 * UP).to_edge(RIGHT)
        self.play(Create(square_5))
        self.wait()

        self.play(Uncreate(square_1, run_time=0.8),
                  Uncreate(square_2, run_time=0.8),
                  Uncreate(square_3, run_time=0.8),
                  Uncreate(square_4, run_time=0.8),
                  Uncreate(square_5, run_time=0.8))

class MoreConstants(Scene):
    def construct(self):
        circ_1 = Circle().to_edge(UR)
        self.play(GrowFromCenter(circ_1))
        self.wait()

        circ_2 = Circle().to_edge(DL, buff=LARGE_BUFF)
        self.play(GrowFromCenter(circ_2))
        self.wait()

        self.play(ShrinkToCenter(circ_2))
        self.wait()

class NextToMethod(Scene):
    def construct(self):
        dot = Dot(3 * RIGHT)
        self.play(GrowFromCenter(dot))
        self.wait()
        square_1 = Square().move_to(dot)
        square_1.shift(1.3 * RIGHT)
        self.play(FadeIn(square_1))
        self.wait()
        self.play(ShrinkToCenter(square_1))

        square_2 = Square().next_to(dot, RIGHT)
        self.play(FadeIn(square_2))
        self.wait()
        self.play(FadeOut(square_2))

class AlignMethod(Scene):
    def construct(self):
        problem_a = MathTex(
            r"a) -1 \leqslant \log_2 x "
            r"\leqslant 1"
        )
        self.play(FadeIn(problem_a, shift=DOWN))

        problem_b = MathTex(
            r"b) \sin x = \frac{1}{2}"
        )
        problem_b.next_to(problem_a, DOWN);
        problem_b.align_to(problem_a, LEFT)
        self.play(GrowFromCenter(problem_b))
        self.wait()

        problem_c = Tex(
            r"$c) \ \arcsin (-1) = \ ?$"
        )
        problem_c.next_to(problem_b, DOWN, aligned_edge=LEFT)
        self.play(Write(problem_c, run_time=2))
        self.wait()

class CircleAttributes(Scene):
    def construct(self):
        circ_1 = Circle(
            radius=2,
            arc_center=2*LEFT,
            fill_color=DARK_BLUE,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_width=5,
            stroke_opacity=0.9
        )
        self.play(DrawBorderThenFill(circ_1))

        circ_2 = Circle(stroke_color=YELLOW, stroke_width=3)
        circ_2.next_to(circ_1, RIGHT)
        self.play(Create(circ_2))

        circ_3 = Circle(fill_color=ORANGE, fill_opacity=1,
                        radius=0.85, stroke_opacity=0)
        circ_3.next_to(circ_2)
        self.play(FadeIn(circ_3, shift=LEFT))
        self.wait()

        self.play(FadeOut(circ_1), FadeOut(circ_2), FadeOut(circ_3))

class PolygonAttributes(Scene):
    def construct(self):
        rectangle = Polygon(
            2 * LEFT, 2 * RIGHT, 2 * UR, 2 * UL,
            fill_color=GOLD_A,
            fill_opacity=0.5,
            stroke_color=GOLD_E,
            stroke_width=1,
            stroke_opacity=0.8
        ).to_edge(RIGHT, buff=1)
        self.play(FadeIn(rectangle))
        self.wait()

        triangle = Polygon(
            2 * UP, ORIGIN, 2 * RIGHT,
            color=BLUE,
            fill_opacity=0.5
        )
        triangle.to_edge(UL, buff=2)
        self.play(GrowFromCenter(triangle))

        hexagon = RegularPolygon(
            n=6,
            radius=1.5,
            start_angle=30 * DEGREES,
            stroke_width=2,
            stroke_color=TEAL
        )
        self.play(FadeIn(hexagon))
        self.wait()

        trapezoid = Polygon(
            DL, UP, UR, DR + RIGHT,
            fill_opacity=0.4,
            color=LIGHT_BROWN
        ).shift(0.5*DL)
        self.play(TransformFromCopy(rectangle, trapezoid,
                                    run_time=1.5))
        self.wait()

class SquareRectangleAttributes(Scene):
    def construct(self):
        square = Square(
            side_length=3,
            fill_color=GREEN,
            fill_opacity=1,
            stroke_color=TEAL,
            stroke_width=1,
            stroke_opacity=0.8
        ).move_to(2.4 * LEFT)
        self.play(FadeIn(square, shift=2 * DOWN + RIGHT))
        self.wait()

        rectangle = Rectangle(width=3.8, height=2.9,
                              color=PURPLE, stroke_width=10)
        rectangle.move_to(2 * RIGHT)
        self.play(FadeIn(rectangle, shift=2 * DOWN + LEFT))
        self.wait()

        rounded_rect = RoundedRectangle(
            corner_radius=0.3,
            height=3.6,
            width=9,
            stroke_color=WHITE,
            stroke_width=1.5,
            fill_color=BLACK,
            fill_opacity=1
        )

        self.play(Create(rounded_rect, run_time=3))
        self.wait()

class LineAttributes(Scene):
    def construct(self):
        line_1 = Line(
            start=5 * LEFT,
            end=5 * RIGHT,
            stroke_width=3,
            stroke_color=BLUE_A,
            stroke_opacity=0.8
        )

        self.play(Create(line_1), run_time=2)
        self.wait()

        line_2 = Line(4 * LEFT, 4 * RIGHT, color=BLUE_B)
        line_2.shift(UP)
        self.play(Create(line_2), run_time=2)

        dashed_line_1 = DashedLine(
            start=3 * DOWN,
            end = 3 * UP,
            stroke_width=5,
            stroke_opacity=1,
            stroke_color=BLUE_C,
            dashed_ratio=0.8,
            dash_length=0.3
        )
        self.play(Create(dashed_line_1, run_time=2))

        dashed_line_2 = DashedLine(
            3 * DOWN, 3 * UP,
            stroke_color=BLUE_E,
            dashed_ratio=0.5,
            dash_length=0.1
        ).shift(RIGHT)
        self.play(Create(dashed_line_2))
        self.wait()

class ArcAttributes(Scene):
    def construct(self):
        arc_1 = Arc(
            radius=1.5,
            start_angle=0,
            angle=PI,
            arc_center=RIGHT,
            stroke_width=5,
            stroke_color=TEAL_A,
            stroke_opacity=0.8,
            fill_color=GREEN_B,
            fill_opacity=0.8
        )
        self.play(DrawBorderThenFill(arc_1))
        self.play(Create(arc_1.copy().shift(3*RIGHT)))
        self.wait()

        arc_2 = Arc(
            radius=0.5,
            start_angle=TAU / 6,
            angle=TAU / 3,
            color=YELLOW,
            fill_opacity=0.4,
            arc_center=2 * UR
        )
        self.play(Create(arc_2))
        self.wait()

        arc_2b = Arc(0.5, TAU / 6, TAU / 3, color=YELLOW,
                     fill_opacity=0.4).move_to(2 * UR)
        self.play(Create(arc_2b))

class LaTexAttributes(Scene):
    def construct(self):
        viet = Tex(
            "The roots $x_1$, $x_2$ of quadratic "
            "polinomial $P(x)=x^2+bx+c$ satisfy "
            "\\mbox{$x_1$ $+$ $x_2$ $=-b$}, $x_1$$x_2$ $=c$",
            color=LIGHT_GREY,
            width=200,
            tex_to_color_map={
                "$x_1$": YELLOW,
                "$x_2$": ORANGE
            }
        )

        self.play(Write(viet, run_time=5))
        self.wait()

class Angles(Scene):
    def construct(self):
        elbow_1 = Elbow(
            stroke_width=2,
            width=0.4,
            angle=0
        )
        self.play(Create(elbow_1))
        self.wait()

class DecorativeAttributes(Scene):
    def construct(self):
        zeta = MathTex(
            r"\zeta", "(s)", "= 0", font_size=72
        )
        self.play(Write(zeta), run_time=2)
        self.wait()

        underline = Underline(
            mobject=zeta,
            buff=0.1,
            stroke_width=2,
            color=YELLOW
        )
        self.play(Create(underline), run_time=1.5)
        self.wait(0.3)
        self.play(Uncreate(underline))

        box_1 = SurroundingRectangle(
            zeta,
            buff=0.3,
            stroke_width=1.5
        )
        self.play(Create(box_1, run_time=2))
        self.wait()
        self.play(FadeOut(box_1, run_time=1.5))

        box_2 = SurroundingRectangle(
            zeta,
            corner_radius=0.25,
            buff=0.2,
            stroke_width=2,
            stroke_color=WHITE
        )
        self.play(Create(box_2, run_time=1.5))
        self.play(Uncreate(box_2, run_time=1.5))

        brace = Brace(
            zeta,
            direction=DOWN,
            buff=0.15,
            sharpness=1.2,
            color=LIGHT_GREY
        )
        self.play(FadeIn(brace, shift=UP))

        note = Tex("Hard problem", font_size=28)
        note.next_to(brace, DOWN)
        self.play(FadeIn(note, shift=UP))
        self.wait()