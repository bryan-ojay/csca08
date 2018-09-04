class NotCSVError(Exception):
    '''Exception for files that are not .csv files'''

class Product():
    ''' This class defines a product '''
    def __init__(self, category, name, price):
        ''' (Product, str, str, float) -> NoneType
        constructs a new product with its name and price'''
        self.__category = category
        self.__name = name
        self.__price = price
        
    def get_category (self):
        '''(Product)->str
        returns the name of the product'''
        return self.__category
    
    def get_name (self):
        '''(Product)->str
        returns the name of the product'''
        return self.__name
    
    def get_price (self):
        '''(Product)-> float
        returns the price of the product'''        
        return self.__price
    
    def set_category (self, category):
        '''(Product, str)->NoneType
        sets the category of a product to a new category'''
        self.__category = category
        
    def set_name (self, name):
        '''(Product, str)->NoneType
        sets the name of a product to a new name'''
        self.__name = name
        
    def set_price (self, price):
        '''(Product, float)-> NoneType
        sets the price of a product to a new price'''     
        self.__price = price

class GroceryStore():
    ''' This class defines a grocery store '''
    
    def __init__(self):
        ''' (GroceryStore, Product) ->NoneType
        constructs an empty dictionary '''
        self.__category_to_product = {}
        
    def get_category_to_product(self):
        '''(GroceryStore)-> dict
        returns the dictionary of groceries''' 
        return self.__category_to_product
    
    def get_product (self, category):
        '''(GroceryStore, str)-> str
        returns the name and price of the products of a given category'''
        info= ""
        products = self.__category_to_product[category]
        for item in products:
            info = info + item.get_name() + "\t" + str(item.get_price())+ "\n"
        return info
   
    def add_new_product (self, product):
        '''(GroceryStore, Product)-> NoneType
        adds a new Product to __category_to_product with product category as a key
        and product itself''' 
        # if the category of the product exists in the dictionary
        category = product.get_category()
        if (category in self.__category_to_product):
            # add the product as a value for this category
            values = self.__category_to_product[category]
            values.add(product)
            self.__category_to_product[category] = values
        # else
        else:
            #add the product along with its category to the dict
            self.__category_to_product [product.get_category()] = {product}

class StatisticalAnalysis():
    '''A utility class that does some statistical analysis on a given object'''
    
    def get_max(self, grocery, category):
        ''' (StatisticalAnalysis, GroceryStore, str) -> float
        returns the maximum product price of a given category'''
        # get the products of the same category 
        grocery_products = grocery.get_category_to_product()
        products = grocery_products[category]
        # find maximum price of the products
        max = 0 
        for item in products:
            if (max < item.get_price()):
                max = item.get_price()
        return max
    
    def get_min(self, grocery, category):
        ''' (StatisticalAnalysis, GroceryStore, str) -> float
        returns the minimum product price of a given category'''
        # get the products of the same category 
        grocery_products = grocery.get_category_to_product()
        products = grocery_products[category]
        
        # positive infinity as the first min value 
        min = float('inf')
        # find minimum price of the products
        for item in products:
            if (min > item.get_price()):
                min = item.get_price()
        return min                
    def get_mean(self, grocery, category):
        ''' (StatisticalAnalysis, GroceryStore, str) -> float
        returns the average product price of a given category'''
        # get the products of the same category 
        grocery_products = grocery.get_category_to_product()
        products = grocery_products[category]
        
        total = 0
        count = 0
        # find average price of the products 
        for item in products:
            total = total + item.get_price()
            count = count + 1
        return total / count                
    
         
def test_cases():
    # do statistical analysis 
    sa = StatisticalAnalysis()
    categories = my_store.get_category_to_product()
    for next_category in categories:
        print("Max price for " + str(next_category) + 
              " = " + str(sa.get_max(my_store, next_category)))
    print ("***")
    for next_category in categories:
        print("Min price for " + str(next_category) + 
              " = " + str(sa.get_min(my_store, next_category)))    
    print ("***")
    for next_category in categories:
        print("Mean price for " + str(next_category) + 
              " = " + str(sa.get_mean(my_store, next_category)))     
        
if(__name__ == "__main__"):
    # create a GroceryStore
    my_store = GroceryStore()
    # read a file name
    file_found = False
    file_name = input("Enter a csv file name: ")
    
    # check for valid file
    while not file_found:
        try:
            if (file_name[-4:] != '.csv'):
                raise NotCSVError
            input_file = open(file_name, 'r')
        except (FileNotFoundError, NotCSVError):
            print ("Invalid file.")
            file_name = input("Enter a csv file name: ")
        else:
            file_found = True
            
    file_line = input_file.readline().strip()
    # while it's not end of the file, read the file and create a dict out of it
    while (file_line != ""):
        # make the product and add it to the grocessory store
        (category, name, price) = file_line.split(',')
        
        # make sure the category is in the right tense
        category = category.capitalize()
        try:
            product = Product(category, name, float(price))
        except ValueError:
            price = 0
        finally:
            product = Product(category, name, float(price))
        my_store.add_new_product(product)
        # read a line of the file
        file_line = input_file.readline().strip()
    # close the file
    input_file.close()
    # do statistical analysis
        
 
    # call test cases
    test_cases()
    
    
    # things that you need to take care of:
    # 1- What if the given file name is not a valid file name (i.e. no such a file exists)? DONE
    # 2- What if the file is not a csv file? DONE
    # 3- What if the third item in each line of the file is not a float number DONE?
    # 4- What if the category is passed to the methods with a different case (i.e. vegetable instead of Vegetable) DONE?
    # 5- What if the given category does not exists (e.g. print(sa.get_max(my_store, "Toy"))?
    # 6- What if the methods are called with wrong argument type (e.g. sa.get_max(my_store, 3) my_store is not of type GroceryStore and category is not of type str)
    # 7- etc. etc. etc.

