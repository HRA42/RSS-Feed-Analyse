__doc__ = """
Implementiert die Initialisierung der Datenbank.
"""

import dbm
import json

def init_dbm_store():
    """
    Initialisiert die Datenbank, wenn sie nicht vorhanden ist
    """
    if dbm.whichdb('database/store') is None:
        print("Creating new database")
        db = dbm.open('database/store', 'n')
        db.close()
        return True
    else:
        print("Database already exists")
        return False

def store_results(items):
    """
    Speicher den RSS-Feed in der Datenbank.
    Wenn der RSS-Feed bereits in der Datenbank vorhanden ist, wird er nicht gespeichert.
    Wenn der RSS-Feed nicht in der Datenbank vorhanden ist, wird er gespeichert.
    Wemm der RSS-Feed einen neuen Eintrag enthält, wird dieser in der Datenbank gespeichert.
    Items-Schema des RSS Feed:
    {
        Index: int,
        Title: str,
        Link: str,
        PubDate: str
    }
    """
    db = dbm.open('database/store', 'w')
    for item in items:
        if item['Index'] not in db:
            db[item['Index']] = json.dumps(item)
    db.close()

def print_results():
    """
    Gibt alle Einträge nach Index sortiert der Datenbank aus.
    """
    db = dbm.open('database/store', 'r')
    items = [json.loads(db[key].decode('utf-8')) for key in db.keys()]
    sorted_items = sorted(items, key=lambda x: int(x['Index']))
    for item in sorted_items:
        print(json.dumps(item))
    db.close()
    
def return_latest_index():
    """
    Gibt den höchsten Index Eintrag der Datenbank zurück.
    """
    db = dbm.open('database/store', 'r')
    items = [json.loads(db[key].decode('utf-8')) for key in db.keys()]
    sorted_items = sorted(items, key=lambda x: int(x['Index']))
    db.close()
    latest_index = sorted_items[-1]['Index']
    return latest_index
    
def return_latest_item():
    """
    Gibt den höchsten Index Eintrag der Datenbank zurück.
    """
    db = dbm.open('database/store', 'r')
    items = [json.loads(db[key].decode('utf-8')) for key in db.keys()]
    sorted_items = sorted(items, key=lambda x: int(x['Index']))
    db.close()
    latest_item = sorted_items[-1]
    return latest_item

def get_missing_entries(current_feed):
    """
    Compares the current feed with the entries in the database and returns any missing entries.
    """
    missing_entries = []
    with dbm.open("database/store", "r") as db_store:
        for item in current_feed:
            if isinstance(item, dict) and "Index" in item:
                if item["Index"].encode() not in db_store:
                    missing_entries.append(item)
    return missing_entries
