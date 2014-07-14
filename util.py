from IPython.display import HTML
from base64 import b64encode


def Video(filename):
    video = open(filename, "rb").read()
    video_encoded = b64encode(video)
    video_tag = '<video controls alt="test" src="data:video/x-m4v;base64,{0}">'.format(video_encoded)
    return HTML(data=video_tag)
