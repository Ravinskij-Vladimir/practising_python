from manim import *

class Intro(Scene):

    def write_and_clear(self, tex):
        self.play(Write(tex), run_time=3)
        self.wait()
        self.play(Unwrite(tex, reverse=False))
        self.wait()

    def construct(self):
        start = Tex("Замечательные точки треугольника")
        self.play(Write(start), run_time=3)
        self.play(start.animate.to_edge(UP, buff=0.4))
        self.wait()

        bisectors = Tex("Точка пересечения биссектрис",
            font_size=34).shift(2 * UL + LEFT)
        perpendicular_bisectors = Tex(
            r"Точка пересения \\ серединных перпендекуляров",
            font_size=34
        ).shift(2 * UR + RIGHT)
        heights = Tex("Точка пересечения высот",
            font_size=34).shift(2 * DL + LEFT)
        medians = Tex("Точка пересечения медиан",
            font_size=34).shift(2 * DR + RIGHT)
        
        self.play(AnimationGroup(
            GrowFromPoint(bisectors, ORIGIN),
            GrowFromPoint(perpendicular_bisectors, ORIGIN),
            GrowFromPoint(heights, ORIGIN),
            GrowFromPoint(medians, ORIGIN),
            lag_ratio=1),
            run_time=6,
            )
        self.wait()
        self.play(FadeOut(*self.mobjects))

        bisectors = Tex("Точка пересечения биссектрис").shift(UP)

        perpendicular_bisectors = Tex(
            r"Точка пересения \\ серединных перпендекуляров")
        
        group = VGroup(bisectors, perpendicular_bisectors).move_to(ORIGIN)
        self.write_and_clear(group)

        heights = Tex("Точка пересечения высот")
        self.write_and_clear(heights)

        medians = Tex("Точка пересечения медиан")
        self.write_and_clear(medians)

class TriangleAndCircle(Scene):
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
        A_dot = Dot(3 * LEFT)
        B_dot = Dot(3 * UP)
        C_dot = Dot(2 * DR)
        triangle = always_redraw(lambda:
            Polygon(
                A_dot.get_center(),
                B_dot.get_center(),
                C_dot.get_center(),
                z_index=-1
            )                  
        )
        self.play(Create(A_dot), Create(B_dot), Create(C_dot))
        self.play(Create(triangle))
        line_AB_perp = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center(), color=GREY).set_opacity(1)
            .rotate(PI / 2).scale(1.3)
        )
        line_AC_perp = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center(), color=GREY).set_opacity(1)
            .rotate(PI / 2).scale(1.3)
        )
        self.play(Create(line_AB_perp), Create(line_AC_perp))
        self.wait()
        O_dot = always_redraw(lambda:
            self.get_intersection([
                Dot(line_AB_perp.get_start()).get_x(), Dot(line_AB_perp.get_start()).get_y(),
                Dot(line_AB_perp.get_end()).get_x(), Dot(line_AB_perp.get_end()).get_y(),
                Dot(line_AC_perp.get_start()).get_x(), Dot(line_AC_perp.get_start()).get_y(),
                Dot(line_AC_perp.get_end()).get_x(), Dot(line_AC_perp.get_end()).get_y()
            ], color=YELLOW_D)
        )
        self.play(Create(O_dot))
        A_dot_copy = always_redraw(lambda:
            A_dot.copy()
        )
        line_AO = always_redraw(lambda:
            Line(O_dot.get_center(), A_dot_copy.get_center())        
        )
        self.play(Create(line_AO))
        circle = always_redraw(lambda:
            Circle(radius=line_AO.get_length(), stroke_width=3, stroke_color=DARK_BLUE).move_to(O_dot)
        )
        trace = TracedPath(A_dot_copy.get_center, stroke_color=DARK_BLUE, stroke_width=3)
        self.add(trace)
        self.play(Rotate(A_dot_copy, -TAU, about_point=O_dot.get_center()), run_time=3)
        self.add(circle)
        self.remove(trace)
        self.wait()
        self.play(A_dot.animate.shift(3 * LEFT + 2 * UP), rate_func=there_and_back, run_time=3)
        self.wait()
        line_AO.add_updater(lambda x: x.set_opacity(0))
        line_AB_perp.add_updater(lambda x: x.set_opacity(0))
        line_AC_perp.add_updater(lambda x: x.set_opacity(0))
        
        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center()).set_opacity(0)
        )
        line_BC = always_redraw(lambda:
            Line(B_dot.get_center(), C_dot.get_center()).set_opacity(0)
        )
        line_AC = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center()).set_opacity(0)
        )
        self.add(line_AC, line_BC, line_AB)

        A1_dot = always_redraw(lambda:
            Dot(line_BC.point_from_proportion(
                line_AB.get_length() / (line_AB.get_length() + line_AC.get_length()))
            )
        )

        B1_dot = always_redraw(lambda:
            Dot(line_AC.point_from_proportion(
                line_AB.get_length() / (line_BC.get_length() + line_AB.get_length())
                )
            )
        )
        
        

        bisector_A = always_redraw(lambda:
            Line(A_dot.get_center(), A1_dot.get_center(), color=TEAL)
        )
        bisector_B = always_redraw(lambda:
            Line(B_dot.get_center(), B1_dot.get_center(), color=TEAL)
        )
        self.play(Create(A1_dot), Create(B1_dot),
                  TransformFromCopy(line_AC, bisector_B),
                  TransformFromCopy(line_AB, bisector_A), run_time=3)

        O1_dot = always_redraw(lambda:
            self.get_intersection([
                bisector_A.get_start()[0], bisector_A.get_start()[1],
                bisector_A.get_end()[0], bisector_A.get_end()[1],
                bisector_B.get_start()[0], bisector_B.get_start()[1],
                bisector_B.get_end()[0], bisector_B.get_end()[1]
            ], color=YELLOW)                       
        )
        self.play(Create(O1_dot))
        O1_dot_proj = always_redraw(lambda:
            Dot(line_AC.get_projection(O1_dot.get_center())).set_opacity(0)                            
        )
        self.add(O1_dot_proj)
        small_circle = always_redraw(lambda:
            Circle(radius=Line(O1_dot.get_center(), O1_dot_proj.get_center()).get_length(),
                   color=PURPLE).move_to(O1_dot)
        )
        self.play(Create(small_circle))
        self.play(B_dot.animate.shift(2*LEFT), rate_func=there_and_back, run_time=3)
        self.wait(2)
        bisector_A.add_updater(lambda x: x.set_opacity(0))
        bisector_B.add_updater(lambda x: x.set_opacity(0))
        self.play(A_dot.animate.shift(DOWN),
                  C_dot.animate.shift(2 * UL),
                  B_dot.animate.shift(2 * LEFT),
                  rate_func=there_and_back,
                  run_time=3)
        self.play(A_dot.animate.shift(2 * UR),
                  B_dot.animate.shift(2 * RIGHT + DOWN),
                  C_dot.animate.shift(3 * LEFT + 2 * DOWN),
                  rate_func=there_and_back,
                  run_time=3)
        self.wait()
        

