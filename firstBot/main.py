from typing import Final
import os
from discord import Intents, Client, Message
from responses import handle_response

intents: Intents = Intents.default();
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty becasue intents were not enabled")
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message,user_message)

def main() -> None:
    client.run("MTIwOTc2NDIyNDk5NDEyMzc4OA.GJ22uY.v_nOPISYq8G1k8IrL7mOe2zoHpiGv1E0UlmyGc")

if __name__ == '__main__':
    main()