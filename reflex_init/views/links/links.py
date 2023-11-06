import reflex as rx

from reflex_init.components.link_button import link_button
from reflex_init.components.link_icons import link_icons
from reflex_init.components.title import title
from reflex_init.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title(
            'Social media links',
        ),
        link_icons(),
        width='100%',
        align_items='center',
    )
