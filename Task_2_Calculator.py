from tkinter import*

root=Tk()

root.title("Simple Calculator")

e = Entry(root, width=15, borderwidth=5, font=("Arial", 20), justify='right')
e.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10)


def button_click(number):

     # Deleting whatever in the box

    current=e.get()

    e.delete(0,END)

    e.insert(0,str(current)+str(number))
 
 
def button_clear():

    e.delete(0,END)

def operation(op):

    global f_num,math_op

    f_num=float(e.get())

    math_op=op

    e.delete(0,END)

def button_equal():

    global f_num,math_op

    second_number=float(e.get())

    e.delete(0,END)


    result=0

    if math_op=="+":

      result=f_num+second_number

    elif math_op=="-":

      result=f_num-second_number

    elif math_op=="*":

      result=f_num*second_number

    elif math_op=="/":

        if second_number!=0:

            result=f_num/second_number

        else:

            result="Can't divide"

    e.insert(0,result)

# Define Button
 
 
bttn_1=Button(root,text="1",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(1))

bttn_2=Button(root,text="2",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(2))

bttn_3=Button(root,text="3",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(3))

bttn_4=Button(root,text="4",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(4))

bttn_5=Button(root,text="5",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(5))

bttn_6=Button(root,text="6",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(6))

bttn_7=Button(root,text="7",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(7))

bttn_8=Button(root,text="8",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(8))

bttn_9=Button(root,text="9",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(9))

bttn_0=Button(root,text="0",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(0))

bttn_add=Button(root,text="+",padx=20,pady=20,font=("Arial",14),fg="dark orange",command=lambda:operation("+"))

bttn_sub=Button(root,text="-",padx=22,pady=20,font=("Arial",14),fg="dark orange",command=lambda:operation("-"))

bttn_mul=Button(root,text="*",padx=22,pady=20,font=("Arial",14),fg="dark orange",command=lambda:operation("*"))

bttn_div=Button(root,text="/",padx=23,pady=20,font=("Arial",14),fg="dark orange",command=lambda:operation("/"))

bttn_equal=Button(root,text="=",padx=20,pady=20,font=("Arial",14),bg="dark orange",fg="black",command=button_equal)

bttn_crear=Button(root,text="Clr",padx=16,pady=24,font=("Arial",13),fg="dark orange",command=button_clear)

# Putting button on Screen

bttn_1.grid(row=3,column=0)

bttn_2.grid(row=3,column=1)

bttn_3.grid(row=3,column=2)         

bttn_4.grid(row=2,column=0)

bttn_5.grid(row=2,column=1)

bttn_6.grid(row=2,column=2)

bttn_7.grid(row=1,column=0)

bttn_8.grid(row=1,column=1)

bttn_9.grid(row=1,column=2)

bttn_0.grid(row=4,column=0)

bttn_crear.grid(row=1,column=3)

bttn_add.grid(row=4,column=1)

bttn_sub.grid(row=4,column=2)

bttn_mul.grid(row=3,column=3)

bttn_div.grid(row=2,column=3)
 
bttn_equal.grid(row=4,column=3)
 

root.mainloop()
 