from manim import *

class LineA(Scene):
    def construct(self):
        A = Dot(DL)
        B = Dot(UR)
        l = always_redraw(lambda:
            Line(A.get_center(), B.get_center())
        )
        C = always_redraw(lambda:
            B.copy().scale(2 / 3, about_point=A.get_center())
            .scale(3 / 2)
        )
        self.play(Create(A), Create(B), Create(l))
        self.play(Create(C))
        self.wait()
        self.play(B.animate.shift(RIGHT), rate_func=there_and_back)

class Menelaus(Scene):

    def get_intersection(self, dots, **kwargs):
        x1_1, y1_1 = dots[0], dots[1]
        x1_2, y1_2 = dots[2], dots[3]
        x2_1, y2_1 = dots[4], dots[5]
        x2_2, y2_2 = dots[6], dots[7]

        A1 = y1_1 - y1_2
        B1 = x1_2 - x1_1
        C1 = x1_1*y1_2 - x1_2*y1_1
        A2 = y2_1 - y2_2
        B2 = x2_2 - x2_1
        C2 = x2_1*y2_2 - x2_2*y2_1

        result_dot = Dot()
        if B1*A2 - B2*A1 and A1:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            x = (-C1 - B1*y) / A1
            result_dot = Dot(x * RIGHT + y * UP, **kwargs)
        elif B1*A2 - B2*A1 and A2:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            x = (-C2 - B2*y) / A2
            result_dot = Dot(x * RIGHT + y * UP, **kwargs)
        else:
            result_dot = None
        return result_dot


    def construct(self):
        plane = NumberPlane(
            background_line_style={
                "stroke_width": 2,
                "stroke_color": GREY,
                "stroke_opacity": 0.7
            }
        ).set_stroke(GREY, 2, 0.7)
        self.play(Create(plane), run_time=2)
        # Постановка проблемы и первоначальные условия
        A_dot = Dot(LEFT, radius=0.03)
        A_label = always_redraw(lambda: 
            Text("A", font_size=18).next_to(A_dot, DOWN, buff=0.1)
        )
        B_dot = Dot(UP, radius=0.03)
        B_label = always_redraw(lambda: 
            Text("B", font_size=18).next_to(B_dot, UP, buff=0.1)
        )
        C_dot = Dot(0.5 * RIGHT, radius=0.03)
        C_label = always_redraw(lambda: 
            Text("C", font_size=18).next_to(C_dot, DOWN, buff=0.1)
        )
        
        dots = VGroup(A_dot, A_label, B_dot, B_label, C_dot, C_label)
        dots.scale(2, about_point=ORIGIN)
        triangle = always_redraw(lambda:
            Polygon(A_dot.get_center(),
                    B_dot.get_center(),
                    C_dot.get_center(),
                    z_index=-1)
        )
        self.play(Create(dots), run_time=1.5)
        self.play(Create(triangle), run_time=2)
        self.play(B_dot.animate.shift(RIGHT), rate_func=there_and_back, run_time=3)
        self.wait()
        line_CE = always_redraw(lambda:
            Line(C_dot.get_center(), C_dot.get_center() + 4 * RIGHT, color=BLUE, z_index=-1)
        )
        
        E_dot = always_redraw(lambda:
            Dot(line_CE.get_right(), radius=0.06).scale(2 / 3, about_point=C_dot.get_center())
            .scale(3 / 2)
        )
        
        E_label = always_redraw(lambda:
            Text("E", font_size=18).next_to(E_dot, DOWN, buff=0.1)
        )
        self.play(Create(line_CE), Create(E_dot), Create(E_label))

        #Сдвиг точки вдоль прямой
        D_dot = always_redraw(lambda:
            B_dot.copy().scale(2 / 3, about_point=A_dot.get_center())
            .scale(3 / 2)
        )
        
        D_label = always_redraw(lambda:
            Text("D", font_size=18).next_to(D_dot, LEFT, buff=0.1)
        )

        line_DE = always_redraw(lambda:
            Line(D_dot.get_center(), E_dot.get_center(), z_index=-1, color=BLUE)
        )
        self.play(Create(D_dot), Create(D_label), Create(line_DE))
        F_dot = always_redraw(lambda:
            self.get_intersection([
                D_dot.get_x(), D_dot.get_y(),
                E_dot.get_x(), E_dot.get_y(),
                C_dot.get_x(), C_dot.get_y(),
                B_dot.get_x(), B_dot.get_y()
            ],
            radius=0.06)
        )
        F_label = always_redraw(lambda:
            Text("F", font_size=18).next_to(F_dot, RIGHT + 0.3 * UP, buff=0.1))
        self.play(Create(F_dot), Create(F_label))
        dots.add(D_dot, D_label, F_dot, F_label, E_dot, E_label)
        self.play(E_dot.animate.shift(1.5*LEFT), rate_func=there_and_back, run_time=3)
        self.wait()
        composition = VGroup(triangle, dots, line_CE, line_DE)
        self.play(composition.animate.to_corner(UL, buff=0.5))
        self.wait()

        menelaus_text = Text("Теорема Менелая").to_edge(UR, buff=0.7)
        menelaus_formula = MathTex(
            r"\frac{AD}{DB} \cdot \frac{BF}{FC} \cdot \frac{CE}{EA} = 1"
        ).next_to(menelaus_text, DOWN)
        self.play(Write(menelaus_text), run_time=2)
        self.play(Create(menelaus_formula), run_time=3)
        self.wait()
        self.play(FadeOut(menelaus_formula, menelaus_text, shift=DOWN))
        self.play(FadeOut(plane))

        #доказательство
        first_part = Tex(
            "1. Проведем прямую $CO$ из точки $C$, параллельную стороне треугольника $AB$. Тогда "
            "$O$ - точка пересечения данной прямой с $DE$.",
            font_size=20
        ).to_edge(UR, buff=0.5)
        self.play(Write(first_part), run_time=4)
        B1_dot = always_redraw(lambda:
            Dot(Line(C_dot.get_center(), C_dot.get_center() + 2 * RIGHT + 4 * UP)
            .get_right()).set_opacity(0)
        )
        #B1_dot = Dot(B_dot.get_center() + 3 * RIGHT)
        self.play(Create(B1_dot))
        line_CB1 = always_redraw(lambda:
            Line(C_dot.get_center(), B1_dot.get_center(), color=RED)
        )
        O_dot = always_redraw(lambda:
            self.get_intersection([
                C_dot.get_x(), C_dot.get_y(),
                B1_dot.get_x(), B1_dot.get_y(),
                F_dot.get_x(), F_dot.get_y(),
                E_dot.get_x(), E_dot.get_y()
            ],
            radius=0.06)
        )
        O_label = always_redraw(lambda:
            Text("O", font_size=18).next_to(O_dot, UP, buff=0.1)
        )
        line_CO = always_redraw(lambda:
            Line(C_dot.get_center(), O_dot.get_center(), color=BLUE, z_index=-1)
        )

        self.play(Create(O_dot), Create(O_label),
            TransformFromCopy(Line(A_dot.get_center(), B_dot.get_center()),
                line_CO)
        )
        self.wait()
        self.play(
                  #Rotate(B_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(line_CE, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(C_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(O_dot, angle=-PI / 6, about_point=O_dot.get_center() - 3 * RIGHT),
                  Rotate(E_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  run_time=4, rate_func=there_and_back
        )
        self.wait(2)

        # second_part = Tex(
        #     r"2. Рассмотрим $\triangle OEC$ и $\triangle DEA$:",
        #     r"""
        #     \begin{itemize}
        #         \item $\angle OEC$ - общий,  
        #         \item $\angle OCE = \angle DAE$ - соответственные при \\ $OC \, \| \, DA$
        #     \end{itemize}
        #     """,
        #     font_size=20
        # ).next_to(first_part, DOWN, aligned_edge=LEFT)
        # second_part[0].align_to(first_part, LEFT)
        # brace = BraceLabel(second_part[1], 
        #     r"\Longrightarrow \triangle OEC \sim \triangle DEA",
        #     RIGHT,
        #     font_size=20
        # )
        # angle_CEF = Angle(line_CE, line_DE, quadrant=(-1,-1),
        #                   other_angle=True,
        #                   radius=1)
        # angle_OCE = Angle.from_three_points(
        #     O_dot.get_center(),
        #     C_dot.get_center(),
        #     E_dot.get_center(),
        #     color=GREY,
        #     other_angle=True
        # )
        # angle_ADF = Angle.from_three_points(
        #     A_dot.get_center(),
        #     D_dot.get_center(),
        #     F_dot.get_center(),
        #     color=GREY,
        #     other_angle=False
        # )
        # self.play(FadeIn(second_part, shift=UP))
        # self.play(Create(angle_CEF))
        # self.play(Create(angle_OCE), Create(angle_ADF))
        # self.wait(1.5)
        # self.play(TransformFromCopy(second_part, brace))
        # self.wait()

        third_part = Tex(
            r"Из подобия:",
            r"""
            \begin{equation*}
                \frac{OC}{DA} = \frac{OE}{EO} = \frac{CE}{EA} 
                \Longrightarrow OC = \frac{CE \cdot DA}{EA} \;(1)
            \end{equation*}
            """,
            font_size=20
        ).next_to(composition, DOWN)
        # self.play(Write(third_part[0]), run_time=1)
        # self.play(Write(third_part[1][:17]), run_time=2)
        # self.wait()
        # self.play(TransformFromCopy(third_part[1][:17], third_part[1][17:]))
        # self.wait()

        fourth_part = Tex(
            r"4. Рассмотрим $\triangle OFC$ и $\triangle FDB$:",
            r"""
            \begin{itemize}
                \item $\angle OFC = \angle DFB$ - вертикальные,  
                \item $\angle FDB = \angle FOC$ - накрест-лежащие при \\ $OC \, \| \, DA$
            \end{itemize}
            """,
            font_size=20
        ).next_to(third_part, DOWN, aligned_edge=LEFT)
        fourth_part[0].align_to(third_part, LEFT)
        brace_2 = BraceLabel(fourth_part[1], 
            r"\Longrightarrow \triangle OFC \sim \triangle FDB",
            RIGHT,
            font_size=20
        )
        angle_OFC = Angle.from_three_points(
            O_dot.get_center(),
            F_dot.get_center(),
            C_dot.get_center(),
            other_angle=True,
            color=GREEN
        )
        angle_DFB = Angle.from_three_points(
            D_dot.get_center(),
            F_dot.get_center(),
            B_dot.get_center(),
            other_angle=True,
            color=GREEN
        )

        angle_FDB = Angle.from_three_points(
            F_dot.get_center(),
            D_dot.get_center(),
            B_dot.get_center(),
            color=RED_A
        )

        angle_FOC = Angle.from_three_points(
            F_dot.get_center(),
            O_dot.get_center(),
            C_dot.get_center(),
            color=RED_A
        )
        self.play(FadeIn(fourth_part, shift=UP))
        self.play(Create(angle_OFC), Create(angle_DFB))
        self.play(Create(angle_FDB), Create(angle_FOC))
        self.wait(1.5)
        self.play(FadeIn(brace_2, shift=RIGHT))
        self.wait()

        # fifth_part = Tex(
        #     r"Из подобия:",
        #     r"""
        #     \begin{equation*}
        #         \frac{OC}{DB} = \frac{CF}{BF} = \frac{OF}{OD} 
        #         \Longrightarrow OC = \frac{DB \cdot CF}{BF} \; (2)
        #     \end{equation*}
        #     """,
        #     font_size=20
        # ).next_to(fourth_part, DOWN)
        # self.play(Write(fifth_part[0]), run_time=1)
        # self.play(Write(fifth_part[1][:17]), run_time=2)
        # self.wait()
        # self.play(FadeIn(fifth_part[1][17:], shift=RIGHT))
        # self.wait()

        # sixth_part = Tex(
        #     "Из пунктов (1) и (2) получаем:",
        #     r"""
        #         \begin{equation*}
        #             \frac{CE \cdot DA}{EA} = \frac{DB \cdot CF}{BF}
        #             \Longrightarrow \frac{AD}{DB} \cdot \frac{BF}{FC} \cdot \frac{CE}{EA} = 1
        #         \end{equation*}
        #     """,
        #     font_size=20
        # ).next_to(second_part, DOWN, buff=0.5)
        # self.play(Write(sixth_part), run_time=3)
        # self.play(Indicate(sixth_part[1]), run_time=4)
        # box = SurroundingRectangle(sixth_part[1], 
        #     corner_radius=-0.10,
        #     stroke_width=2)
        # self.play(Create(box), run_time=1.5)
        # qed = Tex("Q.E.D.").next_to(sixth_part, RIGHT)
        # self.play(Write(qed), run_time=3)
        
        # self.wait()
        # self.play(FadeOut(*self.mobjects))
        # self.wait()


        

        
        