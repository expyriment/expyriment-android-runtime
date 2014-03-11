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

(c) Oliver Lindemann, 2014

"""

from expyriment import design, control, stimuli, io, misc

control.set_develop_mode(True)

# settings and defaults
design.defaults.experiment_background_colour = misc.constants.C_GREY
design.defaults.experiment_foreground_colour = misc.constants.C_BLACK

exp = design.Experiment(name="bisecting judd")

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

def judd_stimulus(line_length, position, arrows,
                  line_width=3, heigth=60, gap=40):
    """Returns a Judd illusion stimulus.
    Line center is the stimulus canvas center.

    Parameters
    ----------
    line_length: integer
        the length of the line
    position: integer
        the position of the stimulus. Stimulus canvas center is also line
        center
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

    rtn = stimuli.Canvas(size=(line_length+2*gap, heigth), position=position)
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

### Start ###
control.start()

stim = judd_stimulus(line_length=300, position=(0,0), arrows=[True, False])
stim.present()
exp.keyboard.wait()

### End ###
control.end()
