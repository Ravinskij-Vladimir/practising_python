from manim import *

class Homework5(Scene):
    def construct(self):
        small_white_circle = Circle(
            radius=1,
            fill_opacity=0
        ).set_stroke(color=WHITE, width=2, opacity=1)

        big_gray_circle = Circle(
            radius=2,
            stroke_width=2,
            stroke_color=GRAY,
            fill_opacity=0
        )

        self.play(DrawBorderThenFill(small_white_circle, run_time=1.5),
                  DrawBorderThenFill(big_gray_circle, run_time=1.5))
        
        self.wait()
        self.play(FadeOut(small_white_circle, big_gray_circle))
        
        big_pi = Tex("$\\pi$",
                     font_size=225)
        sector = Sector(
            start_angle=0, 
            angle= PI / 4,
            fill_color=ORANGE,
            fill_opacity=0.6,
            stroke_opacity=0,
            z_index=1).shift(0.5*DL)
        rotated_triangle = Triangle(
            radius=1,
            fill_color=PURPLE,
            fill_opacity=1,
            stroke_opacity=0,
            z_index=-1
        ).rotate(PI / 6).shift(0.5*DL)
        self.play(FadeIn(big_pi))
        self.play(FadeIn(sector))
        self.play(FadeIn(rotated_triangle))
        self.wait()
        self.play(FadeOut(rotated_triangle, sector, big_pi))
        

        dot1 = Dot(
            2 * DOWN + 2 * LEFT,
            color=BLUE,
            radius=0.12,
        )
        dot2 = Dot(
            2 * UP + 2 * RIGHT,
            color=BLUE,
            radius=0.12
        )

        bezier = CubicBezier(
            2 * DOWN + 2*LEFT,
            4 * UP + LEFT,
            4 * DOWN + RIGHT,
            2 * UP + 2*RIGHT,
            color=BLUE,
            z_index=-1
        )
        self.play(GrowFromCenter(dot1),
                  GrowFromCenter(dot2))
        self.play(Create(bezier))
        self.wait()
        self.play(FadeOut(bezier, dot2, dot1))

        blue_text = Text(
            "#271eee",
            color="#271eee",
            font_size=100
        )
        red_text = Text(
            "#ff3300",
            color="#ff3300",
            font_size=60
        ).next_to(blue_text, UP, buff=0.2)
        self.play(FadeIn(blue_text))
        self.play(Write(red_text, run_time=2))
        self.wait()
        self.play(FadeOut(blue_text, red_text))


        trig_circle = Circle(
           radius=2
        ).set_stroke(GREY, 1, 1)
        point = Dot(
           2 * RIGHT * np.cos(PI / 5) + 2 * UP * np.sin(PI / 5),
           color=YELLOW
        )
        point_value = MathTex(
           "\\frac{\\pi}{5}"
        ).next_to(point, UR, buff=0.1)
        self.play(Create(trig_circle))
        self.play(Create(point))
        self.play(Write(point_value, run_time=1.5))

        equation = MathTex(
            r"2\cos \frac{\pi}{5}"
            r" = \frac{1}{2}(1 + \sqrt{5})"
            r" = 1.61803..."
        ).rotate(PI/2).to_edge(RIGHT, buff=0.3)
        self.play(Write(equation, run_time=2))
        self.wait()
        self.play(FadeOut(equation, point, point_value, trig_circle))

        line_1 = Line(LEFT, 3 * DR, stroke_width=2)
        line_2 = Line(LEFT, 3 * UR, stroke_width=2)
        center = Dot(ORIGIN, color=YELLOW, stroke_width=1)
        circ = Circle(
            radius = 0.6,
            color=YELLOW
        )
        bigger_circ = circ.copy()
        bigger_circ.scale(scale_factor=4, about_point=LEFT)
        self.play(Create(center))
        self.play(Create(line_1),
                    Create(line_2))
        self.play(Create(circ))
        self.play(TransformFromCopy(circ, bigger_circ, run_time=2))
        self.wait(2)
        self.play(FadeOut(bigger_circ, circ, line_1, line_2, center))

class Test(Scene):
    def construct(self):
       circ = Circle()
       self.play(FadeIn(circ, scale = 0.1))
       self.play(FadeOut(circ, scale = 0.1))