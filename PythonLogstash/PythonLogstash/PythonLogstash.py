import logging
import logstash
import sys
import time
from random import randint




game_logger = logging.getLogger('python-logstash-logger')
game_logger.setLevel(logging.INFO)
game_logger.addHandler(logstash.LogstashHandler('18.212.124.196', 5959, version=1))


def randomPlay():
    return randint(0,2)


def game():
    print "Welcome to my Rock Paper Scissors Game!"
    
    for i in range(10):
        player1 = randomPlay()
        if player1 == 0:
            game_logger.info("'player1Choice' : 'Rock'")
        elif player1 == 1:
            game_logger.info("'player1Choice' : 'Paper'")
        elif player1 == 2:
            game_logger.info("'player1Choice' : 'Scissors'")
                
        player2 = randomPlay()
        if player2 == 0:
            game_logger.info("'player2Choice' : 'Rock'")
        elif player2 == 1:
            game_logger.info("'player2Choice' : 'Paper'")
        elif player2 == 2:
            game_logger.info("'player2Choice' : 'Scissors'")
    
        
        if player1 == player2:
            game_logger.warning("Detected collision of Player Choice")
            game_logger.info("'win' : 'tie'")
                
        if player1 == 0 and player2 == 1:
            game_logger.info("'win' : 'player2'")
        if player1 == 0 and player2 == 2:
            game_logger.info("'win' : 'player1'")
        if player1 == 1 and player2 == 0:
            game_logger.info("'win' : 'player1'")
        if player1 == 1 and player2 == 2:
            game_logger.info("'win' : 'player2'")
        if player1 == 2 and player2 == 0:
            game_logger.info("'win' : 'player2'")
        if player1 == 2 and player2 == 1:
            game_logger.info("'win' : 'player1'")




game()