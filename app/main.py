from footprint import Footprint

if __name__ == "__main__":
    google = Footprint("google.com")
    print(google.host().json)