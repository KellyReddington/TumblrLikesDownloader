# -*- coding: utf-8 -*-
# Created by Kelly Reddington 1/11/2017

import pytumblr
import os
import urllib
import re
from tumblr_keys import *

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

def media_download(mylikes, dirname):
    for i in range(0, len(mylikes['liked_posts'])):
        if mylikes['liked_posts'][i]['type'] == 'photo':
            for j in range(0, len(mylikes['liked_posts'][i]['photos'])):
                url = mylikes['liked_posts'][i]['photos'][j]['original_size']['url']
                name = re.findall(r'tumblr_\w+.\w+', url)
                urllib.urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + '/' + str(len(mylikes['liked_posts'])) + '] Photo ' + name[0])
        elif mylikes['liked_posts'][i]['type'] == 'video':
            url = mylikes['liked_posts'][i]['video_url']
            name = re.findall(r'tumblr_\w+.\w+', url)
            urllib.urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + '/' + str(len(mylikes['liked_posts'])) + '] Video ' + name[0])
        else:
            print('[' + str(i+1) + '/' + str(len(mylikes['liked_posts'])) + ']')

def main():
    info = client.info()
    dirname = info['user']['name']
    blogurl = info['user']['blogs'][0]['url']
    likescount = info['user']['likes']
    statepath = os.path.join(dirname, 'last_offset')
    lastoffset = 0
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    else:
        with open(statepath, 'r') as f:
		lastoffset = int(f.read())

    mylikes = 1
    while mylikes:
        print 'Downloading at offset ', lastoffset
	mylikes = client.likes(offset=lastoffset, limit=50)
	media_download(mylikes, dirname)
        lastoffset += 50
	if mylikes:
            with open(statepath, 'wb') as f:
                f.write(str(lastoffset))


if __name__ == '__main__':
    main()
    print('Done!')
