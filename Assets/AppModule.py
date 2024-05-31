from customtkinter import *
from CTkListbox import *

class app(CTk):
    def __init__(self, title, size):
        super().__init__()
        #Startup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])
        set_appearance_mode("dark")
        #Widgets
        self.menu = Menu(self)
        self.menu.createWidgets()
        self.menu.placeWidgets()
        #Run
        self.mainloop()

class Menu(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        CTkLabel(self, bg_color="#355723", text="").pack(expand= True, fill= "both")
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.topLevelFindRecipe = None
        self.topLevelAddRecipe = None
    
    def windowOpenAddRecipe(self):
        if self.topLevelAddRecipe is None or not self.topLevelAddRecipe.winfo_exists():
            self.topLevelAddRecipe = topLevelWindowAddRecipe(self)
            self.topLevelAddRecipe.addRecipeWindowAttributes1()
            self.topLevelAddRecipe.placeRecipeWindowAttributes1()
        else:
            self.topLevelAddRecipe.focus()
    
    def windowOpenFindRecipe(self):
        if self.topLevelFindRecipe is None or not self.topLevelFindRecipe.winfo_exists():
            self.topLevelFindRecipe = topLevelWindowFindRecipe(self)
            self.topLevelFindRecipe.addRecipeWindowAttributes2()
            self.topLevelFindRecipe.placeRecipeWindowAttributes2()
        else:
            self.topLevelFindRecipe.focus()
        
    def createWidgets(self):
        self.lblTitle = CTkLabel(self, corner_radius=16, fg_color="#CBE8BA", bg_color="#355723", text="Cooklet\nPro", text_color="#631878", font=("BioRhyme", 25))
        self.btnAddRecipe = CTkButton(self, corner_radius=16, border_width=2, fg_color="#FAD2E0", bg_color="#355723", border_color="white", text="Add\nRecipe", text_color="black", font=("Georgia", 24), command=self.windowOpenAddRecipe)
        self.btnFindRecipe = CTkButton(self, corner_radius=16, border_width=2, fg_color="#FAD2E0", bg_color="#355723", border_color="white", text="Find\nRecipe", text_color="black", font=("Georgia", 24), command=self.windowOpenFindRecipe)
    
    def placeWidgets(self):
        self.lblTitle.place(x=30, y=20)
        self.btnAddRecipe.place(x=20, y=160)
        self.btnFindRecipe.place(x=20, y=330)
    


class topLevelWindowAddRecipe(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Recipe")
        self.geometry("600x500")
        self.minsize(600, 500)
        self.maxsize(600, 500)
    
    def addRecipeWindowAttributes1(self):
        CTkLabel(self, bg_color="#355723", text="").pack(expand= True, fill= "both")
        self.lblAddRecipeTitle = CTkLabel(self, corner_radius= 16, bg_color="#355723", fg_color="#FAD2E0", text="Add Recipe", text_color="black", font=("Georgia", 24))
        self.btnEnterRecipe = CTkButton(self, corner_radius=32, border_width=2, bg_color="#355723", fg_color="#FAD2E0", border_color="white", text_color="black", text="Save", font=("Georgia", 20), command=self.getAddRecipeVariables)
        self.btnExit1 = CTkButton(self, corner_radius=16, fg_color="#CBE8BA", bg_color="#355723", text="Cooklet\nPro", text_color="#631878", font=("BioRhyme", 25), command=self.destroy)
        #Name
        self.lblEnterRecipeName = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#355723", text="Name:", text_color="#FAD2E0", font=("Georgia", 20))
        self.entryEnterRecipeName = CTkEntry(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", text_color="black")
        #Servings
        self.lblEnterServings = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#355723", text="Servings:", text_color="#FAD2E0", font=("Georgia", 20))
        self.entryEnterServings = CTkEntry(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=70, text_color="black")
        #Ingredients
        self.lblIngredients = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#355723", text="Ingredients:", text_color="#FAD2E0", font=("Georgia", 20))
        self.txtboxIngredients = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=150, height=220, text_color="black")
        #Ingredient amount
        self.lblIngredientMeasurement = CTkLabel(self, corner_radius=32, bg_color="#355723", fg_color="#355723", text="Amount:", text_color="#FAD2E0", font=("Georgia", 20))
        self.txtboxIngredientMeasurement = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=110, height=220, text_color="black")
        #Method
        self.lblMethod = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#355723", text="Method:", text_color="#FAD2E0", font=("Georgia", 20))
        self.txtboxMethod = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=220, height=220, text_color="black")

    def placeRecipeWindowAttributes1(self):
        self.lblAddRecipeTitle.place(x=230, y=20)
        self.btnEnterRecipe.place(x=230, y=450)
        self.btnExit1.place(x=13, y=10)
        #Name
        self.lblEnterRecipeName.place(x=60, y=100)
        self.entryEnterRecipeName.place(x=135, y=100)
        #Servings
        self.lblEnterServings.place(x=350, y=100)
        self.entryEnterServings.place(x=450, y=100)
        #Ingredients
        self.lblIngredients.place(x=45, y=150)
        self.txtboxIngredients.place(x=40, y=200)
        #IngredientMeasurement
        self.lblIngredientMeasurement.place(x=200, y=150)
        self.txtboxIngredientMeasurement.place(x=200, y=200)
        #Method
        self.lblMethod.place(x=390, y=150)
        self.txtboxMethod.place(x=340, y=200)
    
    def placeAddRecipeVariables(self, recipeName, servingSize, ingredients, ingredientMeasurement, method):
        from tkinter import messagebox
        self.recipeName = recipeName
        self.servingSize = servingSize
        self.ingredients = ingredients
        self.ingredientMeasurement = ingredientMeasurement
        self.method = method


        listVarAddRecipe = {"recipeName": recipeName, "servingSize": servingSize, "ingredients": ingredients, "ingredientMeasurement": ingredientMeasurement, "method": method}

        try:
            import os 

            if servingSize <= 0:
                raise Exception("error")

            path = os.path.join(self.recipeName)
            os.mkdir(path)
            print("Directory '% s' created " % f"{self.recipeName}")
            os.replace(f"{self.recipeName}", f"Recipe Storage/{self.recipeName}")
           
            for step in listVarAddRecipe:
                with open(f"{step}.txt", "w") as fileAddRecipe:
                    print(f"{listVarAddRecipe[step]}", file=fileAddRecipe)
                os.replace(f"{step}.txt", f"Recipe Storage/{self.recipeName}/{step}.txt")

            self.destroy()
        except:
            messagebox.showerror("Input Error", "Input Error!")
    
    def getAddRecipeVariables(self):
        try:
            self.placeAddRecipeVariables(self.entryEnterRecipeName.get(), int(self.entryEnterServings.get()), self.txtboxIngredients.get("1.0", "end-1c"), self.txtboxIngredientMeasurement.get("1.0", "end-1c"), self.txtboxMethod.get("1.0", "end-1c"))
        except:
            print("ERROR")
        
