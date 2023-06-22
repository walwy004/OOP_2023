class Cinema:
    def __init__(self, name):
        self.name = name
        self.theatres = []
        self.currentFilms = set()
        
    def addTheatre(self, theatre):
        self.theatres.append(theatre)
    
    def addFilm(self, film):
        self.currentFilms.add(film)
    
    def displayCurrentFilms(self):
        print("Current Films:")
        
        for film in self.currentFilms:
            print(f"- {film.title}: {film.runTime} minutes")
    
    def viewTheatres(self):
        print(f"\n{self.name}\nTheatres:")
        
        for theatre in self.theatres:
            print(f"- {theatre.description()}")
    
class Film:
    def __init__(self, title, runTime):
        self.title = title
        self.runTime = runTime

class Theatre:
    def __init__(self, seats):
        self.seats = seats
        self.filmsPlaying = []
    
    def addFilm(self, film):
        self.filmsPlaying.append(film)
        
    def description(self):
        title_list = ", ".join([film.title for film in self.filmsPlaying])
        return f"Theatre with {self.seats} seats. Movies playing: {title_list}"

class PremiumTheatre(Theatre):
    def __init__(self, seats, menu):
        super().__init__(seats)
        self.menu = menu
    
    def description(self):
        menuItems = ""
        for item in self.menu:
            menuItems += "- " + item + "\n"
        
        return super().description() + f"\nToday's menu include:\n{menuItems}"
    

cinema = Cinema("Adelaide Cinema Complex")
film1 = Film("Pokemon: The First Movie", 150)
film2 = Film("The Fifth Element", 180)
theatre1 = Theatre(100)
theatre2 = PremiumTheatre(50, ["Popcorn", "Soda", "Nachos"])

theatre1.addFilm(film1)
theatre2.addFilm(film2)

cinema.addTheatre(theatre1)
cinema.addTheatre(theatre2)

cinema.addFilm(film1)
cinema.addFilm(film2)

cinema.displayCurrentFilms()
cinema.viewTheatres()