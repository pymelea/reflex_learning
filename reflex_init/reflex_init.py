import reflex as rx

import reflex_init.styles.styles as styles
from reflex_init.components.footer import footer
from reflex_init.components.navbar import navbar
from reflex_init.styles.styles import Size as Size
from reflex_init.views.header.header import header
from reflex_init.views.links.links import links


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    """The index page."""
    return rx.box(
        navbar(),

        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
            ),
            style=styles.body_style,
        ),

        footer(),

    )



# Add state and page to the app.
app = rx.App(styles=styles.BASE_STYLE)
app.add_page(index)
app.compile()
