import discord
import os
import json
from collections import deque
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Créer une file pour stocker les commandes
command_history = deque(maxlen=100)

@bot.event
async def on_command(ctx):
    # Ajouter la commande à la file
    command_history.append((ctx.author.id, ctx.message.content))

# Commande pour voir la dernière commande rentrée
@bot.command()
async def lastcommand(ctx):
    if command_history:
        last_command = command_history[-1][1]
        await ctx.send(f"Dernière commande : {last_command}")
    else:
        await ctx.send("Aucune commande dans l'historique")

# Commande pour voir toutes les commandes rentrées par les utilisateurs
@bot.command()
async def commandall(ctx):
    if command_history:
        all_commands = "\n".join([f"{command[0]}: {command[1]}" for command in command_history])
        await ctx.send(f"Toutes les commandes :\n{all_commands}")
    else:
        await ctx.send("Aucune commande dans l'historique")


# Commande pour vider l'historique
@bot.command()
async def clearcommand(ctx):
    command_history.clear()
    await ctx.send("Historique des commandes vidé")

# Commande pour voir l'historique de commande d'un utilisateur précis en utilisant son id
@bot.command()
async def commanduser(ctx, user_id: int):
    user_commands = [command[1] for command in command_history if command[0] == user_id]
    if user_commands:
        user_commands_str = "\n".join(user_commands)
        await ctx.send(f"Historique des commandes pour l'utilisateur {user_id} :\n{user_commands_str}")
    else:
        await ctx.send(f"Aucune commande pour l'utilisateur {user_id}")

#Les sujets
topics = ['livres', 'films', 'anime', 'musique']

@bot.command()
async def speak(ctx, topic):
    if topic in topics:
        await ctx.send(f"Oui, je peux parler de {topic} !")
    else:
        await ctx.send(f"Désolé, je ne peux pas parler de {topic}.")


@bot.command(name='recommandations')
async def recommandations(ctx):
    await ctx.send('Dans quel sujet cherchez-vous des recommandations ? (livres, films, anime, musique)')

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    sujet = await bot.wait_for('message', check=check)
    sujet = sujet.content.lower()

    if sujet == 'livres':
        await ctx.send('Quel est votre genre préféré ?')
        await ctx.send('(exemples : science-fiction, romance, thriller, fantasy)')
        genre = await bot.wait_for('message', check=check)
        genre = genre.content.lower()

        if genre == 'science-fiction':
            await ctx.send('Je vous recommande "1984" de George Orwell (1949)')

        elif genre == 'romance':
            await ctx.send('Je vous recommande "Lamour dure trois ans" de Frédéric Beigbeder (1997)')

        elif genre == 'thriller':
            await ctx.send('Je vous recommande "Le Silence des agneaux" de Thomas Harris (1988)')

        elif genre == 'fantasy':
            await ctx.send('Je vous recommande "Le Seigneur des anneaux" de J.R.R. Tolkien (1954)')

        else:
            await ctx.send('Je ne connais pas ce genre. Veuillez choisir parmi les genres proposés.')

    elif sujet == 'films':
        await ctx.send('Quel est votre genre préféré ?')
        await ctx.send('(exemples : action, comédie, drame, science-fiction)')
        genre = await bot.wait_for('message', check=check)
        genre = genre.content.lower()

        if genre == 'action':
            await ctx.send('Je vous recommande "John Wick" avec Keanu Reeves (2014)')

        elif genre == 'comédie':
            await ctx.send('Je vous recommande "La Grande Vadrouille" avec Louis de Funès et Bourvil (1966)')

        elif genre == 'drame':
            await ctx.send('Je vous recommande "Forrest Gump" avec Tom Hanks (1994)')

        elif genre == 'science-fiction':
            await ctx.send('Je vous recommande "Interstellar" avec Matthew McConaughey et Anne Hathaway (2014)')
        
        elif genre == 'luca' :
            await ctx.send('Bien vu batard, teste 50 nuances de grey avec l autre bombasse de je ne sais pas quelle année car on veut juste voir son cul')

        else:
            await ctx.send('Je ne connais pas ce genre. Veuillez choisir parmi les genres proposés.')

    elif sujet == 'anime':
        await ctx.send('Quel est votre genre préféré ?')
        await ctx.send('(exemples : action, comédie, drame, romance)')
        genre = await bot.wait_for('message', check=check)
        genre = genre.content.lower()

        if genre == 'action':
            await ctx.send('Je vous recommande "Death Note" de Tsugumi Ohba et Takeshi Obata (2006-2007)')

        elif genre == 'comédie':
            await ctx.send('Je vous recommande "One Punch Man" de Yusuke Murata (2015-2019)')
        elif genre == 'drame':
            await ctx.send('Je vous recommande "Your Lie in April" de Naoshi Arakawa (2014-2015)')

        elif genre == 'romance':
            await ctx.send('Je vous recommande "Kimi ni Todoke" de Karuho Shiina (2005-2017)')

        else:
            await ctx.send('Je ne connais pas ce genre. Veuillez choisir parmi les genres proposés.')

    elif sujet == 'musique':
        await ctx.send('Quel est votre genre préféré ?')
        await ctx.send('(exemples : rock, pop, metal, jazz)')
        genre = await bot.wait_for('message', check=check)
        genre = genre.content.lower()

        if genre == 'rock':
            await ctx.send('Je vous recommande "Led Zeppelin IV" de Led Zeppelin (1971)')

        elif genre == 'pop':
            await ctx.send('Je vous recommande "Thriller" de Michael Jackson (1982)')

        elif genre == 'metal':
            await ctx.send('Je vous recommande "Master of Puppets" de Metallica (1986)')

        elif genre == 'jazz':
            await ctx.send('Je vous recommande "Kind of Blue" de Miles Davis (1959)')

        else:
            await ctx.send('Je ne connais pas ce genre. Veuillez choisir parmi les genres proposés.')

    else:
        await ctx.send('Je ne connais pas ce sujet. Veuillez choisir parmi les sujets proposés.')

    await ctx.send('Est-ce que vous avez besoin de recommandations dans un autre sujet ? (oui, non)')
    autre_sujet = await bot.wait_for('message', check=check)
    autre_sujet = autre_sujet.content.lower()

    if autre_sujet == 'oui':
        await recommandations(ctx)

    else:
        await ctx.send('Merci d\'avoir utilisé le bot !')

