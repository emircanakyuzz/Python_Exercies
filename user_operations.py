import json

class User():
    def __init__(self, kullanici_adi="", sifre="", email=""):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre    
        self.email = email
        
class Operations():
    def __init__(self):
        self.kayit_listesi = []
        self.giris_yapti = False
        self.giris_yapan_kullanici = {}
        
    def giris(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        try:
            with open ("kullanıcı_bilgileri.json", "r") as file:
                for satir in file:
                    kayitli_kullanicilar = json.loads(satir)
                    if (kayitli_kullanicilar["kullanici_adi"] == kullanici_adi):
                        if (kayitli_kullanicilar["sifre"] == sifre):
                            self.giris_yapti=True
                            self.giris_yapan_kullanici.update({"Kullanıcı Adı": kayitli_kullanicilar["kullanici_adi"], "Şifre": kayitli_kullanicilar["sifre"], "Email": kayitli_kullanicilar["email"]})
        except Exception as error:
            print(f"Kullanıcı adı veya şifre hatalı. Error: {error}")
            
    def json_kayit(self):
        with open ("kullanıcı_bilgileri.json", "a") as file:
            for kayit in self.kayit_listesi:
                dict_kullanici =  json.dumps(kayit.__dict__)   
                file.write(f"{dict_kullanici}\n")
    
    def kayit(self, user: User):
        self.user = user
        self.kayit_listesi.append(user)
        self.json_kayit()
        print(f"Kayıt oluşturuldu...{self.kayit_listesi}")