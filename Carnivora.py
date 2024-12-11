from Animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_karnivora, cara_berburu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_karnivora = jenis_karnivora
        self.cara_berburu = cara_berburu

    def info_carnivora(self):
        super().info_animal(),
        print("jenis karnivora \t: ", self.jenis_karnivora,
              "\ncara_berburu  \t\t: ", self.cara_berburu,
                )
carnivora = Carnivora("harimau", "daging", "di darat", "beranak", "obligat", "soliter")
carnivora.info_carnivora()
print("=========================================================================================")
carnivora1 = Carnivora("singa", "daging", "di darat", "beranak", "obligat", "berkelompok")
carnivora1.info_carnivora()
print("=========================================================================================")
carnivora2 = Carnivora("beruang", "daging dan ikan", "di darat", "beranak", "fakultatif", "soliter")
carnivora2.info_carnivora()
print("=========================================================================================")
