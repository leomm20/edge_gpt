import asyncio
from EdgeGPT import Chatbot


async def consultar(prompt):
    global resp
    bot = Chatbot(cookie_path='cookie.json')
    response = await bot.ask(prompt='respuesta anterior: '+resp+' // '+prompt)
    print(f"{response['item']['messages'][1]['timestamp']} - ", end='')
    print(f"{response['item']['result']['value']} - ", end='')
    print(f"{response['item']['messages'][1]['author']}: ", end='')
    resp = response['item']['messages'][1]['text']
    print(resp)
    await bot.close()


resp = ''
while True:
    pedido = input('Preguntá (esribí salir para cerrar la app): ')
    if not pedido:
        print('No escribiste nada')
    elif pedido.lower() == 'salir':
        print('Chau!')
        exit()
    else:
        asyncio.run(consultar(pedido))
