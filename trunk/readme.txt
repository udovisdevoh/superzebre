1er mai 2009

Nom du projet:
	Super Z�bre
	
Description:
	Programme permettant l'encadrement et l'automatisation de la gestion de projet de d�veloppement logiciel

Membres de l'�quipe:
	Guillaume Lacasse
	Fran�ois Pelletier
	Kevin Melan�on
	�tienne-Joseph Charles
	Frederik Pion
	
Fonctionnalit�s disponibles:
	Analyse textuelle automatis�e
	Cr�ation et modification de CRCs
	Cr�ation et modification de cas d'usage
	Application en mode serveur-client
	Couche persistante permettant de sauvegarder son projet sur le seveur

Comment utiliser le programme:
	Ex�cuter pr�alablement l'application serveur (fichier server.py)
	Ex�cuter l'application client (fichier client.py)
	Attention! Il y a un bug d'encodage dans le projet
	alors il faut ex�cuter client.py dans �clipse, pas en standalone
	
Mod�le de base de donn�es
	Table projet:
		id: cl� primaire unique
		nom: nom du projet (cl� naturelle
		data: (donn�e s�rialis�s)
			texte de l'analyse textuelles
			mots class�s
			cas d'usages en mode textuel