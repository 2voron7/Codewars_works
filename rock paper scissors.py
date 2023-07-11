Player1 = input ('P1 ')
Player2 = input ('P2 ')

# def rps(Player1, Player2):
if Player1 == ('rock') and Player2 == ('scissors'):
    print ('Player 1 wins')
elif Player1 == ('scissors') and Player2 == ('paper'):
    print ('Player 1 wins')
elif Player1 == ('paper') and Player2 == ('rock'):
    print ('Player 1 wins')
elif Player1 == ('rock') and Player2 == ('rock'):
    print ('Draw!')
elif Player1 == ('scissors') and Player2 == ('scissors'):
    print ('Draw!')
elif Player1 == ('paper') and Player2 == ('paper'):
    print ('Draw!')
else:
    print ('Player 2 wins')