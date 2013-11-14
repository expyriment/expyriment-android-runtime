import os
import glob

import expyriment
import android


android.init()
android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

def main():
    projects = {}
    for folder in glob.glob("/mnt/*"):
        if os.path.isdir(folder):
            for project in glob.glob(folder + "/expyriment/*"):
                if os.path.isdir(project):
                    path = project + "/*.py"
                else:
                    path = folder + "expyriment/*.py"
                for pyfile in glob.glob(path):
                    projects[os.path.split(pyfile)[-1]] = pyfile

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
         'verasansmono', 'monotype', 'lucidaconsole', 'droidsansmono),
        ('sans', 'arial', 'helvetica', 'swiss', 'freesans',
         'bitstreamverasans', 'verasans', 'verdana', 'tahoma', 'droidsans),
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
    mouse = expyriment.io.Mouse(show_cursor=False)
    if projects == {}:
        info_box = expyriment.stimuli.TextScreen("No experiments found!",
"Please put your experiments into a folder called 'expyriment', " +
"located on the internal or external sdcard.\n\n" +
"[Touch the screen to exit]")
        info_box.present()
        mouse.wait_press()
    else:
        items = projects.keys()
        items.sort()
        menu = expyriment.io.TextMenu("Run experiment:", items, 320,
                                      scroll_menu=5, mouse=mouse)
        py_file = projects[menu.get()]
        expyriment.control.defaults.event_logging = 1
        os.chdir(os.path.split(py_file)[0])
        execfile("{0}".format(py_file))


if __name__ == "__main__":
    main()
