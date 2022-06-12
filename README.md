<br>English:</br>

<br>Crawler v1.0</br>  

<br>This program is a crawler and can be used to extract some links and information on a website.</br>
<br>It can be used with CLI and you can use the following features.</br>


<br>Return the results in terminal</br>
<br>$ python3 cli.py [--url|u] https://example.net</br>

<br>Exporter les résultats dans un fichier .txt</br>
<br>$ python3 cli.py [--url|u] https://example.net [--export] file_name.txt</br>

<br>The report is a .txt file with the following informations:</br>

<br>-Each unique URLs</br>
<br>-URLs pointing to same domain</br>
<br>-URLs pointing to external domain</br>
<br>-URLs using authentication and other forms (contact, mail...)</br>
<br>-URLs protected by login and password</br>
<br>-URLs with 404 error</br>

<br>Manual:</br>

<br>Help:</br>
<br>$ python3 cli.py --help</br>

<br>usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]</br>

<br>Crawl a website and get all links</br>

<br>options:</br>
<br>  -h, --help         show this help message and exit</br>
<br>  --url URL, -u URL  This is the URL you want to crawl</br>
<br>  --export FILENAME.txt    Export output to a file, give it a file name</br>
<br>  --404              Return links with 404 error</br>
<br>  --external-url     Return links with external domain name</br>
<br>  --protected-url    Return links with login page</br>


<br>Return only 404 error webpages</br>
<br>$ python3 cli.py [--url|u] https://example.net --404</br>

<br>Return only URLs pointing to external domain</br>
<br>$ python3 cli.py [--url|u] https://example.net --external-url</br>

<br>Return only URLs with authentication form</br>
<br>$ python3 cli.py [--url|u] https://example.net --protected_url</br>


<br>________________________________________________________________________________________</br>


<br>Francais:</br>

<br>Premiere version du crawler</br>

<br>Ce programme est un crawler qui permet de parcourir un lien et extracter des informations. </br>
<br>Le programme est utilisable en ligne de commande et proposer les fonctionnalités suivantes :</br>

<br>Afficher les resultats dans le terminal<br />
<br>$ python3 cli.py [--url|u] https://example.net</br>

<br>Exporter les résultats dans un fichier .txt</br>
<br>$ python3 cli.py [--url|u] https://example.net [--export] nom_fichier.txt</br>

<br>Le rapport généré est au format texte et contient les informations suivantes :</br>

<br>-Le nombre d'URL unique</br>
<br>-Les URL's pointant sur le même domaine</br>
<br>-Les adresses pointant sur un domaine externe</br>
<br>-Les adresses contenant des formulaires (tout formulaire confondu)</br>
<br>-Les adresses contenant des pages protégés par mot de passe</br>
<br>-Le nombre d'adresse pointant sur le même nom de domaine renvoyant une page 404</br>

<br>Le mode d'utilations est le suivant:</br>

<br>Help du crawler:</br>
<br>$ python3 cli.py --help</br>

<br>usage: Crawler [-h] --url URL [--export EXPORT] [--404] [--external-url] [--protected-url]</br>

<br>Crawl a website and get all links</br>

<br>options:</br>
<br>  -h, --help         show this help message and exit</br>
<br>  --url URL, -u URL  This is the URL you want to crawl</br>
<br>  --export FILENAME.txt    Export output to a file, give it a file name</br>
<br>  --404              Return links with 404 error</br>
<br>  --external-url     Return links with external domain name</br>
<br>  --protected-url    Return links with login page</br>


<br>Retourner uniquement les pages retournant un code erreur 404</br>
<br>$ python3 cli.py [--url|u] https://example.net --404</br>

<br>Retourner uniquement les adresses pointant vers un nom de domaine externe</br>
<br>$ python3 cli.py [--url|u] https://example.net --external-url</br>

<br>Retourner uniquement les pages nécessitant une authentification</br>
<br><br>$ python3 cli.py [--url|u] https://example.net --protected_url</br>
