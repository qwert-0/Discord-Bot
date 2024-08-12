# import os

# game_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


# class Player:
#     def __init__(self, mark):
#         self.mark = mark

#     """
#     [
#         0,1,2,
#         3,4,5,
#         6,7,8
#     ]
#     """

#     def checkifwin(self):
#         winner = False
#         temp_store = 0
#         if (
#             game_board[0][0] == game_board[0][1]
#             and game_board[0][1] == game_board[0][2]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[1][0] == game_board[1][1]
#             and game_board[1][1] == game_board[1][2]
#             and game_board[1][0] != "-"
#         ):
#             temp_store = game_board[1][0]
#             winner = True
#         elif (
#             game_board[2][0] == game_board[2][1]
#             and game_board[2][1] == game_board[2][2]
#             and game_board[2][0] != "-"
#         ):
#             temp_store = game_board[2][6]
#             winner = True
#         elif (
#             game_board[0][0] == game_board[1][0]
#             and game_board[1][0] == game_board[2][0]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[0][1] == game_board[1][1]
#             and game_board[1][1] == game_board[2][1]
#             and game_board[0][1] != "-"
#         ):
#             temp_store = game_board[1]
#             winner = True
#         elif (
#             game_board[0][2] == game_board[1][2]
#             and game_board[1][2] == game_board[2][2]
#             and game_board[0][2] != "-"
#         ):
#             temp_store = game_board[0][2]
#             winner = True
#         elif (
#             game_board[0][0] == game_board[1][1]
#             and game_board[1][1] == game_board[2][2]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[0][2] == game_board[1][1]
#             and game_board[1][1] == game_board[2][0]
#             and game_board[0][2] != "-"
#         ):
#             temp_store = game_board[0][2]
#             winner = True
#         else:
#             winner = False
#         if winner:
#             return temp_store
#         else:
#             return winner


# def display_board(gameboard):
#     for row in gameboard:
#         print()
#         for i in row:
#             print(i, end=" ")
#     print()


# player1 = Player("-")
# player2 = Player("-")


# def place_mark(n, gameboard, token):
#     if n == 1:
#         gameboard[0][0] = token
#     elif n == 2:
#         gameboard[0][1] = token
#     elif n == 3:
#         gameboard[0][2] = token
#     elif n == 4:
#         gameboard[1][0] = token
#     elif n == 5:
#         gameboard[1][1] = token
#     elif n == 6:
#         gameboard[1][2] = token
#     elif n == 7:
#         gameboard[2][0] = token
#     elif n == 8:
#         gameboard[2][1] = token
#     elif n == 9:
#         gameboard[2][2] = token


# def tictactoe(p1, p2):

#     print("Let the TicTacToe begin!!!")
#     print("Player 1 choose your mark: ")
#     p1.mark = input("X/O: ").upper()
#     if p1.mark == "X":
#         p2.mark = "O"
#     elif p1.mark == "O":
#         p2.mark = "X"
#     whose_chance = 1
#     num_of_chances = 0
#     display_board(game_board)
#     while True:
#         if whose_chance == 1:
#             place = int(input("Player 1: "))
#             token = p1.mark
#         elif whose_chance == 2:
#             place = int(input("Player 2: "))
#             token = p2.mark
#         if 0 < place <= 9:
#             place_mark(place, game_board, token)
#             num_of_chances += 1
#             if whose_chance == 1:
#                 whose_chance = 2
#             elif whose_chance == 2:
#                 whose_chance = 1
#             os.system("cls")
#         else:
#             os.system("cls")
#             print("Invalid Input. Try Again.")
#         display_board(game_board)
#         if p1.checkifwin():
#             print("Player 1 wins!!!!")
#             break
#         elif p2.checkifwin():
#             print("Player 2 wins!!!!")
#             break
#         elif num_of_chances == 9:
#             print("TIE!!!!\nThat was a close match gg.")
#             break


# tictactoe(player1, player2)


