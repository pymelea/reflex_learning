from enum import Enum
import reflex as rx


# Constants
MAX_WIDTH = '600px'


# Sizes
class Size(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    DEFAULT = '1em'
    BIG = '2em'


# Styles
BASE_STYLE = {
    rx.Button: {
        'width': '100%',
        'height': '100%',
        'display': 'block',
        'padding': Size.SMALL.value,
        # "margin": Size.DEFAULT.value,
        'border_radius': Size.DEFAULT.value,
        '_hover': {
            'color': '#EFEFEF',
        }
    },
    rx.Link: {'text_decoration': 'none', '_hover': {}},
}

title_style = dict(
    font_size='1.2em',
    width='100%',
    padding_top=Size.MEDIUM.value,
    padding_bottom='0.2em',
)

button_title_style = dict(font_size=Size.DEFAULT.value)

button_body_style = dict(font_size=Size.MEDIUM.value)

navbar_style = dict(
    position='sticky',
    padding_x='4px',
    bg='#0A3143',
    padding_y='10px',
    z_index='999',
    top='0',
)

footer_style = dict(
    bg='#0A3143',
    padding_x='4px',
    padding_y='12px',
    position='absolute',
    z_index='999',
    bottom='0',
    left='0',
    right='0',
    top='auto',
    align_items='center',
    justify_content='center',
)


body_style = dict(
    width='100vw',
    height='calc(100vh - 53px)',
    # bg='#BFD8D2',
)
