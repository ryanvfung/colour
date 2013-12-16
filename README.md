RGB/Hex Colour Module for Python
================================

Introduction
------------

A simple class-based method of manipulating colours by themselves, in terms of their red, green and blue components.

**Author**: Ryan Fung

**Created**: 2013-12-10

**Last Modified**: 2013-12-16


Functions in the colour module
------------------------------
* **hsl(hue, sat, l)** -- Create and return a colour object based on HSL values, where 'hue' is in degrees, and both saturation 'sat' and lightness 'l' are out of 1
* **hsv(hue, sat, v)** -- Create and return a colour object based on HSV values, where 'hue' is in degrees, and both saturation 'sat' and value 'v' are out of 1
* **hsi(hue, sat, i)** -- Create and return a colour object based on HSI values, where 'hue' is in degrees, and both saturation 'sat' and intensity 'i' are out of 1
* **hslv(hue, sat, arg, argtype)** -- Create and return a colour object based on HSL/HSV/HSI values, where 'hue' is in degrees, saturation 'sat' is out of 1, 'arg' is either lightness out of 1 or value out of 1, 'argtype' is 1 for HSL and 2 for HSV
* **average(*args)** -- Returns the unweighted average of colours
* **weightedAverage(colours, weights)** -- Returns the weighted average of colours

Methods of the Colour class
---------------------------
* **\_\_init\_\_** -- initialises Colour object by parsing input RGB (as 3 int's, tuple or list), greyscale (out of 1 or 255) or hex string values (3 digit or 6 digit, with or without the hash)
* **\_\_str\_\_** -- readable string interpretation
* **\_\_repr\_\_** -- representation interpretation
* **\_\_gt\_\_** -- greater than (>)
* **\_\_lt\_\_** -- less than (<)
* **\_\_ge\_\_** -- greater than or equal to (>=)
* **\_\_le\_\_** -- less than or equal to (<=)
* **\_\_eq\_\_** -- equal to (==)
* **\_\_ne\_\_** -- not equal to (!=)
* **trans(t, other)** -- Returns a Colour object representing the colour when the calling colour has a transparency of 't' out of 1 against an 'other' coloured background
* **lighten(factor)** -- Returns a Colour object representing the colour when the calling colour is lightened by an factor of 'factor'
* **darken(factor)** -- Returns a Colour object representing the colour when the calling colour is darkened by an factor of 'factor'
* **complement()** -- Returns the complement of the calling colour as a Colour object

Data in the Colour class
------------------------
* **red** -- Red colour component out of 255
* **green** -- Green colour component out of 255
* **blue** -- Blue colour component out of 255
* **rgb** -- Tuple (red, green, blue) of the RGB values
* **hex** -- 6-digit Hexadecimal representation in the form RRGGBB
* **hsl** -- Tuple (hue, saturation, lightness)
* **hsv** -- Tuple (hue, saturation, value)
* **hsi** -- Tuple (hue, saturation, intensity)
> For HSL, HSV and HSI tuple implementation:
> * Hues are always in degrees
> * Saturation, Lightness, Value and Intensity are all out of 1

Data in the colour module
-------------------------
### HTML/CSS basic colour keywrds
* **black** = Colour(0)
* **silver** = Colour("C0C0C0")
* **gray** = Colour("808080")
* **white** = Colour(1)
* **maroon** = Colour("800000")
* **red** = Colour("F00")
* **purple** = Colour("800080")
* **fuchsia** = Colour("F0F")
* **green** = Colour("008000")
* **lime** = Colour("0F0")
* **olive** = Colour("808000")
* **yellow** = Colour("FF0")
* **navy** = Colour("000080")
* **blue** = Colour("00F")
* **teal** = Colour("008080")
* **aqua** = Colour("0FF")


Upcoming Features to be Implemented
-----------------------------------
* Generic expansion of features


Change log
----------
### 2013-12-12 Version 0.1
* Initial release
* Defined **\_\_str\_\_**, **\_\_repr\_\_**, and comparison methods
* Defined **red**, **green**, **blue**, **hex** values

### 2013-12-13 Version 0.2
* Changed truncation to rounding when converting from RGB to hex after initialising Colour object
* Defined **trans**, **lighten**, **darken**, **complement** methods
* Defined **rgb** value
	#### 2013-12-13 Version 0.2.1
	* Added support for tuple or list input arguments

### 2013-12-15 Version 0.3
* Defined **average**, **weightedAverage** functions
	#### 2013-12-15 Version 0.3.1
	* Defined HTML/CSS basic colour keywrds

### 2013-12-16 Version 0.4
* Defined **hsl**, **hsv**, **hsi** functions to define Colour objects in those forms
* Defined **hsl**, **hsv**, **hsi** values