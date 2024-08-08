from manim import *

class Homework6(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        self.play(FadeIn(red_dot, shift=UR))
        self.play(Indicate(red_dot, scale_factor=3, run_time=3))
        self.play(FadeOut(red_dot, shift=UR))
        self.wait()

        rect = Rectangle() 
        self.play(Create(rect))
        wide_stroke_rect = Rectangle(
            fill_color=BLUE_D,
                fill_opacity=1,
        ).set_stroke(GRAY, 5, 1)
        wide_stroke_rect.save_state()
        self.play(Transform(rect, wide_stroke_rect))
        self.play(ApplyMethod(wide_stroke_rect.set_fill, ORANGE))
        right_bird_wing = Line(UR, ORIGIN).shift(UP)
        left_bird_wing = Line(ORIGIN, UL).shift(UP)
        self.play(Create(right_bird_wing))
        self.play(Create(left_bird_wing))
        self.wait()
        wide_rect_copy = wide_stroke_rect.copy().set_fill(BLUE_D, 1).set_stroke(BLUE, 5, 1)
        self.play(Transform(wide_stroke_rect, wide_rect_copy))
        self.wait()
        self.play(FadeOut(rect, wide_rect_copy, wide_stroke_rect, right_bird_wing, left_bird_wing, scale=0.2))


        integral = MathTex("\\oint", font_size=225)
        self.play(SpinInFromNothing(integral))
        self.play(Rotate(integral, -PI))
        self.play(integral.animate.rotate(PI / 2))
        self.play(integral.animate.rotate(PI / 2))
        self.wait()
        self.play(FadeOut(integral))

        inequation = MathTex(
            r"3 \frac{10}{71}<"
            r"\pi<"
            r"3 \frac{1}{7}"
        )
        box = SurroundingRectangle(
            inequation,
            color=WHITE,
            buff=0.3,
            stroke_width=1
        )
        self.play(Write(inequation, run_time=2))
        self.play(ShowPassingFlash(box))
        self.play(Create(box))
        self.play(Uncreate(box))
        self.wait()
        self.play(Unwrite(inequation))

        spline = CubicBezier(
            2*DOWN,
            4*LEFT + DOWN,
            4*RIGHT + UP,
            2*UP,
            color=RED 
        )
        star = Star(
            inner_radius=0,
            outer_radius=0.15,
            n=12,
            color=YELLOW
        )
        self.play(Create(spline))
        self.play(FadeIn(star, shift=UP))
        self.play(star.animate.move_to(4*LEFT + 2 * DOWN))
        self.play(star.animate.shift(4*RIGHT))
        self.play(MoveAlongPath(star, spline))
        self.wait()
        self.play(FadeOut(spline, star))

        scale = Text("SCALE", font_size=48, font="Arial")
        self.play(AddTextLetterByLetter(scale, run_time=1.5))
        self.play(Indicate(scale, scale_factor=3, color=WHITE, run_time=4))
        self.wait()
        scale_2 = scale.copy().scale(1.5).shift(RIGHT)
        self.play(ReplacementTransform(scale, scale_2))
        self.wait()
        self.play(Wiggle(scale_2))
        self.wait()
        self.play(FadeOut(scale_2, shift=DR))

        circle1 = Circle(radius=1)
        circle2 = Circle(radius=1.5)
        circle3 = Circle(radius=2)
        formula = MathTex(
            r"\frac{\partial f}{\partial x}+"
            r"i \frac{\partial f}{\partial y}=0"
        )
        self.play(AnimationGroup(
            GrowFromCenter(circle1),
            GrowFromCenter(circle2),
            GrowFromCenter(circle3),
            Write(formula), 
            lag_ratio=1))
        self.wait()

class Test(Scene):
    def construct(self):
        pass