from player import Player
from map import world
from commands import command
print world


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
	capture = raw_input("""Type help to see a list of possible commands.  
Enter a command.  >> """)
	command(capture, newPlayer, world)

