from Animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kulit, kemampuan_khusus, ukuran_tubuh ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.kemampuan_khusus = kemampuan_khusus
        self.ukuran_tubuh = ukuran_tubuh

    def info_mamalia(self):
        super().info_animal(),
        print("kulit \t\t\t: ", self.kulit,
              "\nkemampuan_khusus\t: ", self.kemampuan_khusus,
              "\nukuran tubuh \t\t: ", self.ukuran_tubuh 
                )
        
mamalia = Mamalia("kucing", "daging", "di darat", "melahirkan", "berbulu", "gesit", "sedang")
mamalia.info_mamalia()
print("=========================================================================================")
mamalia1 = Mamalia("lumba lumba", "ikan", "di laut", "melahirkan", "kulit licin", "cerdas", "sedang")
mamalia1.info_mamalia()
print("=========================================================================================")
mamalia2= Mamalia("hamster", "biji", "di sabana", "melahirkan", "berbulu pendek", "pandai menggali", "sedang")
mamalia2.info_mamalia()