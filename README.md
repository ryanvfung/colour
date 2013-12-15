RGB/Hex Colour Module for Python
================================

Introduction
------------

A simple class-based method of manipulating colours by themselves, in terms of their red, green and blue components.

**Author**: Ryan Fung

**Created**: 2013-12-10

**Last Modified**: 2013-12-15


Functions in the Colour module
------------------------------
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
* **rgb** -- Tuple (red,green,blue) of the RGB values
* **hex** - 6-digit Hexadecimal representation in the form RRGGBB

Upcoming Features to be Implemented
-----------------------------------
None


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