message_history = {}

@bot.event
async def on_message(message):
    message_history[message.author.id] = message_history.get(message.author.id, []) + [f'{message.created_at}: {message.content}']
    await bot.process_commands(message)

@bot.command()
async def historique(ctx, user_id: int):
    messages = message_history.get(user_id, [])
    if not messages:
        await ctx.send('Aucun message trouvé pour cet utilisateur.')
    else:
        await ctx.send('\n'.join(messages))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node("Avez-vous de la fièvre?")
root.left = Node("Avez-vous des douleurs musculaires?")
root.left.left = Node("Avez-vous une toux sèche?")
root.left.right = Node("Avez-vous des frissons et des tremblements?")
root.right = Node("Avez-vous un écoulement nasal?")
root.right.left = Node("Votre nez est-il bouché?")
root.right.right = Node("Avez-vous mal à la gorge?")


@bot.command()
async def symptomes(ctx):
    current_node = root
    while current_node.left is not None and current_node.right is not None:
        await ctx.send(current_node.value)
        response = await bot.wait_for("message", check=lambda message: message.author == ctx.author)

        if response.content.lower() == "reset":
            current_node = root
        elif response.content.lower() == "oui":
            current_node = current_node.left
        else:
            current_node = current_node.right

    if current_node == root.left.left:
        await ctx.send("T'es chiant tu as trop de symptomes.")
    elif current_node == root.left.right:
        await ctx.send("Vous pourriez avoir la grippe.")
    elif current_node == root.right.left:
        await ctx.send("Vous pourriez avoir un rhume.")
    elif current_node == root.right.right:
        await ctx.send("Bah tu as que dalle, pourquoi tu me demandes ?.")


# Ouvre le fichier JSON en mode d'ajout
file = open("messages.json", "a")

# Définir un évenement de message pour enregistrer chaque message
@bot.event
async def on_message(message):
    # Ignorez les messages du bot
    if message.author == bot.user:
        return
    
    # Construire un dictionnaire avec les informations du message
    msg_dict = {
        "author": message.author.name,
        "channel": message.channel.name,
        "content": message.content
    }
    
    # Enregistrez le message dans le fichier JSON
    json.dump(msg_dict, file)
    file.write("\n")
    file.flush() # pour vider le buffer et forcer l'enregistrement immédiat dans le fichier
    
    # N'interférez pas avec les commandes du bot
    await bot.process_commands(message)
    



class HashTable:
    def __init__(self):
        self.size = 1024
        self.table = [None] * self.size

    def _hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def __getitem__(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def __delitem__(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        raise KeyError(key)
    
table = HashTable()
table['foo'] = 'bar'
print(table['foo'])  # Output: 'bar'
del table['foo']

async def envoyer_mp(user_id, message):
    # Récupérer le membre à qui envoyer le message
    member = await bot.fetch_user(user_id)

    # Créer l'objet Message à envoyer
    message_obj = discord.Embed(description=message)

    # Envoyer le message privé
    await member.send(embed=message_obj)

    # Retourner une confirmation que le message a été envoyé avec succès
    return f"Message envoyé à {member.name}#{member.discriminator}"

@bot.command()
async def histo(ctx, user_id: int):
    messages = []
    async for message in ctx.history():
        if message.author.id == user_id:
            messages.append(message.content)
    response = '\n'.join(messages)
    await ctx.send(response)









@bot.event
async def on_ready():
    print(f'{bot.user} le bot est up sur:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')

bot.run(
  "MTA5NjMyOTQxMTYxMzE3OTk2NA.Gf2Y5_.g_e8gPEbC4g60xdz3i_jZuLD3Jg9njw1UZGfEY")
