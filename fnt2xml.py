# -*- coding:utf-8 -*-
# author: nobody
# createdAt: 2018/7/11

input = 'jiesuan_num.fnt'
arr = input.split('.')
arr[0] += 'xml'
output = '.'.join(arr)

header = '<?xml version="1.0"?>'

import xml.etree.ElementTree as etree

root = etree.Element("font")
info = etree.SubElement(root, "info")
common = etree.SubElement(root, "common")
pages = etree.SubElement(root, "pages")
page = etree.SubElement(pages, "page")
page.attrib['id'] = '0'
page.attrib['file'] = input.split('.')[0] + '.png'
chars = etree.SubElement(root, "chars")
tree = etree.ElementTree(root)


with open(input) as fr:
    originfnt = filter(lambda x: x, fr.readlines())


def parseline(line):
    line = line.strip()
    parts = line.split(' ')
    tag = parts[0].strip()
    attrs = filter(lambda x:len(x)==2, [p.strip().split('=') for p in parts[1:]])
    for a in attrs:
        print a
        if a[1].startswith('"') and a[1].endswith('"'):
            a[1] = a[1][1:-1]
    return tag, attrs


for line in originfnt:
    if line.startswith('info'):
        tag, attrs = parseline(line)
        for a in attrs:
            info.attrib[a[0]] = a[1]
    if line.startswith('common'):
        tag, attrs = parseline(line)
        for a in attrs:
            common.attrib[a[0]] = a[1]
    if line.startswith('page'):
        tag, attrs = parseline(line)
        for a in attrs:
            page.attrib[a[0]] = a[1]
    if line.startswith('chars '):
        tag, attrs = parseline(line)
        for a in attrs:
            chars.attrib[a[0]] = a[1]
    if line.startswith('char '):
        tag, attrs = parseline(line)
        char = etree.SubElement(chars, "char")
        for a in attrs:
            char.attrib[a[0]] = a[1]

s = '\n'.join([header, etree.tostring(root)])
with open(output, 'w') as fw:
    fw.write(s)
