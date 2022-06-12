English:

Crawler v1.0

This program is a crawler and can be used to extract some links and information on a website.
It can be used with CLI and you can use the following features.


Return the results in terminal
$ python3 cli.py [--url|u] https://example.net

Exporter les résultats dans un fichier .txt
$ python3 cli.py [--url|u] https://example.net [--export] file_name.txt

The report is a .txt file with the following informations:

-Each unique URLs
-URLs pointing to same domain
-URLs pointing to external domain
-URLs using authentication and other forms (contact, mail...)
-URLs protected by login and password
-URLs with 404 error

Manual:

Help:
$ python3 cli.py --help

usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]

Crawl a website and get all links

options:
  -h, --help         show this help message and exit
  --url URL, -u URL  This is the URL you want to crawl
  --export FILENAME.txt    Export output to a file, give it a file name
  --404              Return links with 404 error
  --external-url     Return links with external domain name
  --protected-url    Return links with login page


Return only 404 error webpages
$ python3 cli.py [--url|u] https://example.net --404

Return only URLs pointing to external domain
$ python3 cli.py [--url|u] https://example.net --external-url

Return only URLs with authentication form
$ python3 cli.py [--url|u] https://example.net --protected_url


________________________________________________________________________________________


Francais:

Premiere version du crawler

Ce programme est un crawler qui permet de parcourir un lien et extracter des informations. 
Le programme est utilisable en ligne de commande et proposer les fonctionnalités suivantes :

Afficher les resultats dans le terminal<br />
$ python3 cli.py [--url|u] https://example.net

Exporter les résultats dans un fichier .txt
$ python3 cli.py [--url|u] https://example.net [--export] nom_fichier.txt

Le rapport généré est au format texte et contient les informations suivantes :

-Le nombre d'URL unique
-Les URL's pointant sur le même domaine
-Les adresses pointant sur un domaine externe
-Les adresses contenant des formulaires (tout formulaire confondu)
-Les adresses contenant des pages protégés par mot de passe
-Le nombre d'adresse pointant sur le même nom de domaine renvoyant une page 404

Le mode d'utilations est le suivant:

Help du crawler:
$ python3 cli.py --help

usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]

Crawl a website and get all links

options:
  -h, --help         show this help message and exit
  --url URL, -u URL  This is the URL you want to crawl
  --export FILENAME.txt    Export output to a file, give it a file name
  --404              Return links with 404 error
  --external-url     Return links with external domain name
  --protected-url    Return links with login page


Retourner uniquement les pages retournant un code erreur 404
$ python3 cli.py [--url|u] https://example.net --404

Retourner uniquement les adresses pointant vers un nom de domaine externe
$ python3 cli.py [--url|u] https://example.net --external-url

Retourner uniquement les pages nécessitant une authentification
$ python3 cli.py [--url|u] https://example.net --protected_url
