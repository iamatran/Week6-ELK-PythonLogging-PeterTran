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
    
    for i in range(30):
        player1 = randomPlay()
        if player1 == 0:
            extra = {'player1Choice' : 'Rock'}
            game_logger.info('outcome', extra=extra)
        elif player1 == 1:
            extra = {'player1Choice' : 'Paper'}
            game_logger.info('outcome', extra=extra)
        elif player1 == 2:
            extra = {'player1Choice' : 'Scissors'}
            game_logger.info('outcome', extra=extra)
                
        player2 = randomPlay()
        if player2 == 0:
            extra = {'player2Choice' : 'Rock'}
            game_logger.info('outcome', extra=extra)
        elif player2 == 1:
            extra = {'player2Choice' : 'Paper'}
            game_logger.info('outcome', extra=extra)
        elif player2 == 2:
            extra = {'player2Choice' : 'Scissors'}
            game_logger.info('outcome', extra=extra)
    
        
        if player1 == player2:
            game_logger.warning('Detected collision of Player Choice')
            extra = {'win' : 'tie'}
            game_logger.info('outcome', extra=extra)
                
        if player1 == 0 and player2 == 1:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 0 and player2 == 2:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)
        if player1 == 1 and player2 == 0:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)
        if player1 == 1 and player2 == 2:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 2 and player2 == 0:
            extra = {'win' : 'player2'}
            game_logger.info('outcome', extra=extra)
        if player1 == 2 and player2 == 1:
            extra = {'win' : 'player1'}
            game_logger.info('outcome', extra=extra)

   


game()