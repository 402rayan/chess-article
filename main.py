from requestMaker import RequestMaker as rm # Import the class RequestMaker from RequestMaker.py


# print(rm.getPlayerData("Hikaru")) # https://api.chess.com/pub/player/Hikaru
# print(rm.getPlayerNamesByTitle("GM")) # https://api.chess.com/pub/titled/GM

print(rm.retrieveAllGamesFromPlayerName("402ray")) # https://api.chess.com/pub/player/Hikaru/games/2021/01

# https://lumbrasgigabase.com/en/download-in-pgn-format-en/ LIENS POUR DL LES PARTIES EN PGN