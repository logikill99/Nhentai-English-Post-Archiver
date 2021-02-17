import os, random
from hentai import Hentai, Format
from time import sleep

postID = 0

with open('post_ids.txt', 'w') as f:
    f.write('')

def checkHentaiID(hentaiID):
    print(f'Checking Post ID: {hentaiID}')
    try:
        doujin = Hentai(hentaiID)
    except:
        print(' > Invalid post code.')
        return False
    if "english" in str(doujin.language):
        print(' > Valid Post! Language is English.')
        print('downloading!')

        doujin.download(hentaiID)
        return True
    else:
        print('> Valid Post but language is not English.')
        return False

x = int(input('Posts to find: '))
for i in range(0, x):
    postID += 1
    c = checkHentaiID(postID)
    if c:
        with open('post_ids.txt', 'a') as f:
            f.write(f'{postID}\n')
            
    sleep(0.1)

print('done lol')