Projectevaluatie
Inleiding

In dit project heb ik een Python-programma ontwikkeld dat fungeert als een Trojan Framework met een commando- en controleserver (C&C) voor het beheren van verschillende functionaliteiten op de target host. Het programma maakt gebruik van de GitHub API om te communiceren met een externe GitHub-repo.
Algemene werking van het programma

Het main.py-bestand maakt automatisch verbinding met de externe GitHub-repo en haalt het actions.json-bestand op om te controleren of er acties moeten worden uitgevoerd. Vervolgens controleert het de configuratiebestand (config.json), dat fungeert als een gids om de modules te vinden en uit te voeren. Dit configuratiebestand kan op elk moment worden aangepast om modules toe te voegen indien deze dan ook worden toegevoegd in de /modules map van de repo. Het uitvoeren van de module gebeurt met behulp van de geïmporteerde CNC-module (Command and Control) die de functie execute_github_module() gebruikt en de uitvoer retourneert. De functie upload_data() wordt gebruikt om de gegevens naar het juiste bestand in de externe GitHub-opslagplaats te uploaden.
Functionaliteiten van het programma

Op dit moment biedt het programma de volgende functionaliteiten:

    Network_Discovery-module: retourneert alle IP-adressen van de adapters op de targethost.
    Wifi_info-module: haalt alle wifi-wachtwoorden op die aanwezig zijn op de targethost.
    Trojan-module: verzamelt en retourneert systeeminformatie van de targethost. Dit is de eerste module die wordt uitgevoerd op de doelmachine.
    Screenshot-module: maakt een schermafbeelding van het scherm van de target en retourneert deze in PNG formaat.

Uitvoering van de modules

Het programma voert de modules dynamisch uit, deze worden dus NIET geimporteerd. Door gebruik te maken van de functie execute_github_module(). Hiermee kan de code van de module dynamisch worden geïmporteerd en uitgevoerd met behulp van de library importlib importlib en exec() functie. Deze aanpak biedt flexibiliteit bij het toevoegen en uitvoeren van modules op basis van de acties die zijn gespecificeerd in het actions.json-bestand.
Moeilijkheden die zijn ondervonden

Tijdens de ontwikkeling van het project zijn de volgende moeilijkheden ondervonden:

    Dynamische uitvoering van modules: Het implementeren van de dynamische uitvoering van modules was uitdagend. Er moest onderzoek worden gedaan en geëxperimenteerd worden met verschillende bibliotheken en functies om de meest geschikte aanpak te vinden.
    Omgaan met verschillende gegevensindelingen: Het uploaden van gegevens naar de externe GitHub-repo vereiste het omgaan met verschillende gegevensindelingen en formaten (bv .png). Er was wat trial-and-error nodig om ervoor te zorgen dat de gegevens correct werden geformatteerd en geüpload.

Lessen geleerd en persoonlijke ervaring

Het werken aan dit project was een plezierige ervaring, omdat het aansloot bij mijn persoonlijke intresse.

Het stelde me in staat om concepten met betrekking tot botnets en het op afstand besturen van machines te verkennen. Als extra stap ben ik van plan om het programma te testen op persoonlijk bezeten virtuele machines om de functionaliteit als botnet te evalueren, uitsluitend voor educatieve doeleinden natuurlijk.

Over het algemeen heeft dit project mij waardevolle inzichten geboden in de functionaliteit van python libraries en modules.
