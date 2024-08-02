from manim import *

class Homework2(Scene):
    def construct(self):
        sum_of_odds = MathTex("1 + 3 + 5 + 7 + 9 = 5^2", color = WHITE)
        self.play(Write(sum_of_odds, run_time=2))
        self.wait()
        self.play(Unwrite(sum_of_odds))

        sum_to_32 = MathTex("1 + 5 + 10 + 10 + 5 + 1 = 2^5", color = WHITE)
        self.play(Write(sum_to_32, run_time=2))
        self.wait()
        self.play(Unwrite(sum_to_32))
        self.wait()

        math_lifehack = MathTex("(a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad - bc)^2")
        self.play(FadeIn(math_lifehack, shift = DOWN, run_time = 0.7))
        self.wait()
        self.play(FadeOut(math_lifehack, shift = DOWN, run_time = 0.7))

        inequation = MathTex("x_1 < x_2 < x_3 < ... < x_n", color = LIGHT_GREY)
        self.play(Write(inequation, run_time=2))
        self.wait()
        self.play(Unwrite(inequation, run_time=2))

        sum_and_prod = MathTex(r"1 + 2 + 3 = 1 \times 2 \times 3")
        self.play(GrowFromCenter(sum_and_prod, run_time=0.8))
        self.wait()
        self.play(FadeOut(sum_and_prod))

        sin_of_double_angle = MathTex(r"\sin 2\alpha = 2 \sin \alpha \cos \alpha")
        self.play(FadeIn(sin_of_double_angle, shift = DOWN, run_time = 0.7))
        self.wait()
        self.play(FadeOut(sin_of_double_angle, shift = DOWN, run_time = 0.7))

        log_identity = MathTex(r"a^{log_ab} = b")
        self.play(Write(log_identity))
        self.wait()
        self.play(Unwrite(log_identity))

        sum_of_inverse_squares = MathTex(
            r"\frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2}"
            r" + ... = \frac{\pi^2}{6}", color = YELLOW
            )
        self.play(GrowFromCenter(sum_of_inverse_squares, run_time=0.8))
        self.wait()
        self.play(FadeOut(sum_of_inverse_squares, run_time=0.8))

        distributivity_of_logical_and = MathTex(
            r"A \cap (B \cup C) = (A \cap B) \cup (A \cap C)"
        )
        self.play(FadeIn(distributivity_of_logical_and, shift = DOWN,
                         run_time=0.8))
        self.wait()
        self.play(FadeOut(distributivity_of_logical_and, shift = DOWN,
                         run_time=0.8))
        
        triangles = MathTex(
            r"\triangle ABC = \triangle A_1 B_1 C_1 \Rightarrow \angle A = \angle A_1")
        self.play(Write(triangles, run_time = 2))
        self.wait()
        self.play(Unwrite(triangles))

        Dirichlets_function = MathTex(
            r"D(x) = "
            r"\begin{cases}"
            r"1, \ x \in \mathbb{Q}; \\ 0, \  x \in \mathbb{R} \, \backslash \, \mathbb{Q}."
            r"\end{cases}"
        )
        self.play(GrowFromCenter(Dirichlets_function, run_time = 0.8))
        self.wait()
        self.play(FadeOut(Dirichlets_function, run_time = 0.8))

        gathered_conditions = MathTex(r"""
            \left[
                \begin{array}{lr}
                x > \pi,
                    \\
                    x = \arctg{\sqrt{5}}.
                \end{array}
            \right.
        """
        )
        self.play(FadeIn(gathered_conditions, run_time = 0.8, shift = DOWN))
        self.wait()
        self.play(FadeOut(gathered_conditions, run_time = 0.8, shift = DOWN))

        LaTex_with_russian = Tex(
            r"\LaTeX{} с кириллицей - это прекрасно!"
        )
        self.play(Write(LaTex_with_russian))
        self.wait()
        self.play(Unwrite(LaTex_with_russian))

        cos_between_vectors = Tex(r"\begin{justify}"
            r"Формула косинуса угла между прямыми. "
            r"Если $\vec{a}(x_1, y_1, z_1)$ и "
            r"$\vec{b}(x_2, y_2, z_2)$ --- "
            r"направляющие векторы прямых $a$ и $b$, то \newline"
            r"\end{justify}"
            r"$\cos(\widehat{a, b}) = \frac{| \vec{a} \, \cdot \, \vec{b} |}{| \vec{a} | \, \cdot \, | \vec{b} |}$"
            r"$= \frac{|x_1 \, \cdot \, x_2 \, + \, y_1 \, \cdot \, y_2 \, + \, z_1 \, \cdot \, z_2 |}{\sqrt{x_1^2 \, + \, y_1^2 \, + \, z_1^2} \, \cdot \, \sqrt{x_2^2 \, + \, y_2^2 \, + \, z_2^2}}$" 
            , font_size=38)
        self.play(GrowFromCenter(cos_between_vectors))
        self.wait()
        self.play(FadeOut(cos_between_vectors))

        number_sets = Tex(
            r"Number sets: "
            r"$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Z}$"
            r"$\subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$"
        )

        self.play(FadeIn(number_sets, shift=DOWN, run_time=0.8))
        self.wait()
        self.play(FadeOut(number_sets, shift=DOWN, run_time=0.8))

        limit_e = MathTex(
            r"\lim_{x\to\infty}{\left( 1 + \frac{1}{x} \right)}^x = e"
        )
        self.play(Write(limit_e))
        self.wait()
        self.play(Unwrite(limit_e))

        emptiness = MathTex(r"\varnothing", color = YELLOW_D, font_size=72)
        self.play(GrowFromCenter(emptiness))
        self.wait()
        self.play(FadeOut(emptiness))

        with_no_LaTeX = Text("Текст без LaTeX \nимеет свои преимущества")
        self.play(Write(with_no_LaTeX))
        self.wait()
        self.play(Unwrite(with_no_LaTeX))
        self.wait()
        
        