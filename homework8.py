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

        euler = MathTex("e^{i\pi} + 1 = 0")
        self.play(Write(euler[0][0]), run_time=2)
        i_text = MathTex("i").shift(2 * DR)
        self.play(GrowFromCenter(i_text))
        self.play(Indicate(i_text, scale=3), run_time=2)
        self.play(
            ReplacementTransform(i_text, euler[0][1]),
            Write(euler[0][2]),
            TransformFromCopy(euler[0][0], euler[0][4]),
            Write(euler[0][3]),
            Write(euler[0][5:]),
            lag_ratio=0.7, run_time=1.5)
        self.wait()


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
        # Initial composition
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

        # Theorem
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
        
        # Theorem proof block
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
        
        #In the end
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
        group = VGroup(A,B,C,E,F,ABC,ACE, ABF)
        self.play(group.animate.become(circle))
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

class TriangleHeight(Scene):
    def construct(self):
        A = Dot(ORIGIN)
        B = Dot(2 * RIGHT + 6 * UP)
        C = Dot(7 * RIGHT)
        vertices = VGroup(A, B, C).move_to(ORIGIN)
        vertices.set_stroke(WHITE, 2)
        ABC = always_redraw(
            lambda: Polygon(
                A.get_center(),
                B.get_center(),
                C.get_center()
            )
        )
        self.play(Create(ABC), Create(vertices), run_time=3)

        H = always_redraw(
            lambda: Dot(B.get_center() + 6 * DOWN)
            .set_stroke(BLACK, 2.5)
        )

        BH = always_redraw(
            lambda: Line(B.get_center(), H.get_center(), z_index=-1)
            .set_stroke(BLUE, 3)
        )

        angle = always_redraw(
            lambda: Elbow(width=0.3).set_stroke(BLUE, 2)
            .next_to(H.get_center(), UR, buff=0)
        )
        self.play(Create(H), Create(BH, run_time=2),
                  Create(angle), lag_ratio=0.3)
        self.play(B.animate.shift(3.5 * RIGHT), run_time=7,
                  rate_func=there_and_back)
        self.wait()
        

class Outro(Scene):
    def construct(self):
        names = ["Debbie Woods",
                 "John Johnson",
                 "Carmen Burgess",
                 "Theodore Day",
                 "Tony Murphy",
                 "Ruth Johnson",
                 "Sandra Garcia",
                 "Colleen Hall",
                 "Eduardo Martin",
                 "Tracy Johnson",
                 "Stacey Scott"]
        for name in names:
            name_tex = Text(name).to_edge(DOWN)
            self.play(FadeIn(name_tex), run_time=0.2)
            self.play(name_tex.animate.to_edge(UP), run_time=0.4)
            self.play(FadeOut(name_tex), run_time=0.2)
        self.wait()

class TheEnd(Scene):
    def construct(self):
        end = Text("The end!", font="Comic Sans MS", font_size=96)
        line = Underline(end, color=YELLOW)
        self.play(Write(end), run_time=4)
        self.play(Flash(end), Create(line, rate_func=there_and_back, run_time=2))
        self.play(Unwrite(end), reverse=False, run_time=3)


class Yensen(Scene):
    def construct(self):
        pass

class FillingCircle(Scene):
    def construct(self):
        big_circ = Circle().set_stroke(GREEN_D, 5, 1)
        fill_percentage = ValueTracker(-0.15)
        circ = always_redraw(lambda:
            Sector(start_angle=PI / 2,
                angle = 360 * DEGREES * fill_percentage.get_value(),
                color=GREEN).set_stroke(BLACK, 0, 0)
        )
        perc_value = always_redraw( lambda:
            DecimalNumber(fill_percentage.get_value() * 100))
        percentage = always_redraw(lambda:
            Text(f"Fill percentage: {np.round(-fill_percentage.get_value() * 100, 2)}%").shift(2 * UP)
        )
        self.play(Write(percentage))
        self.play(GrowFromCenter(big_circ))
        self.play(GrowFromPoint(circ, ORIGIN), run_time=2)
        self.play(fill_percentage.animate.set_value(-0.75),
                  rate_func=there_and_back,
                  run_time=5)
        self.wait()

