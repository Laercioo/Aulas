from faker import Faker

faker = Faker('pt_BR')

persona = {
    "nome": faker.name(),
    "cidade": randon.randint(18,50),
}

print(persona)