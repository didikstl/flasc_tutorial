# _______________-lesson 2
# from faker import Faker
# import requests
#
# def requirements_output() -> str:
#     with open('requirements.txt', 'r', encoding='UTF-16') as fails:
#         return fails.read()
#
#
# def faker_mail(lenght: int = 100) -> list:
#     faker = Faker('EN')
#     data = []
#     for _ in range(lenght):
#         data.append(faker.name() + faker.ascii_free_email())
#     return data
#
#
# def quantity_in_space() -> str:
#     data = requests.get('http://api.open-notify.org/astros.json').json()
#     return f'According to the website, there are {data["number"]} astronauts in space'