# -*- coding: utf-8 -*-
""" RGB/Hex Colour Module
    Version 0.2.1 release
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
            self.hex = format(int(round(self.red)), "02X") + \
                format(int(round(self.green)), "02X") + \
                format(int(round(self.blue)), "02X")
            self.rgb = (self.red, self.green, self.blue)
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
        return "rgba" + self.__repr__()[6:]

    def __repr__(self):
        return "Colour({},{},{})".format(self.red, self.green, self.blue)

    def __gt__(self, other):
        raise TypeError("no ordering relation is defined for colours")

    def __lt__(self, other):
        raise TypeError("no ordering relation is defined for colours")

    def __ge__(self, other):
        raise TypeError("no ordering relation is defined for colours")

    def __le__(self, other):
        raise TypeError("no ordering relation is defined for colours")

    def __eq__(self, other):
        if self.rgb == other.rgb:
            return True
        else:
            return False

    def __ne__(self, other):
        return not(self == other)

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
