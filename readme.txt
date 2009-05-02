1er mai 2009

Nom du projet:
	Super Zèbre
	
Description:
	Programme permettant l'encadrement et l'automatisation de la gestion de projet de développement logiciel

Membres de l'équipe:
	Guillaume Lacasse
	François Pelletier
	Kevin Melançon
	Étienne-Joseph Charles
	Frederik Pion
	
Fonctionnalités disponibles:
	Analyse textuelle automatisée
	Création et modification de CRCs
	Création et modification de cas d'usage
	Application en mode serveur-client
	Couche persistante permettant de sauvegarder son projet sur le seveur

Comment utiliser le programme:
	Exécuter préalablement l'application serveur (fichier server.py)
	Exécuter l'application client (fichier client.py)
	Attention! Il y a un bug d'encodage dans le projet
	alors il faut exécuter client.py dans éclipse, pas en standalone
	
Modèle de base de données
	Table projet:
		id: clé primaire unique
		nom: nom du projet (clé naturelle
		data: (donnée sérialisés)
			texte de l'analyse textuelles
			mots classés
			cas d'usages en mode textuel