#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib,re,sys

class BlipVideo:
    def __init__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            pass

    def get_info(self,url):
        pass

    def get_rss(self,url):
        urlR=re.compile('http:\/\/blip\.tv/([^/]+)/([^/]+)-(\d+)')
        (channel,name,vid)=urlR.findall(url)[0]
        return 'http://blip.tv/rss/flash/%s' % vid

    def check(self):
        pass


if __name__=="__main__":
    blip=BlipVideo()
