from matplotlib.pyplot import ylabel
from Processor import Processor
from Visualizer import Visualizer
from datetime import datetime
from Logger import Logger
from Parser import Parser

logger = Logger()
parser = Parser(date="2021_06_30")
processor = Processor()

events = parser.get_logged_events()
visualizer = Visualizer(events)

mouse_movements = visualizer.get_mouse_movements()
speeds = processor.generate_mouse_movement_speed(mouse_movements)

visualizer.generate_plot([speeds,], y_label="pixels / millisecond")
