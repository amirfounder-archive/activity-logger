from classes.Parser import Parser
from classes.Logger import MyException
from utils.utils import generate_date
from matplotlib import pyplot as plt


class Grapher:

    def __init__(self, events):
        self.data = self.generate_data(events)
        self.mouse_movements = self.data['mouse_movements']
        self.mouse_clicks = self.data['mouse_clicks']
        self.mouse_scrolls = self.data['mouse_scrolls']
        self.key_presses = self.data['key_presses']
        self.key_releases = self.data['key_releases']

    def get_mouse_movements(self):
        return self.mouse_movements

    def get_mouse_clicks(self):
        return self.mouse_clicks

    def get_mouse_scrolls(self):
        return self.mouse_scrolls

    def get_key_presses(self):
        return self.key_presses

    def get_key_releases(self):
        return self.key_releases

    def generate_data(self, events):
        data = {
            'mouse_movements': [],
            'mouse_clicks': [],
            'mouse_scrolls': [],
            'key_presses': [],
            'key_releases': []
        }
        for event in events:
            if event['type'] == 'mm':
                data['mouse_movements'].append(event)
            elif event['type'] == 'ms':
                data['mouse_scrolls'].append(event)
            elif event['type'] == 'mc':
                data['mouse_clicks'].append(event)
            elif event['type'] == 'kp':
                data['key_presses'].append(event)
            elif event['type'] == 'kr':
                data['key_releases'].append(event)
            else:
                pass
        return data

    def generate_plot(self, values, x_label='X-Axis', y_label='Y-Axis'):
        plt.plot(*values)
        plt.ylabel = y_label
        plt.xlabel = x_label
        plt.show()
