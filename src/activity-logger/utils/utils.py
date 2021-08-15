import os
from utils.constants import *
from datetime import datetime

def get_project_path():
  """Gets the project path of the current user

  Returns:
      String: Project pathname
  """
  current_directory = os.getcwd()
  current_directory_arr = current_directory.split('\\')
  index = current_directory_arr.index(PROJECT_NAME)
  return '\\'.join(current_directory_arr[:(index + 1)])


def generate_timestamp():
  """Generates current timestamp. Primary usecase: logging

  Returns:
      String: Timestamp (Hours, Minutes, Seconds, Microseconds)
  """
  return datetime.now().strftime(r'%H_%M_%S_%f')


def generate_date():
  """Generates current date. Primary usecase: logging file name

  Returns:
      String: Today's date (Month, Date, Year)
  """
  return datetime.now().strftime(r'%Y_%m_%d')