from manim import *
import numpy as np


def f(x: float) -> float:
    return x * np.log(x) - 1


def bisection_steps(a: float, b: float, tol: float = 0.02, max_iter: int = 30):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("O intervalo inicial deve conter mudança de sinal.")

    steps = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        steps.append((i, a, b, c, fc))
        if abs(fc) < tol:
            break
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return steps


def false_position_steps(a: float, b: float, tol: float = 0.02, max_iter: int = 30):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("O intervalo inicial deve conter mudança de sinal.")

    steps = []
    for i in range(1, max_iter + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        steps.append((i, a, b, c, fc))
        if abs(fc) < tol:
            break
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return steps


def build_header(scene_label: str, accent=WHITE):
    box = RoundedRectangle(
        width=13.0,
        height=1.75,
        corner_radius=0.20,
        stroke_width=2,
        stroke_color=GREY_B,
        fill_color=BLACK,
        fill_opacity=0.28,
    ).to_edge(UP, buff=0.15)

    left = VGroup(
        Text("Comparação entre Bisseção e Falsa Posição", font_size=25, weight=BOLD),
        Text("f(x) = x ln(x) - 1", font_size=20),
        Text("Critério de parada: |f(c)| < 0,02", font_size=18),
    ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

    left.scale(0.94)
    left.move_to(box.get_left() + RIGHT * 3.95).shift(LEFT * 0.10)

    badge = RoundedRectangle(
        width=2.80,
        height=0.52,
        corner_radius=0.14,
        stroke_width=2,
        stroke_color=accent,
        fill_color=accent,
        fill_opacity=0.15,
    )
    badge_text = Text(scene_label, font_size=19, weight=BOLD, color=accent)
    badge_group = VGroup(badge, badge_text)
    badge_text.move_to(badge.get_center())
    badge_group.move_to(box.get_right() + LEFT * 1.55)

    return VGroup(box, left, badge_group)


def build_axes_group():
    axes = Axes(
        x_range=[0.9, 2.15, 0.25],
        y_range=[-1.30, 0.95, 0.25],
        x_length=7.90,
        y_length=4.40,
        tips=False,
        axis_config={
            "include_numbers": True,
            "font_size": 20,
            "stroke_color": GREY_B,
        },
    )

    labels = axes.get_axis_labels(
        Text("x", font_size=20),
        Text("f(x)", font_size=20),
    )

    curve = axes.plot(
        lambda x: f(x),
        x_range=[0.9, 2.10],
        color=GREEN_C,
        stroke_width=4,
    )

    group = VGroup(axes, labels, curve)
    group.move_to(LEFT * 2.45 + DOWN * 0.55)
    return axes, curve, group


def build_panel(
    title: str,
    step_i: int,
    a: float,
    b: float,
    c: float,
    fc: float,
    note: str,
    accent=WHITE,
    extra_line: str | None = None,
):
    box = RoundedRectangle(
        width=4.90,
        height=3.25,
        corner_radius=0.18,
        stroke_width=2,
        stroke_color=accent,
        fill_color=BLACK,
        fill_opacity=0.30,
    )

    header = Text(title, font_size=22, weight=BOLD, color=accent)

    items = [
        Text(f"Iteração: {step_i}", font_size=18),
        Text(f"a = {a:.4f}", font_size=18),
        Text(f"b = {b:.4f}", font_size=18),
        Text(f"c = {c:.4f}", font_size=18),
        Text(f"|f(c)| = {abs(fc):.4f}", font_size=18),
    ]

    if extra_line is not None:
        items.append(Text(extra_line, font_size=16, color=GREY_A))

    items.append(Text(note, font_size=15))

    body = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
    content = VGroup(header, body).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
    content.scale(0.93)
    content.move_to(box.get_center()).shift(LEFT * 0.03)

    panel = VGroup(box, content)
    panel.move_to(RIGHT * 4.45 + DOWN * 0.05)
    return panel


def build_summary_box(title: str, root_value: float, residual: float, iterations: int, accent=WHITE):
    box = RoundedRectangle(
        width=12.25,
        height=1.20,
        corner_radius=0.18,
        stroke_width=2,
        stroke_color=accent,
        fill_color=BLACK,
        fill_opacity=0.26,
    )

    content = VGroup(
        Text(title, font_size=20, weight=BOLD, color=accent),
        Text(f"x ≈ {root_value:.6f}", font_size=20),
        Text(f"|f(c)| ≈ {residual:.6f}", font_size=18),
        Text(f"Iterações: {iterations}", font_size=18),
    ).arrange(RIGHT, buff=0.5)

    content.move_to(box.get_center())
    group = VGroup(box, content)
    group.move_to(DOWN * 3.10)
    return group


class BissecaoScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f111a"

        header = build_header("Bisseção", accent=BLUE_C)
        axes, curve, graph_group = build_axes_group()

        self.play(FadeIn(header, shift=UP * 0.10), run_time=0.7)
        self.play(Create(axes), Create(curve), FadeIn(graph_group[1]), run_time=1.0)

        steps = bisection_steps(1, 2, tol=0.02)

        a, b = 1.0, 2.0
        interval = Line(
            axes.c2p(a, 0),
            axes.c2p(b, 0),
            color=BLUE_C,
            stroke_width=8,
            stroke_opacity=0.85,
        )
        a_dot = Dot(axes.c2p(a, 0), color=BLUE_C, radius=0.075)
        b_dot = Dot(axes.c2p(b, 0), color=BLUE_C, radius=0.075)

        self.play(Create(interval), FadeIn(a_dot), FadeIn(b_dot), run_time=0.8)

        i0, a0, b0, c0, fc0 = steps[0]
        panel = build_panel(
            "Estado da iteração",
            i0, a0, b0, c0, fc0,
            "Corta o intervalo ao meio.",
            accent=BLUE_C,
        )
        self.play(FadeIn(panel, shift=RIGHT * 0.10), run_time=0.7)

        last_c = c0
        last_fc = fc0

        for i, a, b, c, fc in steps:
            mid_on_x = Dot(axes.c2p(c, 0), color=YELLOW, radius=0.07)
            mid_on_curve = Dot(axes.c2p(c, fc), color=YELLOW, radius=0.06)
            connector = DashedLine(
                axes.c2p(c, 0),
                axes.c2p(c, fc),
                color=YELLOW,
                dash_length=0.08,
                stroke_width=2,
            )
            label_c = Text(f"c{i}", font_size=15, color=YELLOW).next_to(mid_on_x, UP, buff=0.10)
            marker_group = VGroup(mid_on_x, mid_on_curve, connector, label_c)

            self.play(FadeIn(marker_group, scale=0.95), run_time=0.45)

            new_panel = build_panel(
                "Estado da iteração",
                i, a, b, c, fc,
                "Mantém a metade que ainda contém a raiz.",
                accent=BLUE_C,
            )
            self.play(ReplacementTransform(panel, new_panel), run_time=0.35)
            panel = new_panel

            last_c = c
            last_fc = fc

            if abs(fc) < 0.02:
                self.play(FadeOut(marker_group), run_time=0.2)
                break

            fa = f(a)
            if fa * fc < 0:
                new_a, new_b = a, c
            else:
                new_a, new_b = c, b

            new_interval = Line(
                axes.c2p(new_a, 0),
                axes.c2p(new_b, 0),
                color=BLUE_C,
                stroke_width=8,
                stroke_opacity=0.85,
            )
            new_a_dot = Dot(axes.c2p(new_a, 0), color=BLUE_C, radius=0.075)
            new_b_dot = Dot(axes.c2p(new_b, 0), color=BLUE_C, radius=0.075)

            self.play(
                ReplacementTransform(interval, new_interval),
                ReplacementTransform(a_dot, new_a_dot),
                ReplacementTransform(b_dot, new_b_dot),
                run_time=0.45,
            )
            interval, a_dot, b_dot = new_interval, new_a_dot, new_b_dot

            self.play(FadeOut(marker_group, shift=UP * 0.08), run_time=0.25)

        summary = build_summary_box(
            "Resultado final da bisseção",
            last_c,
            abs(last_fc),
            len(steps),
            accent=BLUE_C,
        )
        self.play(FadeIn(summary, shift=UP * 0.10), run_time=0.6)
        self.wait(1.5)


class FalsaPosicaoScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f111a"

        header = build_header("Falsa Posição", accent=ORANGE)
        axes, curve, graph_group = build_axes_group()

        self.play(FadeIn(header, shift=UP * 0.10), run_time=0.7)
        self.play(Create(axes), Create(curve), FadeIn(graph_group[1]), run_time=1.0)

        steps = false_position_steps(1, 2, tol=0.02)

        a, b = 1.0, 2.0
        fa, fb = f(a), f(b)

        interval = Line(
            axes.c2p(a, 0),
            axes.c2p(b, 0),
            color=ORANGE,
            stroke_width=7,
            stroke_opacity=0.50,
        )
        a_dot = Dot(axes.c2p(a, fa), color=ORANGE, radius=0.075)
        b_dot = Dot(axes.c2p(b, fb), color=ORANGE, radius=0.075)

        a_proj = DashedLine(
            axes.c2p(a, 0),
            axes.c2p(a, fa),
            color=ORANGE,
            stroke_opacity=0.45,
            stroke_width=2,
        )
        b_proj = DashedLine(
            axes.c2p(b, 0),
            axes.c2p(b, fb),
            color=ORANGE,
            stroke_opacity=0.45,
            stroke_width=2,
        )

        self.play(Create(interval), FadeIn(a_dot), FadeIn(b_dot), run_time=0.8)
        self.play(Create(a_proj), Create(b_proj), run_time=0.5)

        i0, a0, b0, c0, fc0 = steps[0]
        panel = build_panel(
            "Estado da iteração",
            i0, a0, b0, c0, fc0,
            "Usa a secante entre os extremos.",
            accent=ORANGE,
            extra_line="m = (f(b) - f(a)) / (b - a)",
        )
        self.play(FadeIn(panel, shift=RIGHT * 0.10), run_time=0.7)

        last_c = c0
        last_fc = fc0

        for i, a, b, c, fc in steps:
            fa, fb = f(a), f(b)

            secant = Line(
                axes.c2p(a, fa),
                axes.c2p(b, fb),
                color=ORANGE.interpolate(YELLOW, 0.20),
                stroke_width=5,
            )

            self.play(Create(secant), run_time=0.5)
            self.wait(0.15)

            estimate_on_x = Dot(axes.c2p(c, 0), color=YELLOW, radius=0.07)
            estimate_on_curve = Dot(axes.c2p(c, fc), color=YELLOW, radius=0.06)
            connector = DashedLine(
                axes.c2p(c, 0),
                axes.c2p(c, fc),
                color=YELLOW,
                dash_length=0.08,
                stroke_width=2,
            )
            label_c = Text(f"c{i}", font_size=15, color=YELLOW).next_to(estimate_on_x, UP, buff=0.10)
            marker_group = VGroup(estimate_on_x, estimate_on_curve, connector, label_c)

            self.play(FadeIn(marker_group, scale=0.95), run_time=0.35)

            new_panel = build_panel(
                "Estado da iteração",
                i, a, b, c, fc,
                "A secante puxa a aproximação com mais rapidez.",
                accent=ORANGE,
                extra_line="Não calcula derivada explícita.",
            )
            self.play(ReplacementTransform(panel, new_panel), run_time=0.35)
            panel = new_panel

            last_c = c
            last_fc = fc

            if abs(fc) < 0.02:
                self.play(FadeOut(marker_group), run_time=0.2)
                break

            if fa * fc < 0:
                new_a, new_b = a, c
            else:
                new_a, new_b = c, b

            new_fa, new_fb = f(new_a), f(new_b)

            new_interval = Line(
                axes.c2p(new_a, 0),
                axes.c2p(new_b, 0),
                color=ORANGE,
                stroke_width=7,
                stroke_opacity=0.50,
            )
            new_a_dot = Dot(axes.c2p(new_a, new_fa), color=ORANGE, radius=0.075)
            new_b_dot = Dot(axes.c2p(new_b, new_fb), color=ORANGE, radius=0.075)

            new_a_proj = DashedLine(
                axes.c2p(new_a, 0),
                axes.c2p(new_a, new_fa),
                color=ORANGE,
                stroke_opacity=0.45,
                stroke_width=2,
            )
            new_b_proj = DashedLine(
                axes.c2p(new_b, 0),
                axes.c2p(new_b, new_fb),
                color=ORANGE,
                stroke_opacity=0.45,
                stroke_width=2,
            )

            self.play(
                ReplacementTransform(interval, new_interval),
                ReplacementTransform(a_dot, new_a_dot),
                ReplacementTransform(b_dot, new_b_dot),
                ReplacementTransform(a_proj, new_a_proj),
                ReplacementTransform(b_proj, new_b_proj),
                run_time=0.45,
            )
            interval, a_dot, b_dot = new_interval, new_a_dot, new_b_dot
            a_proj, b_proj = new_a_proj, new_b_proj

            self.play(FadeOut(marker_group, shift=UP * 0.08), run_time=0.25)
            self.play(FadeOut(secant), run_time=0.15)

        summary = build_summary_box(
            "Resultado final da falsa posição",
            last_c,
            abs(last_fc),
            len(steps),
            accent=ORANGE,
        )
        self.play(FadeIn(summary, shift=UP * 0.10), run_time=0.6)
        self.wait(1.5)
