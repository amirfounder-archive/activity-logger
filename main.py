from Logger import Logger
import threading

logger = Logger()

t1 = threading.Thread(target=logger.activate_mouse_listener)
t2 = threading.Thread(target=logger.activate_keyboard_listener)

t1.start()
t2.start()
