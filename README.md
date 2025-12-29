# multi-animation
Animation for our final project in Benson's Multi class.
This project is made with manim a tool designed for mathimatical animations. 
Creators:
Calder Russell and Isaiah Sippel

# Green’s Theorem — Manim Animation Storyboard (README)

**Shot-by-shot plan** for a Manim animation that visually motivates and “proof-sketches” Green’s Theorem, then **uses the theorem to compute a real example**. It’s written so it can be translated  into Manim objects, animations, and transitions.

---

## 0) Goal + Big Idea (what the viewer should walk away with)

**Goal:** Show that a circulation-type **line integral around a closed curve** equals a **double integral of curl (scalar curl) over the region inside**.

**Green’s Theorem (planar form):**
\[
\oint_C \langle P(x,y),Q(x,y)\rangle \cdot d\vec r
=
\iint_R \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dA
\]
- \(C\): positively oriented (counterclockwise), simple closed curve bounding region \(R\).
- Left side: **circulation along the boundary**
- Right side: **sum of tiny local rotation (curl) over the interior**

---

## 1) Scene 1 — Establish the world: vector field + curve \(C\)

### Visual elements to create
- A 2D coordinate plane (Axes).
- A vector field \( \vec F(x,y)=\langle P(x,y),Q(x,y)\rangle \) drawn as arrows (VectorField / Arrow grid).
- A closed curve \(C\) drawn on top of the field (ParametricFunction).
- An orientation arrow on \(C\) (a small moving dot + tangent arrow, or an arrowhead on the curve) to show counterclockwise direction.

### Animation beats
1. **Fade in axes**.
2. **Draw vector field** gradually (grow arrows or fade them in).
3. **Draw curve \(C\)** with a “Write/Creation” animation.
4. Add label:  
   - “Vector field \(\vec F=\langle P,Q\rangle\)” near a corner  
   - “Closed curve \(C\)” near the curve  
5. Show a dot moving once around \(C\) (just a quick loop) to establish direction.

### Coding notes
- Keep field not too dense (performance + readability).
- Choose a field that has visible circulation (swirl-ish), but not chaotic.

---

## 2) Scene 2 — Zoom out: what is the line integral measuring?

**You said:** “zoom out and explain what a line integral is finding and what curl is so the viewer could understand.”

### Visual + text elements
- Camera zooms out (or scale down everything and reposition).
- A title card / overlay:  
  **“Line integral around \(C\): circulation along the boundary”**
- At a point on the curve, show:
  - Tangent vector \(\hat{T}\) (arrow along the curve)
  - Field vector \(\vec F\) (arrow from that point)
  - Highlight the dot product idea: \(\vec F\cdot d\vec r\)

### Animation beats
1. **Camera zoom out** to give space for explanatory overlays.
2. Freeze a point on \(C\). Draw:
   - \(\vec F\) at that point (a highlighted arrow)
   - \(d\vec r\) or \(\hat{T}\) along the curve (another highlighted arrow)
3. Fade in text:
   \[
   \oint_C \vec F\cdot d\vec r
   \quad\text{adds up the “along-the-path” component of }\vec F
   \]
4. Animate “projection”:
   - Show the component of \(\vec F\) along \(\hat{T}\) (like a dashed line projection).
   - Then show a tiny arc-length piece \(ds\).
5. Add a short intuitive sentence:
   - “If the field pushes with the direction of travel, contribution is positive. If it pushes against, negative.”

---

## 3) Scene 3 — Introduce curl (scalar curl in 2D) as local rotation

### Visual elements
- Pick a point inside \(R\).
- Draw a tiny circle (or tiny square) centered at that point.
- Show the field vectors around that tiny loop.
- Animate a small “paddle wheel” icon (simple spokes) to show rotation direction.

### Text overlays
- “Scalar curl (2D):”
  \[
  \operatorname{curl}\vec F
  =
  \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}
  \]
- Caption:
  - “Measures *tendency to rotate* per unit area.”

### Animation beats
1. Zoom slightly to the interior point.
2. Draw a small loop (circle).
3. Show arrows of \(\vec F\) sampled around the loop.
4. Animate a paddle wheel rotating:
   - If curl > 0: CCW spin
   - If curl < 0: CW spin
5. Emphasize “local”:
   - circle shrinks (scale down) while text says “per unit area”.

---

## 4) Scene 4 — Zoom back in: partition the region into small pieces

**You said:** “zoom back in… take small chunks … solve separately … add them… infinite partitions… arrive at the double integral.”

### Core idea to show
Break the region \(R\) into many little cells. Each cell has its own tiny boundary. When you add line integrals around all little boundaries:
- **Interior edges cancel** (traversed twice in opposite directions)
- Only the **outer boundary \(C\)** remains

### Visual elements
- Return view to the full curve and interior.
- Overlay a grid clipped to the region (or generate a mesh of little rectangles inside).
- For a *single* cell:
  - highlight its boundary in bright color
  - show mini line integral around it

### Animation beats (important sequence)
1. **Zoom back in** so the curve and interior fill the frame again.
2. Introduce a partition:
   - Draw a coarse grid inside \(R\) (start with, say, 4–9 cells).
3. Highlight one cell:
   - Trace its boundary with a moving dot.
   - Show:
     \[
     \oint_{\partial(\text{cell})} \vec F\cdot d\vec r
     \]
4. Duplicate to multiple cells:
   - Show several cell-boundaries being traced quickly.
