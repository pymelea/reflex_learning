import reflex as rx

import reflex_init.styles.styles as styles


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='Lily Perera', size='xl', src='photo.jpg'),
        rx.text(
            '@Pymelea',
            font_size=styles.Size.DEFAULT.value,
            padding_y='0.5em',
        ),
        rx.heading(
            '"Just a Latin American girl who love to code"',
            size='sm',
            padding_y='1em'
        ),
        rx.text(
            'Hi there! My name is Lily Perera and I a Software Engineer',
            padding_y='0.3em',
        ),
        rx.text(
            """I have been coding for 3 years working in Python, who enjoy learning every \
                new day and improving my skills. I am always looking for new challenges,\
                and and I still feel I have a lot to learn. I like knowledge, solving problems \
                and knowing how things work. Curious person who has always had desires to \
                discover, which has led me to move constantly.
                """,
            padding_y='0.3em',
        ),
        rx.text(
            ' @Welcome to my website!',
            align_items='center',
            padding_top='0.5em',
            padding_y='0.3em',
        ),
        position='sticky',
        padding_x='14px',
        padding_y='14px',
        z_index='999',
    )
