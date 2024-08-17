import discord
from discord.ext import commands
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)

# Token de acesso ao Bot
TOKEN = 'YOUR_TOKEN_HERE' 

# Configurando os intents necessários
intents = discord.Intents.default()
intents.members = True  # Permite que o bot veja informações sobre os membros
intents.message_content = True  # Para acessar o conteúdo das mensagens

# Defina o prefixo do comando (ex: !, ?, etc.) e passe os intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Bot conectado como {bot.user}')

# Comando para enviar mensagens para todos os usuários, exceto aqueles com cargos administrativos
@bot.command()
async def send_message(ctx, *, message: str):
    if ctx.guild:
        # Lista de roles que o bot deve ignorar
        admin_roles = ['admin', 'moderador', 'administrator', 'mod']
        
        for member in ctx.guild.members:
            # Ignora membros que possuem qualquer uma das roles administrativas
            if any(role.name.lower() in admin_roles for role in member.roles):
                logging.info(f'Membro {member.name} ignorado devido ao cargo administrativo.')
                continue
            
            try:
                # Envia uma mensagem privada para o membro
                await member.send(message)
                await ctx.send(f'Mensagem enviada para {member.name}.')
                logging.info(f'Mensagem enviada para {member.name}.')
            except Exception as e:
                await ctx.send(f'Não foi possível enviar mensagem para {member.name}.')
                logging.error(f'Erro ao enviar mensagem para {member.name}: {e}')
    else:
        await ctx.send('Este comando só pode ser usado em servidores.')
        logging.warning('Comando usado fora de um servidor.')

bot.run(TOKEN)


## Utilize o comando !send_message + a mensagem que será enviada dentro do servidor
