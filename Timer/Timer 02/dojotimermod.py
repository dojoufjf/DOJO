#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DojoTimer - a simple timer for Coding Dojos.

Copyrights (C) 2008 Flávio Amieiro <amieiro.flavio@gmail.com>
SOUND ADDED BY 2011 Rafael Werneck <rafael.werneck@ice.ufjf.br>
EXTRA MODIFICATIONS BY 2011 Rafael Ribeiro <rafaelribeirodecarvalho@gmail.com>
              
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 dated June, 1991.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Library General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

If you find any bugs or have any suggestions email: <amieiro.flavio@gmail.com>, <rafael.werneck@ice.ufjf.br>, <rafaelribeirodecarvalho@gmail.com>.
"""

from Tkinter import *
import tkSimpleDialog
import tkSnack

class Clock(object):
    """
    Main class for the app.

    Takes as arguments to __init__:
    master: the parent window
    default_time: the desired default time

    """
    
    def __init__(self, master, default_time=1):
        
        # Create a frame
        self.frame = Frame(master)
        self.frame.pack()

        # Get the TopLevel window
        self.top = self.frame.winfo_toplevel()

        # Change some of it's attributes
        self.top.title("DojoTimer") # change the title
        self.top.attributes('-topmost', 1) # make it always on top
        self.top.resizable(0, 0) # make it unresizeable

        # A separate method is responsible for creating the other widgets
        self.__create_widgets()

        # Some default values
        self.running = False
        self.default_time = default_time # defaul time (in minutes)
        self.seconds = 60 * self.default_time
        self.labelstr.set(
            '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        )

    def __create_widgets(self):
        """ This function creates some widgets for the timer."""
        # self.labelstr is going to be used as text in the label
        # (which shows the time left). When this variable's value
        # is modified (with the method .set('str')) the label
        # changes on the fly.
        self.labelstr = StringVar()
        self.label = Label(
            self.frame,
            textvariable=self.labelstr,
            fg='#198931',
            font=('Helvetica', '48')
        )
        self.label.pack()

        # Some buttons
        self.start_btn = Button(self.frame, text="Start", command=self.start)
        self.start_btn.pack(side=LEFT)

        self.stop_btn = Button(self.frame, text='Pause', command=self.stop)
        self.stop_btn.pack(side=LEFT)

        self.reset_btn = Button(self.frame, text='Reset', command=self.reset)
        self.reset_btn.pack(side=LEFT)

        self.set_time_btn = Button(
            self.frame,
            text = 'Set time',
            command = self.set_time,
            )
        self.set_time_btn.pack(side=LEFT)

        self.quit_btn = Button(self.frame, text='Quit', command=self.frame.quit)
        self.quit_btn.pack(side=LEFT)

    def start(self):
        """
        Start the clock
        """
        end_sound.stop()
        little_time_sound.play_once = 1
        if not self.seconds:
            self.top.iconify()
            self.reset()
        if not self.running:
            self.top.iconify()
            self.running = True
            self.top.title("*DojoTimer*")
            self.update()

    def update(self):
        """
        Update the display
        """
        if self.running:
            if 0 < self.seconds <= 30:
                self.label['fg'] = '#efbf16'
                if little_time_sound.play_once == 1:
                    little_time_sound.play()
                    little_time_sound.play_once = 0
            elif self.seconds <= 0:
                self.top.deiconify()
                self.label['fg'] = '#d70505'
                end_sound.play()
                self.stop()
            new_str = '%02d:%02d' % ((self.seconds / 60), (self.seconds % 60))
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            self.top.title(self.labelstr.get())
            if self.seconds:
                self.seconds -= 1

    def stop(self):
        """
        Stop the clock
        """
        self.top.title("DojoTimer")
        self.running = False

    def reset(self):
        """
        Stop the clock and reset the time
        """
        end_sound.stop()
        self.stop()
        self.seconds = 60 * self.default_time
        self.label['fg'] = '#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)

    def set_time(self):
        """
        Gets user input from a dialog and updates
        self.default_time according to it
        """
        end_sound.stop()
        try:
            self.default_time = tkSimpleDialog.askfloat(
                'Set time',
                'Specify the time (in minutes)',
                parent=self.top
            )
            self.reset()
        except TypeError:
            pass

if __name__ == '__main__':
    root = Tk()
    rootSnack = Tk()
    
    tkSnack.initializeSnack(rootSnack)
    rootSnack.withdraw()
    
    end_sound = tkSnack.Sound()
    end_sound.read('despertador.mp3')
    little_time_sound = tkSnack.Sound()
    little_time_sound.read('final.wav')
    little_time_sound.play_once = 1
    
    clock = Clock(root, 5)
    root.mainloop()
