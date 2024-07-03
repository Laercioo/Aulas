





from faker import Faker
faker = Faker('pt_BR')


persona = {
    "nome": faker.name(),
    "cidade": faker.city(),
    "idade": faker.random_int(18,68)
    
}

print(persona)