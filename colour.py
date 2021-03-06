# -*- coding: utf-8 -*-
""" RGB/Hex Colour Module
    Version 0.4 release
    @author: Ryan Fung
    Create Date: 2013-12-10
    Last Modified: 2013-12-13
"""


class Colour(object):
    def __init__(self, *args):
        """Parse the initialising argument(s) as either as: three integers
        corresponding to RGB values out of 255; an RGB tuple or list;
        a greyscale percentage; greyscale value out of 255; a 3 digit
        hexadecimal string; or a 6 digit hexadecimal string."""
        def colourConvert():
            """Post-process parsed red, green and blue values into hex"""
            r = self.red
            g = self.green
            b = self.blue
            self.hex = format(int(round(r)), "02X") + \
                format(int(round(g)), "02X") + \
                format(int(round(b)), "02X")
            self.rgb = (r, g, b)
            hueConvert()

        def hueConvert():
            """Calculates HSL, HSV, HSI values"""
            r = self.red / 255.
            g = self.green / 255.
            b = self.blue / 255.
            M = max(r, g, b)
            m = min(r, g, b)
            C = float(M - m)
            if C == 0:
                hue = 0
            elif M == r:
                hue = ((g-b)/C) % 6
            elif M == g:
                hue = ((b-r)/C) + 2
            elif M == b:
                hue = ((r-g)/C) + 4
            hue *= 60  # normalising against 360°
            self.hue = hue
            # calculate lightness values
            L = (M + m)/2.
            V = M
            I = (r + g + b)/3.
            # calculate saturation values
            if C == 0:
                S_HSL = S_HSV = S_HSI = 0
            else:
                S_HSL = C/(1-abs((2*L)-1))
                S_HSV = C/V
                S_HSI = 1 - (float(m)/I)
            self.hsl = (hue, S_HSL, L)
            self.hsv = (hue, S_HSV, V)
            self.hsi = (hue, S_HSI, I)

        if len(args) == 1 and type(args[0]) in [tuple, list]:
            args = args[0]
        if len(args) == 3:
            """Validate and parse RGB arguments"""
            if (max(args) > 255) or (min(args) < 0):
                raise ValueError("RGB values must be between 0 and 255")
            self.red, self.green, self.blue = args
            colourConvert()
        elif len(args) == 1 and type(args[0]) in [int, float, long]:
            """Validate greyscale input"""
            if args[0] < 0 or args[0] > 255:
                raise ValueError("Greyscale value must be either out of 1 or \
255")
            if args[0] <= 1:
                self.red = self.green = self.blue = args[0] * 255
            else:
                self.red = self.green = self.blue = args[0]
            colourConvert()
        elif len(args) == 1 and type(args[0]) == str:
            """Validate hex input"""
            string = args[0]
            if len(string) in [4, 7] and string[0] == "#":
                string = string[1:]
            hexerror = "Hex string must be in the form 'RGB', '#RGB', 'RRGGBB\
' or '#RRGGBB', and each digit must be a valid hexadecimal digit"
            if len(string) not in [3, 6]:
                raise TypeError(hexerror)
            if len(string) == 3:
                try:
                    self.red = int(string[0], 16)*17
                    self.green = int(string[1], 16)*17
                    self.blue = int(string[2], 16)*17
                except ValueError:
                    raise ValueError(hexerror+"3")
            elif len(string) == 6:
                try:
                    self.red = int(string[0:2], 16)
                    self.green = int(string[2:4], 16)
                    self.blue = int(string[4:6], 16)
                except ValueError:
                    raise ValueError(hexerror+"6")
            colourConvert()
        else:
            raise TypeError("Input arguments must either be 3 RGB values out \
of 255, a greyscale value out of either 1 or 255, or a hexadecimal string")

    def __str__(self):
        """x.__str__() <==> str(x)"""
        return "rgba" + self.__repr__()[6:]

    def __repr__(self):
        """x.__repr__() <==> repr(x)"""
        return "Colour({},{},{})".format(self.red, self.green, self.blue)

    def __gt__(self, other):
        """x.__gt__(y) <==> x>y"""
        raise TypeError("no ordering relation is defined for colours")

    def __lt__(self, other):
        """x.__lt__(y) <==> x<y"""
        raise TypeError("no ordering relation is defined for colours")

    def __ge__(self, other):
        """x.__ge__(y) <==> x>=y"""
        raise TypeError("no ordering relation is defined for colours")

    def __le__(self, other):
        """x.__le__(y) <==> x<=y"""
        raise TypeError("no ordering relation is defined for colours")

    def __eq__(self, other):
        """x.__eq__(y) <==> x==y"""
        return True if self.rgb == other.rgb else False

    def __ne__(self, other):
        """x.__ne__(y) <==> x!=y"""
        return not(self == other)

    def __add__(self, other):
        """x.__add__(y) <==> x+y
        Add the RGB components up to a maximum of 255"""
        red = self.red + other.red
        green = self.green + other.green
        blue = self.blue + other.blue
        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255
        return Colour(red, green, blue)

    def trans(self, t, other):
        """Returns a Colour object representing the colour when the calling
        colour has a transparency of 't' out of 1 against an 'other' coloured
        background"""
        if t < 0 or t > 1:
            raise ValueError("Transparency must be between 0 and 1")
        r = (self.red * t) + (other.red * (1-t))
        g = (self.green * t) + (other.green * (1-t))
        b = (self.blue * t) + (other.blue * (1-t))
        return Colour(r, g, b)

    def lighten(self, factor):
        """Returns a Colour object representing the colour when the calling
        colour is lightened by an factor of 'factor'"""
        if factor < 0 or factor > 1:
            raise ValueError("Lighten factor must be between 0 and 1")
        return Colour("FFF").trans(0.25, self)

    def darken(self, factor):
        """Returns a Colour object representing the colour when the calling
        colour is darkened by an factor of 'factor'"""
        if factor < 0 or factor > 1:
            raise ValueError("Darken factor must be between 0 and 1")
        return Colour("000").trans(0.25, self)

    def complement(self):
        """Returns the complement of the calling colour as a Colour object"""
        return Colour(255-self.red, 255-self.green, 255-self.blue)


