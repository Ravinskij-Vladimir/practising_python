from manim import *

class HomeWork3(Scene):
    def construct(self):
        square_1 = Square().shift(LEFT)
        self.play(FadeIn(square_1, shift=RIGHT, run_time=0.8))
        square_2 = square_1.copy().next_to(square_1)
        self.play(FadeIn(square_2, shift=LEFT, run_time=0.8))

        rect = Rectangle(width=4.75, height=2.5)
        rect.shift(0.125*RIGHT)
        self.play(Create(rect))
        self.wait()

        delta = Tex(r"$\delta$", font_size = 96)
        delta.move_to(square_1)
        self.play(Write(delta))

        self.play(FadeOut(square_1), FadeOut(square_2), 
                  FadeOut(rect), FadeOut(delta))
        
        pythagoras = Tex(
            r"\S 1. Pythagoras"
        ).shift(3*UP)
        self.play(FadeIn(pythagoras, shift=LEFT))

        euclid = Tex(
            r"\S 2. Euclid"
        ).next_to(pythagoras, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(euclid, shift=LEFT))

        ptolemy = Tex(
            r"\S 3. Ptolemy"
        ).next_to(euclid, DOWN).align_to(euclid, LEFT)
        self.play(FadeIn(ptolemy, shift=LEFT))
        self.wait()

        self.play(FadeOut(pythagoras), FadeOut(euclid), FadeOut(ptolemy))

        right_triangle = Polygon(UL, DL, DOWN + 2 * RIGHT)
        self.play(Create(right_triangle))
        three = Text("3", font_size=32).next_to(right_triangle, LEFT)
        four = Text("4", font_size=32).next_to(right_triangle, DOWN)
        five = Text("5", font_size=32).next_to(right_triangle, UP).shift(DOWN)

        self.play(FadeIn(three, shift=LEFT, run_time=0.7),
                  FadeIn(four, shift=DOWN, run_time=0.7),
                  FadeIn(five, shift=UR, run_time=0.7))
        self.wait()
        self.play(FadeOut(right_triangle),
                  FadeOut(three),
                  FadeOut(four),
                  FadeOut(five))
        
        square = Square()
        A = Text('A', font_size=32).next_to(square, DL, buff=0.1)
        B = Text('B', font_size=32).next_to(square, UL, buff=0.1)
        C = Text('C', font_size=32).next_to(square, UR, buff=0.1)
        D = Text('D', font_size=32).next_to(square, DR, buff=0.1)
        self.play(GrowFromCenter(square))
        self.play(FadeIn(A, run_time=0.7, shift=DL),
                  FadeIn(B, run_time=0.7, shift=UL),
                  FadeIn(C, run_time=0.7, shift=UR),
                  FadeIn(D, run_time=0.7, shift=DR))
        self.wait()
        self.play(FadeOut(A, shift=UR),
                  FadeOut(B, shift=DR),
                  FadeOut(C, shift=DL),
                  FadeOut(D, shift=UL))
        self.play(ShrinkToCenter(square))
        self.wait()

        condition = Tex(
            r"\#1. Условие"
        ).to_edge(UL, buff=0.2)

        note = Tex(
            "Заметка"
        ).to_edge(RIGHT, buff=0.2)

        answer = Tex(
            "Ответ"
        ).to_edge(DL, buff=0.2)

        formula = Tex(
            "Формула"
        ).to_edge(DR, buff=0.2)

        solution = Tex(
            "Решение"
        )

        self.play(FadeIn(condition, run_time=0.5))
        self.play(FadeIn(note, run_time=0.5))
        self.play(FadeIn(formula, run_time=0.5))
        self.play(FadeIn(answer, run_time=0.5))
        self.play(Write(solution))

        self.play(FadeOut(condition),
                  FadeOut(note),
                  FadeOut(answer),
                  FadeOut(formula),
                  FadeOut(solution))
        
        circ_1 = Circle().shift(RIGHT)
        circ_2 = Circle().to_edge(UP, buff=0.5).shift(RIGHT)
        self.play(GrowFromCenter(circ_1))
        self.play(Create(circ_2))
        self.wait()
        self.play(FadeOut(circ_1), FadeOut(circ_2))

class Test(Scene):
    def construct(self):
        pass
        