class topLevelWindowFindRecipe(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Find Recipe")
        self.geometry("600x500")
        self.minsize(600, 500)
        self.maxsize(600, 500)
        self.topLevelViewRecipe = None
        
    def listUpdate(self):
        x = 0
        for directory in os.listdir("Recipe Storage"):
            self.listBoxFindRecipe.delete(x)
            x += 1
        x = 0
        for directory2 in os.listdir("Recipe Storage"):
            if self.entryFindRecipeSearchBar.get() in directory2.lower():
                self.listBoxFindRecipe.insert(x, directory2)
            x += 1

    def listGet(self, num):
        try:
            self.entryFindRecipeSearchBar.delete(0, END)
            self.entryFindRecipeSearchBar.insert(index=0, string=f"{num}")
        except:
            print("ERROR")
    
    def delOption(self):
        directory = self.listBoxFindRecipe.get()
        for file in os.listdir(f"Recipe Storage/{directory}"):
            os.remove(f"Recipe Storage/{directory}/{file}")
        os.rmdir(f"Recipe Storage/{directory}")
        self.listUpdate()

    def addRecipeWindowAttributes2(self):
        CTkLabel(self, bg_color="#355723", text="").pack(expand= True, fill= "both")
        self.lblFindRecipeTitle = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#FAD2E0", text="Find Recipe", text_color="black", font=("Georgia", 24))
        self.btnViewRecipe2 = CTkButton(self, corner_radius=32, border_width=2, bg_color="#355723", fg_color="#FAD2E0", border_color="white", text="View", text_color="black", font=("Georgia", 20), command=lambda: self.windowOpenViewRecipe())
        self.btnExit2 = CTkButton(self, corner_radius=16, fg_color="#CBE8BA", bg_color="#355723", text="Cooklet\nPro", text_color="#631878", font=("BioRhyme", 25), command=self.destroy)
        self.btnDelete = CTkButton(self, corner_radius=32, border_width=2, bg_color="#355723", fg_color="#FAD2E0", border_color="white", text="Delete", text_color="black", font=("Georgia", 20), command=self.delOption)
        #Search Bar Label
        self.lblFindRecipeSearchBar = CTkLabel(self, corner_radius=32, bg_color="#355723", fg_color="black", text="Search Recipe", font=("Arial", 15))
        #Search Bar Entry
        self.entryFindRecipeSearchBar = CTkEntry(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=300, text_color="black")
        #Find Recipe Listbox
        self.listBoxFindRecipe = CTkListbox(self, bg_color="#355723", fg_color="#D6D6D6", height=200, width=300, text_color="black", command=self.listGet)

    def placeRecipeWindowAttributes2(self):
        self.lblFindRecipeTitle.place(x=220, y=30)
        self.btnViewRecipe2.place(x=330, y=440)
        self.btnExit2.place(x=13, y=13)
        self.btnDelete.place(x=120, y=440)
        #Search Bar Label
        #self.lblFindRecipeSearchBar.place(x=20, y=50)
        #Search Bar Entry
        self.entryFindRecipeSearchBar.place(x=150, y=110)
        #Find Recipe Listbox
        self.listBoxFindRecipe.place(x=135, y=170)
        indexValue = 0
        for directory in os.listdir("Recipe Storage"):
            self.listBoxFindRecipe.insert(indexValue, directory)
            indexValue += 1
        self.bind("<KeyRelease>", lambda e: self.listUpdate())

    def windowOpenViewRecipe(self):
        from tkinter import messagebox
        try:
            if self.topLevelViewRecipe is None or not self.topLevelViewRecipe.winfo_exists():
                self.topLevelViewRecipe = topLevelWindowViewRecipe(self)
                self.topLevelViewRecipe.viewRecipeWindowAttributes(self.entryFindRecipeSearchBar.get())
                self.topLevelViewRecipe.placeViewRecipeWindowAttributes()
            else:
                self.topLevelViewRecipe.focus()
        except:
            self.topLevelViewRecipe.destroy()
            messagebox.showerror("Error", "Not a valid entry.")
        
class topLevelWindowViewRecipe(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(f"How to make")
        self.geometry("600x500")
        self.minsize(600, 500)
        self.maxsize(600, 500)
        
    def viewRecipeWindowAttributes(self, recipe):
        CTkLabel(self, bg_color="#355723", text="").pack(expand= True, fill= "both")
        self.lblViewRecipeTitle = CTkLabel(self, corner_radius= 32, bg_color="#355723", fg_color="#FAD2E0", text=f"{recipe}", text_color="black", font=("Georgia", 24))
        #Veiw serving size
        with open(f"Recipe Storage/{recipe}/servingSize.txt", "r") as addServingSize:
           servingSize = addServingSize.read()
        self.txtViewRecipeServings = CTkLabel(self, corner_radius= 16, bg_color="#355723", fg_color="#FAD2E0", text=f"Serving Size: {servingSize}", text_color="black", font=("Georgia", 18))
        #View method
        with open(f"Recipe Storage/{recipe}/method.txt", "r") as addMethod:
           method = addMethod.read()
        self.txtboxViewRecipeMethod = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=220, height=220, text_color="black")
        self.txtboxViewRecipeMethod.insert(index="1.0", text=method)
        #View ingredients
        with open(f"Recipe Storage/{recipe}/ingredients.txt", "r") as addIngredients:
           ingredients = addIngredients.read()
        self.txtboxViewRecipeIngredients = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=150, height=220, text_color="black")
        self.txtboxViewRecipeIngredients.insert(index="1.0", text=ingredients)
        #View ingredient measurements
        with open(f"Recipe Storage/{recipe}/ingredientMeasurement.txt", "r") as addIngredientMeasurement:
            ingredientMeasurement = addIngredientMeasurement.read()
        self.txtboxViewRecipeIngredientMeasurement = CTkTextbox(self, corner_radius=32, bg_color="#355723", fg_color="#D6D6D6", width=110, height=220, text_color="black")
        self.txtboxViewRecipeIngredientMeasurement.insert(index="1.0", text=ingredientMeasurement)
        #Exit button
        self.btnExit = CTkButton(self, corner_radius=32, border_width=2, bg_color="#355723", fg_color="#FAD2E0", border_color="white", text="Exit", text_color="black", font=("Georgia", 20), command=self.destroy)

    def placeViewRecipeWindowAttributes(self):
        self.lblViewRecipeTitle.place(x=220, y=13)
        self.txtViewRecipeServings.place(x=220, y=80)
        #Ingredients
        self.txtboxViewRecipeIngredients.place(x=50, y=150)
        #ingredient measurement
        self.txtboxViewRecipeIngredientMeasurement.place(x=210, y=150)
        #Method
        self.txtboxViewRecipeMethod.place(x=340, y=150)
        #exit button
        self.btnExit.place(x=210, y=460)