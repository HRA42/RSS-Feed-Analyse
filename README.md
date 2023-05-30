# RSS-Feed Analyse

## Beschreibung
1. Prüfe RSS-Feed
2. Speichere den RSS in einer Datenbank
3. Prüfe, ob sich der RSS-Feed geändert hat
4. Sende E-Mail bei Änderung

## Installation
Setze eine Umgebungsvariable mit dem Namen `RSS_URL` und dem Wert des RSS-Feeds.

```bash
export RSS_URL="Ziel-URL"
export FROM_ADDR="Absender-Adresse"
export TO_ADDR="Empfänger-Adresse"
export SMTP_SERVER="SMTP-Server"
export SMTP_PORT="SMTP-Port"
export SMTP_USERNAME="SMTP-Username"
export SMTP_PASSWORD="SMTP-Password"
pip install -r requirements.txt
python3 main.py
```

Alternativ kann Docker verwendet werden.

```bash
docker run -d \
    -e RSS_URL="Ziel-URL" \
    -e FROM_ADDR="Absender-Adresse" \
    -e TO_ADDR="Empfänger-Adresse" \
    -e SMTP_SERVER="SMTP-Server" \
    -e SMTP_PORT="SMTP-Port" \
    -e SMTP_USERNAME="SMTP-Username" \
    -e SMTP_PASSWORD="SMTP-Password" \
    --name rss-feed-analyse \
    ghcr.io/hra42/rss-feed-analyse:latest
```

Danach muss der Docker Container mit einem Cronjob in dem gewünschten Intervall gestartet werden.