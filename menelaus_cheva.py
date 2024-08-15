from manim import *

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
        # Постановка проблемы и первоначальные условия
        self.next_section("Start")
        plane = NumberPlane(
            background_line_style={
                "stroke_width": 2,
                "stroke_color": GREY,
                "stroke_opacity": 0.7
            }
        ).set_stroke(GREY, 2, 0.7)
        self.play(Create(plane), run_time=2)
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
        self.play(Create(menelaus_formula), run_time=2)
        self.wait()
        first_pair_1 = Line(
            A_dot.get_center(),
            D_dot.get_center(),
            color=YELLOW
        )
        first_pair_2 = Line(
            D_dot.get_center(),
            B_dot.get_center(),
            color=YELLOW
        )
        second_pair_1 = Line(
            B_dot.get_center(),
            F_dot.get_center(),
            color=YELLOW
        )
        second_pair_2 = Line(
            F_dot.get_center(),
            C_dot.get_center(),
            color=YELLOW
        )
        third_pair_1 = Line(
            E_dot.get_center(),
            C_dot.get_center(),
            color=YELLOW
        )
        third_pair_2 = Line(
            E_dot.get_center(),
            A_dot.get_center(),
            color=YELLOW
        )
        self.play(Create(first_pair_1), Create(first_pair_2),
                  run_time=3, rate_func=there_and_back)
        self.play(Create(second_pair_1), Create(second_pair_2),
                  run_time=3, rate_func=there_and_back)
        self.play(Create(third_pair_1), Create(third_pair_2),
                  run_time=3, rate_func=there_and_back)
        self.remove(first_pair_1, first_pair_2, second_pair_1, second_pair_2,
                    third_pair_1, third_pair_2)

        
        self.play(FadeOut(menelaus_formula, menelaus_text, shift=DOWN))
        self.play(FadeOut(plane))



        #доказательство
        self.next_section("proof block, first part")
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
                  Rotate(line_CE, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(C_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(O_dot, angle=-PI / 6, about_point=O_dot.get_center() - 3 * RIGHT),
                  Rotate(E_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  run_time=4, rate_func=there_and_back
        )
        self.wait(2)

        self.next_section("Second part")
        second_part = Tex(
            r"2. Рассмотрим $\triangle OEC$ и $\triangle DEA$:",
            r"""
            \begin{itemize}
                \item $\angle OEC$ - общий,  
                \item $\angle COE = \angle ADE$ - соответственные при \\ $OC \, \| \, DA$
            \end{itemize}
            """,
            font_size=20
        ).next_to(first_part, DOWN, aligned_edge=LEFT)
        second_part[0].align_to(first_part, LEFT)
        brace = BraceLabel(second_part[1], 
            r"\Longrightarrow \triangle OEC \sim \triangle DEA",
            RIGHT,
            font_size=20
        )
        angle_CEF = Angle(line_CE, line_DE, quadrant=(-1,-1),
                          other_angle=True,
                          radius=1)
        angle_COE = Angle.from_three_points(
            C_dot.get_center(),
            O_dot.get_center(),
            E_dot.get_center(),
            color=GREY,
            other_angle=False
        )
        angle_ADF = Angle.from_three_points(
            A_dot.get_center(),
            D_dot.get_center(),
            F_dot.get_center(),
            color=GREY,
            other_angle=False
        )
        self.play(FadeIn(second_part, shift=UP))
        self.play(Create(angle_CEF))
        self.play(Create(angle_COE), Create(angle_ADF))
        self.wait(1.5)
        self.play(TransformFromCopy(second_part, brace))
        self.wait()

        self.next_section("Third part")
        third_part = Tex(
            r"Из подобия:",
            r"""
            \begin{equation*}
                \frac{OC}{DA} = \frac{OE}{ED} = \frac{CE}{EA} 
                \Longrightarrow OC = \frac{CE \cdot DA}{EA} \;(1)
            \end{equation*}
            """,
            font_size=20
        ).next_to(composition, DOWN)
        self.play(Write(third_part[0]), run_time=1)
        self.play(Write(third_part[1][:17]), run_time=2)
        self.wait()
        self.play(TransformFromCopy(third_part[1][:17], third_part[1][17:]))
        self.wait()

        self.next_section("Fourth part")
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
        self.play(Create(angle_OFC), Create(angle_DFB), run_time=2)
        self.play(Create(angle_FDB), Create(angle_FOC), run_time=2)
        self.wait(1.5)
        self.play(FadeIn(brace_2, shift=RIGHT))
        self.wait()

        self.next_section("Fifth part")
        fifth_part = Tex(
            r"Из подобия:",
            r"""
            \begin{equation*}
                \frac{OC}{DB} = \frac{CF}{BF} = \frac{OF}{OD} 
                \Longrightarrow OC = \frac{DB \cdot CF}{BF} \; (2)
            \end{equation*}
            """,
            font_size=20
        ).next_to(fourth_part, DOWN)
        self.play(Write(fifth_part[0]), run_time=1)
        self.play(Write(fifth_part[1][:17]), run_time=2)
        self.wait()
        self.play(FadeIn(fifth_part[1][17:], shift=RIGHT))
        self.wait()

        self.next_section("Sixth part")
        sixth_part = Tex(
            "Из пунктов (1) и (2) получаем:",
            r"""
                \begin{equation*}
                    \frac{CE \cdot DA}{EA} = \frac{DB \cdot CF}{BF}
                    \Longrightarrow \frac{AD}{DB} \cdot \frac{BF}{FC} \cdot \frac{CE}{EA} = 1
                \end{equation*}
            """,
            font_size=20
        ).next_to(second_part, DOWN, buff=0.5)
        self.play(Write(sixth_part), run_time=3)
        self.play(Indicate(sixth_part[1]), run_time=4)
        box = SurroundingRectangle(sixth_part[1], 
            corner_radius=-0.10,
            stroke_width=2)
        self.play(Create(box), run_time=2)
        qed = Tex("Q.E.D.").next_to(sixth_part, DR)
        self.play(Write(qed), run_time=3)
        
        self.next_section("The end")
        self.wait()
        self.play(FadeOut(*self.mobjects))
        self.wait()


        
class Cheva(Scene):
    FONT_SIZE = 36
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
        self.next_section("Start")
        plane = NumberPlane().set_stroke(GREY, 2, 0.7)
        self.add(plane)
        A_dot = Dot(2*LEFT + DOWN)
        A_label = always_redraw(lambda:
            Tex("$A$", font_size=self.FONT_SIZE)
            .next_to(A_dot, LEFT)
        )

        B_dot = Dot(2* UP)
        B_label = always_redraw(lambda:
            Tex("$B$", font_size=self.FONT_SIZE)
            .next_to(B_dot, UP)
        )

        C_dot = Dot(2*RIGHT)
        C_label = always_redraw(lambda:
            Tex("$C$", font_size=self.FONT_SIZE)
            .next_to(C_dot, RIGHT)
        )
        vertices = VGroup(A_dot, A_label,
                          B_dot, B_label,
                          C_dot, C_label)
        triangle = always_redraw(lambda:
            Polygon(
                A_dot.get_center(),
                B_dot.get_center(),
                C_dot.get_center(),
                z_index=-1
            )
        )
        self.play(Create(vertices))
        self.play(GrowFromCenter(triangle))
        self.wait()
        self.next_section("C1 point")

        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center()).set_opacity(0)
        )
        line_BC = always_redraw(lambda:
            Line(B_dot.get_center(), C_dot.get_center()).set_opacity(0)
        )
        line_AC = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center()).set_opacity(0)
        )
        self.add(line_AB, line_AC, line_BC)
        
        C_1_dot = A_dot.copy()
        C_1_label = always_redraw(lambda:
            Tex("$C_1$", font_size=self.FONT_SIZE)
            .next_to(C_1_dot, LEFT)
        )
        self.add(C_1_label)
        self.play(C_1_dot.animate.move_to(
            line_AB.point_from_proportion(1 / 3)
        ))
        self.remove(C_1_dot)
        C_1_dot = always_redraw(lambda:
            Dot(line_AB.point_from_proportion(1 / 3))
        )
        self.add(C_1_dot)
        self.play(A_dot.animate.shift(UL), rate_func=there_and_back,
                  run_time=2)
        
        self.wait()

        self.next_section("A1 point")
        A_1_dot = B_dot.copy()
        A_1_label = always_redraw(lambda:
            Tex("$A_1$", font_size=self.FONT_SIZE)
            .next_to(A_1_dot, RIGHT)
        )
        self.add(A_1_label)
        self.play(A_1_dot.animate.move_to(
            line_BC.point_from_proportion(2 / 5)
        ))
        self.remove(A_1_dot)
        A_1_dot = always_redraw(lambda:
            Dot(line_BC.point_from_proportion(2 / 5))
        )
        self.add(A_1_dot)
       
        self.wait()

        self.next_section("B1 point")
        B_1_dot = C_dot.copy()
        B_1_label = always_redraw(lambda:
            Tex("$B_1$", font_size=self.FONT_SIZE)
            .next_to(B_1_dot, DOWN)
        )
        self.add(B_1_label)
        self.play(B_1_dot.animate.move_to(
            line_AC.point_from_proportion(1 / 4)
        ))
        self.remove(B_1_dot)
        B_1_dot = always_redraw(lambda:
            Dot(line_AC.point_from_proportion(1 / 4))
        )
        self.add(B_1_dot)
        
        self.wait()

        self.next_section("chevians")
        line_AA1 = always_redraw(lambda:
             Line(A_dot.get_center(), A_1_dot.get_center(),
                    z_index=-1, color=GREEN)                    
        )
        line_BB1 = always_redraw(lambda:
             Line(B_dot.get_center(), B_1_dot.get_center(),
                    z_index=-1, color=GREEN)                    
        )
        line_CC1 = always_redraw(lambda:
             Line(C_dot.get_center(), C_1_dot.get_center(),
                    z_index=-1, color=GREEN)                    
        )
        self.play(Create(line_AA1), Create(line_BB1), Create(line_CC1))
        O_dot = always_redraw(lambda:
            self.get_intersection([
                A_dot.get_x(), A_dot.get_y(),
                A_1_dot.get_x(), A_1_dot.get_y(),
                B_dot.get_x(), B_dot.get_y(),
                B_1_dot.get_x(), B_1_dot.get_y()
            ])
        )
        O_label = always_redraw(lambda:
            Tex("O", font_size=self.FONT_SIZE)
            .next_to(O_dot, UP))
        self.play(Create(O_dot), Create(O_label))
        self.wait()
        self.play(B_dot.animate.shift(UR),
                  A_dot.animate.shift(DOWN),
                  rate_func=there_and_back,
                  run_time=3)
        self.play(B_dot.animate.shift(2 * LEFT),
                  C_dot.animate.shift(UP),
                  rate_func=there_and_back,
                  run_time=3)
        self.play(A_dot.animate.shift(LEFT + 2 * UP),
                  C_dot.animate.shift(2 * DL),
                  rate_func=there_and_back,
                  run_time=3)
        self.wait()

        self.next_section("Cheva formula intro")
        cheva_text = Tex("Теорема Чевы:",
            font_size=self.FONT_SIZE).to_corner(UR, buff=0.4)
        cheva_formula=MathTex(
            r"\frac{AB_1}{B_1C} \cdot \frac{CA_1}{A_1B} \cdot \frac{BC_1}{C_1A} = 1",
            font_size=self.FONT_SIZE
        ).next_to(cheva_text, DOWN).to_edge(RIGHT, buff=0.4)

        self.play(Write(cheva_text))
        self.play(Create(cheva_formula), run_time=2)
        self.play(Indicate(cheva_formula), run_time=2)
        self.wait()
        self.play(FadeOut(plane, cheva_formula, cheva_text))

        self.next_section("Proof block start")
        composition = VGroup(A_dot, A_label,
                            B_dot, B_label,
                            C_dot, C_label,
                            A_1_dot, A_1_label,
                            triangle,
                            C_1_dot, C_1_label,
                            B_1_dot, B_1_label,
                            O_dot, O_label,
                            line_AA1, line_BB1, line_CC1
                            )
        self.play(composition.animate.to_corner(UL, buff=0.4))
        self.wait()
        self.remove(line_AB, line_AC, line_BC)

        self.next_section("First part")
        first_part = Tex(
            "1. Проведем к прямой $BB_1$ перпендекуляры "
            "из точек $A$ и $C$, обозначим основания высот "
            "как $K$ и $N$ соответственно", font_size=20
        ).to_edge(UR, buff=0.4)
        self.play(FadeIn(first_part, shift=UP))
        self.wait()
        


        
        