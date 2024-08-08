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

class SetStrokemethod(Scene):
    def construct (self):
        square = Square(2).set_stroke(YELLOW, 3, 0.5)
        self.play(GrowFromCenter(square))

        line = Line(UL, DR)
        line.set_stroke(color=TEAL_A, width=2, opacity=0.7)
        self.play(Create(line))

        polygon = Polygon(UP, DOWN, RIGHT,
            fill_color=DARK_GREY, fill_opacity=0.5)
        polygon.set_stroke(ORANGE, 2.5).shift(2 * RIGHT)
        self.play(GrowFromCenter(polygon))
        self.wait()

class SetFillMethod(Scene):
    def construct(self):
        circle = Circle(1.5).set_fill(GREY, 0.8)
        self.play(GrowFromCenter(circle))
        self.wait()

        square = Square(3).set_fill(color=RED_E, opacity=0.3)
        self.play(GrowFromCenter(square))
        self.wait()

        note = Tex("$ABCD$ - квадрат", font_size=28, color=YELLOW)
        note.next_to(square, UP)
        self.play(Write(note), run_time=2)

        latex = MathTex(
            r"\angle A + \angle B + \angle C + \angle D = 360^\circ",
            font_size=28
        ).set_fill(YELLOW).next_to(square, DOWN, buff=0.4)
        self.play(Write(latex), run_time=2)
        self.wait()

class SetColorOpacity(Scene):
    def construct(self):
        parallelogram = Polygon(
            ORIGIN, UR, UR + 2 * RIGHT, 2 * RIGHT,
            fill_opacity=0.5   
        ).set_color(ORANGE)
        parallelogram.move_to(3 * RIGHT)
        self.play(GrowFromCenter(parallelogram))
        self.wait()
        self.play(FadeOut(parallelogram))

        triangle = Triangle(radius=2, fill_color=PINK)
        triangle.set_opacity(0.75)
        self.play(GrowFromCenter(triangle))
        self.wait()

        latex = MathTex(
            r"\alpha + \beta + \gamma " +
            r" = 180^\circ", font_size=40
        )
        latex.set_color(YELLOW).next_to(triangle, DOWN)
        self.play(Write(latex), run_time=2)
        self.wait()

class LayerOrder(Scene):
    def construct(self):
        star = Star(
            n=12,
            inner_radius=0.5,
            outer_radius=1.5,
        ).set_color(YELLOW).set_opacity(1)
        star.shift(0.5 * UL)
        square = Square(fill_opacity=1)
        square.set_color(GREEN).shift(0.5 * UR)
        circle = Circle(fill_opacity=1)
        circle.set_color(DARK_BLUE)

        self.play(FadeIn(star, square, circle))
        self.wait()
        self.remove(star, square, circle)
        self.add(circle, star, square)
        self.wait()
        self.play(FadeOut(circle, star, square,
                          shift=DOWN))
        self.wait()
        dot_A = Dot(LEFT, 0.12)
        dot_B = Dot(RIGHT, 0.12)
        line_AB = Line(LEFT, RIGHT, color=PINK).set_z_index(-1)

        self.play(GrowFromCenter(dot_A), GrowFromCenter(dot_B))
        self.play(Create(line_AB, run_time=2))
        self.wait()

        self.play(FadeOut(line_AB, dot_A, dot_B))

        circle.scale(1.5)
        rect = RoundedRectangle(fill_opacity=1, z_index=1)
        self.play(FadeIn(rect, circle))
        self.wait()
        circle.set_z_index(2)
        self.wait()
        rect.set_z_index(3)
        self.wait()

class ColorCode(Scene):
    def construct(self):
        pentagon = RegularPolygon(
            n=5
        ).set_stroke("#fb9503")
        pentagon.to_edge(UP, buff=1)
        self.play(FadeIn(pentagon, shift=DOWN))
        self.wait()

class RotateMethod(Scene):
    def construct(self):
        square_1 = Square().rotate(PI / 4)
        self.play(FadeIn(square_1))
        self.wait()

        dot = Dot(color=YELLOW)
        self.play(GrowFromCenter(dot))
        self.wait()

        square_2 = Square().shift(2.7 * RIGHT)
        self.play(FadeIn(square_2))
        square_2.rotate(90 * DEGREES, about_point=ORIGIN)
        self.wait()

        circle = Circle().shift(2 * LEFT)
        self.play(Create(circle, run_time=2.5))
        self.wait()
        circle.rotate(-TAU / 4)
        self.play(Create(circle, run_time=2.5))
        self.wait()

