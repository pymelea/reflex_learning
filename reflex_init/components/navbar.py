import reflex as rx

import reflex_init.styles.styles as styles


def navbar() -> rx.Component:
    """The index page."""
    return rx.hstack(
        rx.avatar(name='Lily Perera', size='sm', src='avatar.jpg'),
        rx.text("def pymelea_dev(args, kwargs):", height='30px', color='#EFEFEF'),
        style=styles.navbar_style,
    )
