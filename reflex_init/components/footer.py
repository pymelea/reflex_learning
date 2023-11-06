import datetime

import reflex as rx

import reflex_init.styles.styles as styles


def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
            f'© {datetime.date.today().year} Lily Perera',
            color='#EFEFEF',
        ),
        rx.text(
            'Made with Love&Code&Python',
            color='#EFEFEF',
        ),
        rx.link(
            rx.text('using Reflex'),
            href='https://reflex.dev/',
            is_external=True,
            color='#EFEFEF',
        ),
        rx.link(
            rx.text('Projects'),
            href='https://lilyperera.tech/projects',
            is_external=True,
            color='#EFEFEF',
        ),
        rx.link(
            rx.text('Contact me'),
            href='emailto:lilycapetillo86@gmail.com',
            is_external=True,
            color='#EFEFEF',
        ),
        rx.link(
            rx.text('    About me'),
            href='https://lilyperera.tech/about_me',
            is_external=True,
            color='#EFEFEF',
        ),
        style=styles.footer_style,
    )
