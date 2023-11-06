from tkinter import*
from PIL import Image, ImageTk
class IMS:
    def __init__ (self,root):
        self.root=root
        self.root.geometry=("1350*700+0+0")
        self.root.title("Shopping Managment System  | Developed by Team 3")
        self.root.config(bg='white')
        #===Title===#
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Shopping Managment System",image=self.icon_title,compound=LEFT,font=('times new roman',40,"bold"),bg="#010c48",fg='white').place(x=0,y=0,relwidth=1,height=70)

        #===btnLogout===#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,'bold'),bg="yellow",cursor='hand2').place(x=1350,y=10,height=30,width=150)
        #===clock===#
        self.lbl_clock=Label(self.root,text="Welcome to Shopping Managment System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=('times new roman',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        

        #===Left Menu===#
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.BOX)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=9,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file='images/side.png')
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        
        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)     
        btn_supplier=Button(LeftMenu,text="Supplier",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)     
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)           
        btn_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)           
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)           
        btn_exit=Button(LeftMenu,text="exit",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("times new roman",20, 'bold'),bg="white",bd=3,cursor='hand2').pack(side=TOP,fill=X)   
        
        
        
 