class ScaleMethod(Scene):
    def construct(self):
        star_1 = Star(n=12, inner_radius=-1.5)
        self.play(GrowFromCenter(star_1))
        self.wait()

        star_2 = star_1.copy()
        star_2.scale(2)
        self.play(GrowFromCenter(star_2))
        self.wait()

        self.play(FadeOut(star_1, star_2, shift=DOWN),
                  lag_ratio=0.1)
        
        triangle = Triangle(fill_opacity=0.7)
        triangle.set_color(GOLD_A).shift(UP)
        self.play(Create(triangle))
        self.wait()

        triangle_a = triangle.copy()
        triangle_b = triangle.copy()
        triangle_a.scale(scale_factor=2, about_point=3 * UL)
        dot_a = Dot(3 * UL, color=YELLOW, z_index=1)
        line_a = DashedLine(
            3 * UL,
            3 * RIGHT + DOWN,
            dashed_ratio=0.8,
            dash_length=0.15
        )
        line_a.set_stroke(GREY_A, 2)
        self.play(GrowFromCenter(dot_a))
        self.play(Create(line_a, run_time=1.5))
        self.play(TransformFromCopy(triangle, triangle_a),
                  run_time=1.5)
        self.wait()

        triangle_b.scale(scale_factor=-1.5, about_point=ORIGIN)
        dot_b = Dot(ORIGIN, color=YELLOW, z_index=1)
        line_b = DashedLine(UP, 1.5 * DOWN,
            dashed_ratio=0.8, dash_length=0.15)
        line_b.set_stroke(GREY_A, 2)
        self.play(GrowFromCenter(dot_b))
        self.play(Create(line_b))
        self.play(TransformFromCopy(triangle, triangle_b,
                                    run_time=1.5))
        self.wait(2)


class TryScale(Scene):
    def construct(self):
        triangle = Triangle(radius=1)
        self.play(GrowFromCenter(triangle))
        triangle_a = triangle.copy()
        triangle_b = triangle.copy()

        dot_a = Dot(UP, color=YELLOW)
        self.play(GrowFromCenter(dot_a))
        self.wait()

        triangle_a.scale(scale_factor=-1, about_point=dot_a.get_center())
        self.play(TransformFromCopy(triangle, triangle_a))
        self.wait()

class AppearanceAnimation(Scene):
    def construct(self):
        circ = Circle(fill_opacity=0.7)
        circ.set_color(GREEN)
        inequality = MathTex(r"e^\pi > \pi ^ e")
        text = Text("Посимвольное появление", font="Arial")
        text.set_color(WHITE).shift(2 * UP).scale(0.5)
        arrow = Arrow().scale(1.5).shift(1.5 * DOWN)

        self.play(FadeIn(circ))
        self.wait()
        self.play(FadeIn(circ, shift=DOWN))
        self.wait()
        self.play(FadeIn(circ, shift=2 * DR, scale=0.5, run_time=2))
        self.wait()
        self.play(FadeOut(circ, scale=0))

        circ.set_color(YELLOW)

        self.play(FadeIn(circ, scale=0))
        self.wait()
        self.play(GrowFromCenter(circ))
        self.play(GrowFromCenter(circ, point_color=WHITE))
        self.play(GrowFromPoint(circ, 3 * UR))
        self.play(GrowFromEdge(circ, RIGHT))
        self.wait()
        self.play(FadeOut(circ))
        circ.set_color(RED)
        self.wait()

        self.play(Create(arrow), run_time=2)
        self.play(GrowArrow(arrow), run_time=2)
        self.wait()

        square = Square()
        self.play(SpinInFromNothing(square))
        self.play(DrawBorderThenFill(circ))
        self.play(Write(inequality, run_time=1.5))
        self.wait()
        self.play(AddTextLetterByLetter(text))
        self.wait()

class IndicationAnimation(Scene):
    def construct(self):
        circ = Circle().set_fill(WHITE, 0.9).set_stroke(WHITE, 2)
        identity = MathTex("a^2 + b^2 = c^2")
        identity.scale(2)
        box_1 = SurroundingRectangle(identity, buff=0.4)
        box_1.set_stroke(WHITE, 3)
        box_2 = SurroundingRectangle(
            identity,
            corner_radius=0.2,
            buff=0.3
        )
        title = Tex("Pythagorean theorem", color=ORANGE)
        title.scale(0.8).next_to(identity, UP)
        underline = Underline(identity, color=YELLOW)

        self.play(Write(identity, run_time=3))
        self.play(Create(box_1, run_time=2.5))
        self.play(FadeOut(box_1, run_time=1.5))
        self.play(Create(box_2, run_time=2.5))
        self.play(FadeOut(box_2, run_time=1.5))
        self.play(Create(underline, run_time=1.5))
        self.play(FadeOut(underline, run_time=1.5))
        self.wait()

        self.play(ShowPassingFlash(box_1, run_time=2))
        self.play(ShowPassingFlash(box_2, run_time=2))
        self.play(ShowPassingFlash(underline))
        self.wait()
        self.play(Indicate(identity, run_time=4,
            scale_factor=1.5, color=YELLOW_D))
        
        self.play(Indicate(identity[0][-1]), run_time=3)
        self.play(GrowFromCenter(title))
        self.play(Wiggle(identity, run_time=4))
        self.wait()
        
