from manim import *

# Note to anyone using this repo, attempt to run this function before anything else to ensure manim is working properly on your local environment.. 


class SetupTest(Scene):
    def construct(self):
        # Green's equation 
        # Use MathTex (or Tex) in recent manim versions — TextMobject was removed/deprecated.
        greens_eq = MathTex(
            r"\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA",
            tex_to_color_map={"C": BLUE, "D": GREEN}
        )
        greens_eq.scale(1)
        self.play(Write(greens_eq))
        self.wait(2)
        self.play(FadeOut(greens_eq))