import os
from utils.constants import *

from utils.utils import generate_date, get_project_path


class Parser:

    def __init__(self):
        self.log_directory = f'{get_project_path()}\\logs'
        self.todays_log_directory = f'{self.log_directory}\\{generate_date()}'

    # GET LOGGED EVENTS

    def get_all_logged_events(self, format=True):

        logged_events = []

        for log_dir in os.listdir(self.log_directory):
            log_dir_full_path = f'{self.log_directory}\\{log_dir}'

            for file in os.listdir(log_dir_full_path):
                file_full_path = f'{log_dir_full_path}\\{file}'
                
                data = open(file_full_path, 'r').read().split('\n')
                logged_events += data

        return self.format_events(logged_events) if format else logged_events

    def get_todays_logged_events(self, format=True):

        logged_events = []

        for file in os.listdir(self.todays_log_directory):
            file_full_path = f'{self.todays_log_directory}\\{file}'

            data = open(file_full_path, 'r').read().split('\n')
            logged_events += data

        return self.format_events(logged_events) if format else logged_events

    # FILTER EVENTS

    def filter_by_event_type(self, events, event_type):
        return list(filter(lambda e: e != None and (e['type'] == event_type), events))
    
    def filter_by_multiple_event_types(self, events, event_types):
        events = []
        
        for event_type in event_types:
            events += self.filter_by_event_type(events, event_type)
        
        return events

    def filter_by_mouse_movement_events(self, events):
        return self.filter_by_event_type(events, MOUSE_MOVE_EVENT)
    
    def filter_by_mouse_click_events(self, events):
        return self.filter_by_event_type(events, MOUSE_CLICK_EVENT)
    
    def filter_by_mouse_scroll_events(self, events):
        return self.filter_by_event_type(events, MOUSE_SCROLL_EVENT)
    
    def filter_by_keyboard_press_events(self, events):
        return self.filter_by_event_type(events, KEY_PRESS_EVENT)
    
    def filter_by_keyboard_release_events(self, events):
        return self.filter_by_event_type(events, KEY_RELEASE_EVENT)

    def filter_events(self, events):
        data = {
            'mouse_movements': [],
            'mouse_clicks': [],
            'mouse_scrolls': [],
            'key_presses': [],
            'key_releases': []
        }
        for event in events:
            if event == None:
                pass
            elif event['type'] == MOUSE_MOVE_EVENT:
                data['mouse_movements'].append(event)
            elif event['type'] == MOUSE_SCROLL_EVENT:
                data['mouse_scrolls'].append(event)
            elif event['type'] == MOUSE_CLICK_EVENT:
                data['mouse_clicks'].append(event)
            elif event['type'] == KEY_PRESS_EVENT:
                data['key_presses'].append(event)
            elif event['type'] == KEY_RELEASE_EVENT:
                data['key_releases'].append(event)
            else:
                pass
        return data
    # FORMAT EVENTS

    def format_events(self, events):

        formatted_events = []

        for event in events:
            formatted_events.append(self.format_event(event, events))

        return formatted_events

    def format_event(self, event, events):
        event_attributes = event.split(',')
        try:
            event_type = event_attributes[1]
            if event_type == MOUSE_SCROLL_EVENT:
                return self.format_mouse_scroll_event(event_attributes)
            elif event_type == MOUSE_CLICK_EVENT:
                return self.format_mouse_click_event(event_attributes)
            elif event_type == MOUSE_MOVE_EVENT:
                return self.format_mouse_move_event(event_attributes)
            elif event_type == KEY_PRESS_EVENT:
                return self.format_key_press_event(event_attributes)
            elif event_type == KEY_RELEASE_EVENT:
                return self.format_key_release_event(event_attributes)
            else:
                print('not a valid mouse event type')
        except IndexError:
            print(
                f'Index out of range on line: {events.index(event)}')

    @staticmethod
    def format_mouse_click_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3],
            'button': attrs[4],
            'pressed': attrs[5]
        }

    @staticmethod
    def format_mouse_scroll_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3],
            'dx': attrs[4],
            'dy': attrs[5]
        }

    @staticmethod
    def format_mouse_move_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'x': attrs[2],
            'y': attrs[3]
        }

    @staticmethod
    def format_key_press_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'key': attrs[2]
        }

    @staticmethod
    def format_key_release_event(attrs):
        return {
            'timestamp': attrs[0],
            'type': attrs[1],
            'key': attrs[2]
        }
