import os
from utils.constants import *

from utils.utils import generate_date, get_project_path


class Parser:

    def __init__(self, date=None):
        self.date = generate_date() if date == None else date
        self.target_log_directory = f'{get_project_path()}\\logs\\{self.date}'
        self.target_log_files = os.listdir(self.target_log_directory)
        self.target_log_filepaths = []

        # GENERATE FILE PATHS
        for file in self.target_log_files:
            self.target_log_filepaths.append(
                f'{self.target_log_directory}\\{file}')

    def get_logged_events(self, format=True):

        logged_events = []

        for file_path in self.target_log_filepaths:
            file_events = open(file_path, 'r').read().split('\n')
            logged_events += file_events

        if format:
            formatted = []
            for event in logged_events:
                if event != '':
                    formatted.append(self.format_event(event, logged_events))
            return formatted

        return logged_events

    def format_event(self, event, logged_events):
        event_attributes = event.split(',')
        try:
            event_type = event_attributes[1]
            if event_type == MOUSE_SCROLL_EVENT:
                return self.parse_mouse_scroll_event(event_attributes)
            elif event_type == MOUSE_CLICK_EVENT:
                return self.parse_mouse_click_event(event_attributes)
            elif event_type == MOUSE_MOVE_EVENT:
                return self.parse_mouse_move_event(event_attributes)
            elif event_type == KEY_PRESS_EVENT:
                return self.parse_key_press_event(event_attributes)
            elif event_type == KEY_RELEASE_EVENT:
                return self.parse_key_release_event(event_attributes)
            else:
                print('not a valid mouse event type')
        except IndexError:
            print(f'Index out of range on line: {logged_events.index(event)} in folder: ${self.date}')

    @staticmethod
    def parse_mouse_click_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3],
            'button': attrs[4],
            'pressed': attrs[5]
        }

    @staticmethod
    def parse_mouse_scroll_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3],
            'dx': attrs[4],
            'dy': attrs[5]
        }

    @staticmethod
    def parse_mouse_move_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3]
        }

    @staticmethod
    def parse_key_press_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'key': attrs[2]
        }

    @staticmethod
    def parse_key_release_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'key': attrs[2]
        }