class Heights(Scene):

    def construct(self):
        A_dot = Dot(3 * LEFT, z_index=2)
        B_dot = Dot(3 * UP, z_index=2)
        C_dot = Dot(2 * DR, z_index=2)
        triangle = always_redraw(lambda:
            Polygon(
                A_dot.get_center(),
                B_dot.get_center(),
                C_dot.get_center(),
                z_index=-1
            )                  
        )
        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center(), color=BLUE)
        )
        line_AC = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center(), color=BLUE)
        )
        line_BC = always_redraw(lambda:
            Line(B_dot.get_center(), C_dot.get_center(), color=BLUE)
        )
        self.play(Create(A_dot), Create(B_dot), Create(C_dot))
        self.play(Create(triangle))
        self.add(line_AB, line_AC, line_BC)
        A_proj = always_redraw(lambda:
            Dot(line_BC.get_projection(A_dot.get_center()), z_index=2)
        )
        B_proj = always_redraw(lambda:
            Dot(line_AC.get_projection(B_dot.get_center()), z_index=2)
        )
        C_proj = always_redraw(lambda:
            Dot(line_AB.get_projection(C_dot.get_center()), z_index=2)
        )

        line_AA1 = always_redraw(lambda:
            Line(A_dot.get_center(), A_proj.get_center(), color=TEAL)
        )
        line_BB1 = always_redraw(lambda:
            Line(B_dot.get_center(), B_proj.get_center(), color=TEAL)
        )
        line_CC1 = always_redraw(lambda:
            Line(C_dot.get_center(), C_proj.get_center(), color=TEAL)
        )

        # Костыльные продолжения отрезков
        line_BC1 = always_redraw(lambda:
            Line(B_dot.get_center(), C_proj.get_center(), color=BLUE)
        ) 
        line_CB1 = always_redraw(lambda:
            Line(C_dot.get_center(), B_proj.get_center(), color=BLUE)
        ) 

        self.play(Create(A_proj), Create(B_proj), Create(C_proj),
                  Create(line_AA1), Create(line_BB1), Create(line_CC1))

        right_angle_1 = always_redraw(lambda:
            RightAngle(line_CC1, line_BC1, quadrant=(-1,-1))
            .scale(0.5, about_point=C_proj.get_center())
        )
        right_angle_2 = always_redraw(lambda:
            RightAngle(line_AA1, line_BC, quadrant=(-1,-1))
            .scale(0.5, about_point=A_proj.get_center())
        )
        right_angle_3 = always_redraw(lambda:
            RightAngle(line_BB1, line_CB1, quadrant=(-1,-1))
            .scale(0.5, about_point=B_proj.get_center())
        )
        self.add(line_CB1, line_BC1)
        self.play(Create(right_angle_1), Create(right_angle_2),
                  Create(right_angle_3))
        
        
        O_dot = always_redraw(lambda:
            Dot(
                line_intersection(
                    [line_AA1.get_start(), line_AA1.get_end()],
                    [line_BB1.get_start(), line_BB1.get_end()]
                ),
                color=YELLOW, z_index=1
            )
        )

        self.play(Create(O_dot))

        # Очередные костыльные продолжения отрезков
        line_AO = always_redraw(lambda:
            Line(A_dot.get_center(), O_dot.get_center(), color=TEAL)
        )
        line_CO = always_redraw(lambda:
            Line(C_dot.get_center(), O_dot.get_center(), color=TEAL)
        ) 
        line_BO = always_redraw(lambda:
            Line(B_dot.get_center(), O_dot.get_center(), color=TEAL)
        ) 

        self.add(line_AO, line_CO, line_BO)

        self.play(B_dot.animate.shift(3 * LEFT), rate_func=there_and_back,
                  run_time=3)
        self.play(C_dot.animate.shift(DL),
                  B_dot.animate.shift(RIGHT),
                  A_dot.animate.shift(UP),
                  rate_func=there_and_back,
                  run_time=5)
        self.play(C_dot.animate.shift(1.3 * UR),
                  B_dot.animate.shift(2 * LEFT),
                  A_dot.animate.shift(DL),
                  rate_func=there_and_back,
                  run_time=5)
        self.wait()
        self.play(FadeOut(*self.mobjects))
        

