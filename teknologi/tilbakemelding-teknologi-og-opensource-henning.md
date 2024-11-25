# Tilbakemelding - Teknologi og Open Source

Hei, Team Mission Possilbe! Her er en oppsummering av feedack fra møte jeg hadde med Sivert, Arild og Mufrid.

Jeg har lest gjennom mesteparten av innholdet i git-repo deres og syns det er veldig inspirerende! Det jeg mener er
spesielt inspirerende er hvordan dere jobber med forskning og teknologi med gode kjerneverdier, og ikke minst deres
ønske om å dele erfaringener med andre som ønsker å bli en del av First Lego Leauge!

Mitt inntrykk er at dere har relativt god kontroll på hvordan løse de forskjellige oppgavene, og ikke minst teknologien.
Her kommer noen tilbakemeldinger som jeg håper vil hjelpe med å støtte oppp øsket deres om å dele med andre hva dere har
lært etter 7 år med First Lego League!

## Open Source
Det er veldig kult å dele hva man gjør, spesielt med fokus på å hjelpe andre i gang med tilsvarende prosjekter. Derfor
tenker jeg det kan være veldig fint å tenke på hva som er det første man ser når man går inn på repo deres i GitHub.
I dag har dere en `README.md` som beskriver teamet deres og ønsket om å dele, men kanskje dere også klarer å skrive litt
om hvordan leseren bør navigere seg og lese koden?

Et tips til å klare det kan være å utvide `README.md` med et par seksjoner. Ofte, i Open Source-prosjekter, ser man
tilsvarende oppbygning:
```markdown
Prosjekttittel og prosjektbeskrivelse

## Om Oss
Her kan dere ha akkurat den samme teksten dere har i dag.

## Kom i gang
Her kan man f.eks beskrive litt hvordan man kommer i gang med First Lego Leauge, og hvordan sette opp det relevenate
for teknologien deres.

## Bidra
Ofte kan det være fint å tipse nykommere om hvordan man kan bidra med videreutvikling av prosjektet.
```

