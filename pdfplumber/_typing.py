from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Literal,
    Sequence,
    Tuple,
    TypedDict,
    Union,
)

T_seq = Sequence
T_num = Union[int, float]
T_point = Tuple[T_num, T_num]
T_bbox = Tuple[T_num, T_num, T_num, T_num]
T_obj = Dict[str, Any]
T_obj_list = List[T_obj]
T_obj_iter = Iterable[T_obj]

# {'points', 'doctop', 'page_number', 'bottom', 'object_type', 'top'}


# At one point this could be converted to a namedtupe, but with __getitem__, so it stays
# compatible
class PDFObject(TypedDict):
    """Represents an character on a page in an PDF document.

    Attributes:
        bottom: Distance of bottom of the character from top of page.
        doctop: Distance of top of character from top of document.
        height: Height of the character.
        object_type: "char"
        page_number: Page number on which this character was found.
        top: Distance of top of character from top of page.
        width: Width of the character.
        x0: Distance of left side of character from left side of page.
        x1: Distance of right side of character from left side of page.
        y0: Distance of bottom of character from bottom of page.
        y1: Distance of top of character from bottom of page.
    """

    bottom: float
    doctop: float
    height: float
    object_type: Literal[
        "char",
        "curve",
        "image",
        "line",
        "rect",
        "textboxhorizontal",
        "textboxvertical",
        "textlinehorizontal",
        "textlinevertical",
    ]

    width: float
    x0: float
    x1: float
    y0: float
    y1: float
    page_number: int

    # these need to be distributed into the the child classes properly
    bits: Any
    evenodd: Any
    srcsize: Any
    imagemask: Any
    stroke: Any
    path: Any
    colorspace: Any
    font: str
    name: Any
    stream: Any


# TODO: documentation
class TextBoxHorizontal(PDFObject):
    pass


class TextLineHorizontal(PDFObject):
    pass


class TextLineVertical(PDFObject):
    pass


class TextBoxVertical(PDFObject):
    pass


class Char(PDFObject):
    """Represents an character on a page in an PDF document.

    Attributes:
        adv: Equal to text width * the font size * scaling factor.
        bottom: Distance of bottom of the character from top of page.
        doctop: Distance of top of character from top of document.
        fontname: Name of the character's font face.
        height: Height of the character.
        matrix: The "current transformation matrix" for this character. (See below for
            details.)
        non_stroking_color: The character's interior color.
        object_type: "char"
        page_number: Page number on which this character was found.
        size: Font size.
        stroking_color: The color of the character's outline (i.e., stroke), expressed
            as a tuple or integer, depending on the “color space” used.
        text: E.g., "z", or "Z" or " ".
        top: Distance of top of character from top of page.
        upright: Whether the character is upright.
        width: Width of the character.
        x0: Distance of left side of character from left side of page.
        x1: Distance of right side of character from left side of page.
        y0: Distance of bottom of character from bottom of page.
        y1: Distance of top of character from bottom of page.
    """

    adv: float

    fontname: str
    matrix: Any
    non_stroking_color: Union[int, Tuple]

    size: float
    stroking_color: Union[int, Tuple]
    text: str

    upright: bool


class Line(PDFObject):
    """Represents an character on a page in an PDF document.

    Attributes:
        bottom: Distance of bottom of the line from top of page.
        doctop: Distance of top of line from top of document.
        height: Height of line.
        linewidth: Thickness of line.
        non_stroking_color: The non-stroking color specified for the line’s path.
        object_type: "line"
        page_number: Page number on which this line was found.
        stroking_color: The color of the line, expressed as a tuple or integer,
            depending on the “color space” used.
        top: Distance of top of line from top of page.
        width: Width of line.
        x0: Distance of left-side extremity from left side of page.
        x1: Distance of right-side extremity from left side of page.
        y0: Distance of bottom extremity from bottom of page.
        y1: Distance of top extremity bottom of page.
    """

    linewidth: float
    non_stroking_color: Union[int, Tuple]

    stroking_color: Union[int, Tuple]


class Rect(PDFObject):
    """Represents an character on a page in an PDF document.

    Attributes:
        bottom: Distance of bottom of the rect from top of page.
        doctop: Distance of top of rect from top of document.
        height: Height of rectangle.
        linewidth: Thickness of rect.
        non_stroking_color: The non-stroking color specified for the rect’s path.
        object_type: "rect"
        page_number: Page number on which this rect was found.
        stroking_color: The color of the rect, expressed as a tuple or integer,
            depending on the “color space” used.
        top: Distance of top of rect from top of page.
        width: Width of rect.
        x0: Distance of left-side extremity from left side of page.
        x1: Distance of right-side extremity from left side of page.
        y0: Distance of bottom extremity from bottom of page.
        y1: Distance of top extremity bottom of page.
    """

    linewidth: float
    non_stroking_color: Union[int, Tuple]

    stroking_color: Union[int, Tuple]


class Curve(PDFObject):
    """Represents an character on a page in an PDF document.

    Attributes:
        bottom: Distance of bottom of the curve from top of page.
        doctop: Distance of top of curve from top of document.
        height: Height of rectangle.
        linewidth: Thickness of curve.
        non_stroking_color: The non-stroking color specified for the curve’s path.
        object_type: "curve"
        page_number: Page number on which this curve was found.
        stroking_color: The color of the curve, expressed as a tuple or integer,
            depending on the “color space” used.
        top: Distance of top of curve from top of page.
        width: Width of curve.
        x0: Distance of left-side extremity from left side of page.
        x1: Distance of right-side extremity from left side of page.
        y0: Distance of bottom extremity from bottom of page.
        y1: Distance of top extremity bottom of page.
        fill: Whether the shape defined by the curve's path is filled.
        points:: Points — as a list of (x, top) tuples — describing the curve.
    """

    linewidth: float
    # both seem to be needed
    pts: Tuple[float, float]
    points: Tuple[float, float]
    non_stroking_color: Union[int, Tuple]

    stroking_color: Union[int, Tuple]

    fill: Any


class Image(PDFObject):
    """Represents an character on a page in an PDF document.

    Attributes:
        bottom: Distance of bottom of the curve from top of page.
        doctop: Distance of top of curve from top of document.
        height: Height of rectangle.
        linewidth: Thickness of curve.
        non_stroking_color: The non-stroking color specified for the curve’s path.
        object_type: "curve"
        page_number: Page number on which this curve was found.
        stroking_color: The color of the curve, expressed as a tuple or integer,
            depending on the “color space” used.
        top: Distance of top of curve from top of page.
        width: Width of curve.
        x0: Distance of left-side extremity from left side of page.
        x1: Distance of right-side extremity from left side of page.
        y0: Distance of bottom extremity from bottom of page.
        y1: Distance of top extremity bottom of page.
        fill: Whether the shape defined by the curve's path is filled.
        points:: Points — as a list of (x, top) tuples — describing the curve.
    """

    linewidth: float
    # TODO both seem to be needed
    pts: Tuple[float, float]
    points: Tuple[float, float]
    non_stroking_color: Union[int, Tuple]

    stroking_color: Union[int, Tuple]