# class tictactoe:
#     def __init__(self, gameboard, p1, p2) -> None:
#         self.gameboard = gameboard
#         self.p1 = p1
#         self.p2 = p2

#     def checkifwin(self, game_board):
#         winner = False
#         temp_store = 0
#         if (
#             game_board[0][0] == game_board[0][1]
#             and game_board[0][1] == game_board[0][2]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[1][0] == game_board[1][1]
#             and game_board[1][1] == game_board[1][2]
#             and game_board[1][0] != "-"
#         ):
#             temp_store = game_board[1][0]
#             winner = True
#         elif (
#             game_board[2][0] == game_board[2][1]
#             and game_board[2][1] == game_board[2][2]
#             and game_board[2][0] != "-"
#         ):
#             temp_store = game_board[2][6]
#             winner = True
#         elif (
#             game_board[0][0] == game_board[1][0]
#             and game_board[1][0] == game_board[2][0]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[0][1] == game_board[1][1]
#             and game_board[1][1] == game_board[2][1]
#             and game_board[0][1] != "-"
#         ):
#             temp_store = game_board[1]
#             winner = True
#         elif (
#             game_board[0][2] == game_board[1][2]
#             and game_board[1][2] == game_board[2][2]
#             and game_board[0][2] != "-"
#         ):
#             temp_store = game_board[0][2]
#             winner = True
#         elif (
#             game_board[0][0] == game_board[1][1]
#             and game_board[1][1] == game_board[2][2]
#             and game_board[0][0] != "-"
#         ):
#             temp_store = game_board[0][0]
#             winner = True
#         elif (
#             game_board[0][2] == game_board[1][1]
#             and game_board[1][1] == game_board[2][0]
#             and game_board[0][2] != "-"
#         ):
#             temp_store = game_board[0][2]
#             winner = True
#         else:
#             winner = False
#         if winner:
#             return temp_store
#         else:
#             return winner

#     def place(self, mark, gameboard, i, j):
#         if gameboard[i][j] == "-":
#             gameboard[i][j] = mark
#             return True
#         else:
#             return False

#     def place_mark(self, n, gameboard, token):
#         if n == 1:
#             gameboard[0][0] = token
#         elif n == 2:
#             gameboard[0][1] = token
#         elif n == 3:
#             gameboard[0][2] = token
#         elif n == 4:
#             gameboard[1][0] = token
#         elif n == 5:
#             gameboard[1][1] = token
#         elif n == 6:
#             gameboard[1][2] = token
#         elif n == 7:
#             gameboard[2][0] = token
#         elif n == 8:
#             gameboard[2][1] = token
#         elif n == 9:
#             gameboard[2][2] = token

#     def tictactoe(self, gameboard, p1, p2):
#         print("~~~~~~~~~TicTacToe~~~~~~~~~")

# from bs4 import BeautifulSoup
# import requests

# s = "this is a short sentince"
# q = s.split()
# query = "+".join(q)

# URL = f"https://www.google.com/search?q={query}"
# page = requests.get(URL)
# bs = BeautifulSoup(page.text, "html.parser")
# print(bs)


import praw
import random

reddit = praw.Reddit(
    client_id="Qq15oEA8RFB62o9g7b3i2g",
    client_secret="EgwmLX7GUumSYivhNcFLDQwqE7M-HQ",
    username="",
    user_agent="testscript by u/",
    check_for_async=False,
)


# post = reddit.post(
#     "https://www.reddit.com/r/cats/comments/zqeotp/foster_fail_a_story_in_photos/?utm_source=share&utm_medium=web2x&context=3"
# )
# print(post.shorlink)

post = reddit.submission(
    url="https://www.reddit.com/r/cats/comments/zqeotp/foster_fail_a_story_in_photos/?utm_source=share&utm_medium=web2x&context=3"
)

post2 = reddit.submission(
    url="https://www.reddit.com/r/MemeVideos/comments/zqgx38/the_bois/?utm_source=share&utm_medium=web2x&context=3"
)



print(post.url)
print(post2.url)
