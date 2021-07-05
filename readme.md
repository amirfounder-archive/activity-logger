# Amir Sharapov (@amirfounder) Logger

This program will log a user's:

- Key Presses
- Key Releases
- Mouse Movements
- Mouse Clicks
- Mouse Scrolls

# Pre-Reqs / Dependencies

- Computer (required)
- Python 3.8

## Installed with Python

- 'threading' library
  - Docs: https://docs.python.org/3/library/threading.html
- 'os' library
  - Docs: https://docs.python.org/3/library/os.html

## External Libraries

- 'pynput' library
  - Package Index: https://pypi.org/project/pynput/
  - Docs: https://pynput.readthedocs.io/en/latest/index.html
- 'six' library: (Pynput dependency)
  - Docs: https://six.readthedocs.io/

# Usage

1. CD into yoru project directory
2. Install external libraries: `pip install -r requirements.txt`
3. Run main class
4. To kill logger, press `'ctrl_r' + 'shift_r' + 'del'` and perform any action with the mouse (move, click, scroll)