





from faker import Faker
faker = Faker('pt_BR')


persona = {
    "nome": faker.name(),
    "cidade": faker.postcode(),
    "idade": faker.random_int(18,68)
    
}

print(persona)