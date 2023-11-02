# def requirements_output():
#     data = ''
#     with open('requirements.txt', 'r', encoding='UTF-16') as fails:
#
#         for fail in fails.readlines():
#             data += fail.strip() + " "
#     return data
#
# print(requirements_output())


# main _____________________________________________
# @app.route('/password')
# def password():
#     lenght = request.args.get('lenght', '10')
#
#     if lenght.isdigit():
#         lenght = int(lenght)
#
#     else:
#         return f'<h1>Invalid lenght value: {lenght}<h1/>'
#     return generate_password(lenght)
# utisl__________________________________________________
# def generate_password(lenght: int = 10) -> str:
#     chars = string.ascii_letters + string.digits
#     result = ''
#     for _ in range(lenght):
#         result += random.choice(chars)
#     return f'<h1>{result}</h1>'
import requests

def space():
    data = requests.get('http://api.open-notify.org/astros.json').json()
    return f'According to the website, there are {data["number"]} astronauts in space'

print(space())