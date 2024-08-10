from manim import *

class Tracker(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        sinus = FunctionGraph(lambda x: np.sin(x), [-7, 7])
        sinus.set_stroke(GREY, 2)
        tangent = always_redraw(
            lambda: TangentLine(sinus, tracker.get_value(), 3)
        )
        number = always_redraw(
            lambda: DecimalNumber(tracker.get_value())
        )
        self.play(FadeIn(sinus, tangent, number, scale=0.2))
        self.play(tracker.animate.set_value(1), run_time=7, rate_func=there_and_back)
        self.wait()
    

class Fermat(Scene):
    def construct(self):
        A = Dot(3 * UL)
        B = Dot(2 * UR + RIGHT)
        P = Dot(LEFT)
        line = Line(4 * LEFT, 4 * RIGHT).set_stroke(BLUE, 2)
        AP = always_redraw(
            lambda: Line(A.get_center(), P.get_center())
        )
        BP = always_redraw(
            lambda: Line(B.get_center(), P.get_center())
        )
        A_sym = Dot(3 * DL)
        line_sym = DashedLine(A_sym, A)
        right_angle = RightAngle(line, line_sym, 0.3)
        right_angle.set_stroke(BLUE, 2)
        AP_sym = always_redraw(
            lambda: Line(A_sym.get_center(), P.get_center())
        )
        label = MathTex("A", "B", "l", "A'").scale(0.75)
        label[0].next_to(A, UL, buff=0.1)
        label[1].next_to(B, UR, buff=0.1)
        label[2].next_to(4 * RIGHT, UL, buff=0.1)
        label[3].next_to(A_sym, DL, buff=0.1)
        label_P = always_redraw(
            lambda: MathTex("P")
                .scale(0.75)
                .next_to(P, UP, buff=0.15)
        )

        self.play(
            AnimationGroup(
                Create(line),
                GrowFromCenter(A),
                GrowFromCenter(B),
                lag_ratio=1
            )
        )
        self.play(
            Create(AP),
            Create(BP),
            Create(P),
            run_time=3
        )

        self.play(
            Write(label[:-1]),
            GrowFromCenter(label_P),
            run_time=2
        )
        self.wait()
        self.play(
            P.animate.shift(3 * RIGHT),
            rate_func=there_and_back,
            run_time=5
        )
        self.wait()

        # симметричные построения
        self.play(
            AnimationGroup(
                Create(line_sym),
                GrowFromCenter(A_sym),
                GrowFromCenter(label[-1]),
                Create(right_angle),
                lag_ratio=0.2,
                run_time=2
            )
        )

        self.play(Create(AP_sym), run_time=1.5)
        self.play(
            P.animate.shift(3 * RIGHT),
            rate_func=there_and_back,
            run_time=6
        )
        self.wait()

        # Ответ
        shortest_way = Line(A_sym.get_center(),
            B.get_center()).set_stroke(YELLOW, 3)
        self.play(Create(shortest_way), run_time=2)
        self.play(P.animate.shift(1.6 * RIGHT), run_time=2)
        self.wait()

class Fracts(Scene):
    def construct(self):
        frac = MathTex(
            r"\frac{\pi}{3^e + 1}"
        )
        self.play(Write(frac[0][:2]))
        self.wait()
        denominator = MathTex(
            r"3^e + 1"
        ).shift(2 * UP)
        self.play(Write(denominator))
        arc = Arc(radius=2, start_angle=PI/2, angle=-PI)
        self.wait()
        self.play(MoveAlongPath(denominator, arc))
        self.play(denominator.animate.next_to(frac[0][1], DOWN))
        self.wait()
        self.play(FadeOut(*self.mobjects))


class AAA(Scene):
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


class Parallel(Scene):
    def construct(self):
        geometry = VGroup()
        plane = NumberPlane(
            background_line_style={
                "stroke_width": 2,
                "stroke_color": GREY,
                "stroke_opacity": 0.7
            }
        )
        self.add(plane)
        line_1 = Line(4 * LEFT, 4 * RIGHT).shift(DOWN)
        line_2 = line_1.copy().shift(2 * UP)
        self.play(Create(line_1), Create(line_2))
        A = Dot(UR)
        B = Dot(DL)
        self.play(Create(A), Create(B))
        size_tracer = ValueTracker(1)
        line_ab = always_redraw(
            lambda: Line(B.get_center(), A.get_center())
        )
        angle_1 = always_redraw(
            lambda: Angle(line_1, line_ab)
        )
        angle_2 = always_redraw(
            lambda: Angle(line_2, line_ab, quadrant=(-1,-1))
        )
        A_label = always_redraw(
            lambda: MathTex("A").next_to(angle_1, DOWN)
        )
        B_label = always_redraw(
            lambda: MathTex("B").next_to(angle_2, UP)
        )

        C = Dot(3 * LEFT + UP)
        C_label = MathTex("C").next_to(C, UP)
        D = Dot(3 * RIGHT + DOWN)
        D_label = MathTex("D").next_to(D, DOWN)
        self.play(Create(line_ab))
        self.play(Create(angle_1), Create(A_label))
        self.play(Create(angle_2), Create(B_label))
        self.play(AnimationGroup(
            Create(C), Create(C_label),
            Create(D), Create(D_label)
        ), lag_ratio=0.2)

        self.play(A.animate.shift(3*RIGHT), run_time=2,
                  rate_func=there_and_back)
        self.play(B.animate.shift(2*LEFT))
        self.play(B.animate.shift(5 * RIGHT))
        self.play(B.animate.shift(3 * LEFT))
        self.wait()

        equation = MathTex(
            r"BC \, \| \, AD \Longrightarrow \angle CBA = \angle DAB"
        ).shift(2.5 * UP)
        self.play(Write(equation, run_time=3))
        self.play(Indicate(equation, run_time=3))
        self.wait()
        composition = VGroup(
            A, B, C, D,
            A_label, B_label, C_label, D_label,
            angle_1, angle_2, line_ab, line_1, line_2
        )

        self.play(FadeOut(equation, plane))
        for i in angle_1, angle_2, A_label, B_label:
            i.clear_updaters()
        size_tracer.set_value(0.87)
        self.play(composition.animate.scale(size_tracer.get_value()))
        self.wait()
        self.play(composition.animate.to_edge(UL, buff=0.2))
        self.wait()
        
        first_part = Tex(
            "1. Отметим середину отрезка $AB$, обозначим её буквой $O$",
            font_size=20
        ).to_corner(UR, buff=0.5)
        second_part = Tex(
            "2. Проведем к прямым из точки $O$ перпендекуляры, отметим основания"
            " полученных перпендекуляров как $E$ и $F$ соответственно",
            font_size=20
        ).next_to(first_part, DOWN).to_edge(RIGHT, buff=0.3)


        self.play(FadeIn(first_part, shift=UP))
        self.wait(3)
        O = Dot(line_ab.get_center(), z_index=1)
        O_label = MathTex("O").next_to(O, LEFT).scale(size_tracer.get_value())
        perp_1 = Line(line_ab.get_center(), line_ab.get_center() + size_tracer.get_value() * UP, color=YELLOW)
        
        E = Dot(line_ab.get_center() + size_tracer.get_value() * UP, color=YELLOW)
        E_label = MathTex("E", color=YELLOW).next_to(E, UP).scale(size_tracer.get_value())

        right_angle_1 = RightAngle(perp_1, line_2, quadrant=(-1,-1)).scale(0.5,
                about_point=E.get_center())
        perp_2 = Line(line_ab.get_center(), line_ab.get_center() + size_tracer.get_value() * DOWN, color=YELLOW)

        F = Dot(line_ab.get_center() + size_tracer.get_value() * DOWN, color=YELLOW)
        F_label = MathTex("F", color=YELLOW).next_to(F, DOWN).scale(size_tracer.get_value())
        right_angle_2 = RightAngle(perp_2, line_1, quadrant=(-1,1)).scale(0.5,
                about_point=F.get_center())

        self.play(Create(O), Write(O_label))
        self.play(Write(second_part), 
                  Create(perp_1),
                  Create(right_angle_1),
                  Create(E),
                  Write(E_label),
                  Create(perp_2),
                  Create(right_angle_2),
                  Create(F),
                  Write(F_label),
                  run_time=6,
                  lag_ratio=0.3)
        self.wait()

        double_angle_FOB_1 = Angle(
            line_ab, perp_1, radius=0.3
        )
        double_angle_FOB_2 = Angle(
            line_ab, perp_1, radius=0.35
        )
        double_angle_EOA_1 = Angle(
            line_ab, perp_2, radius=0.3, quadrant=(-1,1)
        )
        double_angle_EOA_2 = Angle(
            line_ab, perp_2, radius=0.35, quadrant=(-1,1)
        )
        self.play(Create(double_angle_FOB_1),
                  Create(double_angle_FOB_2),
                  Create(double_angle_EOA_1),
                  Create(double_angle_EOA_2)
        )

        third_part = Tex(
            "3. Обозначим вертикальные углы $\\angle EOB$ и $\\angle FOA$."
            " По свойству, они равны.", font_size=20
        ).next_to(second_part, DOWN).to_edge(RIGHT, buff=0.3)
        self.play(FadeIn(third_part))
        self.wait(2)
        fourth_part_1 = Tex(
            "4. Рассмотрим $\\triangle AOF$ и $\\triangle BOE$:",
            font_size=20,
        ).next_to(third_part, DOWN, aligned_edge=LEFT)
        fourth_part = Tex(
            r"""\begin{itemize}
            \item $\angle EOB = \angle AOF$ (вертикальные),
            \item $AO = OB$ ($O$ - середина отрезка $AB$),
            \item $\angle BEO = \angle AFO$ (прямые)
            \end{itemize}""",
            font_size=20
        ).next_to(fourth_part_1, DOWN, aligned_edge=LEFT)
        self.play(Write(fourth_part_1), run_time=2)
        self.play(Write(fourth_part), run_time=7)
        self.wait()
        ergo = BraceLabel(fourth_part,
            r"\Longrightarrow \triangle AOF = \triangle BOE", RIGHT, font_size=20)
        self.play(FadeIn(ergo, shift=LEFT))
        self.wait()
        fifth_part = Tex(
            "5. Из равенства треугольников следует равенство углов "
            "$\\angle CBA$ и $\\angle DAB$",
            font_size=20
        ).next_to(fourth_part, DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=0.3)
        qed = Tex("Q.E.D.", font_size = 48).next_to(fifth_part, DOWN)
        self.play(FadeIn(fifth_part, shift=DOWN))
        self.play(Indicate(angle_1), Indicate(angle_2), run_time=2)
        self.wait(2)
        self.play(Write(qed), run_time=4)
        self.play(Indicate(qed), run_time=3)
        box = SurroundingRectangle(qed, color=YELLOW)
        self.play(Create(box), run_time=2)
        self.wait(2)
        self.play(FadeOut(*self.mobjects, shift=DOWN), run_time=6, lag_ratio=0.1)
        self.wait()

            
         

class ManyTriangles(Scene):
    def construct(self):
        A = Dot(UP, z_index=1)
        B = Dot(DL, z_index=1)
        C = Dot(DR, z_index=1)
        self.play(Create(A), Create(B), Create(C))
        ABC = always_redraw(
            lambda: Polygon(
                A.get_center(),
                B.get_center(),
                C.get_center()
            )
        )
        self.play(Create(ABC))
        circle = Circle()
        circle.add_updater(lambda x: x.surround(ABC, buffer_factor=1, dim_to_match=2))
        self.play(Create(circle))
        self.play(A.animate.shift(2*RIGHT), rate_func=there_and_back, run_time=3)
        self.wait()

        E = Dot(2 * RIGHT, z_index=1)
        F = Dot(2 * LEFT, z_index=1)
        self.play(Create(E), Create(F))
        ABF = always_redraw(
            lambda: Polygon(
                A.get_center(),
                B.get_center(),
                F.get_center()
            )
        )
        ACE = always_redraw(
            lambda: Polygon(
                A.get_center(),
                C.get_center(),
                E.get_center()
            )
        )
        self.play(Create(ACE), Create(ABF))
        self.play(A.animate.shift(2*RIGHT), rate_func=there_and_back, run_time=3)
        self.wait()
        self.play(AnimationGroup(
            Rotate(A, PI / 3, about_point=ORIGIN),
            Rotate(B, PI / 3, about_point=ORIGIN),
            Rotate(C, PI / 3, about_point=ORIGIN),
        ), rate_func=there_and_back, run_time=4)
        self.wait()

        self.play(Rotate(B, TAU, about_point = 2 * DL), run_time=3)
        self.wait()

class Introduction(Scene):
    def construct(self):
        greeting = Text("Какой-то левый чел", font="Rozovii Chulok", font_size=84,
                         stroke_color=GREY, stroke_width=2)
        sub_greet = Text(
            "представляет", color=GREY
            ).next_to(greeting, DOWN, buff=0.4)
        self.play(SpinInFromNothing(greeting), run_time=3, lag_ratio=0.1)
        self.play(Write(sub_greet), run_time=2)
        self.wait()
        self.play(FadeOut(greeting, sub_greet, shift=DOWN), run_time=2, lag_ratio=0.1)

