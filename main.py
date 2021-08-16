from display import Display
from sanstitre2 import CATEGORIES
from sanstitre1 import Api
from sanstitre0 import Database
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
                    self.select_alternative(products[int(choice) - 1], self.database)
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
            except ValueError:
                print('Choix incorrect, veuillez réessayer')
                next_step = False

    def select_alternative(self, display, product):
        data = (product)
        alternative = self.database.better_produit(data)
        if alternative:
            display.display_alternative(product, alternative)
            next_step = False
            #Input phase to choose next step
            while not next_step:
                next_step = True
                choice = display.display_input()
                if choice == "home":
                    self.__init__()
                elif choice == "1":
                    data = (alternative[1], alternative[3], alternative[4],
                            alternative[2], product[0])
                    self.database.insert_alternative(data)
                    self.__init__()
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
        else:
            print("Désolé, aucun produit de substition trouvé pour cet article "
                  "retour à l'accueil")
            self.__init__()

    def select_saved_categories(self, display):

        categories = self.database.get_saved_categories()
        if categories:
            display.display_saved_categories(categories)
            #Input phase to choose next step
            next_step = False
            while not next_step:
                next_step = True
                choice = display.display_input()
                if choice == "home":
                    self.__init__()
                try:
                    if int(choice) - 1 in range(len(categories)):
                        self.select_saved_products(categories[int(choice) - 1], self.database)
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


Main()