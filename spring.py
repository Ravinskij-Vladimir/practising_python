from manim import *
class UseParametricFunction(Scene):
    def construct(self):
        vt = ValueTracker(0.5)
        graph = ParametricFunction(lambda u : np.array([0.05*u, 0.5*np.cos(u), 0.5*np.sin(u)]),
                                t_range=np.array([-4*TAU, 4*TAU, 0.1])).align_to(np.array([-4,0,0]), np.array([-1,0,0]))
        def changeLength(mob):
            i = vt.get_value()
            mob.become(ParametricFunction(lambda u : np.array([0.09*i*u, 0.5*np.cos(u), 0.5*np.sin(u)]),
                                t_range=np.array([-4*TAU, 4*TAU, 0.1])).align_to(np.array([-4,0,0]), np.array([-1,0,0])))

        graph.add_updater(changeLength)

        self.add(graph)
        for _ in range(4):
            self.play(vt.animate.set_value(2))
            self.play(vt.animate.set_value(0.5))
        return super().construct()