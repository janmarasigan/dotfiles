import json
import subprocess
from collections import defaultdict
from datetime import datetime, timezone

from kitty.boss import get_boss
from kitty.fast_data_types import Screen, add_timer
from kitty.rgb import Color
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    Formatter,
    TabBarData,
    as_rgb,
    draw_attributed_string,
    draw_title,
    draw_tab_with_powerline
)
from kitty.utils import color_as_int

timer_id = None

ICON = " 楽  "
RIGHT_MARGIN = 1
REFRESH_TIME = 15

icon_fg = as_rgb(color_as_int(Color(255, 250, 205)))
#icon_bg = as_rgb(color_as_int(Color(29, 210, 254)))
icon_bg = as_rgb(0x1dd2fe)

def calc_draw_spaces(*args) -> int:
    length = 0
    for i in args:
        if not isinstance(i, str):
            i = str(i)
        length += len(i)
    return length


def _draw_icon(screen: Screen, index: int) -> int:
    if index != 1:
        return 0

    fg, bg = screen.cursor.fg, screen.cursor.bg
    screen.cursor.fg = icon_fg
    screen.cursor.bg = icon_bg
    screen.draw(ICON)
    screen.cursor.fg, screen.cursor.bg = fg, bg
    screen.cursor.x = len(ICON)
    return screen.cursor.x

def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:

    _draw_icon(screen, index)
    draw_tab_with_powerline(
        draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
    )

    return screen.cursor.x