import discord
import user_cls
import sqlite3

class mainbot(discord.Client):
    def __init__(self):
        super().__init__()
        self.user_dict = {}

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        mes = message.content.lower()
        if mes.startswith('!recycle'):
            if 'buy' in mes:
                reply("reply_buy")

            elif 'join' in mes:
                if message.author not in self.user_dict.keys():
                    u_name = message.author
                    user = user_cls.user()
                    self.user_dict[u_name] = user
                    await message.channel.send(f'{message.author} has joined')
                else:
                    await message.channel.send(f'You have already joined')

            elif 'top' in mes:
                top = 0
                top_u = None
                for user in self.user_dict.keys():
                    if int(self.user_dict[user].points) > int(top):
                        top = self.user_dict[user].points
                        top_u = user
                await message.channel.send(f"{top_u} has highest score with {self.user_dict[top_u].get_points()} points")
            elif 'hash' in mes:
                hash_inp = mes.split(' ')[2]
                conn = sqlite3.connect("discordDB.db")
                cur = conn.cursor()
                data = cur.execute(f"SELECT hashno FROM hash WHERE hashno = {hash_inp}")
                if data == None:
                    await message.channel.send("Error")
                else:
                    cur.execute(f"DELETE FROM 'hash' WHERE hashno = {hash_inp}")
                    cur.close()
                    conn.commit()
                    conn.close()
                    await message.channel.send(f"{message.author} "+self.user_dict[message.author].add())


bot = mainbot()
bot.run()