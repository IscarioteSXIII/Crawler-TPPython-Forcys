# Crawler-TPPython-Forcys
Premiere version du crawler, sans utilisation de selenium

Ce programme est un crawler qui permet de parcourir un lien et extracter des informations. 
Le programme est utilisable en ligne de commande et proposer les fonctionnalités suivantes :

Retourner un rapport dans le terminal<br />
$ python3 cli.py [--url|u] https://example.net

Retourner un rapport dans un fichier passé en paramètre
$ python3 cli.py [--url|u] https://example.net [--export] nom_fichier

Le rapport généré est au format texte et contient les informations suivantes :

-Le nombre d'URL unique
-Les URL's pointant sur le même domaine
-Les adresses pointant sur un domaine externe
-Les adresses contenant des formulaires (tout formulaire confondu)
-Les adresses contenant des pages protégés par mot de passe
-Le nombre d'adresse pointant sur le même nom de domaine renvoyant une page 404

Le mode d'utilations est le suivant:

Aide du crawler:
$ python3 cli.py --help

usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]

Crawl a website and get all links

options:
  -h, --help         show this help message and exit
  --url URL, -u URL  This is the URL you want to crawl
  --export EXPORT    Export output to a file, give it a file name
  --404              Return links with 404 error
  --external-url     Return links with external domain name
  --protected-url    Return links with login page


Retourner uniquement les pages retournant un code erreur 404
$ python3 cli.py [--url|u] https://example.net --404

Retourner uniquement les adresses pointant vers un nom de domaine externe
$ python3 cli.py [--url|u] https://example.net --external-url

Retourner uniquement les pages nécessitant une authentification
$ python3 cli.py [--url|u] https://example.net --protected_url