class Medians(Scene):
    def construct(self):
        A_dot = Dot(3 * LEFT, z_index=2)
        B_dot = Dot(3 * UP, z_index=2)
        C_dot = Dot(2 * DR, z_index=2)
        triangle = always_redraw(lambda:
            Polygon(
                A_dot.get_center(),
                B_dot.get_center(),
                C_dot.get_center(),
                z_index=-1
            )                  
        )
        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center(), color=BLUE)
        )
        line_AC = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center(), color=BLUE)
        )
        line_BC = always_redraw(lambda:
            Line(B_dot.get_center(), C_dot.get_center(), color=BLUE)
        )
        self.play(Create(A_dot), Create(B_dot), Create(C_dot))
        self.play(Create(triangle))
        self.add(line_AB, line_AC, line_BC)

        A1_dot = always_redraw(lambda:
            Dot(line_BC.get_center())
        )
        B1_dot = always_redraw(lambda:
            Dot(line_AC.get_center())
        )
        C1_dot = always_redraw(lambda:
            Dot(line_AB.get_center())
        )
        self.play(Create(A1_dot), Create(B1_dot), Create(C1_dot))
        line_AA1 = always_redraw(lambda:
            Line(A_dot.get_center(), A1_dot.get_center(), z_index=-1,
                 color=TEAL)
        )
        line_BB1 = always_redraw(lambda:
            Line(B_dot.get_center(), B1_dot.get_center(), z_index=-1,
                 color=TEAL)
        )
        line_CC1 = always_redraw(lambda:
            Line(C_dot.get_center(), C1_dot.get_center(), z_index=-1,
                 color=TEAL)
        )

        # Засечки
        serif_AB1 = always_redraw(lambda:
            Line(A_dot.get_center(), B1_dot.get_center())
            .rotate(PI / 2).scale(0.1)
        )
        serif_B1C = always_redraw(lambda:
            Line(B1_dot.get_center(), C_dot.get_center())
            .rotate(PI / 2).scale(0.1)
        )
        serif_AC1 = always_redraw(lambda:
            Line(A_dot.get_center(), C1_dot.get_center(), color=GOLD)
            .rotate(PI / 2).scale(0.1)
        )
        serif_C1B = always_redraw(lambda:
            Line(C1_dot.get_center(), B_dot.get_center(), color=GOLD)
            .rotate(PI / 2).scale(0.1)
        )
        serif_BA1 = always_redraw(lambda:
            Line(B_dot.get_center(), A1_dot.get_center(), color=PINK)
            .rotate(PI / 2).scale(0.1)
        )
        serif_A1C = always_redraw(lambda:
            Line(A1_dot.get_center(), C_dot.get_center(), color=PINK)
            .rotate(PI / 2).scale(0.1)
        )

        self.play(Create(line_AA1), Create(line_BB1), Create(line_CC1))
        self.play(Create(serif_AB1), Create(serif_B1C),
                  Create(serif_AC1), Create(serif_C1B),
                  Create(serif_BA1), Create(serif_A1C))
        O_dot = always_redraw(lambda:
            Dot(line_intersection(
                [line_CC1.get_start(), line_CC1.get_end()],
                [line_AA1.get_start(), line_AA1.get_end()]
            ), color=YELLOW)
        )
        
        self.play(Create(O_dot))
        self.wait()
        self.play(B_dot.animate.shift(2 * RIGHT),
                  rate_func=there_and_back, run_time=3)
        self.play(A_dot.animate.shift(3 * DR),
                  C_dot.animate.shift(2 * UR),
                  B_dot.animate.shift(2 * LEFT),
                  rate_func=there_and_back, run_time=3)
        self.play(A_dot.animate.shift(3 * DL),
                  C_dot.animate.shift(1.8 * DOWN),
                  B_dot.animate.shift(0.8 * UR),
                  rate_func=there_and_back, run_time=3)
        self.wait()
        self.play(FadeOut(*self.mobjects))