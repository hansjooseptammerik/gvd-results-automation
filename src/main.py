from gvd_featured_scraper import fetch_featured_event, save_event_to_file

if __name__ == "__main__":
    event_data = fetch_featured_event()
    save_event_to_file(event_data)