En siste ting, når det gjelder Open Source. Selv om det kanskje ikke er superviktig for dette prosjektet kan det være
lurt av dere å tenke på hvordan dere ønsker at kode og forskningen skal kunne bli tatt i bruk av andre. Slik det det er
nå lar det hvem som helst ta det videre uten nødvendigvis å annerkjenne kilden. Det kan man løse ved å legge til en
såkalt lisensfil. Den beskriver hvordan man skal gå frem dersom man ønsker å gjenbruke og/eller videreutvikle på
hele eller deler av prosjektet deres. Lisensfiler kan være litt vanskelige å forstå seg på, så her kan det være lurt å
f.eks. ta en runde med Arild, Mufrid eller meg hvis dere vil legge til en. GitHub har selv lagt ut [en liten guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
slik at det å velge riktig lisens blir litt lettere. For dere så tror jeg det holder med MIT-lisens.

## Prosjektstrukturen
Strukturen dere har i prosjektet fremstår veldig ryddig. Ting er plassert i forståelige undermapper,
og det var lett å navigere. Det jeg bet meg merke til er at dere har litt forskjellige konvensjoner på hvordan dere
navngir filer, og dere har noen mapper som inneholder både kodefiler og tekstfiler.

Dette er ikke et stort problem, men det kan kanskje bli det dersom f.eks. prosjektets innhold dobbler i størrelse.
Ser dere noen andre utfordringer dette kan introdusere for prosjektet?

## Koden
Det er veldig fint med en gjenbrukbar klasse som håndterer den vaskelige logikken slik at dere kan fokusere på å løse
oppggavene i rundefiler. Jeg får også inntrykk av at dere har god forståelse for koden deres når jeg ser at dere har
utvidet `chewbacca` med blant annet jevn svinging med akselerasjon, og hvordan dere utvider med nye program for å løse
hver oppgave.

Slik jeg forstår det har dere prøvd å **refactorere** deler av koden deres ved å bl.a. splitte store funksjoner inn i
mindre. Dette er veldig bra og kan bidra til kode som er enklere å lese samt jobbe med generelt. Her er litt av det
vi pratet om på møtet som dere kan vurdere neste gang dere gjør en refactor. Husk at dette ikke er en fasit, og
det finnes utallige måter å gå frem på, så finn en løsning som passer teamets måte å skrive kode på.

### Hvordan gå frem for å splitte opp store metoder
1. **Se etter kode som gjentar seg flere steder.** Dette kan være et tegn på at koden kan brytes ut i en hjelpemetode.
   F.eks. ser jeg den samme koden i `drive_gyro_dist` og `drive_gyro_turn`, for å sette `start_speed` ned hvis den er
   høyere enn max fart. Dette er et fint eksempel på noe som kan brytes ut i en mindre metode, og kanskje det gjør koden
   mer leselig?
```python
#setter start_speed ned hvis start_speed er høyere enn max fart
if start_speed > v1:
    for i in range(start_speed, 0, -1):
        v1 = math.sqrt(target_distance * Chewbacca.ACCELERATION + 0.5*i**2 + 0.5*end_speed**2)
        if i <= v1:
            start_speed = i
            break

# Kan f.eks. se slik ut hvis det som står inne i if-en er i en metode, men kanskje dere finner på et bedre navn selv.
if start_speed > v1:
    set_ned_start_speed()
```

2. **Se etter kode som er tung å lese.** F.eks. ser jeg i `drive_gyro_turn` at retningen som settes inneholder en del
   logikk og spenner over flere kodelinjer. Jeg får intrykk av at alle disse kodelinjene handler om å sette rettning,
   og kan f.eks. flyttes ut i en metode med beskrivende navn. Da slipper leseren å tenke på hvordan det gjøres, men
   kan kan heller konstatere hva som gjøres. Et forslag kan være å teste lesbarheten på koden dere har skrevet på andre
   i temaet. Det blir ofte lettere da å finne ut hva man skal gjøre med koden.
```python
def drive_gyro_turn(self, speed, turn_radius, turn_angle, turn_right = True, start_speed = 0, end_speed = 0, stop_at_end = True, kP=1.0):

    # svingens retning vises i turn_right variabelen og turn_angle gjøres alltid positiv.
    if turn_right & (turn_angle >= 0) :
        turn_right = True
        turn_angle = turn_angle * 1
    
    elif turn_right & (turn_angle < 0) :
        turn_right = False
        turn_angle = turn_angle * -1
    
    elif (turn_right == False) & (turn_angle >= 0) :
        turn_right = False
        turn_angle = turn_angle * 1
    
    elif (turn_right == False)  & (turn_angle < 0) :
        turn_right = True
        turn_angle = turn_angle * -1
    
    # Resten av koden under ...

# Kanskje det kunne sett litt slik ut? Igjen, kan det hende at dere har et bedre navn for metoden siden dere kjenner koden best.
def drive_gyro_turn(self, speed, turn_radius, turn_angle, turn_right = True, start_speed = 0, end_speed = 0, stop_at_end = True, kP=1.0):
    set_turn_direction(turn_right, turn_angle)
    
    # Resten av koden under ...
```

### Hvordan oppnå mer leselig kode?
1. **Beskrivende variabel- og metodenavn** hjelper veldig for en leser. Dette syns jeg generelt sett dere er veldig gode
   på, men jeg ser noen variabler som `v`, `r1`, `r2`, osv. Da er det fort gjort å gå i surr med hva variabelen er ment for.
   Dette må dere gjøre en vurdering på, men hvis `v` og `r` står for ting som `velocity` og `radius` kan det lønne seg å
   benytte ordene istedet for første bokstav.

2. **Prøv å identifisere boolske uttrykk som kanskje kan skrives enklere.** Her tenker jeg det er spesielt to ting man
   kan se etter:
    * Noen boolske uttrykk virker logiske første gang man skriver de, men når man kommer tilbake til de senere ser man at
      dersom man "snur de på hodet" lan det bli lest litt lettere. F.eks. `if not rygger` kan sansynligvis skrives
      som `if kjorer_fremover`.
    * Andre boolske uttrykk kan bli vanskelige å forstå når man slår sammen flere uttrykk med en logisk AND eller OR.
      F.eks. kan man flytte uttrykke ut i en funksjon, sånn som dette: `if (not rygger) & turn_right:` blir til
      `if kjorer_fremover_og_svinger_hoyre():`, som da igjen gjør at leseren slipper å tenke på hvordan det gjøres, og
      heller kan konstatere hva som skjer.

3. **Dersom kode ikke er så enkelt å flytte ut, kan det hjelpe med en kommentar eller to.** Dette ser jeg dere gjør
   flere steder og det er bra. Fortsett med dette, og kanskje det å prøve å beskrive koden med ord hjelper med å skjønne
   den bedre selv også! :)

### Måter å redusere størrelsen på en kodefil
- Det er mange konfigurasjonsvariabler i starten av `chewbacca` som brukes mest i konstruktøren. Dette går helt fint,
  men det gjør også at man må scrolle litt for å komme ned til det faktiske koden.
    - Finnes det en måte å holde disse utenfor selve `__init__.py`?
- Kommentert ut og ubrukt kode kan fjernes. Her kan man ta nytte av hvordan `git` fungerer. Der lagres all historikk
  og derfor kan dere trygt fjerne kode som ikke er i bruk eller kommentert ut. Så lenge dere fortsetter med de gode
  commit-meldingene dere har til nå vil dette gå helt fint!

### Alt i alt, veldig bra jobba!
