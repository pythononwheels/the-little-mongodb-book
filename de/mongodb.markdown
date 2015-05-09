# Über dieses Buch #

## Lizenz ##
Das kleine MongoDB Buch ist unter der Attribution-NonCommercial 3.0 
Unported license lizensiert . **Sie sollten für dieses Buch nicht bezahlt haben müssen.**

Sie können das Buch grundsätzlich vervielfältigen, verteilen, verändern oder sonstwie verbreiten.
Ich möchte sie jedoch bitten, das sie dies immer mit dem Hinweis auf
mich, Karl Seguin, tun und das Buch nicht für kommerzielle Zwecke verwenden.

Hier können sie den kompletten Inhalt der Lizenz einsehen: 

<http://creativecommons.org/licenses/by-nc/3.0/legalcode>

## Über den Autor ##
Karl Seguin ist ein Softwareentwickler mit Erfahrung in vielen Bereichen und Technologien.
Er ist ein Experte in .Net und Ruby. Des weiteren trägt er semi-aktiv zu OSS Projekten bei, 
ist technischer Autor und hält gelegentlich Vorträge. 
Bezogen auf MongoDB war er Kern Entwickler der C# MongoDB Library NoRM, schrieb
das interaktive tutorial [mongly](http://openmymind.net/mongly/) und entwickelte [Mongo Web Admin](https://github.com/karlseguin/Mongo-Web-Admin). 

Sein kostenloser service für Spiele Entwickler, [mogade.com](http://mogade.com/), 
läuft natürlich auf MongoDB.

Karl hat auch das
[The Little Redis Book](http://openmymind.net/2012/1/23/The-Little-Redis-Book/)
geschrieben

Hier findet ihr seinen blog: <http://openmymind.net>, und seine tweets via [@karlseguin](http://twitter.com/karlseguin)

## With Thanks To ##
Ein besonderes Dankeschön geht an [Perry Neal](http://twitter.com/perryneal) 
Der mir seine Augen, seinen Verstand und seine Leidenschaft geliehen hat. 
Deine Hilfe ist unbezahlbar. Ich danke dir.

## Aktuelle Version ##
Diese Version wurde von Asya Kamsky für MongoDB 2.6 aktualisiert.  

The aktuellen Original-Quellen dieses Buches findet ihr unter:

<http://github.com/karlseguin/the-little-mongodb-book>.

## Die deutsche Übersetzung ##
Die deutsche Übersetzung wurde erstellt von Klaas-Henning Zweck.
Die aktuellen Quellen der deutschen Übersetzung des Buches findet ihr hier:

<https://github.com/pythononwheels/the-little-mongodb-book>.

Und hier findet ihr die jeweils aktuellen PDF, ePub und mobi Versionen.

<http://pythononwheels.org/the-little-mongodb-book>

Anmerkungen zur deutschen Übersetzung (Rechtschreibung, Sprachstil etc.)
könnt ihr gerne via github, email (khz@tzi.org) oder twitter [@pythononwheels](http://twitter.com/pythononwheels) 
beisteuern.

# Einleitung #
 > It's not my fault the chapters are short, MongoDB is just easy to learn.
 
 > Es ist nicht meine Schuld das die Kapitel so kurz sind, MongoDB ist eben einfach leicht zu lernen.


Oftmals wird gesagt das sich Technologie rasant entwickelt. Es ist zwar richtig, das die Liste der Technologien 
und Techniken immer länger wird, aber ich war immer der Meinung das die fundamentalen Methoden und Technologien 
für Softwareentwickler sich eher langsam entwickeln. Man kann Jahre damit verbringen eine kleine, aber
wichtige Technik zu erlernen.
Auffällig ist jedoch, mit welcher Geschwindigkeit (heute) Technologien ersetzt werden. Scheinbar über Nacht wird  
etabliertes von einer veränderten Ausrichtung des Entwickler-Fokus bedroht.

Nichts könnte repräsentativer für diesen plötzlichen Wandel sein als der Erfolg der NoSQL Technologien gegen
die sehr gut etablierte Basis der relationalen Datenbanken (RDBMS). 
Vor nicht all zu langer Zeit basierte das Netz noch auf ein paar RDBMS und plötzlich hatten sich fünf
oder sechs NoSQL Systeme als eine echte Alternative etabliert.

Auch wenn diese Veränderungen scheinbar über Nacht kamen, benötigen sie in Wahrheit manchmal Jahre um
sich in der Breite zu etablieren. Der anfängliche Enthusiasmus bezieht sich auf eine relativ kleine Gruppe 
von Entwicklern und Firmen. 

Aus Fehlern wird gelernt, Lösungen werden verfeinert (refined) und wenn andere sehen das sich eine neue Technologie 
durchsetzt, dann fangen sie langsam an diese Technologie auch einzusetzen.
Noch einmal, das was ich eben gesagt habe trifft insbesondere für NoSQL DBs zu. Viele NoSQL Lösungsansätze sind
eben kein neuer Ersatz für bestehende Probleme sondern adressieren spezifische Bedarfe die von bestehenden (SQL)
Systemen nicht abgedeckt werden.

Nach dieser Einleitung sollte ich zunächst erläutern was NoSQL eigentlich bedeutet.
Es ist ein weiter Begriff der von verschiedenen Menschen unterschiedlich interpretiert wird.
Persönlich benutze ich den Begriff eher weit gefasst für Systeme im Bereich der Datenspeicherung.
Anders gesagt bedeutet NoSQL (für mich) der Überzeugung zu sein, das Datenpersistenz nicht die Verantwortung
eines einzelenen Systems ist.

Hersteller relationaler Datenbankmanagementsysteme versuchen seit langer Zeit ihre Systeme als eine "One size
fits all" Lösung zu positionieren. NoSQL Systeme hingegen gehe eher in Richtung kleinere Einheiten der 
Verantwortlichkeit um das beste tool für den jeweiligen Zweck wirksam einsetzen zu können.
Also kann es durchaus so sein, das ihr NoSQL Anwendungs-Stack auch relationale Datenbanken, wie zum Beispiel MySQL
beeinhaltet, sie aber eben auch z.B. Redis zur schnellen Datensuche und Hadoop für intensive
Datenverarbeitung nutzen. 
Kurz gesagt geht es beinm Thema NoSQL um Offenheit und Bewusstsein für Alternative, existierende und neue Muster
und Tools um Daten zu Verwalten.

Jetzt fragen sie sich sicherlich wie nun MongoDB in all dies hineinpasst. Als Dokumentenorientierte Datenbank (DB)
ist MongoDB ein sehr breit einsetzbares (generalized) NoSQL System. Es sollte als eine Alternative zu relationalen
Datenbanksystemen (RDB) betrachtet werden. Wie auch bei RDB Systemen kann MongoDB davon profitieren, wenn man
es mit einem etwas speziellerne NoSQL System für bestimmte Bereiche kombiniert.
MongoDB selbst hat Vor- und auch Nachteile, auf die in späteren Kapiteln des Buches eingegangen wird.

Wie sie vielleicht schon bemerkt haben, benutzen wir in diesem Buch die Begriffe MongoDB und Mongo als
Synonyme.

# Getting started #

Der grösste Teil des Buches befasst sich mit den MongoDB Kernfunktionen. Deshalb werden wir sehr viel
mit der MongoDB shell arbeiten. Die shell ist sowohl ein gutes Tool zum lerene als auch zur Administration,
zum Ausführen ihrer Programme benötigen sie jedoch auch einen MongoDB Treiber.

Das bringt uns zur ersten Sache die sie über MongoDB lernen sollten: die MongoDB Treiber. MonmgoDB hat
eine ganze [Reihe von offiziellen Treibern](http://docs.mongodb.org/ecosystem/drivers/) für verschiedene 
Programmiersprachen. Diese Treiber sind vergleichbar mit den Datenbanktreibern die sie wahrscheinliche schon
von anderen DBDatenbank Systemen kennen. Auf der Basis dieser Treiber hat die Entwicklergemeinde speziellere
libraries und Frameworks für verschieden Sprachen implementiert. 
Beispiele sind [NoRM](https://github.com/atheken/NoRM), eine C# library die LINQ implementiert, sowie 
[MongoMapper](https://github.com/jnunemaker/mongomapper), eine Active-Record freundliche Ruby library.
Ob sie ihre Programme mit den Basistreiber oder mit Hilfe einer höheren Library entwicklen liegt alleine
bei ihnen. Ich möchte dies hier nur klarstellen, da Menschen die neu bei MongoDB sind manchmal durch den
Umstand verwirrt werden, das es offizielle Treiber und Community libraries gibt.
Erstere konzentrieren sich mehr auf Konnektivität und Kommunikaiton mit MongoDB während die Community libraries
sich mehr auf die Programmiersprachen und Framework spezifischen Aspekte beziehen.

Während sie dieses Buch lesen möchte ich sie ermutigen auch immer praktisch zu probieren was ich vorstelle
und auch Fragen die sie haben selbst durch ausprobierne zu klären. Es ist sehr leicht mit MongoDb zu starten,
also lassen sie uns ein paar Minuten nehmen um die Umgebung aufzusetzen.

1. Gehen sie auf die [offizielle download Seite](http://www.mongodb.org/downloads) und laden sie das MongoDB 
release (Ich empfehle die "stable version") für ihr Betriebssystem. Für Entwicklungszwecke können sie sowohl
die 32-Bit als auch die 64-Bit Version nehmen.

2. Packen sie die Archivdatei aus (in welchem Verzeichnis sie wollen) und wechseln sie in das Unterverzeichnis 
`bin`. Starten sie jetzt noch nichts, zur ihrer Information sage ich ihnen aber schonmal das es sich bei `mongod``
um den Server Prozeß und bei `mongo`um die client shell handelt. Dies sind die beiden Programme mit denen 
wir die meiste Zeit arbeiten werden.

3. Erstellen sie eine Textdatei Namens `mongodb.config` im Unterverzeichnis `bin`.

4. Fügen sie die folgende Zeile zur Datei `mongodb.config` hinzu: 
`dbpath=PATH_TO_WHERE_YOU_WANT_TO_STORE_YOUR_DATABASE_FILES`. Achten sie darauf das die Pfadangabe für
ihre Betriebssystem richtig formuliert ist. Für Windows könnte der Eintrag Beispielsweise so aussehen 
`dbpath=c:\mongodb\data` und für Linux z.B. so `dbpath=/var/lib/mongodb/data`.

5. Stellen sie sicher das der angegebene `dbpath`auch existiert. Oder erstellen sie ihn jetzt.

6. Starten sie jetzt `mongod` mit dem Parameter `--config /path/to/your/mongodb.config`.

Hier ein komplettes Beispiel für Windows Anwender. Wenn sie das Archiv in das Verzeichnis `c:\mongodb\`
entpackt haben und sie haben als Datenverzeichnis `c:\mongodb\data\` angelegt, dann müssen sie 
das wie folgt in der Datei `c:\mongodb\bin\mongodb.config` spezifizieren: `dbpath=c:\mongodb\data\`.
Sie starten `mongod` dann von der Kommandozeile mit: `c:\mongodb\bin\mongod --config c:\mongodb\bin\mongodb.config`.

Sie können das `bin` Verzeichnnis natürlich auch zu ihrer PATH Umgebungsvariable hinzufügen um die Aufrufe
kürzer (less verbose) zu machen. 
Für MacOSX und Linux Anwender funktioniert das im wesentlichen genauso, sie müssen nur die Pfade entsprechend
anpassen.

Ich hoffe sie haben MongoDB nun gestartet. Sollten sie eine Fehlermeldung sehen, lesen sie diese bitte genau durch.
Der Server ist wirlklich gut darin zu melden was schief gelaufen ist.

Sie können jetzt `mongo` starten (ohne das *d*) um eine shell mit dem Server zu verbinden. Geben sie als Test
`db.version()` um sicher zu stellen das alles funktioniert. Sie sollten als Ausgabe die Versionsnummer 
(von MongoDB) sehen die sie installiert haben.

# Kapitel 1 - Die Grundlagen #
 
Wir beginnen unsere Reise mit den Grundlegenden Mechanismen der Arbeit mit MongoDB. Natürlich sind dies
die Kernthemen um MongoDB zu verstehen aber es sollte und auch einen guten Eindruck vermitteln wo
MongoDB einsetzbar ist.

Es gibt sechs einfache Konzepte die wir verstehen müssen.

1. MongoDB hat das selbe Konzept einer `Datenbank` das sie vermutlich schon kennen (oder das eines Schemas für
die Oracle Leute). In jeder MongoDB Instanz kann es Null oder mehr Datenbanken geben, von denen jede als 
übergeordnerter Container für weitere Inhalte fungiert.

2. Jede Datenbank hat Null oder mehr `collections`. Eine collection hat so viele gemeinsamkeiten mit einer klassischen
Tabelle, das man sich die beiden als identisch vorstellen kann.

3. `collections` bestehen aus Null oder mehr `Dokumenten`. Sie können sich ein `Dokument` als eine Zeile einer 
Tabelle vorstellen.

4. Jedes `Dokument` besteht aus einem oder mehr `Feldern`, die sie sich wie Spalten einer Tabelle vorstellen können.

5. `Indexe` funktionieren in MongoDB grösstenteils so wie in den entsprechenden RDBMS.

6. `Cursors` sind anders als die vorherigen fünf Konzepte. Sie werden oftmals übersehen, sind aber meines
Erachtens nach wichtig genug, sie gesondert zu besprechen. Es ist wichtig zu verstehen, das wann immer sie
in MongoDB nach Daten suchen, sie einen Zeiger auf das Ergebnis als Antowrt erhalten. Dieser Zeiger wird
`cursor` genannt. Mit diesem `cursor` können sie verschiedene Operationen, wie Beispielsweise `zählen` oder 
`überspringen` (skipping ahead) ausführen bevor sie die eigentlichen Daten übertragen.

Zur Wiederholung: MongoDB besteht aus `Datenbanken` die `collections` enthalten. Jede `collection` enthält
`Dokumente`, die wiederum aus `Feldern` bestehen. Sie können `collections` indexieren um die Such- und 
Sortiergeschwindigkeit zu erhöhen. 
Und am Ende erhalten wir die Suchergebnisse in Form eines `cursors` dessen eigentliche Ausführung so lange
verzögert wird bis sie wirklich benötigt wird.

Warum benutzen wir hier neue Begriffe (collection vs. Tabelle, Dokument vs. Zeile, Feld vs. Spalte)? Machen
wir das nur um die Dinge zu komplizieren ? In Wahrheit sind die Konzepte zwar ähnlich der Konzepte in der
Welt der raltionalen Datenbanken aber sie sind eben doch nicht genau gleich.
Der Hautpunterschied liegt darin, das relationale Datenbanken ihre `Spalten` auf `Tabellen` Ebene definieren
wohingegen dokumenten-orientierte Datenbanken ihre `Felder` auf der `Dokumenten` Ebene definieren.
Das bedeutet das jedes `Dokument` einer `collection` seine eigenen `Felder` haben kann. (Die sich
von anderen Dokumenten in der selben `collection` unterscheiden können).
Einen `collection` ist also ein eher *dummer* container im Vergleich zu einer Tabelle, während in einem `Dokument``
viel mehr Informatione  als in einer `Zeile` stecken.










 
