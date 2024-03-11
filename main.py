from tkinter import *

main_window = Tk()
main_window.title('Resume Interface Application')
main_window.geometry('600x600')
main_window.resizable(False, False)

frame1 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame1.place(x=0, y=0)

frame2 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame2.place(x=300, y=0)

frame3 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame3.place(x=0, y=200)

frame4 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame4.place(x=300, y=200)

frame5 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame5.place(x=0, y=400)

frame6 = Frame(main_window, highlightbackground="black", highlightthickness=3, width=300, height=200)
frame6.place(x=300, y=400)

lbl1 = Label(frame1, text='Personal Information', font=('Helvetica', 14))
lbl1.place(x=5, y=5)

lbl1a = Label(frame1, text='Name', font=('Helvetica', 11))
lbl1a.place(x=5, y=30)

ent1a = Entry(frame1)
ent1a.place(x=130, y=30)

lbl1b = Label(frame1, text='Current Address', font=('Helvetica', 11))
lbl1b.place(x=5, y=50)

ent1b = Entry(frame1)
ent1b.place(x=130, y=50)

lbl1c = Label(frame1, text='Telephone Number', font=('Helvetica', 10))
lbl1c.place(x=5, y=70)

ent1c = Entry(frame1)
ent1c.place(x=130, y=70)

lbl1d = Label(frame1, text='Email Address', font=('Helvetica', 11))
lbl1d.place(x=5, y=90)

ent1b = Entry(frame1)
ent1b.place(x=130, y=90)

lbl2 = Label(frame2, text='Objective', font=('Helvetica', 14))
lbl2.place(x=5, y=5)

lbl2a = Label(frame2, text='Short sentence of your goal \n for your job application', font=('Helvetica', 10))
lbl2a.place(x=5, y=30)

txt = Text(frame2, width=30, height=5)
txt.place(x=5, y=75)

lbl3 = Label(frame5, text='Technical Skills', font=('Helvetica', 14))
lbl3.place(x=5, y=5)

text1 = Text(frame5, width=30, height=7.5)
text1.place(x=5, y=30)

lbl3 = Label(frame3, text='Education', font=('Helvetica', 14))
lbl3.place(x=5, y=5)

lbl3a = Label(frame3, text='College/University Name', font=('Helvetica', 8))
lbl3a.place(x=5, y=30)

ent3a = Entry(frame3)
ent3a.place(x=130, y=30)

lbl3b = Label(frame3, text='School Address', font=('Helvetica', 11))
lbl3b.place(x=5, y=50)

ent3b = Entry(frame3)
ent3b.place(x=130, y=50)

lbl3c = Label(frame3, text='Date of Graduation', font=('Helvetica', 8))
lbl3c.place(x=5, y=70)

ent3c = Entry(frame3)
ent3c.place(x=130, y=70)

lbl3d = Label(frame3, text='Course/Program', font=('Helvetica', 11))
lbl3d.place(x=5, y=90)

ent3d = Entry(frame3)
ent3d.place(x=130, y=90)

lbl3e = Label(frame3, text='Certificates/Awards Attained', font=('Helvetica', 7))
lbl3e.place(x=5, y=110)

ent3e = Entry(frame3)
ent3e.place(x=130, y=110)

lbl4 = Label(frame4, text='Work and Related Experience', font=('Helvetica', 14))
lbl4.place(x=5, y=5)

lbl4a = Label(frame4, text='Job Name', font=('Helvetica', 11))
lbl4a.place(x=5, y=30)

ent4a = Entry(frame4)
ent4a.place(x=130, y=30)

lbl4b = Label(frame4, text='Company Name', font=('Helvetica', 11))
lbl4b.place(x=5, y=50)

ent4b = Entry(frame4)
ent4b.place(x=130, y=50)

lbl4c = Label(frame4, text='Inclusive Date/s', font=('Helvetica', 11))
lbl4c.place(x=5, y=70)

ent4c = Entry(frame4)
ent4c.place(x=130, y=70)

lbl4d = Label(frame4, text='Monthly Salary', font=('Helvetica', 11))
lbl4d.place(x=5, y=90)

ent4d = Entry(frame4)
ent4d.place(x=130, y=90)

lbl4e = Label(frame4, text='Reason for Leaving', font=('Helvetica', 10))
lbl4e.place(x=5, y=110)

ent4e = Entry(frame4)
ent4e.place(x=130, y=110)

lbl5 = Label(frame6, text='Character Reference, 3-5 People', font=('Helvetica', 13))
lbl5.place(x=5, y=5)

lbl5a = Label(frame6, text='Name', font=('Helvetica', 11))
lbl5a.place(x=5, y=30)

ent5a = Entry(frame6)
ent5a.place(x=130, y=30)

lbl5b = Label(frame6, text='Company', font=('Helvetica', 11))
lbl5b.place(x=5, y=50)

ent5b = Entry(frame6)
ent5b.place(x=130, y=50)

lbl5c = Label(frame6, text='Position', font=('Helvetica', 11))
lbl5c.place(x=5, y=70)

ent5c = Entry(frame6)
ent5c.place(x=130, y=70)

lbl5d = Label(frame6, text='Contact Number', font=('Helvetica', 11))
lbl5d.place(x=5, y=90)

ent5d = Entry(frame6)
ent5d.place(x=130, y=90)

main_window.mainloop()