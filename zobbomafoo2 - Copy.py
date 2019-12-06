# Work with Python 3.6
import discord
import asyncio
import praw
import wget
import re
import random

TOKEN = ''


r = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='testscript by /u/fakebot3',
                     username='')


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await self.change_presence(activity=discord.Game(name='Soon TM'))

    async def on_message(self, message):

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return


        if message.content.startswith('!reddit'):
            #await message.channel.send('Getting Image'.format(message))
            sub = message.content.split()
            subreddit = r.subreddit(sub[-1])
            print("finding:", sub[-1])
            
            counter = 0
            post = random.randint(0,200)
            
            for submission in subreddit.hot(limit=200):
                counter += 1
                if counter == post:
                    url_text = submission.url
                    title_text = submission.title
                    await message.channel.send(title_text)
                    await message.channel.send(url_text)

        if message.content.startswith('!vc'):
            author = message.author
            channel = author.VoiceChannel
            await client.join_voice_channel(channel)


    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(503152348865101844) # channel ID goes here
        await asyncio.sleep(5)
        #while True:
            #msg1 = input("Message: ")
            #await channel.send(msg1)


client = MyClient()
client.run(TOKEN)
