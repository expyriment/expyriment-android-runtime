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

    expyriment.stimuli.defaults.textline_text_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.stimuli.defaults.textbox_text_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.stimuli.defaults.textscreen_heading_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.stimuli.defaults.textscreen_text_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.io.defaults.textinput_message_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.io.defaults.textinput_user_text_font = \
            os.path.abspath("fonts/FreeMono.ttf")
    expyriment.io.defaults.menu_heading_font = \
            os.path.abspath("fonts/FreeSans.ttf")
    expyriment.io.defaults.menu_text_font = \
            os.path.abspath("fonts/FreeMono.ttf")

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
