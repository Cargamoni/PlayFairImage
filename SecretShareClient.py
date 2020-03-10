#!/usr/bin/env python3
from threading import Thread
import socket
import struct
import base64

# --- constants ---
# address = ("192.168.1.158", 12801)
ADDRESS = ("localhost", 12801)

# --- classes ---
class Receiving(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        s = socket.socket()
        s.connect(ADDRESS)

        try:
            running = True
            while running:
                # receive size
                len_str = s.recv(4)
                size = struct.unpack('!i', len_str)[0]

                print('size:', size)
                # receive string
                img_str = b''

                while size > 0:
                    if size >= 4096:
                        data = s.recv(4096)
                    else:
                        data = s.recv(size)

                    if not data:
                        break
                    size -= len(data)
                    img_str += data

                print('len:', len(img_str))
                # convert base64 to image
                fh = open("imageToSave.bmp", "wb")
                fh.write(base64.b64decode(img_str))
                fh.close()
                print("Transferring Image Data Complete !")
                running = False
        except Exception as e:
            print(e)
        finally:
            # exit
            print("Closing socket and exit")

            s.close()

# --- main ---
#Receiving().run()
if __name__ == '__main__':
    Client = Receiving()
    Client.run()