
# Irakasleen Ordutegia App

**Deskribapena**  
Irakasleen ordutegia kudeatzeko aplikazioa. Irakasleak gehitu, kendu eta bakoitzaren ordutegia editatu daiteke, eta ordutegi komun libreak ikusi.

**Komponentuak**  
- **Irakaslea**: Irakasle baten informazioa eta ordutegia gordetzen dituen klasea.  
- **IrakasleaController**: Irakasleen zerrenda kudeatzen du; irakasleak kargatu, gorde, gehitu eta kendu.  
- **Main (Flet aplikazioa)**: Interfazea eta erabiltzailearen ekintzak kudeatzen ditu, Flet liburutegia erabiliz.

**Funtzionalitate nagusiak**  
- Irakasle berriak sortu eta ezabatu.  
- Irakaslearen ordutegia aldatu (orduak gehitu eta kendu).  
- Ordu libre komunak kalkulatu hautatutako irakasle batzuen artean.

**Erabilera**  
1. Exekutatu `main.py` (edo zure script nagusia).  
2. Izena sartu eta irakasleak kudeatu.  
3. Orduak gehitu edo kendu hautatutako irakaslearentzat.  
4. Hautatu irakasle batzuk eta ikusi ordu libre komunak.

## Behar diren paketeak (Dependencies)

Proiektu honek **Flet** liburutegia erabiltzen du interfazea sortzeko. Horretarako `requirements.txt` fitxategia dugu, bertan behar diren paketeak zehazten direlarik.

`requirements.txt` edukia:
\`\`\`
flet
\`\`\`

Paketeak instalatzeko, terminalean honako komandoa exekutatu:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Horrela, Flet eta beste behar diren liburutegi guztiak automatikoki instalatuko dira, eta aplikazioa behar bezala exekutatu ahal izango da.
