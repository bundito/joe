import os
import os.path


class DownloadItem:

    def __init__(self, path):

        self.dirname = os.path.dirname(path)
        self.filename = os.path.basename(path)
        self.fullpath = path
        self.type = ""


#----------------- START -----------------------#


entries = ('/home/user/video1.mp4', '/home/user/videos/video11.mkv', '/home/user2/my-vacation.avi', \
           '/home/user4/training.avi', '/home/user99/bootleg_movie.mkv')

Listing = []

for item in entries:
    obj = DownloadItem(item)
    Listing.append(obj)

