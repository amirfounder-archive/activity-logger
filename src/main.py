from utils.constants import MOUSE_CLICK_EVENT
from matplotlib.pyplot import ylabel
from datetime import datetime

from classes.Calculator import Calculator
from classes.Grapher import Grapher
from classes.Logger import Logger
from classes.Parser import Parser

# LOGGING DATA
# logger = Logger(print=True)
# logger.start_logger()

# PROCESS DATA
parser = Parser()

events = parser.get_all_logged_events()
data = parser.filter_events(events)
for key in data:
  print(f'{key}: {len(data[key])}')

# calculator = Calculator()
# visualizer = Grapher(events)

# mouse_movements = visualizer.get_mouse_movements()
# speeds = calculator.generate_mouse_movement_speed(mouse_movements)

# visualizer.generate_plot([speeds,], y_label="pixels / millisecond")
