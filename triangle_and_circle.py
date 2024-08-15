from manim import *

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
        A_dot = Dot(2 * LEFT)
        B_dot = Dot(2 * UP)
        C_dot = Dot(RIGHT)
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
        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center(), color=TEAL).rotate(PI / 2)
        )
        line_AC = always_redraw(lambda:
            Line(A_dot.get_center(), C_dot.get_center(), color=TEAL).rotate(PI / 2)
        )
        self.play(Create(line_AB), Create(line_AC))
        self.wait()
        O_dot = always_redraw(lambda:
            self.get_intersection([
                Dot(line_AB.get_start()).get_x(), Dot(line_AB.get_start()).get_y(),
                Dot(line_AB.get_end()).get_x(), Dot(line_AB.get_end()).get_y(),
                Dot(line_AC.get_start()).get_x(), Dot(line_AC.get_start()).get_y(),
                Dot(line_AC.get_end()).get_x(), Dot(line_AC.get_end()).get_y()
            ])
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
            Circle(radius=line_AO.get_length(), stroke_width=3).move_to(O_dot)
        )
        trace = TracedPath(A_dot_copy.get_center, stroke_color=RED, stroke_width=3)
        self.add(trace)
        self.play(Rotate(A_dot_copy, -TAU, about_point=O_dot.get_center()), run_time=3)
        self.add(circle)
        self.remove(trace)
        self.wait()
        self.play(A_dot.animate.shift(LEFT), rate_func=there_and_back, run_time=3)
        self.wait()