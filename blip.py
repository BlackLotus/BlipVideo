#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib,re,sys,shlex

class BlipVideo:

    def __init__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            rss=self.get_rss(url)
            self.get_info(rss)

    def get_info(self,url):
        site=urllib.urlopen(url).read()
        title=re.findall('<media:title>(.+)</media:title>',site)[0]
        self.blips=dict(re.findall('<blip:(.+)>(.+)</blip:.+>',site))
        self.medias=[]
        for media in re.findall('<media:content (.+)\/>',site):
            self.medias.append(dict([re.findall('(.*)=(.*)',m)[0] for m in shlex.split(media)]))

    def get_rss(self,url):
        urlR=re.compile('http:\/\/blip\.tv/([^/]+)/([^/]+)-(\d+)')
        (channel,name,vid)=urlR.findall(url)[0]
        return 'http://blip.tv/rss/flash/%s' % vid

if __name__=="__main__":
    blip=BlipVideo('http://blip.tv/the-spoony-experiment/final-fantasy-xiii-review-part-4-6588174')
    #print blip.blips
#    print blip.get_rss('http://blip.tv/the-spoony-experiment/final-fantasy-xiii-review-part-4-6588174')
