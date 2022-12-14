"""Contains the RGB color class and common colors

Color source: https://www.webucator.com/article/python-color-constants-module/
"""

# Standard modules
from typing import Union, Self

# Local modules
from ..utils.enum import Enum


class RGBColor(tuple):
    """RGB color class"""

    def __new__(cls, red: int, green: int, blue: int) -> Self:
        return tuple.__new__(cls, (round(red), round(green), round(blue)))

    # PROPERTIES

    @property
    def red(self) -> int:
        return self[0]

    @property
    def green(self) -> int:
        return self[1]

    @property
    def blue(self) -> int:
        return self[2]

    @property
    def hex(self) -> str:
        return '#%02x%02x%02x' % self

    # CLASS METHODS

    @classmethod
    def from_hex(cls, value: str) -> Self:
        """Convert a hex color string to RGB"""
        value = value.replace("#", "").replace("0x", "")
        return RGBColor(*(int(value[i:i+2], 16) for i in (0, 2, 4)))

    # METHODS

    def rgba(self, value: int) -> tuple[int, int, int, int]:
        """Get a RGBA color tuple"""
        return self[0], self[1], self[2], value

    def list(self) -> list[int]:
        """Create a list with the red, green and blue values as elements"""
        return [*self]

    def dict(self, keys: tuple[str, str, str] = ("red", "green", "blue")) -> dict[str, int]:
        """Create a dictionary with the x and y values as value of specific keys"""
        return {keys[0]: self[0], keys[1]: self[1], keys[2]: self[2]}

    def clamp(self) -> Self:
        """Clamp the values to be greater equals 0 and lower equals 255"""
        clamped: list = self.list()
        for i in range(3):
            if clamped[i] < 0:
                clamped[i] = 0
            elif clamped[i] > 255:
                clamped[i] = 255
        return RGBColor(*clamped)

    def mix(self, color: Self) -> Self:
        """Mix two RGB colors"""
        return ((self + color) * 0.5).clamp()

    # OVERLOADS

    def __eq__(self, other: Self) -> bool:
        return self[0] == other[0] and self[1] == other[1] and self[2] == other[2]

    def __ne__(self, other: Self) -> bool:
        return self[0] != other[0] or self[1] != other[1] or self[2] != other[2]

    def __add__(self, other: Self) -> Self:
        return RGBColor(self[0] + other[0], self[1] + other[1], self[2] + other[2]).clamp()

    def __sub__(self, other: Self) -> Self:
        return RGBColor(self[0] - other[0], self[1] - other[1], self[2] - other[2]).clamp()

    def __mul__(self, factor: Union[int, float]) -> Self:
        return RGBColor(self[0] * factor, self[1] * factor, self[2] * factor).clamp()

    def __truediv__(self, divisor: Union[int, float]) -> Self:
        return RGBColor(self[0] / divisor, self[1] / divisor, self[2] / divisor).clamp()

    def __floordiv__(self, divisor: Union[int, float]) -> Self:
        return RGBColor(self[0] // divisor, self[1] // divisor, self[2] // divisor).clamp()

    def __pow__(self, power: float, modulo: float = None):
        return RGBColor(pow(self[0], power, modulo), pow(self[1], power, modulo), pow(self[2], power, modulo)).clamp()

    def __repr__(self) -> str:
        return f"RGB[id={id(self)}, red={self[0]}, green={self[1]}, blue={self[2]}]"

    def __str__(self) -> str:
        return f"({self[0]}, {self[1]}, {self[2]})"


class RGB(Enum):
    """RGB color library enum"""

    ALICEBLUE: RGBColor = RGBColor(240, 248, 255)
    ANTIQUEWHITE: RGBColor = RGBColor(250, 235, 215)
    ANTIQUEWHITE1: RGBColor = RGBColor(255, 239, 219)
    ANTIQUEWHITE2: RGBColor = RGBColor(238, 223, 204)
    ANTIQUEWHITE3: RGBColor = RGBColor(205, 192, 176)
    ANTIQUEWHITE4: RGBColor = RGBColor(139, 131, 120)
    AQUA: RGBColor = RGBColor(0, 255, 255)
    AQUAMARINE1: RGBColor = RGBColor(127, 255, 212)
    AQUAMARINE2: RGBColor = RGBColor(118, 238, 198)
    AQUAMARINE3: RGBColor = RGBColor(102, 205, 170)
    AQUAMARINE4: RGBColor = RGBColor(69, 139, 116)
    AZURE1: RGBColor = RGBColor(240, 255, 255)
    AZURE2: RGBColor = RGBColor(224, 238, 238)
    AZURE3: RGBColor = RGBColor(193, 205, 205)
    AZURE4: RGBColor = RGBColor(131, 139, 139)
    BANANA: RGBColor = RGBColor(227, 207, 87)
    BEIGE: RGBColor = RGBColor(245, 245, 220)
    BISQUE1: RGBColor = RGBColor(255, 228, 196)
    BISQUE2: RGBColor = RGBColor(238, 213, 183)
    BISQUE3: RGBColor = RGBColor(205, 183, 158)
    BISQUE4: RGBColor = RGBColor(139, 125, 107)
    BLACK: RGBColor = RGBColor(0, 0, 0)
    BLANCHEDALMOND: RGBColor = RGBColor(255, 235, 205)
    BLUE: RGBColor = RGBColor(0, 0, 255)
    BLUE2: RGBColor = RGBColor(0, 0, 238)
    BLUE3: RGBColor = RGBColor(0, 0, 205)
    BLUE4: RGBColor = RGBColor(0, 0, 139)
    BLUEVIOLET: RGBColor = RGBColor(138, 43, 226)
    BRICK: RGBColor = RGBColor(156, 102, 31)
    BROWN: RGBColor = RGBColor(165, 42, 42)
    BROWN1: RGBColor = RGBColor(255, 64, 64)
    BROWN2: RGBColor = RGBColor(238, 59, 59)
    BROWN3: RGBColor = RGBColor(205, 51, 51)
    BROWN4: RGBColor = RGBColor(139, 35, 35)
    BURLYWOOD: RGBColor = RGBColor(222, 184, 135)
    BURLYWOOD1: RGBColor = RGBColor(255, 211, 155)
    BURLYWOOD2: RGBColor = RGBColor(238, 197, 145)
    BURLYWOOD3: RGBColor = RGBColor(205, 170, 125)
    BURLYWOOD4: RGBColor = RGBColor(139, 115, 85)
    BURNTSIENNA: RGBColor = RGBColor(138, 54, 15)
    BURNTUMBER: RGBColor = RGBColor(138, 51, 36)
    CADETBLUE: RGBColor = RGBColor(95, 158, 160)
    CADETBLUE1: RGBColor = RGBColor(152, 245, 255)
    CADETBLUE2: RGBColor = RGBColor(142, 229, 238)
    CADETBLUE3: RGBColor = RGBColor(122, 197, 205)
    CADETBLUE4: RGBColor = RGBColor(83, 134, 139)
    CADMIUMORANGE: RGBColor = RGBColor(255, 97, 3)
    CADMIUMYELLOW: RGBColor = RGBColor(255, 153, 18)
    CARROT: RGBColor = RGBColor(237, 145, 33)
    CHARTREUSE1: RGBColor = RGBColor(127, 255, 0)
    CHARTREUSE2: RGBColor = RGBColor(118, 238, 0)
    CHARTREUSE3: RGBColor = RGBColor(102, 205, 0)
    CHARTREUSE4: RGBColor = RGBColor(69, 139, 0)
    CHOCOLATE: RGBColor = RGBColor(210, 105, 30)
    CHOCOLATE1: RGBColor = RGBColor(255, 127, 36)
    CHOCOLATE2: RGBColor = RGBColor(238, 118, 33)
    CHOCOLATE3: RGBColor = RGBColor(205, 102, 29)
    CHOCOLATE4: RGBColor = RGBColor(139, 69, 19)
    COBALT: RGBColor = RGBColor(61, 89, 171)
    COBALTGREEN: RGBColor = RGBColor(61, 145, 64)
    COLDGREY: RGBColor = RGBColor(128, 138, 135)
    CORAL: RGBColor = RGBColor(255, 127, 80)
    CORAL1: RGBColor = RGBColor(255, 114, 86)
    CORAL2: RGBColor = RGBColor(238, 106, 80)
    CORAL3: RGBColor = RGBColor(205, 91, 69)
    CORAL4: RGBColor = RGBColor(139, 62, 47)
    CORNFLOWERBLUE: RGBColor = RGBColor(100, 149, 237)
    CORNSILK1: RGBColor = RGBColor(255, 248, 220)
    CORNSILK2: RGBColor = RGBColor(238, 232, 205)
    CORNSILK3: RGBColor = RGBColor(205, 200, 177)
    CORNSILK4: RGBColor = RGBColor(139, 136, 120)
    CRIMSON: RGBColor = RGBColor(220, 20, 60)
    CYAN2: RGBColor = RGBColor(0, 238, 238)
    CYAN3: RGBColor = RGBColor(0, 205, 205)
    CYAN4: RGBColor = RGBColor(0, 139, 139)
    DARKGOLDENROD: RGBColor = RGBColor(184, 134, 11)
    DARKGOLDENROD1: RGBColor = RGBColor(255, 185, 15)
    DARKGOLDENROD2: RGBColor = RGBColor(238, 173, 14)
    DARKGOLDENROD3: RGBColor = RGBColor(205, 149, 12)
    DARKGOLDENROD4: RGBColor = RGBColor(139, 101, 8)
    DARKGRAY: RGBColor = RGBColor(169, 169, 169)
    DARKGREEN: RGBColor = RGBColor(0, 100, 0)
    DARKKHAKI: RGBColor = RGBColor(189, 183, 107)
    DARKOLIVEGREEN: RGBColor = RGBColor(85, 107, 47)
    DARKOLIVEGREEN1: RGBColor = RGBColor(202, 255, 112)
    DARKOLIVEGREEN2: RGBColor = RGBColor(188, 238, 104)
    DARKOLIVEGREEN3: RGBColor = RGBColor(162, 205, 90)
    DARKOLIVEGREEN4: RGBColor = RGBColor(110, 139, 61)
    DARKORANGE: RGBColor = RGBColor(255, 140, 0)
    DARKORANGE1: RGBColor = RGBColor(255, 127, 0)
    DARKORANGE2: RGBColor = RGBColor(238, 118, 0)
    DARKORANGE3: RGBColor = RGBColor(205, 102, 0)
    DARKORANGE4: RGBColor = RGBColor(139, 69, 0)
    DARKORCHID: RGBColor = RGBColor(153, 50, 204)
    DARKORCHID1: RGBColor = RGBColor(191, 62, 255)
    DARKORCHID2: RGBColor = RGBColor(178, 58, 238)
    DARKORCHID3: RGBColor = RGBColor(154, 50, 205)
    DARKORCHID4: RGBColor = RGBColor(104, 34, 139)
    DARKSALMON: RGBColor = RGBColor(233, 150, 122)
    DARKSEAGREEN: RGBColor = RGBColor(143, 188, 143)
    DARKSEAGREEN1: RGBColor = RGBColor(193, 255, 193)
    DARKSEAGREEN2: RGBColor = RGBColor(180, 238, 180)
    DARKSEAGREEN3: RGBColor = RGBColor(155, 205, 155)
    DARKSEAGREEN4: RGBColor = RGBColor(105, 139, 105)
    DARKSLATEBLUE: RGBColor = RGBColor(72, 61, 139)
    DARKSLATEGRAY: RGBColor = RGBColor(47, 79, 79)
    DARKSLATEGRAY1: RGBColor = RGBColor(151, 255, 255)
    DARKSLATEGRAY2: RGBColor = RGBColor(141, 238, 238)
    DARKSLATEGRAY3: RGBColor = RGBColor(121, 205, 205)
    DARKSLATEGRAY4: RGBColor = RGBColor(82, 139, 139)
    DARKTURQUOISE: RGBColor = RGBColor(0, 206, 209)
    DARKVIOLET: RGBColor = RGBColor(148, 0, 211)
    DEEPPINK1: RGBColor = RGBColor(255, 20, 147)
    DEEPPINK2: RGBColor = RGBColor(238, 18, 137)
    DEEPPINK3: RGBColor = RGBColor(205, 16, 118)
    DEEPPINK4: RGBColor = RGBColor(139, 10, 80)
    DEEPSKYBLUE1: RGBColor = RGBColor(0, 191, 255)
    DEEPSKYBLUE2: RGBColor = RGBColor(0, 178, 238)
    DEEPSKYBLUE3: RGBColor = RGBColor(0, 154, 205)
    DEEPSKYBLUE4: RGBColor = RGBColor(0, 104, 139)
    DIMGRAY: RGBColor = RGBColor(105, 105, 105)
    DODGERBLUE1: RGBColor = RGBColor(30, 144, 255)
    DODGERBLUE2: RGBColor = RGBColor(28, 134, 238)
    DODGERBLUE3: RGBColor = RGBColor(24, 116, 205)
    DODGERBLUE4: RGBColor = RGBColor(16, 78, 139)
    EGGSHELL: RGBColor = RGBColor(252, 230, 201)
    EMERALDGREEN: RGBColor = RGBColor(0, 201, 87)
    FIREBRICK: RGBColor = RGBColor(178, 34, 34)
    FIREBRICK1: RGBColor = RGBColor(255, 48, 48)
    FIREBRICK2: RGBColor = RGBColor(238, 44, 44)
    FIREBRICK3: RGBColor = RGBColor(205, 38, 38)
    FIREBRICK4: RGBColor = RGBColor(139, 26, 26)
    FLESH: RGBColor = RGBColor(255, 125, 64)
    FLORALWHITE: RGBColor = RGBColor(255, 250, 240)
    FORESTGREEN: RGBColor = RGBColor(34, 139, 34)
    GAINSBORO: RGBColor = RGBColor(220, 220, 220)
    GHOSTWHITE: RGBColor = RGBColor(248, 248, 255)
    GOLD1: RGBColor = RGBColor(255, 215, 0)
    GOLD2: RGBColor = RGBColor(238, 201, 0)
    GOLD3: RGBColor = RGBColor(205, 173, 0)
    GOLD4: RGBColor = RGBColor(139, 117, 0)
    GOLDENROD: RGBColor = RGBColor(218, 165, 32)
    GOLDENROD1: RGBColor = RGBColor(255, 193, 37)
    GOLDENROD2: RGBColor = RGBColor(238, 180, 34)
    GOLDENROD3: RGBColor = RGBColor(205, 155, 29)
    GOLDENROD4: RGBColor = RGBColor(139, 105, 20)
    GRAY: RGBColor = RGBColor(128, 128, 128)
    GRAY1: RGBColor = RGBColor(3, 3, 3)
    GRAY10: RGBColor = RGBColor(26, 26, 26)
    GRAY11: RGBColor = RGBColor(28, 28, 28)
    GRAY12: RGBColor = RGBColor(31, 31, 31)
    GRAY13: RGBColor = RGBColor(33, 33, 33)
    GRAY14: RGBColor = RGBColor(36, 36, 36)
    GRAY15: RGBColor = RGBColor(38, 38, 38)
    GRAY16: RGBColor = RGBColor(41, 41, 41)
    GRAY17: RGBColor = RGBColor(43, 43, 43)
    GRAY18: RGBColor = RGBColor(46, 46, 46)
    GRAY19: RGBColor = RGBColor(48, 48, 48)
    GRAY2: RGBColor = RGBColor(5, 5, 5)
    GRAY20: RGBColor = RGBColor(51, 51, 51)
    GRAY21: RGBColor = RGBColor(54, 54, 54)
    GRAY22: RGBColor = RGBColor(56, 56, 56)
    GRAY23: RGBColor = RGBColor(59, 59, 59)
    GRAY24: RGBColor = RGBColor(61, 61, 61)
    GRAY25: RGBColor = RGBColor(64, 64, 64)
    GRAY26: RGBColor = RGBColor(66, 66, 66)
    GRAY27: RGBColor = RGBColor(69, 69, 69)
    GRAY28: RGBColor = RGBColor(71, 71, 71)
    GRAY29: RGBColor = RGBColor(74, 74, 74)
    GRAY3: RGBColor = RGBColor(8, 8, 8)
    GRAY30: RGBColor = RGBColor(77, 77, 77)
    GRAY31: RGBColor = RGBColor(79, 79, 79)
    GRAY32: RGBColor = RGBColor(82, 82, 82)
    GRAY33: RGBColor = RGBColor(84, 84, 84)
    GRAY34: RGBColor = RGBColor(87, 87, 87)
    GRAY35: RGBColor = RGBColor(89, 89, 89)
    GRAY36: RGBColor = RGBColor(92, 92, 92)
    GRAY37: RGBColor = RGBColor(94, 94, 94)
    GRAY38: RGBColor = RGBColor(97, 97, 97)
    GRAY39: RGBColor = RGBColor(99, 99, 99)
    GRAY4: RGBColor = RGBColor(10, 10, 10)
    GRAY40: RGBColor = RGBColor(102, 102, 102)
    GRAY42: RGBColor = RGBColor(107, 107, 107)
    GRAY43: RGBColor = RGBColor(110, 110, 110)
    GRAY44: RGBColor = RGBColor(112, 112, 112)
    GRAY45: RGBColor = RGBColor(115, 115, 115)
    GRAY46: RGBColor = RGBColor(117, 117, 117)
    GRAY47: RGBColor = RGBColor(120, 120, 120)
    GRAY48: RGBColor = RGBColor(122, 122, 122)
    GRAY49: RGBColor = RGBColor(125, 125, 125)
    GRAY5: RGBColor = RGBColor(13, 13, 13)
    GRAY50: RGBColor = RGBColor(127, 127, 127)
    GRAY51: RGBColor = RGBColor(130, 130, 130)
    GRAY52: RGBColor = RGBColor(133, 133, 133)
    GRAY53: RGBColor = RGBColor(135, 135, 135)
    GRAY54: RGBColor = RGBColor(138, 138, 138)
    GRAY55: RGBColor = RGBColor(140, 140, 140)
    GRAY56: RGBColor = RGBColor(143, 143, 143)
    GRAY57: RGBColor = RGBColor(145, 145, 145)
    GRAY58: RGBColor = RGBColor(148, 148, 148)
    GRAY59: RGBColor = RGBColor(150, 150, 150)
    GRAY6: RGBColor = RGBColor(15, 15, 15)
    GRAY60: RGBColor = RGBColor(153, 153, 153)
    GRAY61: RGBColor = RGBColor(156, 156, 156)
    GRAY62: RGBColor = RGBColor(158, 158, 158)
    GRAY63: RGBColor = RGBColor(161, 161, 161)
    GRAY64: RGBColor = RGBColor(163, 163, 163)
    GRAY65: RGBColor = RGBColor(166, 166, 166)
    GRAY66: RGBColor = RGBColor(168, 168, 168)
    GRAY67: RGBColor = RGBColor(171, 171, 171)
    GRAY68: RGBColor = RGBColor(173, 173, 173)
    GRAY69: RGBColor = RGBColor(176, 176, 176)
    GRAY7: RGBColor = RGBColor(18, 18, 18)
    GRAY70: RGBColor = RGBColor(179, 179, 179)
    GRAY71: RGBColor = RGBColor(181, 181, 181)
    GRAY72: RGBColor = RGBColor(184, 184, 184)
    GRAY73: RGBColor = RGBColor(186, 186, 186)
    GRAY74: RGBColor = RGBColor(189, 189, 189)
    GRAY75: RGBColor = RGBColor(191, 191, 191)
    GRAY76: RGBColor = RGBColor(194, 194, 194)
    GRAY77: RGBColor = RGBColor(196, 196, 196)
    GRAY78: RGBColor = RGBColor(199, 199, 199)
    GRAY79: RGBColor = RGBColor(201, 201, 201)
    GRAY8: RGBColor = RGBColor(20, 20, 20)
    GRAY80: RGBColor = RGBColor(204, 204, 204)
    GRAY81: RGBColor = RGBColor(207, 207, 207)
    GRAY82: RGBColor = RGBColor(209, 209, 209)
    GRAY83: RGBColor = RGBColor(212, 212, 212)
    GRAY84: RGBColor = RGBColor(214, 214, 214)
    GRAY85: RGBColor = RGBColor(217, 217, 217)
    GRAY86: RGBColor = RGBColor(219, 219, 219)
    GRAY87: RGBColor = RGBColor(222, 222, 222)
    GRAY88: RGBColor = RGBColor(224, 224, 224)
    GRAY89: RGBColor = RGBColor(227, 227, 227)
    GRAY9: RGBColor = RGBColor(23, 23, 23)
    GRAY90: RGBColor = RGBColor(229, 229, 229)
    GRAY91: RGBColor = RGBColor(232, 232, 232)
    GRAY92: RGBColor = RGBColor(235, 235, 235)
    GRAY93: RGBColor = RGBColor(237, 237, 237)
    GRAY94: RGBColor = RGBColor(240, 240, 240)
    GRAY95: RGBColor = RGBColor(242, 242, 242)
    GRAY97: RGBColor = RGBColor(247, 247, 247)
    GRAY98: RGBColor = RGBColor(250, 250, 250)
    GRAY99: RGBColor = RGBColor(252, 252, 252)
    GREEN: RGBColor = RGBColor(0, 128, 0)
    GREEN1: RGBColor = RGBColor(0, 255, 0)
    GREEN2: RGBColor = RGBColor(0, 238, 0)
    GREEN3: RGBColor = RGBColor(0, 205, 0)
    GREEN4: RGBColor = RGBColor(0, 139, 0)
    GREENYELLOW: RGBColor = RGBColor(173, 255, 47)
    HONEYDEW1: RGBColor = RGBColor(240, 255, 240)
    HONEYDEW2: RGBColor = RGBColor(224, 238, 224)
    HONEYDEW3: RGBColor = RGBColor(193, 205, 193)
    HONEYDEW4: RGBColor = RGBColor(131, 139, 131)
    HOTPINK: RGBColor = RGBColor(255, 105, 180)
    HOTPINK1: RGBColor = RGBColor(255, 110, 180)
    HOTPINK2: RGBColor = RGBColor(238, 106, 167)
    HOTPINK3: RGBColor = RGBColor(205, 96, 144)
    HOTPINK4: RGBColor = RGBColor(139, 58, 98)
    INDIANRED: RGBColor = RGBColor(205, 92, 92)
    INDIANRED1: RGBColor = RGBColor(255, 106, 106)
    INDIANRED2: RGBColor = RGBColor(238, 99, 99)
    INDIANRED3: RGBColor = RGBColor(205, 85, 85)
    INDIANRED4: RGBColor = RGBColor(139, 58, 58)
    INDIGO: RGBColor = RGBColor(75, 0, 130)
    IVORY1: RGBColor = RGBColor(255, 255, 240)
    IVORY2: RGBColor = RGBColor(238, 238, 224)
    IVORY3: RGBColor = RGBColor(205, 205, 193)
    IVORY4: RGBColor = RGBColor(139, 139, 131)
    IVORYBLACK: RGBColor = RGBColor(41, 36, 33)
    KHAKI: RGBColor = RGBColor(240, 230, 140)
    KHAKI1: RGBColor = RGBColor(255, 246, 143)
    KHAKI2: RGBColor = RGBColor(238, 230, 133)
    KHAKI3: RGBColor = RGBColor(205, 198, 115)
    KHAKI4: RGBColor = RGBColor(139, 134, 78)
    LAVENDER: RGBColor = RGBColor(230, 230, 250)
    LAVENDERBLUSH1: RGBColor = RGBColor(255, 240, 245)
    LAVENDERBLUSH2: RGBColor = RGBColor(238, 224, 229)
    LAVENDERBLUSH3: RGBColor = RGBColor(205, 193, 197)
    LAVENDERBLUSH4: RGBColor = RGBColor(139, 131, 134)
    LAWNGREEN: RGBColor = RGBColor(124, 252, 0)
    LEMONCHIFFON1: RGBColor = RGBColor(255, 250, 205)
    LEMONCHIFFON2: RGBColor = RGBColor(238, 233, 191)
    LEMONCHIFFON3: RGBColor = RGBColor(205, 201, 165)
    LEMONCHIFFON4: RGBColor = RGBColor(139, 137, 112)
    LIGHTBLUE: RGBColor = RGBColor(173, 216, 230)
    LIGHTBLUE1: RGBColor = RGBColor(191, 239, 255)
    LIGHTBLUE2: RGBColor = RGBColor(178, 223, 238)
    LIGHTBLUE3: RGBColor = RGBColor(154, 192, 205)
    LIGHTBLUE4: RGBColor = RGBColor(104, 131, 139)
    LIGHTCORAL: RGBColor = RGBColor(240, 128, 128)
    LIGHTCYAN1: RGBColor = RGBColor(224, 255, 255)
    LIGHTCYAN2: RGBColor = RGBColor(209, 238, 238)
    LIGHTCYAN3: RGBColor = RGBColor(180, 205, 205)
    LIGHTCYAN4: RGBColor = RGBColor(122, 139, 139)
    LIGHTGOLDENROD1: RGBColor = RGBColor(255, 236, 139)
    LIGHTGOLDENROD2: RGBColor = RGBColor(238, 220, 130)
    LIGHTGOLDENROD3: RGBColor = RGBColor(205, 190, 112)
    LIGHTGOLDENROD4: RGBColor = RGBColor(139, 129, 76)
    LIGHTGOLDENRODYELLOW: RGBColor = RGBColor(250, 250, 210)
    LIGHTGREY: RGBColor = RGBColor(211, 211, 211)
    LIGHTPINK: RGBColor = RGBColor(255, 182, 193)
    LIGHTPINK1: RGBColor = RGBColor(255, 174, 185)
    LIGHTPINK2: RGBColor = RGBColor(238, 162, 173)
    LIGHTPINK3: RGBColor = RGBColor(205, 140, 149)
    LIGHTPINK4: RGBColor = RGBColor(139, 95, 101)
    LIGHTSALMON1: RGBColor = RGBColor(255, 160, 122)
    LIGHTSALMON2: RGBColor = RGBColor(238, 149, 114)
    LIGHTSALMON3: RGBColor = RGBColor(205, 129, 98)
    LIGHTSALMON4: RGBColor = RGBColor(139, 87, 66)
    LIGHTSEAGREEN: RGBColor = RGBColor(32, 178, 170)
    LIGHTSKYBLUE: RGBColor = RGBColor(135, 206, 250)
    LIGHTSKYBLUE1: RGBColor = RGBColor(176, 226, 255)
    LIGHTSKYBLUE2: RGBColor = RGBColor(164, 211, 238)
    LIGHTSKYBLUE3: RGBColor = RGBColor(141, 182, 205)
    LIGHTSKYBLUE4: RGBColor = RGBColor(96, 123, 139)
    LIGHTSLATEBLUE: RGBColor = RGBColor(132, 112, 255)
    LIGHTSLATEGRAY: RGBColor = RGBColor(119, 136, 153)
    LIGHTSTEELBLUE: RGBColor = RGBColor(176, 196, 222)
    LIGHTSTEELBLUE1: RGBColor = RGBColor(202, 225, 255)
    LIGHTSTEELBLUE2: RGBColor = RGBColor(188, 210, 238)
    LIGHTSTEELBLUE3: RGBColor = RGBColor(162, 181, 205)
    LIGHTSTEELBLUE4: RGBColor = RGBColor(110, 123, 139)
    LIGHTYELLOW1: RGBColor = RGBColor(255, 255, 224)
    LIGHTYELLOW2: RGBColor = RGBColor(238, 238, 209)
    LIGHTYELLOW3: RGBColor = RGBColor(205, 205, 180)
    LIGHTYELLOW4: RGBColor = RGBColor(139, 139, 122)
    LIMEGREEN: RGBColor = RGBColor(50, 205, 50)
    LINEN: RGBColor = RGBColor(250, 240, 230)
    MAGENTA: RGBColor = RGBColor(255, 0, 255)
    MAGENTA2: RGBColor = RGBColor(238, 0, 238)
    MAGENTA3: RGBColor = RGBColor(205, 0, 205)
    MAGENTA4: RGBColor = RGBColor(139, 0, 139)
    MANGANESEBLUE: RGBColor = RGBColor(3, 168, 158)
    MAROON: RGBColor = RGBColor(128, 0, 0)
    MAROON1: RGBColor = RGBColor(255, 52, 179)
    MAROON2: RGBColor = RGBColor(238, 48, 167)
    MAROON3: RGBColor = RGBColor(205, 41, 144)
    MAROON4: RGBColor = RGBColor(139, 28, 98)
    MEDIUMORCHID: RGBColor = RGBColor(186, 85, 211)
    MEDIUMORCHID1: RGBColor = RGBColor(224, 102, 255)
    MEDIUMORCHID2: RGBColor = RGBColor(209, 95, 238)
    MEDIUMORCHID3: RGBColor = RGBColor(180, 82, 205)
    MEDIUMORCHID4: RGBColor = RGBColor(122, 55, 139)
    MEDIUMPURPLE: RGBColor = RGBColor(147, 112, 219)
    MEDIUMPURPLE1: RGBColor = RGBColor(171, 130, 255)
    MEDIUMPURPLE2: RGBColor = RGBColor(159, 121, 238)
    MEDIUMPURPLE3: RGBColor = RGBColor(137, 104, 205)
    MEDIUMPURPLE4: RGBColor = RGBColor(93, 71, 139)
    MEDIUMSEAGREEN: RGBColor = RGBColor(60, 179, 113)
    MEDIUMSLATEBLUE: RGBColor = RGBColor(123, 104, 238)
    MEDIUMSPRINGGREEN: RGBColor = RGBColor(0, 250, 154)
    MEDIUMTURQUOISE: RGBColor = RGBColor(72, 209, 204)
    MEDIUMVIOLETRED: RGBColor = RGBColor(199, 21, 133)
    MELON: RGBColor = RGBColor(227, 168, 105)
    MIDNIGHTBLUE: RGBColor = RGBColor(25, 25, 112)
    MINT: RGBColor = RGBColor(189, 252, 201)
    MINTCREAM: RGBColor = RGBColor(245, 255, 250)
    MISTYROSE1: RGBColor = RGBColor(255, 228, 225)
    MISTYROSE2: RGBColor = RGBColor(238, 213, 210)
    MISTYROSE3: RGBColor = RGBColor(205, 183, 181)
    MISTYROSE4: RGBColor = RGBColor(139, 125, 123)
    MOCCASIN: RGBColor = RGBColor(255, 228, 181)
    NAVAJOWHITE1: RGBColor = RGBColor(255, 222, 173)
    NAVAJOWHITE2: RGBColor = RGBColor(238, 207, 161)
    NAVAJOWHITE3: RGBColor = RGBColor(205, 179, 139)
    NAVAJOWHITE4: RGBColor = RGBColor(139, 121, 94)
    NAVY: RGBColor = RGBColor(0, 0, 128)
    OLDLACE: RGBColor = RGBColor(253, 245, 230)
    OLIVE: RGBColor = RGBColor(128, 128, 0)
    OLIVEDRAB: RGBColor = RGBColor(107, 142, 35)
    OLIVEDRAB1: RGBColor = RGBColor(192, 255, 62)
    OLIVEDRAB2: RGBColor = RGBColor(179, 238, 58)
    OLIVEDRAB3: RGBColor = RGBColor(154, 205, 50)
    OLIVEDRAB4: RGBColor = RGBColor(105, 139, 34)
    ORANGE: RGBColor = RGBColor(255, 128, 0)
    ORANGE1: RGBColor = RGBColor(255, 165, 0)
    ORANGE2: RGBColor = RGBColor(238, 154, 0)
    ORANGE3: RGBColor = RGBColor(205, 133, 0)
    ORANGE4: RGBColor = RGBColor(139, 90, 0)
    ORANGERED1: RGBColor = RGBColor(255, 69, 0)
    ORANGERED2: RGBColor = RGBColor(238, 64, 0)
    ORANGERED3: RGBColor = RGBColor(205, 55, 0)
    ORANGERED4: RGBColor = RGBColor(139, 37, 0)
    ORCHID: RGBColor = RGBColor(218, 112, 214)
    ORCHID1: RGBColor = RGBColor(255, 131, 250)
    ORCHID2: RGBColor = RGBColor(238, 122, 233)
    ORCHID3: RGBColor = RGBColor(205, 105, 201)
    ORCHID4: RGBColor = RGBColor(139, 71, 137)
    PALEGOLDENROD: RGBColor = RGBColor(238, 232, 170)
    PALEGREEN: RGBColor = RGBColor(152, 251, 152)
    PALEGREEN1: RGBColor = RGBColor(154, 255, 154)
    PALEGREEN2: RGBColor = RGBColor(144, 238, 144)
    PALEGREEN3: RGBColor = RGBColor(124, 205, 124)
    PALEGREEN4: RGBColor = RGBColor(84, 139, 84)
    PALETURQUOISE1: RGBColor = RGBColor(187, 255, 255)
    PALETURQUOISE2: RGBColor = RGBColor(174, 238, 238)
    PALETURQUOISE3: RGBColor = RGBColor(150, 205, 205)
    PALETURQUOISE4: RGBColor = RGBColor(102, 139, 139)
    PALEVIOLETRED: RGBColor = RGBColor(219, 112, 147)
    PALEVIOLETRED1: RGBColor = RGBColor(255, 130, 171)
    PALEVIOLETRED2: RGBColor = RGBColor(238, 121, 159)
    PALEVIOLETRED3: RGBColor = RGBColor(205, 104, 137)
    PALEVIOLETRED4: RGBColor = RGBColor(139, 71, 93)
    PAPAYAWHIP: RGBColor = RGBColor(255, 239, 213)
    PEACHPUFF1: RGBColor = RGBColor(255, 218, 185)
    PEACHPUFF2: RGBColor = RGBColor(238, 203, 173)
    PEACHPUFF3: RGBColor = RGBColor(205, 175, 149)
    PEACHPUFF4: RGBColor = RGBColor(139, 119, 101)
    PEACOCK: RGBColor = RGBColor(51, 161, 201)
    PINK: RGBColor = RGBColor(255, 192, 203)
    PINK1: RGBColor = RGBColor(255, 181, 197)
    PINK2: RGBColor = RGBColor(238, 169, 184)
    PINK3: RGBColor = RGBColor(205, 145, 158)
    PINK4: RGBColor = RGBColor(139, 99, 108)
    PLUM: RGBColor = RGBColor(221, 160, 221)
    PLUM1: RGBColor = RGBColor(255, 187, 255)
    PLUM2: RGBColor = RGBColor(238, 174, 238)
    PLUM3: RGBColor = RGBColor(205, 150, 205)
    PLUM4: RGBColor = RGBColor(139, 102, 139)
    POWDERBLUE: RGBColor = RGBColor(176, 224, 230)
    PURPLE: RGBColor = RGBColor(128, 0, 128)
    PURPLE1: RGBColor = RGBColor(155, 48, 255)
    PURPLE2: RGBColor = RGBColor(145, 44, 238)
    PURPLE3: RGBColor = RGBColor(125, 38, 205)
    PURPLE4: RGBColor = RGBColor(85, 26, 139)
    RASPBERRY: RGBColor = RGBColor(135, 38, 87)
    RAWSIENNA: RGBColor = RGBColor(199, 97, 20)
    RED1: RGBColor = RGBColor(255, 0, 0)
    RED2: RGBColor = RGBColor(238, 0, 0)
    RED3: RGBColor = RGBColor(205, 0, 0)
    RED4: RGBColor = RGBColor(139, 0, 0)
    ROSYBROWN: RGBColor = RGBColor(188, 143, 143)
    ROSYBROWN1: RGBColor = RGBColor(255, 193, 193)
    ROSYBROWN2: RGBColor = RGBColor(238, 180, 180)
    ROSYBROWN3: RGBColor = RGBColor(205, 155, 155)
    ROSYBROWN4: RGBColor = RGBColor(139, 105, 105)
    ROYALBLUE: RGBColor = RGBColor(65, 105, 225)
    ROYALBLUE1: RGBColor = RGBColor(72, 118, 255)
    ROYALBLUE2: RGBColor = RGBColor(67, 110, 238)
    ROYALBLUE3: RGBColor = RGBColor(58, 95, 205)
    ROYALBLUE4: RGBColor = RGBColor(39, 64, 139)
    SALMON: RGBColor = RGBColor(250, 128, 114)
    SALMON1: RGBColor = RGBColor(255, 140, 105)
    SALMON2: RGBColor = RGBColor(238, 130, 98)
    SALMON3: RGBColor = RGBColor(205, 112, 84)
    SALMON4: RGBColor = RGBColor(139, 76, 57)
    SANDYBROWN: RGBColor = RGBColor(244, 164, 96)
    SAPGREEN: RGBColor = RGBColor(48, 128, 20)
    SEAGREEN1: RGBColor = RGBColor(84, 255, 159)
    SEAGREEN2: RGBColor = RGBColor(78, 238, 148)
    SEAGREEN3: RGBColor = RGBColor(67, 205, 128)
    SEAGREEN4: RGBColor = RGBColor(46, 139, 87)
    SEASHELL1: RGBColor = RGBColor(255, 245, 238)
    SEASHELL2: RGBColor = RGBColor(238, 229, 222)
    SEASHELL3: RGBColor = RGBColor(205, 197, 191)
    SEASHELL4: RGBColor = RGBColor(139, 134, 130)
    SEPIA: RGBColor = RGBColor(94, 38, 18)
    SGIBEET: RGBColor = RGBColor(142, 56, 142)
    SGIBRIGHTGRAY: RGBColor = RGBColor(197, 193, 170)
    SGICHARTREUSE: RGBColor = RGBColor(113, 198, 113)
    SGIDARKGRAY: RGBColor = RGBColor(85, 85, 85)
    SGIGRAY12: RGBColor = RGBColor(30, 30, 30)
    SGIGRAY16: RGBColor = RGBColor(40, 40, 40)
    SGIGRAY32: RGBColor = RGBColor(81, 81, 81)
    SGIGRAY36: RGBColor = RGBColor(91, 91, 91)
    SGIGRAY52: RGBColor = RGBColor(132, 132, 132)
    SGIGRAY56: RGBColor = RGBColor(142, 142, 142)
    SGIGRAY72: RGBColor = RGBColor(183, 183, 183)
    SGIGRAY76: RGBColor = RGBColor(193, 193, 193)
    SGIGRAY92: RGBColor = RGBColor(234, 234, 234)
    SGIGRAY96: RGBColor = RGBColor(244, 244, 244)
    SGILIGHTBLUE: RGBColor = RGBColor(125, 158, 192)
    SGILIGHTGRAY: RGBColor = RGBColor(170, 170, 170)
    SGIOLIVEDRAB: RGBColor = RGBColor(142, 142, 56)
    SGISALMON: RGBColor = RGBColor(198, 113, 113)
    SGISLATEBLUE: RGBColor = RGBColor(113, 113, 198)
    SGITEAL: RGBColor = RGBColor(56, 142, 142)
    SIENNA: RGBColor = RGBColor(160, 82, 45)
    SIENNA1: RGBColor = RGBColor(255, 130, 71)
    SIENNA2: RGBColor = RGBColor(238, 121, 66)
    SIENNA3: RGBColor = RGBColor(205, 104, 57)
    SIENNA4: RGBColor = RGBColor(139, 71, 38)
    SILVER: RGBColor = RGBColor(192, 192, 192)
    SKYBLUE: RGBColor = RGBColor(135, 206, 235)
    SKYBLUE1: RGBColor = RGBColor(135, 206, 255)
    SKYBLUE2: RGBColor = RGBColor(126, 192, 238)
    SKYBLUE3: RGBColor = RGBColor(108, 166, 205)
    SKYBLUE4: RGBColor = RGBColor(74, 112, 139)
    SLATEBLUE: RGBColor = RGBColor(106, 90, 205)
    SLATEBLUE1: RGBColor = RGBColor(131, 111, 255)
    SLATEBLUE2: RGBColor = RGBColor(122, 103, 238)
    SLATEBLUE3: RGBColor = RGBColor(105, 89, 205)
    SLATEBLUE4: RGBColor = RGBColor(71, 60, 139)
    SLATEGRAY: RGBColor = RGBColor(112, 128, 144)
    SLATEGRAY1: RGBColor = RGBColor(198, 226, 255)
    SLATEGRAY2: RGBColor = RGBColor(185, 211, 238)
    SLATEGRAY3: RGBColor = RGBColor(159, 182, 205)
    SLATEGRAY4: RGBColor = RGBColor(108, 123, 139)
    SNOW1: RGBColor = RGBColor(255, 250, 250)
    SNOW2: RGBColor = RGBColor(238, 233, 233)
    SNOW3: RGBColor = RGBColor(205, 201, 201)
    SNOW4: RGBColor = RGBColor(139, 137, 137)
    SPRINGGREEN: RGBColor = RGBColor(0, 255, 127)
    SPRINGGREEN1: RGBColor = RGBColor(0, 238, 118)
    SPRINGGREEN2: RGBColor = RGBColor(0, 205, 102)
    SPRINGGREEN3: RGBColor = RGBColor(0, 139, 69)
    STEELBLUE: RGBColor = RGBColor(70, 130, 180)
    STEELBLUE1: RGBColor = RGBColor(99, 184, 255)
    STEELBLUE2: RGBColor = RGBColor(92, 172, 238)
    STEELBLUE3: RGBColor = RGBColor(79, 148, 205)
    STEELBLUE4: RGBColor = RGBColor(54, 100, 139)
    TAN: RGBColor = RGBColor(210, 180, 140)
    TAN1: RGBColor = RGBColor(255, 165, 79)
    TAN2: RGBColor = RGBColor(238, 154, 73)
    TAN3: RGBColor = RGBColor(205, 133, 63)
    TAN4: RGBColor = RGBColor(139, 90, 43)
    TEAL: RGBColor = RGBColor(0, 128, 128)
    THISTLE: RGBColor = RGBColor(216, 191, 216)
    THISTLE1: RGBColor = RGBColor(255, 225, 255)
    THISTLE2: RGBColor = RGBColor(238, 210, 238)
    THISTLE3: RGBColor = RGBColor(205, 181, 205)
    THISTLE4: RGBColor = RGBColor(139, 123, 139)
    TOMATO1: RGBColor = RGBColor(255, 99, 71)
    TOMATO2: RGBColor = RGBColor(238, 92, 66)
    TOMATO3: RGBColor = RGBColor(205, 79, 57)
    TOMATO4: RGBColor = RGBColor(139, 54, 38)
    TURQUOISE: RGBColor = RGBColor(64, 224, 208)
    TURQUOISE1: RGBColor = RGBColor(0, 245, 255)
    TURQUOISE2: RGBColor = RGBColor(0, 229, 238)
    TURQUOISE3: RGBColor = RGBColor(0, 197, 205)
    TURQUOISE4: RGBColor = RGBColor(0, 134, 139)
    TURQUOISEBLUE: RGBColor = RGBColor(0, 199, 140)
    VIOLET: RGBColor = RGBColor(238, 130, 238)
    VIOLETRED: RGBColor = RGBColor(208, 32, 144)
    VIOLETRED1: RGBColor = RGBColor(255, 62, 150)
    VIOLETRED2: RGBColor = RGBColor(238, 58, 140)
    VIOLETRED3: RGBColor = RGBColor(205, 50, 120)
    VIOLETRED4: RGBColor = RGBColor(139, 34, 82)
    WARMGREY: RGBColor = RGBColor(128, 128, 105)
    WHEAT: RGBColor = RGBColor(245, 222, 179)
    WHEAT1: RGBColor = RGBColor(255, 231, 186)
    WHEAT2: RGBColor = RGBColor(238, 216, 174)
    WHEAT3: RGBColor = RGBColor(205, 186, 150)
    WHEAT4: RGBColor = RGBColor(139, 126, 102)
    WHITE: RGBColor = RGBColor(255, 255, 255)
    WHITESMOKE: RGBColor = RGBColor(245, 245, 245)
    YELLOW1: RGBColor = RGBColor(255, 255, 0)
    YELLOW2: RGBColor = RGBColor(238, 238, 0)
    YELLOW3: RGBColor = RGBColor(205, 205, 0)
    YELLOW4: RGBColor = RGBColor(139, 139, 0)
