from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
 
class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1200x500+200+200")

        #######################  title  ########################

    
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         #######################  logo  ########################
        
        img2=Image.open(r"C:\Users\HP\Desktop\hotel_management_mini_project_sem2_MCA\images\logo.webp")
        img2 = img2.resize((100, 50), Image.LANCZOS)

        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=2,y=1,width=100,height=50)

        ####################### label frame ########################

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer details",font=("times new roman",14,"bold"),padx=2)
        labelFrameleft.place(x=8,y=45,width=430,height=450)

         ####################### labels and entries ########################

        lub_cust_ref=Label(labelFrameleft,text=("Customer reference"),font=("times new roman",12,"bold"),padx=2,pady=6)
        lub_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelFrameleft,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)

        ####################### cust name ########################

        cname=Label(labelFrameleft,text=("Customer Name:"),font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

         ####################### mother name ########################

        cmname=Label(labelFrameleft,text=("mother name:"),font=("arial",12,"bold"),padx=2,pady=6)
        cmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)


        ####################### Gender ########################

        lab_gender=Label(labelFrameleft,text=("Gender:"),font=("arial",12,"bold"),padx=2,pady=6)
        lab_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelFrameleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        ####################### postcode ########################

        lblpostcode=Label(labelFrameleft,text=("Post code:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        txtpostcode=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtpostcode.grid(row=4,column=1)


        ####################### mobile number ########################

        lblnumber=Label(labelFrameleft,text=("Mobile number:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblnumber.grid(row=5,column=0,sticky=W)

        txtnumber=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtnumber.grid(row=5,column=1)

        ####################### email ########################

        lblemail=Label(labelFrameleft,text=("Email:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)

        ####################### nationality ########################

        lblnation=Label(labelFrameleft,text=("Nationality:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblnation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelFrameleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("india","US","germany","france","england","Others")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)


        ####################### id proof ########################

        lblidproof=Label(labelFrameleft,text=("ID proof:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelFrameleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Aadhar card","Voter id","Pan card","Passport","Others")
        combo_nation.current(0)
        combo_nation.grid(row=8,column=1)

         ####################### id number ########################

        lblidnumber=Label(labelFrameleft,text=("ID number:"),font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtidnumber=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtidnumber.grid(row=9,column=1)


        ####################### address ########################

        lbladdress=Label(labelFrameleft,text=("Address:"),font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtdaddress=ttk.Entry(labelFrameleft,width=29,font=("arial",13,"bold"))
        txtdaddress.grid(row=10,column=1)


        ####################### buttons ########################

        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=4,y=390,width=370,height=30)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        ####################### table frame ########################

        
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details And Search system",font=("times new roman",14,"bold"),padx=2)
        Table_frame.place(x=445,y=50,width=830,height=450)

        lblSearchby=Label(Table_frame,text=("Search bar:"),font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)

        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=13,state="readonly")
        combo_search["value"]=("Mobile number","ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        txtsearch=ttk.Entry(Table_frame,width=15,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(Table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShow.grid(row=0,column=4,padx=1)

        ####################### show data table ########################

        details_frame=Frame(Table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.cust_details_tables=ttk.Treeview(details_frame,columns=("ref","name","mother ","gender","post","mobile",
                                                                     "email","nationality","id proof","idnumbers","address",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)





if __name__ == "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()