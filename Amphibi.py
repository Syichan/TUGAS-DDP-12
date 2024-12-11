from Animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("jenis air \t\t: ", self.jenis_air,
              "\nbernapas  \t\t: ", self.bernapas,
                )
amphibi = Amphibi("katak", "serangga", "di Air", "bertelur", "air tawar", "paru-paru dan kulit")
amphibi.info_amphibi()
print("=========================================================================================")
amphibi1 = Amphibi("salamander", "cacing", "di air", "bertelur dan melahirkan", "air tawar", "kulit")
amphibi1.info_amphibi()
print("=========================================================================================")
amphibi2 = Amphibi("axolotl", "ikan kecil", "di air", "bertelur", "air tawar", "insang")
amphibi2.info_amphibi()
print("=========================================================================================")
