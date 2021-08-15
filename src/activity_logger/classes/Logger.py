import os
from pynput import keyboard, mouse
import threading

from utils.constants import *
from utils.utils import get_project_path, generate_timestamp, generate_date


class MyException(Exception):
    pass


class Logger:

    def __init__(self, print=False):
        self.kill_logger = False
        self.print = print
        self.kill_key_1 = False
        self.kill_key_2 = False

    def start_logger(self):
      t1 = threading.Thread(target=self.activate_mouse_listener)
      t2 = threading.Thread(target=self.activate_keyboard_listener)

      t1.start()
      t2.start()

    # LOGGING

    def log_event(self, event):
        """Logs events to file

        Args:
            event (String): Event
        """
        self.write_to_file(event, self.generate_log_file())
        if self.print: print(event)

    @staticmethod
    def write_to_file(content, pathname):
        """Writes content to file

        Args:
            content (String): Content
            pathname (String): File pathname
        """
        with open('{}'.format(pathname), 'a') as f:
            f.write('{}\n'.format(content))

    @staticmethod
    def generate_log_file():
        """Generates a file pathname for logging

        Returns:
            String: File pathname
        """
        today = generate_date()
        project_path = get_project_path()

        # CREATE LOGS DIRECTORY IF IT DOESN'T EXIST
        project_dirs = os.listdir(project_path)
        if 'logs' not in project_dirs:
            os.mkdir(f'{project_path}/logs')

        # CREATE TODAY'S DIRECTORY IF IT DOESN'T EXIST
        log_dirs = os.listdir(f'{project_path}/logs')
        if today not in log_dirs:
            os.mkdir(f'{project_path}/logs/{today}')

        # GET TODAY'S LOG FILES
        logs = os.listdir(f'{project_path}/logs/{today}')

        # IF TODAY HAS NO LOG FILE, RETURN '1.log'
        if len(logs) == 0:
            return f'{project_path}/logs/{today}/1.log'

        # GET THE LAST LOG FILE AND META
        last_file = logs[len(logs) - 1]
        last_file_name = last_file.replace('.log', '')
        last_file_size = os.path.getsize(
            '{}/logs/{}/{}'.format(
                project_path,
                today,
                last_file
            )
        )

        # GENERATE AND RETURN TARGET FILE PATHNAME
        return '{}/logs/{}/{}.log'.format(
            project_path,
            today,
            last_file_name if
            last_file_size < MAX_LOG_FILE_SIZE else
            int(last_file_name) + 1
        )

    # KEYBOARD

    def on_press(self, key):
        """Logs the key pressed

        Args:
            key (Key): Key pressed
        """
        timestamp = generate_timestamp()
        self.log_event(f'{timestamp},{KEY_PRESS_EVENT},{key}')

        if key == keyboard.Key.ctrl_r:
            self.kill_key_1 = True

        if key == keyboard.Key.shift_r:
            self.kill_key_2 = True
        
        if key == keyboard.Key.delete:
            if self.kill_key_1 and self.kill_key_2:
                self.kill_logger = True
                raise MyException()

    def on_release(self, key):
        """Logs the key released

        Args:
            key (Key): Key released
        """
        timestamp = generate_timestamp()
        self.log_event(f'{timestamp},{KEY_RELEASE_EVENT},{key}')

        if key == keyboard.Key.ctrl_r:
            self.kill_key_1 = False
        
        if key == keyboard.Key.shift_r:
            self.kill_key_2 = False

    # MOUSE

    def on_move(self, x, y):
        """Logs the position of the mouse after movement

        Args:
            x (Int): X coordinate
            y (Int): Y coordinate
        """
        timestamp = generate_timestamp()
        self.log_event(f'{timestamp},{MOUSE_MOVE_EVENT},{x},{y}')

        if self.kill_logger:
            raise MyException()

    def on_click(self, x, y, button, pressed):
        """Logs the position of click

        Args:
            x (Int): X coordinate
            y (Int): Y coordinate
            button (Button): Button (left or right)
            pressed (Boolean): Whether pressed or not
        """
        timestamp = generate_timestamp()
        pressed = 'pressed' if pressed == True else 'released'
        self.log_event(
            f'{timestamp},{MOUSE_CLICK_EVENT},{x},{y},{button},{pressed}')

        if self.kill_logger:
            raise MyException()

    def on_scroll(self, x, y, dx, dy):
        """Logs mouse information when scrolled

        Args:
            x (Int): X coordinate
            y (Int): Y coordinate
            dx (Int): Horizontal Scroll direction
            dy (Int): Vertical Scroll direction
        """
        timestamp = generate_timestamp()
        dy = 'up' if dy > 0 else 'down'
        self.log_event(f'{timestamp},{MOUSE_SCROLL_EVENT},{x},{y},{dx},{dy}')

        if self.kill_logger:
            raise MyException()

    # LISTENERS

    def activate_mouse_listener(self):
        """Activates the mouse listener
        """
        with mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll
        ) as mouse_listener:
            try:
                mouse_listener.join()
            except MyException:
                print('stopping')

    def activate_keyboard_listener(self):
        """Activates the keyboard listener
        """
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as keyboard_listener:
            try:
                keyboard_listener.join()
            except MyException:
                print('stopping')
