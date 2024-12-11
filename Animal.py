# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
# buat 3 objek dari masing masing class child. 

class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):#properti
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def info_animal(self):#methode
        print("nama hewan \t\t: ", self.name,
        "\nmakanan \t\t: ", self.makanan,
        "\nhidup \t\t\t: ", self.hidup,
        "\nberkembang biak \t: ", self.berkembang_biak)