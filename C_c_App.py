from tkinter import *
from tkinter import messagebox, simpledialog
import bcrypt

'''This method will display a screen requiring a user to sing up'''
def signUpUserForm():

    username = ''
    password = ''


    signupPage = Toplevel(page)
    signupPage.geometry('700x500')
    signupPage.title('Sign Up Here')
    Label(signupPage, text='Username ').pack()#pack organizes the widgets in a block manner
    Entry(signupPage, textvariable=username,  width=20).pack()
    Label(signupPage, text='Password* ').pack()
    Entry(signupPage, textvariable=password, show='*', width=20).pack()
    signupPage.configure(background='darkgreen')
    Button(signupPage, text='  ').pack()

    Button(signupPage,text='Save', fg='green', bg='gray', height='4', width='30', command=signUpUser).pack()

    Button(text='Sing Up', fg='green', bg='gray', height='4', width='9').pack()

'''Creates a table with details of when and ages of children to take care of.'''

def creatTable1():
    tbl = Toplevel(page)
    tbl.geometry('980x500')
    tbl.title('Ages Shift With Weeks( Week two,care for  2 years old, etc...)')
    tbl.configure(background='tan')
    for i in range(6):
        for j in range(7):
            frm=Frame(
                master=tbl,relief=RAISED,
                borderwidth=5
            )
            frm.grid(row=i, column=j, padx=6,pady=7)
            label =Label(master=frm, bg='purple', text=f'{i+1} Year(s) old \nDay {j+1}\n week {i+1}' ,  fg='yellow')
            label.pack(padx=7, pady=8)
'''Creates a table for daily activity'''

def planner():
    pln = Toplevel(page)
    pln.geometry('800x100')
    pln.title('Daily Activities ')
    pln.configure(background='cyan')
    for i in range(1):
        for j in range(4):
            frm = Frame(
                master=pln, relief=RAISED,
                borderwidth=5
            )
            frm.grid(row=i, column=j, padx=6, pady=7)
            label = Label(master=frm, bg='green', text=f'Play and then eat  \n Naps {j+1} hour', fg='white')
            label.pack(padx=7, pady=8)

            '''Dispay dialog box indicating a call is being made.'''

def contactingViaPhone():
    messagebox.showinfo("Calling Parents", "CALLING PARENTS...")

def text():
    messagebox.showinfo("Text", "Begin Texting...")

''' Two buttons are created one calls when pressed and the other for texting parents'''
def callParents():

    parnt=Toplevel(page)
    parnt.geometry('330x330')
    parnt.title('Contact Parents Of Child Via Call Or Text')
    parnt.configure(background='tan')
    Button(parnt, text='CALL PARENTS', fg='green', bg='gray', height='10', width='23',command=contactingViaPhone).pack()

    Button(parnt, text='TEXT PARENTS', fg='green', bg='gray', height='10', width='23', command=text).pack()

def careGiverReport():#the user will be prompt to enter a string
    page.withdraw()
    input_Details = simpledialog.askstring(title='Care Report', prompt='Any changes with health, YES or NO: ')
    '''Shows the info about the parents, in a dialog box'''
def parentsContacts():

    messagebox.showinfo('Parents Contacts',' Father: John Kennedy \n Mother: Mary Jane \nAddress: 212 EastLane st, Ave \n Home Phone: 555-5555-555')

''' The user will be prompt to enter a string'''

def behavAlReport():
    page.withdraw()
    input_Details=simpledialog.askstring(title='Behavioral Report', prompt='Type dominant mood today: ')

    '''After the user saves the credentials, him or her will be directed to a page with the menu below '''

def signUpUser():

    user = Toplevel(page)
    user.geometry('700x590')
    user.title('HOME')
    user.configure(background='green')
    Button(user, text='Today Schedule', fg='green', bg='green', height='4', width='30',command=creatTable1).pack()
    Button(user, text='Planned Activities', fg='green', bg='gray', height='6', width='100',command=planner).pack()
    Button(user, text='Behavioral Report', fg='black', bg='yellow', height='6', width='100',command=behavAlReport).pack()
    Button(user, text='Parents Contacts', fg='blue', bg='blue', height='6', width='100', command=parentsContacts).pack()
    Button(user, text='Alert Parents', fg='red', bg='red', height='6', width='100', command=callParents).pack()
    Button(user, text='Care Giver Report', fg='green', bg='gray', height='6', width='100', command=careGiverReport).pack()
    messagebox.showinfo("PASSWORD CREATED", "CHECK YOUR EMAIL TO CONFIRM YOUR IDENTITY.")

    '''Here the verification of password will take place, 
    verifying that the entered password is the same as the one stored in the database
    if it fails, the error dialogue appears.'''

def loggedIntoAccount():

    stordPwrd = b'mypass'  # stored password
    pwrd = b'mypass'  # the entered password

    hashdPasswrd = bcrypt.hashpw(pwrd, bcrypt.gensalt())  # hashing the password
    verifyPasswrd = bcrypt.checkpw(stordPwrd, hashdPasswrd) #comparing stored hashed passwrd to the input
    login = Toplevel(page)

    login.title('Logged In')
    login.configure(background='green')

    if verifyPasswrd:

        login.geometry('700x590')
        login.configure(background='green')
        Button(login, text='Today Schedule', fg='green', bg='green', height='4', width='30', command=creatTable1).pack()
        Button(login, text='Planned Activities', fg='green', bg='gray', height='6', width='100', command=planner).pack()
        Button(login, text='Behavioral Report', fg='black', bg='yellow', height='6', width='100',command=behavAlReport).pack()
        Button(login, text='Parents Contacts', fg='blue', bg='blue', height='6', width='100', command=parentsContacts).pack()
        Button(login, text='Alert Parents', fg='red', bg='red', height='6', width='100', command=callParents).pack()
        Button(login, text='Care Giver Report', fg='green', bg='gray', height='6', width='100', command=careGiverReport).pack()
        messagebox.showinfo('LOGGED IN',"The password 'mypass' was hashed, using bcrypt library, on line 99 of this source code , click Ok to continue.")
    else:
        messagebox.showinfo("Error!", "Invalid credentials")
'''Will dispay a dialog box to tell the user the next action'''

def forgotPass():
    messagebox.showinfo("RESET PASSWORD", "CHECK YOUR EMAIL TO RESET THE PASSWORD!")

'''This method will display the very first page or screen when this program starts running'''

def startIntake():

    global page# declared globally to be available to every function
    page = Tk()# creates tkinter screen
    page.geometry('600x490')
    page.title('WELCOME To ChildCare')
    Label(text='WELCOME To ChildCare', bg='white', font=('Calibri', 25), width='250', height='7').pack()
    Button(text='Login ', fg='green', bg='gray', width='30', height='4', command=loggedIntoAccount).pack()
    Button(text='  ').pack()
    Button(text='Sing Up', fg='green', bg='gray', height='4', width='30', command=signUpUserForm).pack()
    Button(text='  ').pack()
    Button(text='Forgot Passward', fg='green', bg='gray', height='4', width='30',command=forgotPass).pack()# button created, and inside the command will take place when clicked

    page.configure(background='green')




    page.mainloop()


startIntake()

