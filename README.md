# Reddit Paper Fetcher

This simple script's goal is to download the 1st image in a given subreddit
to then be used by the tool of your choice to be set as a wallpaper

## Setup

You will need python 3 installed
I recommend creating a virtual environment for the script but hey, I'm not your mother. :)
Clone the repo wherever you want, cd into it and then do `pip install -r requirements.txt`

## How to use it.

call the reddit-wallpaper.py with these optional arguments:
- --subreddit=subredditName             | defaults to "wallpapers"
- --path=/path/to/save/the/wallpaper    | defaults to "~/Pictures/reddit-wallpaper/"

This will download the 1st image of /r/subredditName/hot

The script writes the path of the download image in stderr when it ends so you can use it in a bash script like so:

This is how I personally use it:

```bash
while true
do
    WALLPAPER=$(python /path/to/reddit-wallpaper.py 2>&1)
    feh --bg-scale $WALLPAPER
    sleep 60
done
```

this script is called every-time I start my window manager and runs in the background.

### Note
> For now the script will only download images that match a 16:9 ratio.
> I will add an additional command line argument to add different allowed aspect ratios and maybe flatout ignore the aspect ratio if the argument isn't specified

### Note 2
> For now, this works only with i.redd.it and imgur direct links to images (links with the extension in the adress).
> I will add more supported websites based on feedback.

I have only tested this on linux but it should work on mac and windows as well, as long as you find a way to automate how the wallpaper will be set.


If you have any feedback, please go on!
