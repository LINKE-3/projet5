from sanstitre2 import CATEGORIES 


class Display():
    def __init__(self):
        self.display_separator()
        print('Selectionnez un numéro (1-2)')
        print('1 - Quel aliment souhaitez-vous remplacer ?')
        print('2 - Retrouver mes aliments substitués.')
      
    def display_separator(self):
        print('_______________________________________________________')
        print('')
        print('_______________________________________________________')

    def display_categories(self):
        self.display_separator()
        print('Voici les categories disponibles')
        print('Choissisez le numéro de la catégorie pour voir ses produits')
        for i, category in enumerate(CATEGORIES):
            print(i + 1, category[1])
 
    def display_input(self):
        print('_______________________________________________________')
        choice = input('Saissisez le numéro de votre choix ou "home" pour revenir au départ : ')
        return choice
    
    def display_products(self, products):
        self.display_separator()
        print('Choissisez le numéro de la catégorie pour voir ses subsitus')
        for i, product in enumerate(products):
            print(i + 1, product[1])
    def display_alternative(self, product, alternative):
        self.display_separator()
        print('Le produit choisi :', product[1])
        print('A un nutriscore de :', product[4])
        print('Voici le lien pour consulter en ligne ce produit :')
        print(product[3])
        print('Remplacez le par :', alternative['product_name'])
        print('Son nutriscore est de :', alternative['nutriments']['nutrition-score-fr'])
        print('Voici le lien pour consulter en ligne ce produit :')
        print(alternative['url'])
        print('Tapez 1 pour l\'enregistrer')
        
    def display_saved_categories(self, categories):
        self.display_separator()
        print('Voici la liste des catégories contenant des produits sauvegardés')
        for index, category in enumerate(categories):
            print(index +1, category[1])
        print('Selectionnez la categorie de votre choix en saissisant son numéro')
    def display_saved_products(self, products):

        self.display_separator()
        print('Voici la liste des produits possédant un substitut')
        for index, product in enumerate(products):
            print(index + 1, product[1])
        print('Selectionnez le produit voulu pour afficher son substitut')
    def display_saved_alternative(self, product, alternative):
        self.display_separator()
        print('Le produit choisi est :', product[1])
        print('Son nutriscore est de :', product[4])
        print('Voici le lien pour consulter en ligne ce produit :')
        print(product[3])
        print('Son substitut enregistré est :', alternative[1])
        print('Son nutriscore est de :', alternative[4])
        print('Voici le lien pour consulter en ligne ce produit :')
        print(alternative[3])
