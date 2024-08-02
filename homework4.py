from manim import *

class Homework4(Scene):
    def construct(self):
        zeta = MathTex(
            r"\zeta", "(2)", " = ", r"\frac{\pi^2}{6}",
            font_size=72
        )

        underline = Underline(
            zeta,
            buff=0.2,
            stroke_width=2,
            color=WHITE
        )
        
        self.play(Write(zeta, run_time=2))
        self.play(Create(underline, run_time=1.5))
        self.wait(0.3)
        self.play(Uncreate(underline))

        box = SurroundingRectangle(
            zeta,
            buff=0.2,
            corner_radius=0.15,
            color=YELLOW,
            stroke_width=2
        )
        self.play(Create(box, run_time=3))
        self.wait(0.3)
        self.play(Uncreate(box))

        brace = Brace(
            zeta[-1],
            buff=0.1,
            sharpness=0.7,
            color=LIGHT_GREY
        )
        note = Tex(
            "Трансцендетно", font_size=28
            ).next_to(brace, DOWN)
        self.play(Indicate(zeta[-1], run_time=1.5))
        self.play(FadeIn(brace, shift=UP))
        self.wait(0.5)
        self.play(Write(note, run_time=1.5))
        self.wait()
        self.play(FadeOut(zeta),
                  FadeOut(brace),
                  FadeOut(note))
        
        circ_1 = Circle(
            arc_center=LEFT,
            radius=1,
            fill_color=RED_A,
            fill_opacity=0.6,
            stroke_width=5,
            stroke_color=ORANGE
        )

        circ_2 = Circle(
            radius=1.3,
            fill_opacity=0,
            stroke_color=ORANGE,
            stroke_opacity=1,
            stroke_width=10
        ).next_to(circ_1)
        self.play(GrowFromCenter(circ_1))
        self.play(GrowFromCenter(circ_2))
        self.wait()
        self.play(FadeOut(circ_1),
                  FadeOut(circ_2))
        
        hexagon = RegularPolygon(
            radius=1.5,
            n=6,
            stroke_color=GREEN_A,
            stroke_opacity=0.7,
            fill_color=TEAL_E,
            fill_opacity=0.3
        )
        octagon = RegularPolygon(
            radius=1.5,
            n=8
        )

        deltoid = Polygon(
            1.5 * LEFT,
            1.5 * UP,
            1.5 * RIGHT,
            3 * DOWN
        )

        self.play(GrowFromCenter(hexagon))
        self.play(GrowFromCenter(octagon))
        self.play(FadeIn(deltoid, shift=UP))
        self.wait(0.5)
        self.play(FadeOut(deltoid, shift=UP))
        self.play(FadeOut(hexagon),
                  FadeOut(octagon))
        
        proxy_rect = Rectangle(
            height=3,
            width=6,
        )
        curved_box = SurroundingRectangle(
            proxy_rect,
            corner_radius=-0.3,
            stroke_color=WHITE,
            stroke_width=2
        )
        box_for_box = SurroundingRectangle(
            curved_box,
            stroke_width=2,
            stroke_color=GRAY
        )

        gray_yellow_square = Square(
            side_length=2,
            fill_color=GRAY,
            fill_opacity=1,
            stroke_color=YELLOW_B,
            stroke_opacity=0.7
        )

        stroky_square = Square(
            side_length=1,
            stroke_color=YELLOW,
            stroke_opacity=1
        )

        self.play(Create(curved_box, run_time=1.7),
                  Create(box_for_box, run_time=2))
        self.play(GrowFromCenter(gray_yellow_square))
        self.play(GrowFromCenter(stroky_square))
        self.wait()
        self.play(FadeOut(curved_box),
                  FadeOut(box_for_box),
                  FadeOut(gray_yellow_square),
                  FadeOut(stroky_square))
        
        line = Line(
            start = 4 * LEFT,
            end = 4 * RIGHT,
            stroke_color=WHITE
        )
        dashed_line = DashedLine(
            start = 4 * LEFT,
            end = 4 * RIGHT,
            stroke_color=WHITE,
            dashed_ratio=0.8,
            dash_length=0.3
        ).next_to(line, DOWN, buff=1)

        self.play(Create(line, run_time=1.5),
                  Create(dashed_line, run_time=1))
        self.wait()
        self.play(FadeOut(line),
                  FadeOut(dashed_line))
        
class Test(Scene):
    def construct(self):
        dot = Dot(
            point = DL,
            radius=0.1,
            color=YELLOW
        )
        self.play(GrowFromCenter(dot))
        self.wait()
        
