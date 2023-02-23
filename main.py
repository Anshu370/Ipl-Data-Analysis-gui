from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as sql



'''GUI SECTION'''

gui = Tk()
gui.title('IPL DATA ANALYSIS PROJECT')
gui.geometry('500x500') # width x height
gui.minsize(1530, 810) # width , height
gui.maxsize(2000, 1500) # width , height



# Heading frame

frame_head = Frame(gui, bg="blue", borderwidth=9, relief=SUNKEN)
frame_head.pack(fill="x")

label_head = Label(frame_head, text="TATA IPL DATA ANALYSIS", font="Algerian 25 italic", bg="blue", fg="white")
label_head.pack(pady=3)

# Bottom frame

frame_bottom = Frame(gui, bg="lightblue3", borderwidth=7, relief=RIDGE)
frame_bottom.pack(side='bottom', fill="y")

# Left side UP frame

frame_left_up = Frame(gui, bg="black", borderwidth=7, relief=RIDGE)
frame_left_up.pack(fill=Y, side=LEFT)

# Workspace frame

frame_workspace = Frame(gui, bg="lightblue2", borderwidth=7, relief=RIDGE)
canvas_b_workspace = Canvas(frame_workspace, width=1125, height=480, scrollregion=(0, 0, 500, 500))

frame_workspace.pack(anchor=NE, fill=BOTH, expand=True)

work_label = Label(frame_workspace, text="Workspace", bg="lightblue2", fg="blue", font="Algerian 25 italic")
work_label.pack()

# bottom frame labels textbox and buttons

label1 = Label(frame_bottom, text="ADD DETAILS", bg="lightblue3", font="Aparajita 15 bold")
label1.grid(row=1, column=1, pady=1.5)

label2 = Label(frame_bottom, text="FIND DATA USING NAME", bg="lightblue3", font="Aparajita 15 bold")
label2.grid(row=2, column=1, pady=1.5, padx=2)

label3 = Label(frame_bottom, text="RESULT", bg="lightblue3", font="Aparajita 15 bold")
label3.grid(row=3, column=1, pady=2)

label4 = Label(frame_bottom, text="NAME", bg="lightblue3", font="Aparajita 15 bold")
label4.grid(row=0, column=2, pady=1.5)

label5 = Label(frame_bottom, text="ROLL", bg="lightblue3", font="Aparajita 15 bold")
label5.grid(row=0, column=3, pady=1.5)

label6 = Label(frame_bottom, text="TEAM", bg="lightblue3", font="Aparajita 15 bold")
label6.grid(row=0, column=4, pady=1.5)

label7 = Label(frame_bottom, text="MATCHES PLAYED", bg="lightblue3", font="Aparajita 15 bold")
label7.grid(row=0, column=5, pady=1.5)

label8 = Label(frame_bottom, text="RUNS & WICKETS", bg="lightblue3", font="Aparajita 15 bold")
label8.grid(row=0, column=6, pady=1.5)

'''ADD details'''
name_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
team_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
matches_played_entry = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")
runs_wicket_entry = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")

name_entry.grid(row=1, column=2, padx=2)
roll_entry.grid(row=1, column=3, padx=2)
team_entry.grid(row=1, column=4, padx=2)
matches_played_entry.grid(row=1, column=5, padx=2)
runs_wicket_entry.grid(row=1, column=6, padx=2)

'''Find data'''
name_entry2 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry2 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")

name_entry2.grid(row=2, column=2, padx=2)
roll_entry2.grid(row=2, column=3, padx=2)

'''RESULT'''
name_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
team_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
matches_played_entry3 = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")
runs_wicket_entry3 = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")

name_entry3.grid(row=3, column=2, padx=2, pady=2.5)
roll_entry3.grid(row=3, column=3, padx=2, pady=2.5)
team_entry3.grid(row=3, column=4, padx=2, pady=2.5)
matches_played_entry3.grid(row=3, column=5, padx=2, pady=2.5)
runs_wicket_entry3.grid(row=3, column=6, padx=2, pady=2.5)

# Function




# Buttons of left side

button_1 = Button(frame_left_up, text="                   Teams of IPL                 ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_2 = Button(frame_left_up, text="           MOST RUNS SCORED         ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_3 = Button(frame_left_up, text="          MOST WICKET TAKERS       ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_4 = Button(frame_left_up, text="        MOST SIXES BY PLAYER        ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_5 = Button(frame_left_up, text="               MOST HATRICKS             ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_6 = Button(frame_left_up, text="SINGLE ACHIEVEMENTS RECORD", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_7 = Button(frame_left_up, text="          INDIVIDUAL RECORDS        ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1")
button_graph = Button(frame_left_up, text="           GRAPHS & CHARTS            ", font="Cavolini 13 italic",
                      borderwidth=5, relief=RAISED,  bg="yellow1")

button_1.pack(pady=6, padx=8)
button_2.pack(pady=6, padx=8)
button_3.pack(pady=6, padx=8)
button_4.pack(pady=6, padx=8)
button_5.pack(pady=6, padx=8)
button_6.pack(pady=6, padx=8)
button_7.pack(pady=6, padx=8)
button_graph.pack(pady=6, padx=8)

# Left side Bottom frame


gui.mainloop()
