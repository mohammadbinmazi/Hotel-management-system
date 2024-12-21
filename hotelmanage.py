from tkinter import*
from PIL import Image,ImageTk 
from customer import cust_win


class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1550x800+0+0")


         ######################  1st image  ########################
        
        img1=Image.open(r"C:\Users\HP\Desktop\hotel_management_mini_project_sem2_MCA\images\hotel.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)

        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

        #######################  logo  ########################
        
        img2=Image.open(r"C:\Users\HP\Desktop\hotel_management_mini_project_sem2_MCA\images\logo.webp")
        img2 = img2.resize((230, 140), Image.LANCZOS)

        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=180,height=140)

        #######################  title  ########################

    
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        

        ####################### Main frame ########################

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        ####################### menu ########################
        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        ####################### button frame ########################

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        ####################### customer button ########################

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

         ####################### room button ########################

        room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

         ####################### detail button ########################

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

         ####################### report button ########################

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

         ####################### logout button ########################

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

         ######################  right side image  ########################
        
        img3=Image.open(r"C:\Users\HP\Desktop\hotel_management_mini_project_sem2_MCA\images\rightimg.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)

        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg2=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg2.place(x=225,y=0,width=1100,height=450)
         ######################  Downside images  ########################
                                #    first
        
        img4=Image.open(r"C:\Users\HP\Desktop\hotel_management_mini_project_sem2_MCA\images\dinner.jpg")
        img4 = img4.resize((230,210), Image.LANCZOS)

        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=230)

    

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)





if __name__== "__main__":
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()