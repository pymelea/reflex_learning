import reflex as rx

import reflex_init.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        align_items='center',
    )

