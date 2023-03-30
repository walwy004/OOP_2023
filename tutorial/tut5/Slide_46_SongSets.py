artists = {"Asking Alexandria", "Avenged Sevenfold",
           "Trivium", "Papa Roach", "All That Remains"}

moreArtists = {"AlterBridge", "Godsmack", "Three Days Grace",
               "Polyphia", "Avenged Sevenfold", "Trivium"}

print(f"All: {artists.union(moreArtists)}")
print(f"Both: {artists.intersection(moreArtists)}")
print(f"Unique to first set: {artists.difference(moreArtists)}")
print(f"Unique to second set: {moreArtists.difference(artists)}")
print(f"Unique in both: {artists.symmetric_difference(moreArtists)}")
