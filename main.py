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
calculator = Calculator()

events = parser.get_all_logged_events()
for event in events:
  print(event)
# visualizer = Grapher(events)

# mouse_movements = visualizer.get_mouse_movements()
# speeds = calculator.generate_mouse_movement_speed(mouse_movements)

# visualizer.generate_plot([speeds,], y_label="pixels / millisecond")
