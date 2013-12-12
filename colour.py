# -*- coding: utf-8 -*-
""" RGB/Hex Colour Module
    Version 0.1 release
    @author: Ryan Fung
    Create Date: 2013-12-10
    Last Modified: 2013-12-12
"""


class Colour(object):
    def __init__(self, *args):
        """Parse the initialising argument(s) as either as: a greyscale
        percentage; greyscale value out of 255; three integers corresponding
        to RGB values out of 255; a 3 digit hexadecimal string; or a 6 digit
        hexadecimal string."""
        def colourConvert():
            """Post-process parsed red, green and blue values into hex"""
            self.hex = format(int(self.red), "02X") + \
                format(int(self.green), "02X") + format(int(self.blue), "02X")
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
        if self.red == other.red and self.green == other.green and \
                self.blue == other.blue:
            return True
        else:
            return False

    def __ne__(self, other):
        return not(self == other)
