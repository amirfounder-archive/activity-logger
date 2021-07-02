from Grapher import Grapher
from datetime import datetime
from Logger import Logger
from Parser import Parser

logger = Logger()
parser = Parser(date="2021_06_29")

events = parser.get_logged_events()

for event in events:
    print(event)