5. **Cancellation moment (key visual):**
   - Pick a shared interior edge between two adjacent cells.
   - Animate arrows along that edge in opposite directions.
   - Then fade them out with a label: “cancels”.
6. After canceling many interior edges, fade out all interior boundaries and leave only \(C\) highlighted.
7. On screen:
   \[
   \sum_{\text{cells}} \oint_{\partial(\text{cell})}\vec F\cdot d\vec r
   =
   \oint_C \vec F\cdot d\vec r
   \]

---

## 5) Scene 5 — From tiny boundary integrals to curl × area (the “well-defined visual proof”)

Now you convert each tiny cell’s boundary integral into (curl at the cell) × (area of the cell).

### Visual strategy (clean and Manim-friendly)
- Focus on a single small rectangle with corners \((x,y)\) and \((x+\Delta x, y+\Delta y)\).
- Show that contributions along opposite sides almost cancel except for a difference tied to partial derivatives.
- Conclude:
  \[
  \oint_{\partial(\text{cell})}\vec F\cdot d\vec r
  \approx
  \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\Delta x\,\Delta y
  \]

### Animation beats
1. Zoom into one rectangle cell.
2. Label its sides:
   - bottom/top with \(\Delta x\)
   - left/right with \(\Delta y\)
3. Animate traversal of the rectangle (a dot moving CCW).
4. Show side-by-side “side contributions”:
   - Bottom edge contributes about \(P(x,y)\Delta x\)
   - Top edge contributes about \(-P(x,y+\Delta y)\Delta x\)
   - Right edge contributes about \(Q(x+\Delta x,y)\Delta y\)
   - Left edge contributes about \(-Q(x,y)\Delta y\)
5. Bring in a “difference quotient” visual:
   - \(Q(x+\Delta x,y)-Q(x,y)\approx \frac{\partial Q}{\partial x}\Delta x\)
   - \(P(x,y+\Delta y)-P(x,y)\approx \frac{\partial P}{\partial y}\Delta y\)
6. Combine terms on screen into:
   \[
   \oint_{\partial(\text{cell})}\vec F\cdot d\vec r
   \approx
   \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\Delta x\Delta y
   \]
7. Zoom back out to many cells:
   - Replace each cell boundary integral with “curl(cell) × area(cell)”
8. Transition from sum to integral:
   - \(\sum (\text{curl}\cdot \Delta A)\) morphs into \(\iint_R \text{curl}\,dA\)

### End of proof scene
Final theorem appears centered:
\[
\oint_C \vec F\cdot d\vec r
=
\iint_R \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dA
\]
with a short caption:
- “Boundary circulation = total interior rotation.”

---

## 6) Scene 6 — Worked example (animate the computation)

**You said:** “solve one problem using the theorem… mostly animating equations.”

### Recommended example format
Choose:
- A simple region \(R\) (disk, rectangle, triangle)
- A nice field \(\vec F=\langle P,Q\rangle\) where curl is simple
- The line integral would be annoying directly, so Green’s feels powerful

### Example template (you’ll fill in the actual field/region you want)
1. Show the problem statement:
   \[
   \text{Compute }\oint_C \vec F\cdot d\vec r
   \quad\text{where }C=\partial R
   \]
2. Write Green’s theorem line:
   \[
   \oint_C \vec F\cdot d\vec r
   =
   \iint_R \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dA
   \]
3. Compute curl:
   - Animate \(\partial Q/\partial x\) being computed
   - Animate \(\partial P/\partial y\) being computed
4. Set up the double integral over \(R\):
   - If region is disk: switch to polar (\(dA=r\,dr\,d\theta\))
   - If rectangle: basic bounds
5. Evaluate the integral:
   - Do algebra step-by-step with TransformMatchingTex
6. Conclude:
   \[
   \oint_C \vec F\cdot d\vec r = \text{(final number)}
   \]
7. (Optional satisfying callback) Briefly animate:
   - a dot traveling around \(C\)
   - the final value appearing next to it as “net circulation”.

---

## 7) Manim implementation checklist (so the plan becomes code)

### Objects you will likely use
- `Axes`, `NumberPlane`
- `VectorField` or custom grid of `Arrow`s
- `ParametricFunction` for curve \(C\)
- `ValueTracker` + updater for moving dot on curve
- `MathTex` / `Tex` for equations
- `SurroundingRectangle`, `VGroup`, `always_redraw`
- Camera controls: `self.camera.frame.animate.scale(...).move_to(...)`

### Animation patterns you’ll reuse
- `Create()`, `Write()`, `FadeIn()`, `FadeOut()`
- `TransformMatchingTex()` for equation morphs
- `ReplacementTransform()` for swapping scenes
- Highlighting: increase stroke width / change opacity / use `Indicate()`

### Visual clarity rules
- Keep the field faint when text is primary.
- Use one “highlight color” for the boundary \(C\) consistently.
- When showing cancellations, make opposite directions extremely obvious.

---

## 8) Scene order (final timeline)

1. **Setup:** axes → vector field → curve \(C\) + orientation
2. **Meaning of line integral:** tangent + projection intuition
3. **Meaning of curl:** local paddle-wheel rotation
4. **Partition region:** small cells, add boundaries
5. **Cancellation:** interior edges cancel → only \(C\) remains
6. **Cell proof:** boundary integral of tiny cell ≈ curl × area
7. **Limit:** sum becomes double integral
8. **Example:** compute with Green’s theorem (equations animated)
9. **Closing shot:** theorem + final numerical result + curve highlighted