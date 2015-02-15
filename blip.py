#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib,re,sys,shlex

class BlipVideo:

    def __init__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            rss=self.get_rss(url)
            self.get_info(rss)

    def __call__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            rss=self.get_rss(url)
            self.get_info(rss)
        return blip.get_video()

    def find_blip(self,url):
        pass

    def get_info(self,url):
        if re.match('.*blip.tv/rss/flash/.*',url):
            site=urllib.urlopen(url).read()
        elif re.match('https?://.*blip.tv/.+',url):
            url=get_rss(url)
        elif re.match('https?://.*',url):
            pass
        else:
            pass
        title=re.findall('<media:title>(.+)</media:title>',site)[0]
        self.blips=dict(re.findall('<blip:(.+)>(.+)</blip:.+>',site))
        self.medias=[]
        self.codecs=[]
        for media in re.findall('<media:content (.+)\/?>',site):
            mdict=dict([re.findall('(.*)=(.*)',m)[0] for m in shlex.split(media)])
            self.codecs.append(mdict['type'])
            self.medias.append(mdict)

    def get_rss(self,url):
        urlR=re.compile('http:\/\/blip\.tv/([^/]+)/([^/]+)-(\d+)')
        (channel,name,vid)=urlR.findall(url)[0]
        return 'http://blip.tv/rss/flash/%s' % vid

    def get_video(self,codec='video/mp4'):
        for media in self.medias:
            if media['type']==codec:
                return media['url']
        return self.medias[0]['url']

if __name__=="__main__":
    if len(sys.argv)>1:
        blip=BlipVideo()
        for i in range(1,len(sys.argv)):
            print(blip(sys.argv[i]))
