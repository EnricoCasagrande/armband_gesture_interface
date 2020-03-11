import collections
import myo
import threading
import time
import sys
import numpy as np

class MyListener(myo.DeviceListener):

    def __init__(self, queue_size=8):
        self.lock = threading.Lock()
        self.emg_data_queue = collections.deque(maxlen=queue_size)

    def on_connect(self, device, timestamp, firmware_version):
        device.set_stream_emg(myo.StreamEmg.enabled)

    def on_emg_data(self, device, timestamp, emg_data):
        with self.lock:
            self.emg_data_queue.append((timestamp, emg_data))

    def get_emg_data(self):
        with self.lock:
            return list(self.emg_data_queue)

myo.init()
hub = myo.Hub()
start = time.time()

gesture_id = sys.argv[1]
gesture_name = sys.argv[2]
length = 10

f = open("./data/dataset-" + gesture_id + "-" + gesture_name + ".csv" ,"a") 

try:
    listener = MyListener()
    hub.run(2000, listener)
    while True:
        data = listener.get_emg_data()
        if time.time() - start >= length:
            f.close()
            break
        if len(data) > 0:
            tmp = []
            for v in listener.get_emg_data():
                tmp.append(v[1])
            tmp = list(np.stack(tmp).flatten())
            if len(tmp) >= 64:
                for value in tmp:
                    f.write("%i;" % value)
                f.write(gesture_id+"\n")    
        time.sleep(0.1)
finally:
    hub.shutdown()

