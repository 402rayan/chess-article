import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

class RequestMaker:
	def __init__(self):
		pass

	# récupère les données d'un joueur donné
	def getPlayerData(playerName):
		assert isinstance(playerName,str), "le nom du joueur doit être une chaine de caractère"
		lien = f"https://api.chess.com/pub/player/{playerName}"
		response = requests.get(lien, headers=headers)
		status = response.status_code
		return response.json() if status == 200 else f"Réponse non-autorisée pour {playerName}, code d'erreur: {status}"
  
	# récupère les noms de tous les joueurs ayant un titre donné (GM, IM, FM, WGM, WIM, WFM)
	def getPlayerNamesByTitle(title):
		assert isinstance(title,str), "le titre doit être une chaine de caractère"
		lien = f"https://api.chess.com/pub/titled/{title}"
		response = requests.get(lien, headers=headers)
		status = response.status_code
		return response.json() if status == 200 else f"Réponse non-autorisée pour {title}, code d'erreur: {status}"

	# récupère les archives de parties d'un joueur donné
	def retrieveAllGamesFromPlayerName(playerName):
		assert isinstance(playerName,str), "le nom du joueur doit être une chaine de caractère"
		mois = ["0" + str(i) if i < 10 else str(i) for i in range(1,13)]
		annees = [str(i) for i in range(2005,2025)]
		for annee in annees:
			for m in mois:
				lien = f"https://api.chess.com/pub/player/{playerName}/games/{annee}/{m}"
				response = requests.get(lien, headers=headers)
				status = response.status_code
				print("En cours de traitement: ", status)