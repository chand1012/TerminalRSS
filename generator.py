import argparse
import configparser
import sys

argument_parser = argparse.ArgumentParser(description='Skin generator for RainMeter.')
argument_parser.add_argument('--url', '-u', dest='url', help='Link for the RSS Feed.')
argument_parser.add_argument('--update', '-U', dest='update', help='Update frequency in ms of the feed.', default='5000')
argument_parser.add_argument('--width', '-width', dest='width', help='The width of the skin.', default='550')
argument_parser.add_argument('--height', '-height', dest='height', help='The height of the skin.', default='300')
argument_parser.add_argument('--bgcolor', '-b', dest='bgcolor', help='The background color as a string formated like so: R,G,B,A', default='0,0,0,200')
argument_parser.add_argument('--color', '-c', dest='color', help='The primary text color formated like so: R,G,B,A', default='0,255,1,255')
argument_parser.add_argument('--font', '-f', dest='font', help='The selected font.', default='Consolas')
argument_parser.add_argument('--inverted', '-i', dest='inverted', action='store_false', help='Inverts the console so that it reads like a traditional RSS feed.')
argument_parser.add_argument('--length', '-l', dest='length', help='The number of lines.', default='10')
argument_parser.add_argument('--test', action='store_true', dest='test', help='Prints out arguments and exits.')
args = argument_parser.parse_args()

color = tuple(map(int, args.color.split(',')))
bgcolor = tuple(map(int, args.bgcolor.split(',')))
height = int(args.height)
width = int(args.width)
update = int(args.update)
length = int(args.length)

if args.test:
    print(f'Color: {color}')
    print(f'Background Color: {bgcolor}')
    print(f'Height: {height}')
    print(f'Width: {width}')
    print(f'Update Time: {update}')
    print(f'Font: {args.font}')
    print(f'Inverted: {args.inverted}')
    print(f'URL: {args.url}')
    print(f'Length: {length}')
    sys.exit(0)

skin = configparser.RawConfigParser()
skin.optionxform = str 

skin['Rainmeter'] = {
    'Update': update,
    'Author': 'chand1012'
}

skin['Variables'] = {
    'Item': '.*<item>.*<title>(.*)</title>.*<link>(.*)</link>.*<author>(.*)</author>'
}

skin['MeasureSite'] = {
    'Measure':'WebParser',
    'URL': args.url,
    'RegExp': '(?siU)<title>(.*)</title>.*<link>(.*)</link>' + ('#Item#'*length)
}

string_index = 4

for i in range(1, length+1):
    skin[f'MeasureItem{i}Title'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index
    }
    string_index += 1

    skin[f'MeasureItem{i}Link'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index
    }
    string_index += 1

    skin[f'MeasureItem{i}Author'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index
    }
    string_index += 1

# Finish This. Needs Meters
# https://docs.rainmeter.net/tips/rss-feed-tutorial/

with open('TerminalRSS.ini', 'w') as f:
    skin.write(f)