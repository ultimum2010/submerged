# Dialog Henning fra CoWork - 2024-11-04

# Open Source

* Flott at dere deler

# Testing

* Hvordan tester dere?
	* Vi står på banen og hvordan vi har lyst til å komme oss dit
* Vi hadde blokkprogrammering før og hadde egne metoder
	* så har vi lagd drive_gyro_dist
		* med ulike parametere

# Koden

* Hvor lenge har du skrevet i Python?
	* Fra i fjor
	* Er komfortabel med det?
		* Synes når jeg kan det at det går mye raskere å skrive
		* De andre synes det er greit
			* jobbet med oppdrag
* Skrev Chewbacca i fjor
	* drive_gyro_turn er ny
	* akselerasjonen i drive_gyro_dist er ny
		* rolig opp til end_speed og så begynne å senke farta
* Er det noen store utfordringer?
	* Fikk hjelp til å skrive og forstå Chewbacca klassen
* Ganske godt oppsett på koden
	* god selvtillitt
	* veldig bra med oppdragsfiler som bruker Chewbacca

# Tilbakemelding fra Henning systemutvikler

* for andre lesere av koden
* for oss selv når vi skal lese koden senere
* Hvordan kan en som leser kodestruktur for første gang orientere seg?
	* Tidligere løste vi et eller to oppdrag og kom tilbake med roboten
	* Denne gangen har vi laget løypene
		* Vi har løype0 og løype1
			* Hvorfor heter prog nr 2 m08 habitat?
				* Så program nr 2 skal løse oppdrag 8 på banen
		* Vi skal ha fem løyper
		* Vi har kalibrering av gyro
		* Vi har vask_hjul hvis roboten har samlet mye støv
			* motorene går mens vi kan vaske hjulene
* Ganske stor fil Chewbacca med ganske store metoder
	* Hvordan kan du redusere de?
		* Vi har tatt ting ut av store metoder
			* akselerasjon
	* Har du kode som du skriver flere ganger?
		* Da kan du ha ekstra metode eller egen plass
* Lesing av logiske begreper
	* elif (not rygger)
		* betyr det at det går rett frem?
	* Prøv å lese det med hyggelige logisk vri
		* metoden kan hete kjøre-fremover
	* Hvis du bruker not kan du prøve å snu på logikken
	* Hvis det er noe som leser litt rart kan du se om du kan legge det bak noe som leser på en hyggeligere måte
* Veldig bra at dere splittet kode i flere funksjoner
	* ikke alltid lett
	* klarer du å finne variabler og logiske uttrykk som brukes flere ganger og som leser litt vanskelig
		* samme linjene som gjentas kan puttes i en metode

# Git

* Hvordan er det å bruke git?
	* Når jeg legger ut er det tilgjengelig for alle andre?
* Har en del utkommentert kode
	* Husk at Git kan hente det for deg om du sletter
