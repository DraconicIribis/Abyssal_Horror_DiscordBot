import os
from os import path
import discord
async def xp_roles(ctx):
  can_do = os.path.isfile('{}.txt'.format(ctx.author))
  with open('{}.txt'.format(ctx.author),'r') as xp_total:
    xp = int(float(xp_total.read()))
    role = discord.utils.get(ctx.author.guild.roles, id=621565009389944833)
    if role not in ctx.author.roles and can_do and xp > 100:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 2661286)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://66.media.tumblr.com/c72c16b21b8023d43d582ca6b10ee595/tumblr_o98by92Qh81vwgyqto1_1280.jpg')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    role = discord.utils.get(ctx.author.guild.roles,id=631245434421248011)
    if role not in ctx.author.roles and can_do and xp > 250:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 1854227)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/008/205/728/large/ulisses-almeida-deaconsofthedeep.jpg?1511185546')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    role = discord.utils.get(ctx.author.guild.roles,id=631245675270635563)
    if role not in ctx.author.roles and can_do and xp > 625:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 790703)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/002/527/566/large/zoewings-zhang-16-5-5.jpg?1462791003')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    role = discord.utils.get(ctx.author.guild.roles,id=621694281614229517)
    if role not in ctx.author.roles and can_do and xp > 1562:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 5442091)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://i.imgur.com/IPbr119.jpg')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    role = discord.utils.get(ctx.author.guild.roles,id=631247287196319764)
    if role not in ctx.author.roles and can_do and xp > 3905:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 10040115)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://i.pinimg.com/originals/dc/0c/4a/dc0c4ab51d2e6547bea512a128c0d3ce.jpg')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    role = discord.utils.get(ctx.author.guild.roles,id=621564341409284116)
    if role not in ctx.author.roles and can_do and xp > 9762:
      await ctx.author.add_roles(role)
      embed = discord.Embed(colour = 655360)
      embed.set_author(name='Level Up!')
      embed.set_image(url='https://i.pinimg.com/736x/54/78/27/547827e8c06160b87474ff4f943c4e3a.jpg')
      embed.add_field(name="{} has leveled up!".format(ctx.author), value='{0} is now a member of the {1}!'.format(ctx.author,role))
      await ctx.send(embed=embed)
      print('{0} leveled up to {1}.'.format(ctx.author,role))
    else:
      pass
    
