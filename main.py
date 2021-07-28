from display import Display
from sanstitre2 import CATEGORIES
from sanstitre1 import Api
from sanstitre0 import Database
class Main():
    
    def __init__(self):
        display = Display()
        next_step = False
        
        while not next_step:
            next_step = True
            choice = display.display_input()
            if choice == "1":
                self.select_category(display)
            elif choice == "2":
                self.select_saved_categories(display)
            elif choice == "exit":
                exit()
            else:
                print('Incorrect choice, please try again.')
                next_step = False
                
              
    def select_category(self, display):
        display.display_categories()
        #Input phase to choose next step
        next_step = False
        while not next_step:
            next_step = True
            choice = display.display_input()
            if choice == "home":
                self.__init__()
            try:
                if int(choice) - 1 in range(len(CATEGORIES)):
                    self.select_product(display, CATEGORIES[int(choice) - 1])
                else:
                    print('Incorrect choice, please try again.')
                    next_step = False
            except ValueError:
                print('Incorrect choice, please try again.')
                next_step = False

    def select_product(self, display, category):

        api = Api()
        database = Database()
        products = database.get_produits(category[0])
        #if there is no products saved yet, ask to the API then save them
        if not products:
            products = api.get_products(category[1])
            for product in products:
                data = (product['product_name'], product['id'], product['url'],
                        product['nutriments']['nutrition-score-fr'], category[0])
                database.insert_produit(data)

        products = database.get_produits(category[0])
        display.display_products(products)
        next_step = False
        #Input phase to choose next step
        while not next_step:
            next_step = True
            choice = display.display_input()
            if choice == "home":
                self.__init__()
            try:
                if int(choice) - 1 in range(len(products)):
                    self.select_alternative(display, products[int(choice) - 1], api, database)
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
            except ValueError:
                print('Choix incorrect, veuillez réessayer')
                next_step = False

    def select_alternative(self, display, product, api, database):
        data = (product)
        alternative = database.better_produit(data)
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
                    data = (alternative['product_name'], alternative['id'], alternative['url'],
                            alternative['nutriments']['nutrition-score-fr'], product[0])
                    database.insert_alternative(data)
                    self.__init__()
                else:
                    print('Choix incorrect, veuillez réessayer')
                    next_step = False
        else:
            print("Désolé, aucun produit de substition trouvé pour cet article "
                  "retour à l'accueil")
            self.__init__()


Main()