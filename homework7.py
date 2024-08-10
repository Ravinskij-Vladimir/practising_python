from manim import *

class homework7(Scene):
    def construct(self):
        plane = NumberPlane(
            background_line_style={
               "stroke_color": GREY_E,
               "stroke_width": 2 
            }
        )
        rule = Text("Правило параллелограмма", font="Times New Roman", z_index=1).move_to(3.3*UP)
        self.play(Write(rule))
        self.play(Create(plane, run_time=2))
        dot_1 = Dot(2*UP, fill_opacity=0)
        dot_2 = Dot(2*RIGHT, fill_opacity=0)
        dot_3 = always_redraw(lambda: Dot(dot_1.get_center() + dot_2.get_center(), fill_opacity=0))
        arrow_1 = always_redraw(lambda: Arrow(
            ORIGIN, dot_1.get_center(), 
            buff=0, tip_length=0.2,
            color=YELLOW
        ).set_stroke(YELLOW, 2))
        arrow_2 = always_redraw(lambda: Arrow(
            ORIGIN, dot_2.get_center(),
            buff=0, tip_length=0.2,
            color=YELLOW
        ).set_stroke(YELLOW, 2))

        arrow_3 = always_redraw(lambda: Arrow(
            ORIGIN, dot_3.get_center(),
            buff=0, tip_length=0.2,
            color=YELLOW
        ).set_stroke(YELLOW, 2))
        self.play(GrowFromCenter(dot_3))
        self.play(GrowArrow(arrow_1), GrowArrow(arrow_2))
        self.play(GrowArrow(arrow_3))
        self.play(dot_1.animate.shift(LEFT), rate_func=there_and_back, run_time=3)
        self.play(Rotate(dot_2, -2*PI / 3, about_point=ORIGIN))
        self.play(dot_1.animate.shift(4*RIGHT + UP))
        self.play(dot_1.animate.move_to(2*UP))
        self.play(dot_2.animate.move_to(2*RIGHT))
        self.play(Rotate(dot_2, -TAU, about_point=ORIGIN, run_time=2))
        self.wait()
        self.play(FadeOut(arrow_1, arrow_2, arrow_3, plane, rule), lag_ratio=0.1, run_time=3)

        circles = VGroup()
        for i in range(12):
            circles.add(Circle(radius=0.3 + 0.05 * i, color=WHITE))

        self.play(Create(circles))
        self.play(circles.animate.arrange(buff=0))
        self.play(circles.animate.arrange(UR, buff=0))
        self.play(circles.animate.arrange_in_grid(rows=3))
        self.play(circles.animate.arrange_in_grid(rows=2))
        self.play(circles.animate.arrange_in_grid(cols=3))
        self.play(FadeOut(circles, shift=DOWN, run_time=1.5), lag_ratio=0.1)
        self.wait()

        determinant = MathTex(
            r"\begin{vmatrix}"
            r"a & b \\"
            r"c & d"
            r"\end{vmatrix}"
        )
        self.play(Write(determinant[0][0:6], run_time=1.5),
                  Write(determinant[0][8:], run_time=2))
        self.play(TransformFromCopy(determinant[0][4], determinant[0][7]),
                  TransformFromCopy(determinant[0][5], determinant[0][6]))
        self.wait()
        self.play(Unwrite(determinant, reverse=False))

        system = MathTex(
            r"\begin{cases}"
            r"x = \pm 1 \\"
            r"x \ge 0 \\"
            r"log_2{x} \neq 2"
            r"\end{cases}" 
        )
        self.play(FadeIn(system[0][:5], shift=RIGHT))
        self.play(Write(system[0][5]), TransformFromCopy(system[0][5], system[0][7:9]), Write(system[0][6]))
        self.play(TransformFromCopy(system[0][5:9], system[0][9:12]))
        self.play(FadeIn(system[0][12:], shift=LEFT))
        self.wait()
        self.play(FadeOut(system), run_time=3, lag_ratio=0.1)

        plane = NumberPlane(
            x_range=(-11,11,1),
            y_range=(-11,11,1),
            background_line_style={
                "stroke_width": 2,
                "stroke_color": GREY,
                "stroke_opacity": 0.4
            }
        ).scale(0.5)
        self.play(Create(plane))

        polygon = Polygon(
            2 * RIGHT + 5 * UP,
            9 * RIGHT + 5  * UP,
            10 * RIGHT,
            4 * RIGHT + 2 * DOWN,
            fill_color = DARK_BLUE,
            fill_opacity=0.6,
            stroke_color=BLUE
        ).scale(0.5, about_point=ORIGIN)
        self.play(DrawBorderThenFill(polygon))

        area = MathTex(
            r"S = i + \frac{b}{2} - 1"
        ).move_to(polygon).shift(0.5*UP)
        self.play(Write(area))

        curved_arrow = CurvedArrow(
            2 * DL, area[0][1].get_center() + 0.1 * DOWN,
            radius=5, color=YELLOW, tip_length=0.2,
            stroke_width=2
        )
        self.play(Create(curved_arrow))
        peak = Text("Формула Пика", font_size=24).next_to(2 * DL, LEFT)
        self.play(FadeIn(peak, shift=RIGHT))
        self.wait(2)
        self.play(FadeOut(curved_arrow, area, plane, peak, polygon), run_time=3, lag_ratio=0.1)
        self.wait()

class TriangleRule(Scene):
    def construct(self):
        plane = NumberPlane(
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 2,
                "stroke_opacity": 0.7
            }
        )
        self.play(Create(plane, run_time=3))
        dot_1 = Dot(2 * RIGHT + UP, fill_opacity=0)
        dot_2 = Dot(3 * RIGHT, fill_opacity=0)
        arrow_1 = always_redraw(lambda:
            Arrow(ORIGIN, dot_1.get_center(),
                  stroke_width=2, tip_length=0.2, buff=0)
        )
        arrow_2 = always_redraw(lambda:
            Arrow(dot_1.get_center(), dot_2.get_center(),
                  stroke_width=2, tip_length=0.2, buff=0
                ))
        
        arrow_3 = always_redraw(lambda:
            Arrow(ORIGIN, dot_2.get_center(),
                  stroke_width=2, tip_length=0.2, buff=0,
                  color=YELLOW)
        )
        a_point = MathTex("\\vec{a}")
        b_point = MathTex("\\vec{b}")
        c_point = MathTex("\\vec{c}")
        a_point.add_updater(lambda x: x.next_to(arrow_1.get_center(), UP, buff=0.3))
        b_point.add_updater(lambda x: x.next_to(arrow_2.get_center(), UP, buff=0.3))
        c_point.add_updater(lambda x: x.next_to(arrow_3.get_center(), DOWN, buff=0.3))
        self.play(GrowArrow(arrow_1), Write(a_point), 
                  GrowArrow(arrow_2), Write(b_point),
                  lag_ratio=0.2)
        self.play(GrowArrow(arrow_3), Write(c_point))
        self.wait()
        self.play(dot_1.animate.shift(2*RIGHT), rate_func=there_and_back, run_time=3)
        self.play(dot_2.animate.shift(3*DOWN), rate_func=there_and_back, run_time=3)
        self.play(dot_1.animate.shift(3*UL), dot_2.animate.shift(UR), rate_func = there_and_back, run_time=3)
        self.wait()

class Test(Scene):
    def construct(self):
        parabola = FunctionGraph(
            lambda x: np.square(x),
            x_range = [-1, 2]
        )
        self.play(Create(parabola))
        self.wait()