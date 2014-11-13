import sys
import os
import glob
from importlib import import_module

import pygame
import expyriment
import android

def find_keyword_files(folder):
    """find all files with keywords in folder and subfolders

    Returns dict of files
    """

    keywords = ["expyriment", "initialize("]
    rtn = {}
    for entry in glob.glob(folder+"/*"):
        if os.path.isdir(entry):
            rtn.update(find_keyword_files(entry))
        elif entry.endswith(".py") and not \
                                os.path.split(entry)[1].startswith("_"):
            try:
                with open(entry) as fl:
                    lines = fl.readlines()
            except:
                lines = ""
            all_keywords_found = True
            for key in keywords:
                if not check_keyword(lines, key):
                    all_keywords_found = False
                    break
            if all_keywords_found:
                rtn[os.path.split(entry)[-1][:-3]] = entry
    return rtn

def check_keyword(lines, keyword):
    """check if keyword occurs in text lines"""
    for l in lines:
        if l.find(keyword)>=0:
            return True
    return False

def launch_experiment(script, name):
        expyriment.stimuli.TextScreen(heading="Starting {0}".format(name),
                        "").present()
        expyriment.misc.Clock().wait(1000)
        expyriment.control.defaults.event_logging = 1
        expyriment.control.defaults.initialize_delay = 0
        script = os.path.abspath(script)
        path, pyfile = os.path.split(script)
        os.chdir(path)
        sys.argv[0] = pyfile
        import_module(os.path.splitext(pyfile)[0])

def main():
    android.init()

    projects = {}
    for folder in glob.glob("/mnt/*"):
        if os.path.isdir(folder):
            projects.update(find_keyword_files(folder + "/expyriment")

    pygame.font.init()
    for font in glob.glob("/system/fonts/*"):
        if font[-4:].lower() in ['.ttf', '.ttc']:
            font = unicode(font)
            name = os.path.split(font)[1]
            bold = name.find('Bold') >= 0
            italic = name.find('Italic') >= 0
            oblique = name.find('Oblique') >= 0
            name = name.replace(".ttf", "")
            if name.endswith("Regular"):
                name = name.replace("Regular", "")
            if name.endswith("Bold"):
                name = name.replace("Bold", "")
            if name.endswith("Italic"):
                name = name.replace("Italic", "")
            if name.endswith("Oblique"):
                name = name.replace("Oblique", "")
            name = ''.join([c.lower() for c in name if c.isalnum()])
            pygame.sysfont._addfont(name, bold, italic or oblique, font,
                                    pygame.sysfont.Sysfonts)

    aliases = (
        ('monospace', 'misc-fixed', 'courier', 'couriernew', 'console',
         'fixed', 'mono', 'freemono', 'bitstreamverasansmono',
         'verasansmono', 'monotype', 'lucidaconsole', 'droidsansmono'),
        ('sans', 'arial', 'helvetica', 'swiss', 'freesans',
         'bitstreamverasans', 'verasans', 'verdana', 'tahoma', 'droidsans'),
        ('serif', 'times', 'freeserif', 'bitstreamveraserif', 'roman',
         'timesroman', 'timesnewroman', 'dutch', 'veraserif',
         'georgia', 'droidserif'),
    )
    for set in aliases:
        found = None
        fname = None
        for name in set:
            if name in pygame.sysfont.Sysfonts:
                found = pygame.sysfont.Sysfonts[name]
                fname = name
                break
        if not found:
            continue
        for name in set:
            if name not in pygame.sysfont.Sysfonts:
                pygame.sysfont.Sysalias[name] = found

    expyriment.control.defaults.event_logging = 0
    exp = expyriment.control.initialize()
    if projects == {}:
        info_box = expyriment.stimuli.TextScreen("No experiments found!",
            "Please put your experiments into a folder called 'expyriment', " +
            "located on the internal or external SDcard.\n\n" +
            "[Touch the screen to exit]")
        info_box.present()
        exp.mouse.wait_press()
    elif len(projects)==1: # started immediately  if no choice
        launch_experiment(projects.values()[0], projects.keys()[0])
    else:
        items = projects.keys()
        items.sort()
        menu = expyriment.io.TextMenu("Run experiment:", items, 320,
                                      scroll_menu=5, mouse=exp.mouse)
        select = menu.get()
        launch_experiment(projects[select], select)


if __name__ == "__main__":
    main()
