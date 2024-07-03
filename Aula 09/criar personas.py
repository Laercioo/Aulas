from faker import Faker


fake = Faker('pt_BR')





def create_persona(number_of_personas: int) -> list:
    personas_list = []

    for i in range(number_of_personas):
        data = {
        "nome": fake.name(),
        "cidade": fake.city(),
        "idade": fake.random_int(18, 100)
        }
        personas_list.append(data)

    return personas_list




lista_de_personas = create_persona(20)    
print(lista_de_personas)