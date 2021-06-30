import os
from utils.constants import *
from datetime import datetime

def get_project_path():
  current_directory = os.getcwd()
  current_directory_arr = current_directory.split('\\')
  index = current_directory_arr.index(PROJECT_NAME)
  return '\\'.join(current_directory_arr[:(index + 1)])


def generate_timestamp():
  return datetime.now().strftime(r'%H_%M_%S_%f')


def generate_date():
  return datetime.now().strftime(r'%m_%d_%Y')