def hsl(hue, sat, l):
    """Create and return a colour object based on HSL values, where 'hue' is
    in degrees, and both saturation 'sat' and lightness 'l' are out of 1"""
    if l < 0 or l > 1:
        raise TypeError("Lightness must be between 0 and 1")
    return hslv(hue, sat, l, 1)


def hsv(hue, sat, v):
    """Create and return a colour object based on HSV values, where 'hue' is
    in degrees, and both saturation 'sat' and value 'v' are out of 1"""
    if v < 0 or v > 1:
        raise TypeError("Value must be between 0 and 1")
    return hslv(hue, sat, v, 2)


def hsi(hue, sat, i):
    """Create and return a colour object based on HSI values, where 'hue' is
    in degrees, and both saturation 'sat' and intensity 'i' are out of 1"""
    if sat < 0 or sat > 1:
        raise TypeError("Saturation must be between 0 and 1")
    if i < 0 or i > 1:
        raise TypeError("Intensity must be between 0 and 1")
    from math import pi, cos
    h = (hue % 120) * pi/180
    x = i * (1 - sat)
    y = i * (1 + float(sat*cos(h))/(cos((pi/3)-h)))
    z = (3 * i) - (x + y)
    if hue < 120:
        rgb = (y, z, x)
    elif hue < 240:
        rgb = (x, y, z)
    elif hue < 360:
        rgb = (z, x, y)
    else:
        rgb = (0, 0, 0)
    if max(rgb) > 1:
        raise TypeError("Invalid HSI values - resultant RGB values outside \
possible range")
    return Colour(255 * rgb[0], 255 * rgb[1], 255 * rgb[2])


def hslv(hue, sat, arg, argtype):
    """Create and return a colour object based on HSL/HSV/HSI values, where
    'hue' is in degrees, saturation 'sat' is out of 1, 'arg' is either
    lightness out of 1 or value out of 1, 'argtype' is 1 for HSL
    and 2 for HSV"""
    if sat < 0 or sat > 1:
        raise TypeError("Saturation must be between 0 and 1")
    if argtype == 3:
        raise NotImplementedError
    if argtype == 1:
        C = (1-abs((2*arg)-1)) * sat
    elif argtype == 2:
        C = arg * sat
    H = hue / 60.
    X = C * (1 - abs((H % 2) - 1))
    if H < 1:
        rgb = (C, X, 0)
    elif H < 2:
        rgb = (X, C, 0)
    elif H < 3:
        rgb = (0, C, X)
    elif H < 4:
        rgb = (0, X, C)
    elif H < 5:
        rgb = (X, 0, C)
    elif H < 6:
        rgb = (C, 0, X)
    else:
        rgb = (0, 0, 0)
    if argtype == 1:
        m = arg - (.5*C)
    elif argtype == 2:
        m = arg - C
    return Colour(255*(rgb[0] + m), 255*(rgb[1] + m), 255*(rgb[2] + m))


def average(*args):
    """Returns the unweighted average of colours"""
    red = green = blue = 0
    try:
        weight = 1./len(args)
        for item in args:
            red += weight * item.red
            green += weight * item.green
            blue += weight * item.blue
    except AttributeError:
        raise TypeError("All arguments must be colours")
    return Colour(red, green, blue)


def weightedAverage(colours, weights):
    """Returns the weighted average of colours"""
    if len(colours) != len(weights):
        raise TypeError("Colours list and weights list must have the \
same length")
    if sum(weights) == 0:
        raise TypeError("Weight List must sum to a non-zero value")
    weight = float(sum(weights))/len(weights)
    red = green = blue = 0
    try:
        for i in range(len(colours)):
            red += weight * colours[i].red * weights[i]
            green += weight * colours[i].green * weights[i]
            blue += weight * colours[i].blue * weights[i]
    except AttributeError:
        raise TypeError("Colours list must only contain colours, Weights \
list must only contain numbers")
    return Colour(red, green, blue)

#  define HTML/CSS basic colour keywrds
black = Colour(0)
silver = Colour("C0C0C0")
gray = Colour("808080")
white = Colour(1)
maroon = Colour("800000")
red = Colour("F00")
purple = Colour("800080")
fuchsia = Colour("F0F")
green = Colour("008000")
lime = Colour("0F0")
olive = Colour("808000")
yellow = Colour("FF0")
navy = Colour("000080")
blue = Colour("00F")
teal = Colour("008080")
aqua = Colour("0FF")
