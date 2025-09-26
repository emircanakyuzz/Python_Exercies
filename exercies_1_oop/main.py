import user_operations

try:
    # Sınıfları import edelim ve hata ayıklama ekleyelim
    user = user_operations.User
    operations = user_operations.Operations()
except Exception as e:
    print(f"Hata: user_operations modülünde sınıf bulunamadı: {e}")
    exit()

while True:
    print("Menü".center(50, "*"))
    print("1- Giriş\n2- Kayıt\n3- Çıkış\n4- Kullanıcı Bilgisi\n5- Programı Sonlandır")
    secim = input("Seçiminiz: ")
    
    if secim == "5":
        break
    elif secim == "1":
        if (operations.giris_yapti == False):     
            kullanici_adi = input("kullanıcı adınızı giriniz: ")
            sifre = input("şifrenizi giriniz: ")
            try:
                operations.giris(kullanici_adi, sifre)
            except Exception as error:
                print(f"Kullanıcı adı veya şifre hatalı: {error}")
            else:
                if (operations.giris_yapti == True):
                    print("Başarı ile giriş yapıldı...")
                else:
                    print("başarısız bir giriş işlemi, kullanıcı adı veya şifre hatalı...")
    
        else:
            yeni_giris = input("zaten giriş yaptınız yeni bir hesaba giriş yapmak istiyorsanız -evet- yazınız...\n")
            if (yeni_giris == "evet"):
                operations.giris_yapti = False
                operations.giris_yapan_kullanici = {}
                print("Şimdi giriş işlemi gerçekleştiriniz...")
            else:
                print(f"oturumdan çıkış yapılamadı... bulunduğunuz oturum: {operations.giris_yapan_kullanici}")
                
    elif secim == "2":
        if operations.giris_yapti == False:
            kullanici_adi = input("kullanıcı adını giriniz:")
            sifre = input("şifrenizi giriniz: ")
            email = input("email adresinizi giriniz: ")
            user0 = user(kullanici_adi, sifre, email)
            operations.kayit(user0)
        
        else:
            yeni_kayit = input("Giriş yapmış bulunmaktasınız. Kayıt işlemi gerçekleştirmek isterseniz önce çıkış yapmalısınız, onaylıyorsanız -evet- yazınız...\n")
            if yeni_kayit == "evet":
                operations.giris_yapti = False
                operations.giris_yapan_kullanici = {}
                print("başarı ile çıkış yapıldı, tekrar seçim yapabilir veya programı sonlandırabilirisiniz...")
            else:
                print(f"oturumdan çıkış yapılamadı... bulunduğunuz oturum: {operations.giris_yapan_kullanici}")
                
            
    elif secim == "3":
        operations.giris_yapti = False
        operations.giris_yapan_kullanici = {}
        print("başarı ile çıkış yapıldı, tekrar seçim yapabilir veya programı sonlandırabilirisiniz...")

    elif secim == "4":
        if (operations.giris_yapti == True):
            print(f"Giriş Yapan Kullanıcı: {operations.giris_yapan_kullanici}")
        else:
            print("Önce giriş yapmalısınız...")
    else:
        print("Geçersiz bir giriş yaptınız, tekrar deneyiniz.")
