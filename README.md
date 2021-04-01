# rainmeter-terminal-rss
Rainmeter RSS Feed that look like a Linux terminal. Currently only works with my [LogDNA Transcriber](https://github.com/chand1012/logdna-xml-transcriber/). You can either clone this repo and run the Python script or download the executable file found in [releases](https://github.com/chand1012/TerminalRSS/releases).

To use:

```
usage: generator.exe [-h] [--url URL] [--update UPDATE] [--width WIDTH] [--height HEIGHT] [--bgcolor BGCOLOR] [--color COLOR] [--font FONT] [--inverted] [--length LENGTH] [--output OUTPUT] [--test]

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     Link for the RSS Feed.
  --update UPDATE, -U UPDATE
                        Update frequency in ms of the feed.
  --width WIDTH, -w WIDTH
                        The width of the skin.
  --height HEIGHT, -ht HEIGHT
                        The height of the skin.
  --bgcolor BGCOLOR, -b BGCOLOR
                        The background color as a string formated like so: R,G,B,A
  --color COLOR, -c COLOR
                        The primary text color formated like so: R,G,B,A
  --font FONT, -f FONT  The selected font.
  --inverted, -i        Inverts the console so that it reads like a traditional RSS feed.
  --length LENGTH, -l LENGTH
                        The number of lines.
  --output OUTPUT, -o OUTPUT
                        File to output to.
  --test                Prints out arguments and exits.
```