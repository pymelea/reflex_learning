import reflex as rx

from reflex_init.styles import styles


def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='check',
                    width=styles.Size.DEFAULT.value,
                    height=styles.Size.BIG.value,
                ),
                rx.tooltip(
                    rx.text(text, font_size=styles.Size.DEFAULT.value),
                    label=text,
                ),
            ),
            variant='outline',
            width='100%',
        ),
        href=url,
        is_external=True,
        width='100%',
    )
