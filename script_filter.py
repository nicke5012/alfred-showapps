import sys
import xml.etree.ElementTree as ET


def to_xml(titles, args=[], valids=[], autocompletes=[]):

    root = ET.Element('items')

    if len(titles) < 1:
        titles = ['No Open Apps']

    for i, thing in enumerate(titles):
        item = ET.SubElement(root, 'item')
        if args:
            item.set('arg', args[i])
        if valids:
            item.set('valid', valids[i])
        else:
            item.set('valid', 'NO')
        if autocompletes:
            item.set('autocomplete', autocompletes[i])

        title = ET.SubElement(item, 'title')
        title.text = titles[i]

    return ET.tostring(root, encoding='utf-8')

if __name__ == '__main__':

    get_apps_input = sys.stdin.read()

    open_apps = get_apps_input.split(',')
    open_apps = [x.strip() for x in open_apps]

    print to_xml(open_apps, args=open_apps, valids=['YES']*len(open_apps))
