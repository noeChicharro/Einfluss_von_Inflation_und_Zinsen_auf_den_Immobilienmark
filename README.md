# 📊 Der Einfluss von Zinsen & Inflation auf den Schweizer Immobilienmarkt (2013–2025)


Dieses Projekt beschäftigt sich mit der Analyse und Visualisierung von Zeitreihen im Kontext von Immobilienpreisen, Zinsen und weiteren wirtschaftlichen Kennzahlen. Es verwendet Daten aus einer MySQL-Datenbank und diverse statistische und maschinelle Lernverfahren.

---

Um das Jupyter Notebook einzusehen ist keine lokale Entwicklungsumgebung nötig. 
Im Fall eines Runs jedoch schon. Dafür die folgenden Schritte befolgen:

## 🧰 Benötigte Python-Pakete

Stelle sicher, dass alle folgenden Pakete installiert sind:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn statsmodels squarify

```

## 🗄️ Datenbank
Um strukturierte Daten gewährleisten zu können wird eine MySql Datenbank verwendet. 
Die dazugehörige Verbindung findet sich unter:

```bash
src/dbConnection/connector.py
```

## 🏗️ Datenbanktabellen erstellen
Um die Datenbank mit allen notwendigen Tabellen und Inhatl auszustatten bitte folgende Datei laufen lassen.

```bash
python src/dbConnection/createTables.py
```

## 📁 Projektstruktur (Auszug)
```bash
├── presentation/                   # Präsentation und Video
├── src/
│   └── dbConnection/
│       ├── archive/                # Archivierte Datenbankeinträge
│       ├── connector.py            # Verbindet mit der MySQL-Datenbank
│       └── createTables.py         # Erstellt alle benötigten Tabellen und deren Inserts
│   └── analyse/
│       ├── assets/                 # Unabhänige Bilder welche im Notebook verwendet werden
│       ├── bruttoinlandprodukt/    # Alle Grafiken welche sich auf Buttoinlandsprodukt beziehen
│       ├── dataHive/               # Alle Grafiken welche sich auf DataHive beziehen
│       ├── lik/                    # Alle Grafiken welche sich auf Lik beziehen
│       ├── wohneigentum/           # Alle Grafiken welche sich auf Wohneigentum beziehen
│       ├── dataHiveService.py      # Service um DataHive Daten gereinigt zur Verfügung zustellen
│       ├── dataService.py          # Service um allgemeine Daten gereinigt zur Verfügung zustellen
│       └── main.ipynb              # Jupyter Notebook 
├── data/                           # Lokale Datenquellen (originale CSVs) *
└── README.md                       # Diese Datei
```

* Für die originale DataHive Datei bitte diesem Link folgen (NDA) : https://drive.google.com/file/d/1dYwbdT2BrDB14WThg1-gI1Hd8jrZviC8/view?usp=sharing