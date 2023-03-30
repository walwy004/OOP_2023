songLibrary = [
    ("Asking Alexandria", "The Black", "Like a House On Fire"),
    ("Avenged Sevenfold", "City of Evil", "Nightmare"),
    ("Trivium", "In Waves", "Shogun"),
    ("Papa Roach", "Infest", "F.E.A.R"),
    ("All That Remains", "The Fall of Ideals", "Overcome")
]

artists = set()
for artist, album, album in songLibrary:
    artists.add(artist)

print(artists)

for artist in artists:
    print(f"{artist} plays good music.")

artistList = list(artists)
artistList.sort()
print(artistList)