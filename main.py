__doc__ = """
Das ist die main Datei. Sie führt das Programm aus.
"""
from os import environ as env
from rss import feed
from store import store_db
from send_email import smtp as email

def main():
    """
    Das ist die main Funktion des Programms.
    TestURL:
    https://blog.kagi.com/rss.xml
    """
    rss_url=env.get("RSS_URL")        
    rss_feed = feed.read_rss_feed(rss_url)
    parsed_rss_feed = feed.parse_rss_feed(rss_feed)
    if store_db.init_dbm_store():
        store_db.store_results(parsed_rss_feed)
        print("Database populated")
    missing = store_db.get_missing_entries(parsed_rss_feed)
    if not missing:
        print("No new entries")
        return 0
    else: 
        print("New entries found")
        store_db.store_results(missing)
        email.send_email(
            subject="Neuer Eintrag im RSS Feed: {rss_url}",
            message="Neuer Eintrag im RSS Feed: {rss_url} \n {missing}",
            from_addr=env.get("FROM_ADDR"),
            to_addr=env.get("TO_ADDR"),
            smtp_server=env.get("SMTP_SERVER"),
            smtp_port=env.get("SMTP_PORT"),
            smtp_username=env.get("SMTP_USERNAME"),
            smtp_password=env.get("SMTP_PASSWORD")
        )
    store_db.print_results()

if __name__ == "__main__":
    main()
