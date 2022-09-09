from footprint import Footprint

if __name__ == "__main__":
    google = Footprint("google.com")

    host_data = google.host()
    if host_data.is_resilient():
        print(host_data.json)
    else:
        print("Incomplete data!")
