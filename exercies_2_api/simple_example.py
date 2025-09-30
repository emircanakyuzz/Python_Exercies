import requests
api_key = '6fdb7cffc98c3468160c229f'

while True:
    kapatiyor_mu = input(f'döviz değişim programını kapatmak için 3, devam etmek için 1 tuşuna basınız...')
    if kapatiyor_mu == "3":
        break
    elif kapatiyor_mu == "1":     
        mevcut_para_birimi = input("mevcut para biriminiz nedir?\n")
        cevrilecek_para_birimi = input("çevrilecek para biriminiz nedir?\n")
        miktar = input("ne kadar miktar?\n")
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{mevcut_para_birimi}'
        try:
            response = requests.get(url)
            response_json = response.json()
            result = (response_json["conversion_rates"][cevrilecek_para_birimi])*float(miktar)
        except Exception as error:
            print(f"Kur dönüşümünde hata gerçekleşti, lütfen kur adlandırmasını doğru yazdığınıza dikkat ediniz... {error}")
            
        print(f"Kur dönüşümü sonucunda elde edilen sonuç: {result} {cevrilecek_para_birimi}")
    else:
        print("yanlış tuşlama yaptınız...")