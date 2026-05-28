# guru-linux-suite
# 🔮 Guru Linux Suite

**Guru Linux Suite** è un'applicazione grafica intuitiva e sicura sviluppata in Python (Tkinter) per il controllo totale, la manutenzione e l'ottimizzazione di sistemi basati su Linux (ottimizzata per Ubuntu, Zorin OS e derivate). 

Progettata con rigidi blocchi di sicurezza, la suite ti permette di velocizzare il sistema e liberare spazio sul disco senza rischiare di compromettere i servizi vitali del sistema operativo.

---

## ✨ Funzionalità Principali

*   ⏱️ **Servizi & Avvio:** Gestisci i servizi `systemd` all'avvio analizzando i tempi di boot. Include le linee guida e i blocchi di sicurezza del "Guru" per impedire la disattivazione di servizi critici (es. rete o interfaccia grafica).
*   🧹 **Pulizia & Ottimizzazione:** Svuota la cache utente, elimina i pacchetti APT residui, contrai i log di sistema a 7 giorni, esegui il TRIM su SSD e imposta lo *swappiness* a 10 per ridurre l'usura del disco e ottimizzare la RAM.
*   🐧 **Editor GRUB:** Modifica in sicurezza il tempo di attesa (timeout) del bootloader GRUB con backup automatico e funzione di ripristino d'emergenza.
*   📦 **Disinstalla App:** Cerca e rimuovi completamente i pacchetti software installati sul sistema (`apt purge`) tramite un'interfaccia comoda e veloce.
*   🔄 **Aggiornamenti:** Sincronizza i server e installa le patch di sicurezza visualizzando l'output del terminale in tempo reale.

---

## 🚀 Come Avviare l'Applicazione

Poiché la suite esegue modifiche profonde a livello di sistema (come la gestione dei servizi e la pulizia dei pacchetti), **deve essere eseguita con i privilegi di root**.

1. Apri il terminale nella cartella del progetto.
2. Lancia lo script digitando verbatim:
```bash
   sudo python3 guru_linux_suite.py
