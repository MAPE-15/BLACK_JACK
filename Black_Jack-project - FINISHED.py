
# BLACK JACK
# FINISHED !!!

import random


def black_jack():

    player_names = input('Type names of players: ').split(', ')

    # lists of players names and their decks who decided to quit
    players_who_quited_names = []
    players_who_quited_decks = []

    # lists of players names and their decks who reached sum over 21
    players_who_over21_names = []
    players_who_over21_decks = []

    # if they want to try again !!!
    def new_game_or_not():
        print('')
        new_game = input('Wanna start a new game or not? yes/no: ').upper()

        if new_game == 'YES':
            print('You have decided to start a new game.')
            black_jack()
        elif new_game == 'NO':
            print('You have decided to exit.')
            exit()
        else:
            print('You typed wrong yes/no try again !')
            new_game_or_not()

    def give_cards():

        # list which contains players cards
        players_cards = []

        # add a new list which contains cards to a list players_cards ([[1, 3]])
        for _ in player_names:
            each_list = list()
            players_cards.append(each_list)

            # add two cards for the beginning of the game to every player
            for _ in range(2):
                karta_cislo = random.randint(1, 10)
                each_list.append(karta_cislo)

        # print all the players names, their decks, and the sum of their decks
        for every_player, every_cards in zip(player_names, players_cards):
            print(every_player + ', your cards:', every_cards)
            print(every_player + ', sum of your cards: ', sum(every_cards))
            print('')

        # now they have to decide to hit (add plus one card to their decks), or to quit and wait for the results
        def hit_or_stand():

            # hit only to each list in players_cards a one number to 1st list, when called hit again -->
            # then hit it to 2nd list in players cards etc...
            # a default value !!!
            kolkaty = -1

            # starting point of the list player_names
            # a default value !!!
            position_card_or_name = 0

            # amount of players !!!
            # a default value !!!
            pocet_hracov = len(player_names)

            while pocet_hracov > 0:

                for _ in player_names:
                    # ask every player to hit or quit
                    hit_stand = input(player_names[position_card_or_name] + ', wanna hit or quit?: ').upper()
                    print('')

                    # if he/she typed hit
                    if hit_stand == 'HIT':
                        # move to a next player, his deck, and his name
                        kolkaty += 1
                        position_card_or_name += 1

                        # if max people reached then start from default value, and ask from beginning
                        if position_card_or_name == pocet_hracov or kolkaty > pocet_hracov:
                            position_card_or_name = 0
                            kolkaty = -1

                        # add 1 card to his deck
                        for _ in range(1):
                            karta_cislo = random.randint(1, 10)
                            players_cards[kolkaty].append(karta_cislo)

                        # print players who quited their decks and the sum of their decks
                        for quited_players_names, quieted_players_decks in zip(players_who_quited_names, players_who_quited_decks):
                            print("QUITED PLAYER'S, ==", quited_players_names, '== cards:', quieted_players_decks)
                            print("QUITED PLAYER'S, ==", quited_players_names, '== sum of cards:', sum(quieted_players_decks))
                            print('')

                        # print players who quited their decks and the sum of their decks
                        for over21_players_names, over21_players_decks in zip(players_who_over21_names, players_who_over21_decks):
                            print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== cards:', over21_players_decks)
                            print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== sum of cards:', sum(over21_players_decks))
                            print('')

                        # print players who are still playing and have not quited
                        for each_name, each_cards in zip(player_names, players_cards):
                            print(each_name + ', your cards:', each_cards)
                            print(each_name + ', sum of your cards:', sum(each_cards))
                            print('')

                            # !!! RESULTS DEFINITION, DESCRIPTION: !!!

                            # if sum of your cards is higher than 21 !!!
                            if sum(each_cards) > 21:

                                print('!!! ' + each_name + ' == MAXIMUM SUM 21 REACHED !!!')
                                print(each_name + ', you are added to over 21 (lost) players !!!')
                                print('')

                                # if one player reaches reaches higher than 21 then delete 1 from the amount of players
                                # f.e. if there are 4 players then reduce it to 3
                                pocet_hracov -= 1

                                # you have to start from the place where the player was removed -->
                                # because few codes above is kolkaty += 1 and position_card_or_name += 1 -->
                                # but if he reaches sum of cards higher then 21 then you don't want to -->
                                # add 1 to kolkaty and position_card_or name you want it to be the same -->
                                # so +1 -1 == 0 !!!
                                kolkaty -= 1
                                position_card_or_name -= 1

                                # if the last player has reached the max value 21 then start from the beginning
                                if each_name == player_names[-1]:
                                    position_card_or_name = 0
                                    kolkaty = -1

                                # add his name and his deck of cards to the list of players names and decks who are over 21 (lost)
                                players_who_over21_names.append(each_name)
                                players_who_over21_decks.append(each_cards)

                                # remove his name and his deck of cards from the list of players who are still playing
                                player_names.remove(each_name)
                                players_cards.remove(each_cards)

                                # if max people reached then start from default value, and ask from beginning
                                # if kolkaty higher than amount of players then start it from the default value -1
                                if position_card_or_name == pocet_hracov or kolkaty > pocet_hracov:
                                    position_card_or_name = 0
                                    kolkaty = -1

                                # print players who are still playing and have not lost or quited
                                for each_name, each_cards in zip(player_names, players_cards):
                                    print(each_name + ', your cards:', each_cards)
                                    print(each_name + ', sum of your cards:', sum(each_cards))
                                    print('')

                            # if their sum is equal to 21
                            elif sum(each_cards) == 21:
                                # print his name and let him/her know that he/she has won
                                print('!!! ' + each_name + ' == YOU REACHED EXACTLY 21 !!!')
                                print(each_name + ', with your deck:', each_cards, '== YOU ARE THE ABSOLUTE WINNER !!!')
                                print('')

                                # ask if they wanna play again
                                new_game_or_not()

                    # if he/she typed quit
                    elif hit_stand == 'QUIT':

                        # if one player reaches reaches higher than 21 then delete 1 from the amount of players
                        # f.e. if there are 4 players then reduce it to 3
                        pocet_hracov -= 1

                        # print who decided to quit
                        print(player_names[position_card_or_name] + ', you have decided to quit.')
                        print(player_names[position_card_or_name] + ', you have quited, must wait for the game to give results.')

                        print('')

                        # add the name of quited player to the list of decks of quited players
                        players_who_quited_names.append(player_names[position_card_or_name])
                        # deck from quited player and add it to list of decks of quited players
                        deck = players_cards[position_card_or_name]
                        players_who_quited_decks.append(deck)

                        # remove the player from the players_name list and remove his deck from the players_cards list
                        player_names.remove(player_names[position_card_or_name])
                        players_cards.pop(position_card_or_name)

                        # if max people reached then start from default value, and ask from beginning
                        # if kolkaty higher than amount of players then start it from the default value -1
                        if position_card_or_name == pocet_hracov or kolkaty > pocet_hracov:
                            position_card_or_name = 0
                            kolkaty = -1

                        # print players who quited their decks and the sum of their decks
                        for quited_players_names, quieted_players_decks in zip(players_who_quited_names, players_who_quited_decks):
                            print("QUITED PLAYER'S, ==", quited_players_names, '== cards:', quieted_players_decks)
                            print("QUITED PLAYER'S, ==", quited_players_names, '== sum of cards:', sum(quieted_players_decks))
                            print('')

                        # print players who lost their decks and the sum of their decks
                        for over21_players_names, over21_players_decks in zip(players_who_over21_names, players_who_over21_decks):
                            print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== cards:', over21_players_decks)
                            print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== sum of cards:', sum(over21_players_decks))
                            print('')

                        # print players who are still playing and have not quited
                        for each_cards, each_name in zip(players_cards, player_names):
                            print(each_name + ', your cards:', each_cards)
                            print(each_name + ', sum of your cards:', sum(each_cards))
                            print('')

                    else:
                        print('!!! Wrong typed hit/quit, try hit/quit again', player_names[position_card_or_name], '!!!')

                # if there are no more players playing and there is at least one player who quited
                if pocet_hracov == 0 and len(players_who_quited_names) > 0:
                    print('-------------------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------------------')
                    print('')

                    # print players who quited their decks and the sum of their decks
                    for quited_players_names, quieted_players_decks in zip(players_who_quited_names,
                                                                           players_who_quited_decks):
                        print("QUITED PLAYER'S, ==", quited_players_names, '== cards:', quieted_players_decks)
                        print("QUITED PLAYER'S, ==", quited_players_names, '== sum of cards:',
                              sum(quieted_players_decks))
                        print('')

                    # print players who quited their decks and the sum of their decks
                    for over21_players_names, over21_players_decks in zip(players_who_over21_names,
                                                                          players_who_over21_decks):
                        print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== cards:', over21_players_decks)
                        print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== sum of cards:',
                              sum(over21_players_decks))
                        print('')

                    # 1st list only_names where will be players names -->
                    # --> and 2nd list only_sum_decks where will be the sum of their decks
                    only_names = []
                    only_sum_decks = []


                    # add players names who quited into the only_names list; and the sum of their decks to the only_sum_decks list
                    for quited_players_names, quieted_players_decks in zip(players_who_quited_names, players_who_quited_decks):
                        only_names.append(quited_players_names)
                        only_sum_decks.append(sum(quieted_players_decks))

                    # list winner_name where will be added one and only winner name
                    winner_name = []
                    # list winner_deck where will be added the highest sum of his deck which is closest to 21
                    winner_deck = []

                    # find where in the list only_sum_decks is the max value in that list
                    position = only_sum_decks.index(max(only_sum_decks))
                    # add the players name into winner_name using the position of the max value in the only_sum_decks list
                    winner_name.append(players_who_quited_names[position])
                    # add the players max sum of his deck from the only_sum_decks to the winner_deck list
                    winner_deck.append(max(only_sum_decks))

                    # announce who is the winner etc...
                    print('!!! Among all quited players only, <' + winner_name[0] + '> was the closest to the number 21,')
                    print('so <' + winner_name[0] + '>, is the one and only winner the sum of his cards:', winner_deck[0], '!!!')
                    print('')

                    # ask if they wanna play, try the new game again
                    new_game_or_not()

                # if there are no more players to play, and nobody quieted, which means everybody lost (above the sum 21)
                elif pocet_hracov == 0 and len(players_who_quited_names) == 0:
                    print('-------------------------------------------------------------------------------------------')
                    print('-------------------------------------------------------------------------------------------')
                    print('')

                    # print players who lost their decks and the sum of their decks
                    for over21_players_names, over21_players_decks in zip(players_who_over21_names,
                                                                          players_who_over21_decks):
                        print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== cards:', over21_players_decks)
                        print("OVER 21 PLAYER'S (LOST), ==", over21_players_names, '== sum of cards:',
                              sum(over21_players_decks))
                        print('')

                    # print that nobody has won
                    print('!!! NOBODY IS THE WINNER, EVERYBODY HAVE LOST !!!')

                    # ask if they wanna play again
                    new_game_or_not()


        hit_or_stand()

    give_cards()


black_jack()
