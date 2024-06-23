import discord
import asyncio

# Función para manejar la solicitud de token y mensaje
def get_input():
    token = input("Por favor, ingresa el token de tu bot de Discord: ").strip()
    message = input("Ingresa el mensaje que quieres enviar repetidamente: ").strip()
    return token, message

# Función para enviar el mensaje repetidamente en todos los servidores
async def spam_message(client, message):
    await client.wait_until_ready()
    while not client.is_closed():
        for guild in client.guilds:
            try:
                channel = next((channel for channel in guild.text_channels if channel.permissions_for(guild.me).send_messages), None)
                if channel:
                    await channel.send(message)
            except Exception as e:
                print(f'Error al enviar mensaje en el servidor {guild.name}: {e}')
        await asyncio.sleep(0)  # Cambia el delay según sea necesario

# Función principal para inicializar el bot
async def main():
    token, message = get_input()
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Bot conectado como {client.user}')
        print('Enviando mensaje repetidamente...')

    @client.event
    async def on_disconnect():
        print('Bot desconectado.')

    await client.start(token)
    await spam_message(client, message)

# Ejecutar el programa
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())