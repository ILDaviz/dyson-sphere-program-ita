# dyson-sphere-program-ita

Ti piace giocare a Dyson sphere program ma ti piacerebbe la traduzione in Italiano? Questa è la soluzione.

## Comandi da lanciare per generare i tuoi testi in autonomia usando ChatGPT

### Impostare l'ambiente
```bash
python3 -m venv venv
```

#### Attiva il source Mac
```bash
source venv/bin/activate
```

#### Attiva il source Windows
```bash
venv\Scripts\activate
```

### Installare le dipendenze
```bash
pip install -r requirements.txt
```

## Struttura del progetto
```
DYSON-SPHERE-PROGRAM-ITA/
├── original/
│   └── 1055/
│       ├── base.txt
│       └── ...
├── translated/
│   └── 1055/
│       ├── base.txt
│       └── ...
├── venv/
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Funzionalità principali
1. **Traduzione dei file**: Utilizza OpenAI GPT per tradurre contenuti presenti in `original/1055/` e salvarli in `translated/1055/`.
2. **Gestione dell'ambiente virtuale**: Fornisce un setup chiaro per creare un ambiente virtuale isolato.
3. **Gestione file**: Legge e scrive i file nelle directory definite.

## Avvio del progetto
1. Posizionare i file da tradurre nella cartella `original/1055/`.
2. Attivare l'ambiente virtuale:
   - **Mac/Linux**: `source venv/bin/activate`
   - **Windows**: `venv\Scripts\activate`
3. Installare le dipendenze con `pip install -r requirements.txt`.
4. Lanciare lo script principale:
   ```bash
   python main.py
   ```
5. I file tradotti saranno salvati nella directory `translated/1055/`.

## Note aggiuntive
- **File di configurazione**: Utilizzare il file `.env` per configurazioni specifiche.
- **Licenza**: Questo progetto è distribuito sotto licenza Apache 2.0.

## Contributi
Contribuzioni sono benvenute! Aprire un `issue` o inviare una `pull request` per miglioramenti o correzioni.

