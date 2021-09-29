class agama:
    def intro(self):
        print("indonesia mempunyai berbagai macam agama")

    def tempatibadah(self):
        print("setiap agama mempunyai tempat ibadah yang berbeda")

class islam(agama):
    def tempatibadah(self):
        print("Umat Islam, beribadah di Masjid dan Musholah")

class kristen(agama):
    def tempatibadah(self):
        print("Umat Kristen, beribadah di Gereja")

class hindu(agama):
    def tempatibadah(self):
        print("Umat Hindu, beribadah di Pura")

class buddha(agama):
    def tempatibadah(self):
        print("Umat Buddha, beribadah di Wihara")

class konghucu(agama):
    def tempatibadah(self):
        print("Umat Konghucu, beribadah di Kong Miao")

obj_agama = agama()
obj_islam = islam()
obj_kristen = kristen()
obj_hindu = hindu()
obj_buddha = buddha()
obj_konghucu = konghucu()

obj_agama.intro()
obj_agama.tempatibadah()

print("\n")

obj_islam.intro()
obj_islam.tempatibadah()

print("\n")

obj_kristen.intro()
obj_kristen.tempatibadah()

print("\n")

obj_hindu.intro()
obj_hindu.tempatibadah()

print("\n")

obj_buddha.intro()
obj_buddha.tempatibadah()

print("\n")

obj_konghucu.intro()
obj_konghucu.tempatibadah()