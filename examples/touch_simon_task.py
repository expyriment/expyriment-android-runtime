#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An experiment to assess a Simon effect with tablet PCs or smartphones using
Expyriment and Expyriment Android Runtime (EAR)

For Simon effect see e.g.: Simon, J. R. (1969). Reactions towards the source
of stimulation. Journal of experimental psychology, 81, 174-176.

(c) Oliver Lindemann, 2014

"""

## TODO: requires 0.7.0+ (plus touchscreen bugfix (commit 9a15d53)

from expyriment import design, control, stimuli, io, misc
from expyriment.design.randomize import rand_int

control.set_develop_mode(True)

# settings and defaults
design.defaults.experiment_background_colour = misc.constants.C_GREY
design.defaults.experiment_foreground_colour = misc.constants.C_BLACK

LEFT = "left"
RIGHT = "right"
GREEN = "green"
BLUE = "blue"
L4B = "left4blue"
L4G = "left4green"

# create design
exp = design.Experiment("Simon Task")
for mapping in [L4B, L4G]:
    b = design.Block()
    b.set_factor("Mapping", mapping)
    for position in [LEFT, RIGHT]:
        for colour in [BLUE, GREEN]:
            t = design.Trial()
            t.set_factor("Position", position)
            t.set_factor("Colour", colour)
            b.add_trial(t, copies=24)
    b.shuffle_trials()
    exp.add_block(b)
exp.add_bws_factor("OrderOfMapping", [1, 2])

exp.data_variable_names = ["trial", "Mapping", "Colour", "Position",
            "required", "Button", "RT", "correct"]

### Initialize ####
control.initialize(exp)

# timings and targets
fixcross_intervall = [600, 800]
error_feedback_time = 2000
target_intervall = [300, 500]
target_positions = ((-200, 0), (200, 0))

green_target = stimuli.Rectangle(size=(50,50), colour=misc.constants.C_GREEN)
blue_target = stimuli.Rectangle(size=(50,50), colour=misc.constants.C_BLUE)
target_frame = stimuli.Rectangle(size=(54, 54))

# buttons
btn_width = 100
buttons = [stimuli.Rectangle(size=(btn_width, exp.screen.size[1]),
                colour=misc.constants.C_DARKGREY,
                position=(-exp.screen.center_x + btn_width/2, 0)),
           stimuli.Rectangle(size=(btn_width, exp.screen.size[1]),
                colour=misc.constants.C_DARKGREY,
                position=(exp.screen.center_x - btn_width/2, 0))]

# standard stimuli
blank = stimuli.BlankScreen()
map(lambda x:x.plot(blank), buttons)
blank.preload()

fixcross = blank.copy()
stimuli.FixCross().plot(fixcross)
fixcross.preload()

exp.mouse.show_cursor()

# trial function
def run_trial(trial_cnt, trial, mapping):
    blank.present()

    # prepare trial
    exp.clock.reset_stopwatch()
    if trial.get_factor("Position")==LEFT:
        target_frame.position = target_positions[0]
    else:
        target_frame.position = target_positions[1]
    if trial.get_factor("Colour")==GREEN:
        green_target.plot(target_frame)
    else:
        blue_target.plot(target_frame)
    target_screen = io.TouchScreenButtonBox(button_fields=buttons,
                    stimuli=[target_frame, stimuli.FixCross()])
    target_screen.create()
    fixcross_time = rand_int(fixcross_intervall[0], fixcross_intervall[1])
    target_time = rand_int(target_intervall[0], target_intervall[1])
    exp.clock.wait(1000 - exp.clock.stopwatch_time)

    # present trial
    fixcross.present()
    exp.clock.wait(fixcross_time)
    target_screen.show()
    exp.clock.reset_stopwatch()
    button, _rt = target_screen.wait(duration=target_time)
    if button is None:
        fixcross.present()
        button, _rt = target_screen.wait()
    rt = exp.clock.stopwatch_time
    blank.present()

    # find required response
    if mapping==L4B:
        if trial.get_factor("Colour")==BLUE:
            required_response = LEFT
        else:
            required_response = RIGHT
    else: #left4green
        if trial.get_factor("Colour")==GREEN:
            required_response = LEFT
        else:
            required_response = RIGHT

    # process response
    if button==buttons[0]:
        button = LEFT
    else:
        button = RIGHT
    correct = int(button==required_response)
    if not(correct):
        error_screen = blank.copy()
        stimuli.TextLine(text="Incorrect response!",
                        text_colour=misc.constants.C_RED,
                        text_size=32).plot(error_screen)
        error_screen.present()
        exp.clock.wait(error_feedback_time)
    # save data
    exp.data.add([trial_cnt, mapping, trial.get_factor("Colour"),
                    trial.get_factor("Position"), required_response,
                    button, rt, correct])
    target_screen.destroy()

### Start ###
control.start()

if exp.get_permuted_bws_factor_condition("OrderOfMapping")==2:
    exp.swap_blocks(0,1)

for block in exp.blocks:
    stimuli.TextScreen("Instructions", block.get_factor("Mapping")).present()
    exp.keyboard.wait()

    # run block
    for cnt, trial in enumerate(block.trials):
        run_trial(cnt, trial, block.get_factor("Mapping"))

### End ###
control.end()
