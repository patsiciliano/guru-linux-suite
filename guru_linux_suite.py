# 🔮 Guru Linux Suite

Benvenuti nella **Guru Linux Suite**, un centro di controllo grafico (GUI) in Python progettato per la manutenzione profonda, la pulizia e l'ottimizzazione avanzata di **Zorin OS** e distribuzioni basate su **Ubuntu/Debian**.

Questo progetto nasce da un'idea della community ed è stato sviluppato in collaborazione con **Gemini Guru**, unendo la potenza degli script di sistema a un'interfaccia sicura, trasparente e facile da usare.

---

## 🚀 Funzionalità Principali

* **⏱️ Servizi & Avvio:** Analisi in tempo reale dei tempi di avvio dei servizi (`systemd-analyze blame`) con linee guida integrate del Guru per disabilitare in sicurezza i servizi superflui senza rischiare di rompere il sistema.
* **🧹 Pulizia & Ottimizzazione:** Svuotamento della cache utente, rimozione automatica dei pacchetti residui (APT), pulizia dei file temporanei obsoleti, rimozione dei runtime Flatpak inutilizzati, ottimizzazione avanzata della RAM (`Swappiness`), contrazione dei log di sistema e comando `TRIM` per preservare e velocizzare gli SSD.
* **🐧 Editor GRUB:** Modifica sicura e guidata del timeout del bootloader con un sistema di backup e ripristino automatico "di fabbrica" in caso di ripensamenti.
* **📦 Disinstalla App:** Gestore grafico per rimuovere completamente i pacchetti di sistema (`apt purge`) con un comodo filtro di ricerca istantaneo.
* **🔄 Aggiornamenti:** Terminale integrato per sincronizzare i server e installare le patch di sicurezza visualizzando l'output in tempo reale.

---

## 📦 Come Installare ed Eseguire

Poiché la suite effettua modifiche strutturali per ottimizzare il sistema (come la gestione dei servizi o la pulizia dei pacchetti), richiede i privilegi di amministratore per funzionare.

1. Scarica il file `guru_linux_suite.py` sul tuo computer.
2. Apri il terminale nella cartella in cui si trova il file.
3. Avvia la suite con il comando:

```bash
sudo python3 guru_linux_suite.py
