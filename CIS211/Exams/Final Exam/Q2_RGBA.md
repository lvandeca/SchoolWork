# Bitty:  Packing and unpacking RGBA values

[RGBA](https://en.wikipedia.org/wiki/RGBA_color_model) 
(red, green, blue, alpha) is an encoding 
of a color, represented by intensities of 
red, green, and blue, and a transparency value, 
represented by a value called "alpha". Often 
these values are packed into a 32-bit integer. 
Then each of the color components may have a 
value between 0 (none) and 255 (full intensity). 
The alpha component likewise has a value between 
0 (fully transparent) and 255 (fully opaque). 


We will adopt the packed binary encoding in which 
the red componet is stored in bits 24..31, 
green in bits 16..23, 
blue in bits 8..15, 
and the alpha component is stored in
 bits 0..7.  

![RGBA encoding, by Jasonm23 - Own work, CC BY-SA 3.0, https://commons
.wikimedia.org/w/index.php?curid=22866719](img/HexRGBAbits.png)

Your task is to pack individual R, G, B, and A values 
into a 32-bit integer and to unpack a 32-bit value into 
individual R, G, B, and A values.  You may assume that 
values for all elements is between 0 and 255, inclusive. 

