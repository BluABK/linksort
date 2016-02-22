import re
import ConfigParser


class Config:  # Shizu's config class # TODO: Add ConfigParser for writing changes to config.ini
    config = ConfigParser.RawConfigParser()

    def __init__(self):
        print "%s[%s]%s:\t Initiating config..." % (my_colour, my_name, clr.off)
        self.config.read('config.ini')

    def anime_basepath(self):
        return str(self.config.get('anime-airing', 'basepath'))


# Variables declared by config file
cfg = Config()


def get_anime_title(filename):
    r = re.match(r'^\[.*?\]\s(.*)\s-\s\d.*', filename)
    return r.group(1)


if __name__ == "__main__":
    anime_basepath = cfg.anime_basepath()
    testdata = [""]
    for file in testdata:
        print get_anime_title(file)
        print "mv ./%s $new_directory/" % file
        print "ln -s $new_directory/%s ./%s" % (file, file)