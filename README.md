English:

Crawler v1.0

This program is a crawler and can be used to extract some links and information on a website.</br>
It can be used with CLI and you can use the following features.</br>


Return the results in terminal</br>
$ python3 cli.py [--url|u] https://example.net</br>

Exporter les résultats dans un fichier .txt</br>
$ python3 cli.py [--url|u] https://example.net [--export] file_name.txt</br>

The report is a .txt file with the following informations:</br>

-Each unique URLs</br>
-URLs pointing to same domain</br>
-URLs pointing to external domain</br>
-URLs using authentication and other forms (contact, mail...)</br>
-URLs protected by login and password</br>
-URLs with 404 error</br>

Manual:</br>

Help:</br>
$ python3 cli.py --help</br>

usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]</br>

Crawl a website and get all links</br>

options:</br>
  -h, --help         show this help message and exit</br>
  --url URL, -u URL  This is the URL you want to crawl</br>
  --export FILENAME.txt    Export output to a file, give it a file name</br>
  --404              Return links with 404 error</br>
  --external-url     Return links with external domain name</br>
  --protected-url    Return links with login page</br>


Return only 404 error webpages</br>
$ python3 cli.py [--url|u] https://example.net --404</br>

Return only URLs pointing to external domain</br>
$ python3 cli.py [--url|u] https://example.net --external-url</br>

Return only URLs with authentication form</br>
$ python3 cli.py [--url|u] https://example.net --protected_url</br>


________________________________________________________________________________________</br>


Francais:</br>

Premiere version du crawler</br>

Ce programme est un crawler qui permet de parcourir un lien et extracter des informations. </br>
Le programme est utilisable en ligne de commande et proposer les fonctionnalités suivantes :</br>

Afficher les resultats dans le terminal<br />
$ python3 cli.py [--url|u] https://example.net</br>

Exporter les résultats dans un fichier .txt</br>
$ python3 cli.py [--url|u] https://example.net [--export] nom_fichier.txt</br>

Le rapport généré est au format texte et contient les informations suivantes :</br>

-Le nombre d'URL unique</br>
-Les URL's pointant sur le même domaine</br>
-Les adresses pointant sur un domaine externe</br>
-Les adresses contenant des formulaires (tout formulaire confondu)</br>
-Les adresses contenant des pages protégés par mot de passe</br>
-Le nombre d'adresse pointant sur le même nom de domaine renvoyant une page 404</br>

Le mode d'utilations est le suivant:</br>

Help du crawler:</br>
$ python3 cli.py --help</br>

usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]</br>

Crawl a website and get all links</br>

options:</br>
  -h, --help         show this help message and exit</br>
  --url URL, -u URL  This is the URL you want to crawl</br>
  --export FILENAME.txt    Export output to a file, give it a file name</br>
  --404              Return links with 404 error</br>
  --external-url     Return links with external domain name</br>
  --protected-url    Return links with login page</br>


Retourner uniquement les pages retournant un code erreur 404</br>
$ python3 cli.py [--url|u] https://example.net --404</br>

Retourner uniquement les adresses pointant vers un nom de domaine externe</br>
$ python3 cli.py [--url|u] https://example.net --external-url</br>

Retourner uniquement les pages nécessitant une authentification</br>
<br>$ python3 cli.py [--url|u] https://example.net --protected_url</br>
