from PIL import ImageDraw as ImageDraw
from typing import Tuple

def draw_box(draw: ImageDraw, box: Tuple[float, float, float, float], img_width: int, img_height: int, text: str=..., color: Tuple[int, int, int]=...) -> None: ...
