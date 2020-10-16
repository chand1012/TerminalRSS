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

length = int(args.length)

if args.test:
    color = tuple(map(int, args.color.split(',')))
    bgcolor = tuple(map(int, args.bgcolor.split(',')))
    height = int(args.height)
    width = int(args.width)
    update = int(args.update)
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
    'Update': args.update,
    'Author': 'chand1012'
}

skin['Variables'] = {
    'Item': '(?(?=.*<item>).*<item>.*<title>(.*)<\/title>.*<link>(.*)<\/link>.*<author>(.*)<\/author>)'
}

skin['MeasureSite'] = {
    'Measure':'WebParser',
    'URL': args.url,
    'RegExp': '(?siU)<title>(.*)<\/title>.*<link>(.*)<\/link>' + ('#Item#'*(length))
}

string_index = 3

for i in range(1, length+1):
    skin[f'MeasureItem{i}Title'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index,
        'DecodeCharacterReference': 1,
        'RegExpSubstitute': 1,
        'Substitute': '"^\s+":"","<!\[CDATA\[":"","\]\]>":"","!\[CDATA\[":"","\]\]":"'
    }
    string_index += 1

    skin[f'MeasureItem{i}Link'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index,
        'DecodeCharacterReference': 1,
        'RegExpSubstitute': 1,
        'Substitute': '"^\s+":"","<!\[CDATA\[":"","\]\]>":"","!\[CDATA\[":"","\]\]":"'
    }
    string_index += 1

    skin[f'MeasureItem{i}Author'] = {
        'Measure': 'WebParser',
        'URL': '[MeasureSite]',
        'StringIndex': string_index,
        'DecodeCharacterReference': 1,
        'RegExpSubstitute': 1,
        'Substitute': '"^\s+":"","<!\[CDATA\[":"","\]\]>":"","!\[CDATA\[":"","\]\]":"'
    }
    string_index += 1

skin['MeterBackground'] = {
    'Meter': 'Image',
    'W': args.width,
    'H': args.height,
    'SolidColor': args.bgcolor
}

# skin['MeterSite'] = {
#     'Meter': 'String',
#     'MeasureName': 'MeasureSiteTitle',
#     'MeterStyle': 'TextStyle',
#     'H'
# }

meter_range = range(1, length+1)
measure_range = 1
y_pos = 1
if args.inverted:
    measure_range = length

for i in meter_range:
    skin[f'MeterItem{i}'] = {
        'Meter': 'String',
        'MeasureName': f'MeasureItem{measure_range}Title',
        'MeterStyle': 'TextStyle',
        'Y': y_pos,
        'LeftMouseUpAction':f'"[MeasureItem{measure_range}Link]"',
        'ToolTipText': f'%1#CRLF#[MeasureItem{measure_range}Author]',
        'DynamicVariables':1,
        'FontColor': args.color,
        'FontFace': args.font,
        'FontSize': 11,
        'ClipString': 1,
        'AntiAlias': 1,
        'Padding': '1,1,1,1',
        'W': args.width
    }
    measure_range -= 1
    y_pos += 15


# Finish This. Needs Meters
# https://docs.rainmeter.net/tips/rss-feed-tutorial/

with open('TerminalRSS.ini', 'w') as f:
    skin.write(f)