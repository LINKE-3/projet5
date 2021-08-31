from display import Display
from CATEGORIES import CATEGORIES
from Database import Database
class Main():
    
    def __init__(self):
        self.display = Display()
        self.database = Database() 
        next_step = False
        
        while not next_step:
            next_step = True
            choice = self.display.display_input()
            if choice == "1":
                self.select_category()
            elif choice == "2":
                self.select_saved_categories()
            elif choice == "exit":
                exit()
            else:
                print('Incorrect choice, please try again.')
                next_step = False
                
              
    def select_category(self):
        self.display.display_categories()
        #Input phase to choose next step
        next_step = False
        while not next_step:
            next_step = True
            choice = self.display.display_input()
            if choice == "home":
                self.__init__()
            try:
                if int(choice) - 1 in range(len(CATEGORIES)):
                    self.select_product(CATEGORIES[int(choice) - 1])
                else:
                    print('Incorrect choice, please try again.')
                    next_step = False
            except ValueError:
                print('Incorrect choice, please try again.')
                next_step = False

    def select_product(self, category):
    
        products = self.database.get_produits(category[0])
        #if there is no products saved yet, ask to the API then save them

        self.display.display_products(products)
        next_step = False
        #Input phase to choose next step
        while not next_step:
            next_step = True
            choice = self.display.display_input()
            if choice == "home":
                self.__init__()
            try:
                if int(choice) - 1 in range(len(products)):
                    self.select_alternative(products[int(choice) - 1])
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
            except ValueError:
                print('Choix incorrect, veuillez réessayer')
                next_step = False

    def select_alternative(self, product):
        alternative = self.database.better_produit(product)
        if alternative:
            self.display.display_alternative(product, alternative)
            next_step = False
            #Input phase to choose next step
            while not next_step:
                next_step = True
                choice = self.display.display_input()
                if choice == "home":
                    self.__init__()
                elif choice == "1":
                    data = (alternative[1], alternative[2], alternative[3], 
                            alternative[4], product[0])
                    self.database.insert_alternative(data)
                    self.__init__()
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
        else:
            print("Désolé, aucun produit de substition trouvé pour cet article "
                  "retour à l'accueil")
            self.__init__()

    def select_saved_categories(self):
        
        categories = self.database.get_saved_categories()
        if categories:
            self.display.display_saved_categories(categories)
            #Input phase to choose next step
            next_step = False
            while not next_step:
                next_step = True
                choice = self.display.display_input()
                if choice == "home":
                    self.display.__init__()         
                try:
                    if int(choice) - 1 in range(len(categories)):
                        self.select_saved_products(categories[int(choice) - 1])
                    else:
                        print('Choix incorrect, veuillez réessayer')
                        next_step = False
                except ValueError:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
        else:
            print("Désolé vous n'avez pas encore enregistré de produit alternatif ")
            print("Retour au menu de départ")
            self.__init__()


    def select_saved_products(self, category):
        products = self.database.get_saved_products(category[0])
        self.display.display_saved_products(products)
        #Input phase to choose next_step step
        next_step = False
        while not next_step:
            next_step = True
            choice = self.display.display_input()
            if choice == "home":
                self.__init__()
            try:
                if int(choice) - 1 in range(len(products)):
                    self.select_saved_alternative(products[int(choice) - 1])
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
            except ValueError:
                print('Incorrect choice, please try again')
                next_step = False

    def select_saved_alternative(self, product):
        alternative = self.database.get_saved_alternative(product)
        self.display.display_saved_alternative(product, alternative)
        #Input phase to choose next_step step
        next_step = False
        while not next_step:
            next_step = True
            choice = input("Tapez 'Home' pour revenir à l'écran d'accueil :")
            if choice == "home":
                self.__init__()
            else:
                print('Choix incorrect, veuillez réessayer.')
                next_step = False

Main()