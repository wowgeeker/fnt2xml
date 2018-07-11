python script for converting bitmap font format from cocos/unity style to xml style required by other game engines, for example:

from:

info face="FZCuYuan-M03S" size=64 bold=0 italic=0 charset="" unicode=0 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=2,2
common lineHeight=72 base=57 scaleW=256 scaleH=256 pages=1 packed=0
page id=0 file="num11.png"
chars count=13
char id=32     x=237   y=58    width=0     height=0     xoffset=0     yoffset=58    xadvance=17    page=0 chnl=0 letter="space"
char id=43     x=151   y=58    width=41    height=41    xoffset=2     yoffset=16    xadvance=38    page=0 chnl=0 letter="+"
char id=45     x=194   y=58    width=41    height=15    xoffset=2     yoffset=30    xadvance=38    page=0 chnl=0 letter="-"
char id=48     x=46    y=2     width=41    height=54    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="0"
char id=49     x=124   y=58    width=25    height=53    xoffset=2     yoffset=4     xadvance=24    page=0 chnl=0 letter="1"
char id=50     x=2     y=58    width=38    height=54    xoffset=3     yoffset=4     xadvance=37    page=0 chnl=0 letter="2"
char id=51     x=173   y=2     width=39    height=54    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="3"
char id=52     x=2     y=2     width=42    height=54    xoffset=1     yoffset=4     xadvance=37    page=0 chnl=0 letter="4"
char id=53     x=84    y=58    width=38    height=53    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="5"
char id=54     x=89    y=2     width=40    height=54    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="6"
char id=55     x=42    y=58    width=40    height=53    xoffset=1     yoffset=4     xadvance=34    page=0 chnl=0 letter="7"
char id=56     x=214   y=2     width=39    height=54    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="8"
char id=57     x=131   y=2     width=40    height=54    xoffset=2     yoffset=4     xadvance=37    page=0 chnl=0 letter="9"


to:


<?xml version="1.0" encoding="utf-8"?>

<font>
  <info aa="1" bold="0" charset="" face="FZCuYuan-M03S" italic="0" padding="0,0,0,0" size="64" smooth="1" spacing="2,2" stretchH="100" unicode="0"/>
  <common base="57" lineHeight="72" packed="0" pages="1" scaleH="256" scaleW="256"/>
  <pages>
    <page file="num11.png" id="0"/>
  </pages>
  <chars count="13">
    <char chnl="0" height="0" id="32" letter="space" page="0" width="0" x="237" xadvance="17" xoffset="0" y="58" yoffset="58"/>
    <char chnl="0" height="41" id="43" letter="+" page="0" width="41" x="151" xadvance="38" xoffset="2" y="58" yoffset="16"/>
    <char chnl="0" height="15" id="45" letter="-" page="0" width="41" x="194" xadvance="38" xoffset="2" y="58" yoffset="30"/>
    <char chnl="0" height="54" id="48" letter="0" page="0" width="41" x="46" xadvance="37" xoffset="2" y="2" yoffset="4"/>
    <char chnl="0" height="53" id="49" letter="1" page="0" width="25" x="124" xadvance="24" xoffset="2" y="58" yoffset="4"/>
    <char chnl="0" height="54" id="50" letter="2" page="0" width="38" x="2" xadvance="37" xoffset="3" y="58" yoffset="4"/>
    <char chnl="0" height="54" id="51" letter="3" page="0" width="39" x="173" xadvance="37" xoffset="2" y="2" yoffset="4"/>
    <char chnl="0" height="54" id="52" letter="4" page="0" width="42" x="2" xadvance="37" xoffset="1" y="2" yoffset="4"/>
    <char chnl="0" height="53" id="53" letter="5" page="0" width="38" x="84" xadvance="37" xoffset="2" y="58" yoffset="4"/>
    <char chnl="0" height="54" id="54" letter="6" page="0" width="40" x="89" xadvance="37" xoffset="2" y="2" yoffset="4"/>
    <char chnl="0" height="53" id="55" letter="7" page="0" width="40" x="42" xadvance="34" xoffset="1" y="58" yoffset="4"/>
    <char chnl="0" height="54" id="56" letter="8" page="0" width="39" x="214" xadvance="37" xoffset="2" y="2" yoffset="4"/>
    <char chnl="0" height="54" id="57" letter="9" page="0" width="40" x="131" xadvance="37" xoffset="2" y="2" yoffset="4"/>
  </chars>
</font>
