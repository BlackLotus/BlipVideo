import urllib,re,sys

class BlipVideo:
    def __init__(self):
        pass

    def get_rss(self,url):
        urlR=re.compile('http:\/\/blip\.tv/([^/]+)/([^/]+)-(\d+)')
        print(urlR.findall(url))
        pass

    def check(self):
        pass


if __name__=="__main__":
    blip=BlipVideo()
    print get_rss()
