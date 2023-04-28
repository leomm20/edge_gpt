import asyncio
from EdgeGPT import Chatbot


async def main():
    bot = Chatbot(cookie_path='cookie.json')
    response = await bot.ask(prompt="Hello world")
    print(f"{response['item']['messages'][1]['timestamp']} - ", end='')
    print(f"{response['item']['result']['value']} - ", end='')
    print(f"{response['item']['messages'][1]['author']}: ", end='')
    print(response['item']['messages'][1]['text'])
    await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