class ProportionalTriangle(Scene):

    def collapsing(self, dest_group, source_group) -> None:
        self.play(ReplacementTransform(source_group, dest_group))
        self.wait()
        self.play(GrowFromPoint(dest_group, ORIGIN),
                  rate_func=lambda t: smooth(1 - t))
        return None
        
    def print_text(self, text) -> None:
        text.shift(3 * UP)
        self.play(Create(text), run_time=2)
        return None

    def construct(self):

        title = Text("Признаки подобия треугольников")
        self.print_text(title)
        self.wait(2)
        self.play(Uncreate(title))
        self.wait()

        two_sides_one_angle = Text("По двум пропорциональным сторонам и углу между ними",
                                   font_size=36)
        self.print_text(two_sides_one_angle)
        # Подобие по двум сторонам и углу между ними
        triangle3 = Polygon(
            LEFT, UP, 0.5 * RIGHT
        ).shift(LEFT)
        angle3 = Angle.from_three_points(UP, LEFT, RIGHT, other_angle=True).shift(LEFT)
         
        line_ab = Line(LEFT, UP, color=YELLOW).shift(LEFT)
        line_ac = Line(LEFT, 0.5 * RIGHT, color=YELLOW).shift(LEFT)
        tr_group_3 = VGroup(triangle3, angle3, line_ab, line_ac)
        tr_group_3_copy = tr_group_3.copy().scale(2, about_point=LEFT).shift(3 * RIGHT)
        for group in tr_group_3, tr_group_3_copy:
            self.play(GrowFromCenter(group[:2]))
        
        for group in tr_group_3, tr_group_3_copy:
            self.play(Create(group[2]), Create(group[3]), rate_func=there_and_back, run_time=4)
        self.wait()
        
        self.collapsing(tr_group_3, tr_group_3_copy)
        self.play(Uncreate(two_sides_one_angle))


        # Подобие по двум углам
        two_angles = Text("По двум равным углам", font_size=36)
        self.print_text(two_angles)
        triangle1 = Polygon(
            LEFT, UP, 0.5 * RIGHT
        ).shift(LEFT)
        angle1 = Angle.from_three_points(UP, LEFT, RIGHT, other_angle=True).shift(LEFT)
        angle_2 = Angle(
            Line(UP, 0.5 * RIGHT),
            Line(0.5 * RIGHT, LEFT),
            quadrant=(-1,1),
            color=GREY
        ).shift(LEFT)
        tr_group1 = VGroup(triangle1, angle1, angle_2)
        tr_group2 = tr_group1.copy().scale(2, about_point = LEFT).shift(3 * RIGHT)
        self.play(GrowFromCenter(tr_group1))
        self.play(GrowFromCenter(tr_group2))
        self.wait()
        self.play(Indicate(tr_group1[1]), Indicate(tr_group2[1]), run_time=1.5)
        self.play(Indicate(tr_group1[2]), Indicate(tr_group2[2]), run_time=1.5)
        self.wait()

        self.collapsing(tr_group1, tr_group2)
        self.play(Uncreate(two_angles))

        # подобие трем сторонам
        three_sides = Text("По трём пропорциональным сторонам", font_size=36)
        self.print_text(three_sides)
        triangle4 = Polygon(LEFT, UP, 0.5 * RIGHT).shift(LEFT)
        line_ab = Line(LEFT, UP, color=YELLOW).shift(LEFT)
        line_bc = Line(UP, 0.5 * RIGHT, color=YELLOW).shift(LEFT)
        
        line_ac_2 = Line(LEFT, 0.5 * RIGHT, color=YELLOW).shift(LEFT)
        tr_group_4 = VGroup(triangle4, line_ab, line_bc, line_ac_2)
        tr_group_5 = tr_group_4.copy().scale(2, about_point=LEFT).shift(3 * RIGHT)
        self.play(GrowFromCenter(tr_group_4[0]))
        self.play(GrowFromCenter(tr_group_5[0]))
                  
        for i in range(1, 4):
            self.play(Create(tr_group_4[i]), Create(tr_group_5[i]), rate_func = there_and_back, run_time=2)
        self.wait()
        
        self.collapsing(tr_group_4, tr_group_5)
        self.play(Uncreate(three_sides))
        self.wait()

        




