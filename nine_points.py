from manim import *

class NinePoints(Scene):
    def construct(self):
        A_dot = Dot(3 * LEFT)
        B_dot = Dot(3 * UP)
        C_dot = Dot(1.5 * RIGHT)

        triangle = always_redraw(lambda:
            Polygon(
                A_dot.get_center(),
                B_dot.get_center(),
                C_dot.get_center(), z_index=-1
            )
        )

        self.play(Create(A_dot), Create(B_dot), Create(C_dot))
        self.play(Create(triangle))

        A1_dot = always_redraw(lambda:
            Dot(Line(B_dot.get_center(), C_dot.get_center())
                .get_center())
        )
        B1_dot = always_redraw(lambda:
            Dot(Line(A_dot.get_center(), C_dot.get_center())
                .get_center())
        )
        C1_dot = always_redraw(lambda:
            Dot(Line(A_dot.get_center(), B_dot.get_center())
                .get_center())
        ) 
        self.play(Create(A1_dot), Create(B1_dot), Create(C1_dot))
        self.wait()

        A2_dot = always_redraw(lambda:
            Dot(Line(B_dot.get_center(), C_dot.get_center())
                .get_projection(A_dot.get_center()))
        )

        B2_dot = always_redraw(lambda:
            Dot(Line(A_dot.get_center(), C_dot.get_center())
                .get_projection(B_dot.get_center()))
        )

        C2_dot = always_redraw(lambda:
            Dot(Line(A_dot.get_center(), B_dot.get_center())
                .get_projection(C_dot.get_center()))
        )

        line_AA2 = always_redraw(lambda:
            Line(A_dot.get_center(), A2_dot.get_center(), color=TEAL, z_index=-1)
        )
        line_BB2 = always_redraw(lambda:
            Line(B_dot.get_center(), B2_dot.get_center(), color=TEAL, z_index=-1)
        )
        line_CC2 = always_redraw(lambda:
            Line(C_dot.get_center(), C2_dot.get_center(), color=TEAL, z_index=-1)
        )

        self.play(Create(A2_dot), Create(B2_dot), Create(C2_dot))
        self.play(Create(line_AA2), Create(line_BB2), Create(line_CC2))
        H_dot = always_redraw(lambda:
            Dot(line_intersection(
                [line_AA2.get_start(), line_AA2.get_end()],
                [line_BB2.get_start(), line_BB2.get_end()]
            ))
        )
        self.play(Create(H_dot))
        self.wait()

        A3_dot = always_redraw(lambda:
            Dot(Line(A_dot.get_center(), H_dot.get_center()).get_center())
        )
        B3_dot = always_redraw(lambda:
            Dot(Line(B_dot.get_center(), H_dot.get_center()).get_center())
        )
        C3_dot = always_redraw(lambda:
            Dot(Line(C_dot.get_center(), H_dot.get_center()).get_center())
        )

        self.play(Create(A3_dot), Create(B3_dot), Create(C3_dot))
        self.wait()

        line_AB = always_redraw(lambda:
            Line(A_dot.get_center(), B_dot.get_center()).set_opacity(0).
            rotate(PI / 2)
        )
        line_BC = always_redraw(lambda:
            Line(B_dot.get_center(), C_dot.get_center()).set_opacity(0).
            rotate(PI / 2)
        )
        self.add(line_AB, line_BC)
        O_dot = always_redraw(lambda:
            Dot(line_intersection(
                [line_AB.get_start(), line_AB.get_end()],
                [line_BC.get_start(), line_BC.get_end()]
            ), color=GREY)
        )
        self.play(Create(O_dot))
        self.wait()
        euler_center = always_redraw(lambda:
            Dot(Line(O_dot.get_center(), H_dot.get_center()).get_center(),
                color=YELLOW)
        )
        self.play(Create(euler_center))
        self.play(Flash(euler_center))
        euler_circle = always_redraw(lambda:
            Circle(radius=Line(
                euler_center.get_center(), A1_dot.get_center()
                ).get_length(), z_index=-1, color=YELLOW).move_to(euler_center)
        )
        self.play(Create(euler_circle))
        # for item in line_AA2, line_BB2, line_CC2:
        #     item.add_updater(lambda x: x.set_opacity(0))
            
        self.play(B_dot.animate.shift(2 * LEFT),
                  C_dot.animate.shift(DOWN),
                   rate_func=there_and_back,
                  run_time=6, lag_ratio=0.7)
        self.wait()