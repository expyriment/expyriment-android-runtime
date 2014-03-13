#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bisecting Judd illusion stimuli. An experiment for tablet PC or smartphone
using Expyriment and Expyriment Android Runtime (EAR)

see e.g.: Bruno N, Bernardis P, Gentilucci M (2008) Visually guided pointing,
    the Muller-Lyer illusion, and the functional interpretation of the
    dorsal-ventral split: conclusions from 33 independent studies.
    Neurosci Biobehav Rev 32:423–437. doi:10.1016/j.neubiorev.
    2007.08.006

(c) Oliver Lindemann & Florian Krause, 2014

"""
## TODO: requires 0.7.0+ (plus mouse_quit_events)

from expyriment import design, control, stimuli, io, misc
from expyriment.design.randomize import rand_int

control.set_develop_mode(True)

# settings and defaults
design.defaults.experiment_background_colour = misc.constants.C_GREY
design.defaults.experiment_foreground_colour = misc.constants.C_BLACK
stimulus_delay = 500

### Design ###
exp = design.Experiment(name="bisecting judd")
bl = design.Block()
for arrow in ["left", "right", "no"]:
    for length in [200, 300, 400]:
        tr = design.Trial()
        tr.set_factor("arrow", arrow)
        tr.set_factor("length", length)
        bl.add_trial(tr, copies=10)
bl.shuffle_trials()
exp.add_block(bl)

exp.data_variable_names = ["trial", "length", "arrow", "pos_x", "pos_y",
                "mark_x", "mark_y", "RT"]

### Initialize ####
control.initialize(exp)

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
blank.preload()

exp.mouse.show_cursor()
exp.mouse.mouse_quit_event = True
def judd_stimulus(line_length, arrows,
                  line_width=3, heigth=60, gap=40):
    """Returns a Judd illusion stimulus.
    Line center is the stimulus canvas center.
    Position will be randomliy selected.

    Parameters
    ----------
    line_length: integer
        the length of the line
    arrows: tuple of boolean
        boolean indicate the presence of arrows head at both side [left, right]
    line_width: integer, optional
        the line width
    height: integer, optional
        height of the stimulus
    gap: integer, optional
        the space at left and right side of line for the arrow heads and tails,
        large the gaps more angular are the arrow heads and tails

    """
    canvas_size = (line_length+2*gap, heigth)
    x_range = (-exp.screen.center_x + canvas_size[0]/2 + 10,
                exp.screen.center_x - canvas_size[0]/2 - 10)
    y_range = (-exp.screen.center_y + canvas_size[1]/2 + 10,
                exp.screen.center_y - canvas_size[1]/2 - 10)
    position = (rand_int(x_range[0], x_range[1]),
                rand_int(y_range[0], y_range[1]))
    rtn = stimuli.Canvas(size=canvas_size, position=position)
    line_ends = ((-line_length/2,0),(line_length/2,0))
    h2 = heigth/2
    arrow_ends = [[line_ends[0][0]-gap,  h2], [line_ends[1][0]+gap,  h2],
                  [line_ends[0][0]-gap, -h2], [line_ends[1][0]+gap, -h2]]
    if arrows[0]: # left
        arrow_ends[0][0] += 2*gap
        arrow_ends[2][0] += 2*gap
    if arrows[1]:
        arrow_ends[1][0] -= 2*gap
        arrow_ends[3][0] -= 2*gap
    stimuli.Line(start_point=arrow_ends[0], end_point=line_ends[0],
                line_width=line_width, anti_aliasing=10).plot(rtn)
    stimuli.Line(start_point=line_ends[1], end_point=arrow_ends[1],
                line_width=line_width, anti_aliasing=10).plot(rtn)
    stimuli.Line(start_point=line_ends[1], end_point=arrow_ends[3],
                line_width=line_width, anti_aliasing=10).plot(rtn)
    stimuli.Line(start_point=line_ends[0], end_point=arrow_ends[2],
                line_width=line_width, anti_aliasing=10).plot(rtn)
    stimuli.Line(start_point=line_ends[0], end_point=line_ends[1],
                line_width=line_width, anti_aliasing=10).plot(rtn)
    return rtn

def run_trial(trial, trial_cnt):
    blank.present()
    if trial.get_factor("arrow")=="left":
        arrows = [True, False]
    elif trial.get_factor("arrow")=="right":
        arrows = [False, True]
    else:
        arrows = [True, True]
    exp.clock.wait(stimulus_delay)
    stim = judd_stimulus(line_length=trial.get_factor("length"),
                            arrows=arrows)
    stim.present()
    exp.clock.reset_stopwatch()
    rect = stimuli.Rectangle(size=stim.size, position=stim.position)
    while True:
        btn_id, click_point, _rt = exp.mouse.wait_press()
        if btn_id is None:
            click_point = (-1, -1)
            break
        if rect.overlapping_with_position(click_point):
            break
    rt = exp.clock.stopwatch_time
    blank.present()
    exp.data.add([trial_cnt, trial.get_factor("length"),
            trial.get_factor("arrow"), stim.position[0], stim.position[1],
            click_point[0], click_point[1], rt])

### Start ###
control.start()

for cnt, trial in enumerate(exp.blocks[0].trials):
    run_trial(trial, cnt)

### End ###
control.end()
