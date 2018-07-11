python script for converting bitmap font format from cocos/unity style to xml style required by other game engines, for example:

from:

info face="FZCuYuan-M03S" size=64 bold=0 italic=0 charset="" unicode=0 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=2,2

common lineHeight=72 base=57 scaleW=256 scaleH=256 pages=1 packed=0

....

to:

<?xml version="1.0" encoding="utf-8"?>

<font>
....
