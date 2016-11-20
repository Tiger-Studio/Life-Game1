def helpwindows():
    root = Tk()             #初始化Tk()
    root.title("help")
    root.geometry('500x220')#size
                
    filename = 'F:\\help2.gif'
    img = PhotoImage(file=filename)
    i = Label(root, image=img)
    i.pack(side=LEFT)
                
    frm = Frame(root)
                
    frm_T = Frame(frm)
    t1 = Label(frm_T, text="next:生成下一代", font=("Arial", 12), width=25, height=2)
    t1.pack(side=TOP)
    t2 = Label(frm_T, text="reset：重置", font=("Arial", 12), width=25, height=2)
    t2.pack(side=TOP)
    t3 = Label(frm_T, text="run：自动生成", font=("Arial", 12), width=25, height=2)
    t3.pack(side=TOP)
    t4 = Label(frm_T, text="stop：停止自动生成", font=("Arial", 12), width=25, height=2)
    t4.pack(side=TOP)
    frm_T.pack(side=TOP)
                
    frm_B = Frame(frm)
    b1 = Label(frm_T, text="Life Game Version 0.5", font=("Arial", 10), width=25, height=1)
    b1.pack(side=BOTTOM)
    b2 = Label(frm_B, text="Copyright(C)2016 Tiger Studio", font=("Arial", 9), width=25, height=1)
    b2.pack(side=BOTTOM)
    frm_B.pack(side=BOTTOM)
                                
    frm.pack()
    
    root.mainloop()