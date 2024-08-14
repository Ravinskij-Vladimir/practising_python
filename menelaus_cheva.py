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
        ).set_stroke(GREY, 2, 0.7).shift(DL)
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
        self.play(Create(dots))
        self.play(Create(triangle), run_time=2)
        self.play(B_dot.animate.shift(RIGHT), rate_func=there_and_back)
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
            r"\frac{AD}{DB} \cdot \frac{BF}{FC} \cdot \frac{CE}{EF} = 1"
        ).next_to(menelaus_text, DOWN)
        self.play(Write(menelaus_text))
        self.play(Create(menelaus_formula))
        self.wait()
        self.play(FadeOut(menelaus_formula, menelaus_text, shift=DOWN))

        #доказательство
        B1_dot = B_dot.copy().shift(3 * RIGHT).set_opacity(0)
        line_CB1 = always_redraw(lambda:
            Line(C_dot.get_center(), B1_dot.get_center(), color=BLUE)
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
        self.play(Create(line_CB1))
        self.play(Create(O_dot), Create(O_label))
        self.wait()
        self.play(
                  B_dot.animate.shift(RIGHT),
                  B1_dot.animate.shift(DL),
                  Rotate(line_CE, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(C_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  Rotate(E_dot, angle=-PI / 6, about_point=A_dot.get_center()),
                  run_time=4, rate_func=there_and_back
        )
        self.wait(2)

        

        
        