class MovementAnimation(Scene):
    def construct(self):
        circle = Circle()
        square = Square(3)
        self.play(circle.animate.shift(RIGHT))
        self.play(circle.animate.to_edge(UP, buff=0.5))
        self.play(circle.animate.move_to(ORIGIN))
        self.play(FadeIn(square))
        self.play(circle.animate.next_to(square, DOWN))
        self.play(circle.animate.align_to(square, LEFT))
        self.play(ApplyMethod(square.shift, 2 * UL))
        self.wait()
        self.play(ApplyMethod(square.to_edge, UR, buff=SMALL_BUFF))
        self.play(ApplyMethod(square.move_to, circle))
        self.play(ApplyMethod(square.align_to, circle, UP))
        self.wait()

        self.play(ApplyMethod(circle.move_to, ORIGIN))
        dot = Dot()
        self.play(GrowFromCenter(dot))
        self.play(dot.animate.shift(RIGHT))
        self.play(MoveAlongPath(dot, circle, run_time=3))
        self.play(FadeOut(circle))
        self.play(square.animate.next_to(dot, DL, buff=0.08))
        self.play(MoveAlongPath(dot, square, run_time=3))

        self.play(FadeOut(square))
        spline = CubicBezier(3 * LEFT, 3 * UP, 2 * DR, 3 * UR)
        self.play(Create(spline), run_time=2)
        self.play(ApplyMethod(dot.move_to, 3 * LEFT))
        self.play(MoveAlongPath(dot, spline, run_time=2))

class RoundCircle(Scene):
    def construct(self):
        circle = Circle(radius=1)
        big_circle=Circle(radius=4)
        self.play(GrowFromCenter(big_circle))
        self.play(circle.animate.move_to(4 * RIGHT))
        self.play(MoveAlongPath(circle, big_circle, run_time=5))
        self.wait()

class TransformAnimation(Scene):
    def construct(self):
        triangle = Triangle().shift(3 * LEFT)
        circle = Circle()
        square = Square().shift(3 * RIGHT)
        dot = Dot(color=WHITE, radius=0.10)

        self.play(FadeIn(triangle))
        self.wait()
        self.play(Transform(triangle, circle))
        self.play(Transform(triangle, square))
        self.play(ReplacementTransform(triangle, dot))
        self.play(FadeOut(dot))
        self.wait()

        euler_1 = MathTex(
            r"\sum_{n=1}^\infty \frac{1}{n^2}="
            r"\frac{\pi^2}{6}"
        ).shift(1.7 * UP)

        euler_1_copy = euler_1.copy()
        euler_2 = MathTex(
            r"\sum_{n=1}^\infty \frac{1}{n^s}="
            r"\prod_{p}\frac{1}{1-p^{-s}}"
        )
        euler_3 = MathTex(
            r"e^{iy}=\cos y + i\sin y"
        ).shift(1.3 * DOWN)

        self.play(FadeIn(circle))
        self.play(ReplacementTransform(circle, euler_1))
        self.play(ClockwiseTransform(euler_1, euler_2))
        self.play(CounterclockwiseTransform(euler_1, euler_3))
        self.wait()
        self.play(TransformFromCopy(euler_1, euler_2))
        self.play(TransformFromCopy(euler_1, euler_1_copy))
        self.wait()

class OtherMethodAnimation(Scene):
    def construct(self):
        circle = Circle()
        self.play(FadeIn(circle))
        self.wait()
        self.play(FadeIn(circle, reverse=True))
        self.wait()

class TimedAnimation(Scene):
    def construct(self):
        circ = Circle(1.4, color=YELLOW).shift(1.9 * LEFT)
        star = Star(color=GOLD).shift(2 * DOWN)
        rect = Rectangle().to_edge(UP, buff=1).scale(0.7)
        shapes = VGroup(circ, star, rect)

        tex = MathTex(r"\int \limits _a^b f(x)\,dx=F(b)-F(a)")
        shapes.add(tex)

        self.play(FadeIn(shapes))
        self.wait()
        self.play(FadeOut(shapes, shift=DOWN))
        self.play(FadeIn(shapes, shift=UP, run_time=3,
                         lag_ratio=0.1))
        self.wait()
        self.play(Rotate(star, about_point=ORIGIN, angle=PI))

class PlotMethod(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6.5, 6.5],
            y_range=[-2.5, 2.5],
            x_axis_config={"numbers_to_include": range(-6, 7)},
            y_axis_config={"numbers_to_include": range(-2, 3)}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        cos = axes.plot(lambda x: 1.5 * np.cos(x))
        self.play(Write(axes, run_time=5), lag_ratio=0.2)
        self.play(Write(labels))
        self.play(Create(cos), run_time=3)
        self.wait(3)
        dot = Dot(6.5*LEFT + 1.5 * UP, color=YELLOW)
        self.play(Create(dot))
        self.play(MoveAlongPath(dot, cos), run_time=3)
        self.wait()