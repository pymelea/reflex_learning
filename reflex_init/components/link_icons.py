import reflex as rx

from reflex_init.styles.styles import Size as Size


def link_icons() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src='icons8-github-50.png',
            ),
            href='https://github.com/pymelea',
            is_external=True,
        ),
        rx.link(
            rx.image(
                src='icons8-linkedin-50.png',
            ),
            href='https://www.linkedin.com/in/pymelea/',
            is_external=True,
        ),
        rx.link(
            rx.image(
                src='icons8-twitter-quadrado-50.png',
            ),
            href='https://twitter.com/pymelea',
            is_external=True,
        ),
        rx.link(
            rx.image(
                src='icons8-instagram-50.png',
            ),
            href='https://www.instagram.com/pymelea/',
            is_external=True,
        ),
        rx.link(
            rx.image(
                src='icons8-pdf-50.png',
            ),
            src='CV_Lily_Perera.pdf',
            is_external=True,
        ),
        rx.link(
            rx.image(
                src='icons8-nova-mensagem-50.png',
            ),
            href='emailto:lilycapetillo86@gmail.com',
            is_external=True,
        ),
        width='400px',
        height='auto',
        align_items='center',
        spacing='2em',
        padding='0.3em',
    )
