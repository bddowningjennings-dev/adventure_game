from __future__ import division
from player import Player
from map import world
from commands import command
from misc_funcs import health_colorer




    
print 40/60
print """
	\033[35m


`````````````````````````````````````````````````````````````````````````````


		
		                                 (`-..________....---'' 
                                  	/._______.._,.---'''     ,
Welcome to the adventure game!    ; )`.      __..-'`-.      /
                                 / /     _.-' _,.;;._ `-._,'
                                / /   ,-' _.-'  //   ``--._``._
                              ,','_.-' ,-' _.- (( =-    -. `-._`-._
                            ,;.''__..-'   _..--.\--'````--.._``-.`-._`.
             _          /\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
  _     _.-,'(__/\__/\-'' `     ___  .          `     \      `--._
,',)---' <-              `     `      ``-.   `     /     /     `   ` 
\_____--.  '`  `               __..-.  \     . (   < _...-----..._   
 \,--..__.  .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( ______
  	                ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   
                                                      ``--------..._``>>>>>>




``````````````````````````````````````````````````````````````````````````````
\033[37m
"""
raw_input('Press any key to continue.>> ')
name = None
while not name:
	name = raw_input('What is your name?>> ')
newPlayer = Player(name)
print """Welcome to the game, {}!""".format(name)
print ''
print ''
world[newPlayer.y][newPlayer.x].describe()
command('dirs',newPlayer, world)
gameState = {"status": True}
while gameState['status'] :
  health_percentage = int(newPlayer.health/newPlayer.max_health * 100)
  health_color = health_colorer(health_percentage)
  prompt_str = """Type help to see a list of possible commands. 
{} Enter a command. >>  """.format(health_color + str('{0:.0f}'.format(health_percentage))+ '%' + '\033[0m' )
  print prompt_str
  capture = raw_input(prompt_str)
  command(capture, newPlayer, world)

