shopping_dict = {
    "Piekarnia": ["bułka", "chleb","Pączek"],
    "warzywniak": ["Marchew", "Seler", "Rukola"]
}
print ("lista zakupów")

Piekarnia = f"idę do piekarni, kupuje tu następujące rzeczy: {shopping_dict['Piekarnia']}"
print(Piekarnia)
Warzywniak = f"Idę do Warzywniak, kupuję tu następujące rzeczy: {shopping_dict['warzywniak']}"
print(Warzywniak)

Piekarnia1 = len(shopping_dict["Piekarnia"])
Warzywniak1=len(shopping_dict["warzywniak"])

suma = Piekarnia1+Warzywniak1
tekst = f"w sumie kupuję {suma} produktów"
print (tekst)
print("test")
