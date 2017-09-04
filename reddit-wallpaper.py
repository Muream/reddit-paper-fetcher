import os
from picture import Picture
import praw
import getopt
import sys

reddit = praw.Reddit(client_id='dz3EeHW-aZg1Tw',
                     client_secret='0R7LVkDDXqknnIlkPTgqqtWPI1k',
                     user_agent='wallpaper-reddit')

def get_wallpaper(subredditName='wallpapers', path='~/Pictures/reddit-wallpapers'):
    opts, args = getopt.getopt(sys.argv[1:], 's:p', ['subreddit=', 'path='])
    for opt, arg in opts:
        if opt in ('-s', '--subreddit'):
            subredditName = arg
        elif opt in ('-p', '--path'):
            path = arg

    if path.startswith('~'):
        path = os.path.expanduser(path)
    if not os.path.isdir(path):
        os.makedirs(path)

    subreddit = reddit.subreddit(subredditName)
    picture = get_first_valid_img(subreddit, path) 
    sys.exit(picture.path)

def get_first_valid_img(subreddit, path, limit=100):
    for index, post in enumerate(subreddit.hot(limit=limit)):
        url = post.url
        picture = Picture(url, path)
        if picture.is_valid:
            picture.publish()
            return picture
        else:
            if os.path.isfile(picture.path):
                os.remove(picture.path)

if __name__ == '__main__':
    get_wallpaper()
