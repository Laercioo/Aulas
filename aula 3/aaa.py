

time = input("digite seu time")


if time == "Corinthians":
    prin("Você é um timão")
elif time == "Bahia":
    print("Você é do Esquadrão")
elif time == "Gremio":
    print("Você é imortal")
else:
    print("Você não é um Timão!")
    
match time:
    
    case "Corinthians":
    print("Você é um timão")
    case "Bahia":
    print("Você é do Esquadrão")
    case_"Gremio":
    print("Você é imortal")