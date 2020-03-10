#!/usr/bin/env python3
from threading import Thread
import socket
import struct  # to send `int` as  `4 bytes`
import base64

# --- constants ---
# address = ("192.168.1.158", 12801)
ADDRESS = ("localhost", 12801)

# --- classes ---
class Streaming(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        s = socket.socket()
        # solution for: "socket.error: [Errno 98] Address already in use"
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ADDRESS)
        s.listen(1)

        print("Wait for connection")

        try:
            sc, info = s.accept()
            print("Image Client Connected:", info)
            while True:
                str = ''
                # image to string
                with open("converted/cipher.bmp", "rb") as imageFile:
                    str = base64.b64encode(imageFile.read())
                img_str = str
                print('len:', len(img_str))
                # send string size
                len_str = struct.pack('!i', len(img_str))
                sc.send(len_str)
                # send string image
                sc.send(img_str)
        except Exception as e:
            print(e)
        finally:
            # exit
            print("Closing socket and exit")
            sc.close()
            s.close()

# --- main ---
#Streaming().run()