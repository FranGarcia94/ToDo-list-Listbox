#============================= To-Do list  =============================#
#                                                                       #
#                      To-Do list with listbox                          #
#                                                                       #
#                                                     @FranGarcia94     #
#=======================================================================#

from tkinter import *


def load_task():
    
    # Create the .txt file if it doesn't exist
    with open('task_list.txt', 'a+') as f:

        f.close()

    with open('task_list.txt', 'r', encoding = "utf-8") as f:

        txt_reader = f.readlines()

    txt_reader = [i[0:-1] for i in txt_reader] # Remove Newline Character
    
    [lb.insert(END, i) for i in txt_reader]


def add_fcn():

    lb.insert(END, enter_task.get())
    enter_task.delete(0,END)
    

def delete_task():

    for i in reversed(lb.curselection()):
        
        lb.delete(i)


def strike():

    for _, v in enumerate(reversed(lb.curselection())):

        task = lb.get(v)
        if task[-1] == u'\u2713':

            aux = task.split(u'\u0335')
            aux_2 = ''.join(aux).split('   ' + u'\u2713')
            
            lb.insert(v, ''.join(aux_2))
        else:
            
            strike_task = ''
            for j in task:

                strike_task += j + u'\u0335'

            strike_task += '   ' + u'\u2713' # Add check
            lb.insert(v, strike_task)
        
    delete_task()

    task_list = [lb.get(k) for k in lb.curselection()]

    if len(task_list) == 1 and task_list[0][-1] == u'\u2713':

        aux = task_list[0].split(u'\u0335')
        aux_2 = ''.join(aux).split('   ' + u'\u2713')
        
        lb.insert(lb.curselection(), ''.join(aux_2))
        delete_task()
    else:

        for task in reversed(task_list):

            strike_task = ''

            for j in task:

                strike_task += j + u'\u0335'

            strike_task += '   ' + u'\u2713' # Add check
            lb.insert(END, strike_task)
            
        delete_task()        
      

def close_gui():
    
    with open('task_list.txt', 'w', encoding = "utf-8") as f:

        for i in lb.get(0, END):

            f.write(i + '\n')

    
    root.destroy()


if __name__ == '__main__':

    def bind_fun(bind_btn):

        def enter_fun(e):

                bind_btn.config(bg = 'lightgreen')

        def leave_fun(e):

                bind_btn.config(bg = '#e1f0e5')
                
        bind_btn.bind('<Enter>', enter_fun)
        bind_btn.bind('<Leave>', leave_fun)

    def btn_style(btn_list: list):

        for i in btn_list:

            i.config(cursor = 'hand2', bg = '#e1f0e5', activebackground = 'green', activeforeground = 'black', font = ('Rockwell 12 bold'))
            bind_fun(i)


    root = Tk()
    root.title('To-Do List')
    # root.iconbitmap("tli.ico")
    root.protocol("WM_DELETE_WINDOW", close_gui)
    root.resizable(False,False)

    # ? ListBox
    lb = Listbox(root, state = 'normal', width = 50, highlightthickness = 3, highlightbackground = 'blue', font = ('Arial 12 bold'), selectmode = EXTENDED)
    lb.grid(row = 1, column = 0, columnspan = 2, sticky = 'nswe')
    lb.config(height = lb.size())

    # ? Entry
    enter_task = Entry(root, highlightthickness = 2, highlightbackground = 'orange')
    enter_task.grid(row = 0, column = 0, sticky = 'nswe')

    # ? Buttons
    add_button = Button(root, text = 'Add', command = add_fcn)
    add_button.grid(row = 0, column = 1, sticky = 'nswe')

    mf = Frame(root, bg = 'green')
    mf.rowconfigure(0, weight = 1)
    mf.columnconfigure(0, weight = 1)
    mf.columnconfigure(1, weight = 1)
    mf.grid(row = 2, column = 0, columnspan = 2, sticky = 'nswe')

    delete_button = Button(mf, text = 'Delete', command = delete_task)
    delete_button.grid(row = 0, column = 0, sticky = 'nswe')

    strikethrough_button = Button(mf, text = 'Strikethrough', command = strike)
    strikethrough_button.grid(row = 0, column = 1, sticky = 'nswe')

    btn_list = [add_button, delete_button, strikethrough_button]
    btn_style(btn_list)

    load_task()

    root.mainloop()