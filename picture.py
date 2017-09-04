import os
from PIL import Image
import urllib.request

class Picture:

    SUPPORTED_WEBSITES = {'imgur': 'imgur', 'reddit': 'i.redd.it'}
    SCREEN_RESOLUTIONS = [(1920, 1080)]

    def __init__(self, url, directory):
        self.url = url
        self.directory = directory
        self.website = self._get_website()
        self.name = self._get_name()
        self.extension = self._get_extension()
        self.path = self._get_full_path()

        self.download()

        self.is_valid = self._is_valid()

    def _get_extension(self):
        """Get the picture extension from its name."""
        split = self.name.split('.')
        if len(split) > 1:
            return split[-1]

    def _get_name(self):
        """"Get the name from the URL."""
        split = self.url.split('/')
        if len(split) > 1:
            return split[-1]

    def _get_website(self):
        """Get the name of the website the picture is from."""
        for website, websiteUrl in self.SUPPORTED_WEBSITES.items():
            if websiteUrl in self.url:
                return website

    def _get_full_path(self):
        """Get the full path of the picture."""
        return os.path.join(self.directory, self.name)

    def _is_valid(self):
        """Check if the image fits all the criteria.

        for now we're only checking the resolution.
        """
        if os.path.isfile(self.path):
            img = Image.open(self.path)
            for resolution in self.SCREEN_RESOLUTIONS:
                x = img.size[0] / resolution[0]
                y = img.size[1] / resolution[1]
                if x == y:
                    return True

    def download_from_imgur(self):
        """Download the picture from imgur."""
        if self.extension:
            urllib.request.urlretrieve(self.url, self.path)

    def download_from_reddit(self):
        """Download the picture from reddit."""
        urllib.request.urlretrieve(self.url, self.path)

    def download(self):
        """Download the image from the provided url."""
        if self.website == 'imgur':
            self.download_from_imgur()
        if self.website == 'reddit':
            self.download_from_reddit()

    def publish(self):
        """converts the image to png and places it in the proper folder."""
        os.chdir(self.directory)
        if not os.path.isdir('old'):
            os.makedirs('old')
        for file in os.listdir(self.directory):
            if os.path.isfile(file):
                if not file == self.name:
                    os.rename(file, 'old/' + file)
