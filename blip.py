#!/usr/bin/python2
# -*- coding: utf-8 -*-
import urllib,re,sys,shlex
import urllib2

class BlipVideo:
    def __init__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            rss=self.get_rss(url)
            self.get_info(rss)
            return self.get_video()

    def __call__(self,url=""):
        if re.match('.*blip.tv/.*',url):
            rss=self.get_rss(url)
            self.get_info(rss)
            return self.get_video()

    def find_blip(self,url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
        req.add_header('Accept','text/html')
        resp = urllib2.urlopen(req)
        site=resp.read()
        links=[]
        for link in re.findall('(https?://blip.tv/[^\'^"^ ]+)',site):
            link=urllib.unquote(link)
            if re.match('(https?://blip.tv/play/+)',link):
                links.append(link)
            else:
                self.get_info(link)
                links.append(self.get_video())
        return links

    def get_info(self,url):
        if re.match('.*blip.tv/rss/flash/.*',url):
            site=urllib.urlopen(url).read()
        elif re.match('https?://.*blip.tv/.+',url):
            url=self.get_rss(url)
            site=urllib.urlopen(url).read()
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
        url=urllib.unquote(url)
        print "Get rss from "+url
        urlR=re.compile('http:\/\/blip\.tv/([^/]+)/([^/]+)-(\d+)')
        if urlR.match(url):
            (channel,name,vid)=urlR.findall(url)[0]
        else:
            site=urllib.urlopen(url).read()
            (channel,name,vid)=urlR.findall(site)[0]
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
            for link in blip.find_blip(sys.argv[i]):
                print link
