import os

"""CMSimfly Initialization setup
"""

# get current directory, on Windows, back slash at the end of the directory
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# config directory
config_dir = _curdir + "/config/"
class Init(object):
    # uwsgi as static class variable, can be accessed by Init.uwsgi
    uwsgi = False
    site_title = "41023210"
    ip = "127.0.0.1"
    #ip = "2001:288:6004:17:fff1:cd25:0000:b005"
    dynamic_port = 9441
    static_port = 8441
    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(_curdir + "/downloads"):
            try:
                os.makedirs(_curdir + "/downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(_curdir + "/images"):
            try:
                os.makedirs(_curdir + "/images")
            except:
                print("mkdir error")


