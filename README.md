# RailNL: Lijnvoering Intercitytreinen

Deze case gaat over het ontwerpen van de lijnvoering voor intercitytreinen. Specifiek richten we ons op de lijnvoering voor trajecten binnen een gegeven tijdsframe. Het doel is om een efficiënte lijnvoering te ontwerpen voor twee verschillende gebieden: Noord & Zuid Holland, en heel Nederland.

## Case Indeling

Om de case laagdrempelig aan te pakken, is deze in twee delen verdeeld. Het aantal stations, trajecten, verbindingen en het tijdsframe verschillen per deel:

### Deel 1: Lijnvoering voor Noord & Zuid Holland
- **Aantal stations:** 22
- **Aantal verbindingen:** 28
- **Aantal treinen/trajecten:** 7
- **Tijdsframe:** 120 minuten

### Deel 2: Lijnvoering voor heel Nederland
- **Aantal stations:** 61
- **Aantal verbindingen:** 89
- **Aantal treinen/trajecten:** 20
- **Tijdsframe:** 180 minuten

## Voorbeeld Traject

Een voorbeeld van een mogelijk traject is:
- **Traject:** [Castricum, Zaandam, Hoorn, Alkmaar]
- **Duur:** 59 minuten

Dit traject zou binnen het tijdsframe van 120 minuten voor Noord & Zuid Holland passen.


## Doel
Het doel van deze case is om een efficiënte en effectieve lijnvoering voor intercitytreinen te ontwerpen, waarbij rekening wordt gehouden met de specifieke eisen. Dit omvat het maximaliseren van de dekking van het netwerk binnen het gegeven tijdsframe.

## Doelfunctie
RailNL heeft recentelijk een doelfunctie opgesteld voor de kwaliteit van de lijnvoering. Als 100% van de verbindingen bereden wordt, levert dat 10000 punten op voor je lijnvoering. Anders krijg je een gedeelte daarvan. Maar hoe minder trajecten voor dezelfde service, hoe goedkoper. En in hoe minder tijd er in al die trajecten samen verbruikt wordt, hoe beter. Dus die factoren worden ook meegewogen in de doelfunctie:  
K = p * 10000 - (T * 100 + Min)  


waarbij:
- \( K \) de kwaliteit van de lijnvoering is,
- \( p \) de fractie van de bereden verbindingen (dus tussen 0 en 1),
- \( T \) het aantal trajecten,
- \( Min\) het aantal minuten in alle trajecten samen.  

## Installatie van vereisten

Om de vereisten te installeren, voer het volgende commando uit in de terminal:

```bash
python3 -m pip install -r requirements.txt
```
## Gebruik
De resultaten van deze case kunnen worden verkregen door:
1. De main te runnen
        - ```python3 main.py```
2. Als input meegeven welke deel van de case je wilt runnen
    - ```nederland```
    - ```holland```
    - **GEEN HOOFDLETTER**
3. Als input meegeven welke algoritme je wilt runnen

De algoritme.. vraagt om meer input, zie volgende stappen

## Structuur 
De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
    - **/code/algoritmes**: bevat de code voor algoritmes
    - **/code/classes**: bevat benodigde classes voor deze case
    - **/code/bouwblokjes**: bevat benodigde functies voor dit project

- **data**
    - **data/images**: bevat meerdere mappen. Elke map slaat de figuren van een bepaald algoritme
    - **data/input**: bevat de input files voor dit project
    - **data/output**: bevat meerdere mappen. Elke map slaat de output van een bepaald algoritme.  
    Sommige mappen scheiden de data in Holland en Nederland.

## Auteurs
- Alec
- Sjeng
- Addey