from tkinter import *
from functools import partial
import re
#import random

class Game:
    def __init__(self,partner, stakes, starting_balance):

        print(stakes)
        print(starting_balance)
        partner.lowstakes_button.config(state=DISABLED)
        
        #disable low stakes button
        background_color = "light blue"

        #initialise vaiables
        self.balance = IntVar()

##        #converter frame
##        self.converter_frame = Frame(width=300, bg=background_color,
##                                     pady=10)
##        self.converter_frame.grid()
##
##        #temperature converter heading
##        self.temp_heading_label = Label(self.converter_frame,
##                                        text = "Temperature Converter",
##                                            font="Arial 16 bold",
##                                            bg=background_color,
##                                            padx=10, pady=10)
##        self.temp_heading_label.grid(row=0)
##
##        #user instructions
##        self.temp_instructions_label = Label(self.converter_frame,
##                                             text = "Type in the amount to be "
##                                                     "converted and then push "
##                                                     "one of the buttons below...",
##                                                     font="Arial 10 italic", wrap=250,
##                                                     justify=LEFT, bg=background_color,
##                                                     padx=10, pady=10)
##        self.temp_instructions_label.grid(row=1)
##
##        #temperature entry box
##        self.to_convert_entry = Entry(self.converter_frame, width=20,
##                                      font="Arial 14 bold")
##        self.to_convert_entry.grid(row=2)
##
##        #conversion buttons frame
##        self.conversion_buttons_frame = Frame(self.converter_frame)
##        self.conversion_buttons_frame.grid(row=3, pady=10)
##
##        self.to_c_button = Button(self.conversion_buttons_frame,
##                                  text="To Centigrade", font="Arial 10 bold",
##                                  bg="Khaki1", padx=10, pady=10,
##                                  command=lambda: self.temp_convert(-459))
##        self.to_c_button.grid(row=0, column=0)
##
##        self.to_f_button = Button(self.conversion_buttons_frame,
##                                  text="To Fahrenheit", font="Arial 10 bold",
##                                  bg="Orchid1", padx=10, pady=10,
##                                  command=lambda: self.temp_convert(-273))
##        self.to_f_button.grid(row=0, column=1)
##
##        #answer label
##        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
##                                     fg = "purple", bg=background_color,
##                                     pady=10, text="Conversion goes here")
##        self.converted_label.grid(row=4)
##
##        #history / help button frame (row 5)
##        self.hist_help_frame = Frame(self.converter_frame)
##        self.hist_help_frame.grid(row=5, pady=10)
##
##        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
##                                     text="Calculation History", width=15,
##                                     command=lambda: self.history(self.all_calc_list))
##        self.history_button.grid(row=0, column=0)
##
##        
##
##        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
##                                  text="Help", width=5, command=self.help)
##        self.help_button.grid(row=0, column=1)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
