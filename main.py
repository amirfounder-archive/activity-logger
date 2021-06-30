import os
from pynput import keyboard, mouse
import threading

from utils.constants import MAX_LOG_FILE_SIZE
from utils.utils import get_project_path, generate_timestamp, generate_date


killed = False


class MyException(Exception):
  pass


def log(event):
  """Logs events to file

  Args:
      event (String): Event
  """
  write_to_file(event, generate_logging_target_file())


def write_to_file(content, pathname):
  """Writes content to file

  Args:
      content (String): Content
      pathname (String): File pathname
  """
  with open('{}'.format(pathname), 'a') as f:
    f.write('{}\n'.format(content))


def generate_logging_target_file():
  """Generates a file pathname for logging

  Returns:
      String: File pathname
  """
  today = generate_date()
  project_path = get_project_path()

  # CREATE LOGS DIRECTORY IF IT DOESN'T EXIST
  project_dirs = os.listdir(project_path)
  if 'logs' not in project_dirs:
    os.mkdir('{}/logs'.format(project_path))
  
  # CREATE TODAY'S DIRECTORY IF IT DOESN'T EXIST
  log_dirs = os.listdir('{}/logs'.format(project_path))
  if today not in log_dirs:
    os.mkdir('{}/logs/{}'.format(project_path, today))
  
  # GET TODAY'S LOG FILES
  logs = os.listdir('{}/logs/{}'.format(project_path, today))

  # IF TODAY HAS NO LOG FILE, RETURN '1.log'
  if len(logs) == 0:
    return '{}/logs/{}/1.log'.format(project_path, today)
  
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

  # RETURN TARGET FILE PATHNAME
  return '{}/logs/{}/{}.log'.format(
    project_path,
    today,
    last_file_name if
    last_file_size < MAX_LOG_FILE_SIZE else
    int(last_file_name) + 1
  )


# KEYBOARD


def on_press(key):
  """Logs the key pressed

  Args:
      key (Key): Key pressed
  """
  timestamp = generate_timestamp()
  log('{},kpress,{}'.format(timestamp, key))

  if key == keyboard.Key.ctrl_r:
    global killed
    killed = True
    raise MyException(key)


def on_release(key):
  """Logs the key released

  Args:
      key (Key): Key released
  """
  timestamp = generate_timestamp()
  log('{},krelease,{}'.format(timestamp, key))


# MOUSE


def on_move(x, y):
  """Logs the position of the mouse after movement

  Args:
      x (Int): X coordinate
      y (Int): Y coordinate
  """
  timestamp = generate_timestamp()
  log('{},mmove,{},{}'.format(timestamp, x, y))

  if killed:
    raise MyException()


def on_click(x, y, button, pressed):
  """Logs the position of click

  Args:
      x (Int): X coordinate
      y (Int): Y coordinate
      button (Button): Button (left or right)
      pressed (Boolean): Whether pressed or not
  """
  timestamp = generate_timestamp()
  log('{},mclick,{},{},{},{}'.format(timestamp, x, y, button, 'down' if pressed else 'up'))

  if killed:
    raise MyException()


def on_scroll(x, y, dx, dy):
  """Logs mouse information when scrolled

  Args:
      x (Int): X coordinate
      y (Int): Y coordinate
      dx (Int): Horizontal Scroll direction
      dy (Int): Vertical Scroll direction
  """
  timestamp = generate_timestamp()
  log('{},mscroll,{},{},{},{}'.format(timestamp, x, y, dx, 'down' if dy < 0 else 'up'))

  if killed:
    raise MyException()


# LISTENERS


def activate_mouse_listener():
  """Activates the mouse listener
  """
  with mouse.Listener(
    on_move= on_move,
    on_click=on_click,
    on_scroll=on_scroll
  ) as mouse_listener:
    try:
      mouse_listener.join()
    except MyException:
      print('stopping')


def activate_keyboard_listener():
  """Activates the keyboard listener
  """
  with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
  ) as keyboard_listener:
    try:
      keyboard_listener.join()
    except MyException:
      print('stopping')


# THREADING


t1 = threading.Thread(target=activate_mouse_listener)
t2 = threading.Thread(target=activate_keyboard_listener)

t1.start()
t2.start()
