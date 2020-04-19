class Footwear:
    __producing_country = "Ukraine"
    
    def __init__ (self, name_of_producer = "default_produser", price_in_UAH = 0, size_in_europe = 41,\
    color = "black", material = "shwadchack", hype = True, presence_of_laces = True):
        self.name_of_producer = name_of_producer
        self.price_in_UAH = price_in_UAH
        self.size_in_europe = size_in_europe
        self.color = color
        self.material = material
        self.hype = hype 
        self.presence_of_laces = presence_of_laces
    
    def __del__ (self):
        print (str(id(self)) + " was deleted")

    def __str__ (self):
        return "name of producer = {}; price in UAH = {}; size in Europe = {}; color = {}; material = {}; hype = {}; presense of laces = {}; producing country = {};"\
        .format(self.name_of_producer, self.price_in_UAH, self.size_in_europe, self.color, self.material,\
        self.hype, self.presence_of_laces, Footwear.__producing_country)
        
    @staticmethod
    def get_producing_country():
        return Footwear.__producing_country
        
if __name__ == "__main__":
    adidas = Footwear("Adidas", 300)
    nike = Footwear("Nike", 27000, 44)
    vans = Footwear("Vans", 2100, 41, "black", "tissue", True, True)
    
    print(adidas.__str__())
    print(nike.__str__())
    print(vans.__str__())