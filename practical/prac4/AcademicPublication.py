class AcademicPublication:
    def __init__(self, year, title):
        self.__year = year
        self.__title = title
        self.__authors = []

    def addAuthor(self, author):
        self.__authors.append(author)

    def getReference(self):
        reference = "Authors: "
        for author in range(len(self.__authors)):
            reference += self.__authors[author]
            if author != len(self.__authors)-1:
                reference += ", "
            else:
                reference += "\n"
        reference += f"Publication Details: ({self.__year}) {self.__title}.\n"
        return reference


class JournalArticle(AcademicPublication):
    def __init__(self, journalName, title, year):
        super().__init__(year, title)
        self.__journalName = journalName

    def getReference(self):
        return super().getReference() + f"In Journal of {self.__journalName}.\n"


class ConferencePaper(AcademicPublication):
    def __init__(self, year, title):
        super().__init__(year, title)
        
    def getReference(self):
        return super().getReference() + f"In Proceedings of {self.conference.name} ({self.conference.acronym})\n"
    

class Conference:
    def __init__(self, acronym, name):
        self.acronym = acronym
        self.name = name
        self.papers = []
    
    def addPaper(self, paper):
        paper.conference = self
        self.papers.append(paper)
        
# Task 3
article1 = JournalArticle("ACM Computing Survey","Information retrieval on the web", 2000)
article1.addAuthor("M Kobayashi")
article1.addAuthor("K Takeda")
print(article1.getReference())

paper1 = ConferencePaper(2021, "A Comparative Study of ML-ELM and DNN for Intrusion Detection")
paper1.addAuthor("Wencheng Yang")
paper1.addAuthor("Song Wang")
paper1.addAuthor("Michael N. Johnstone")

paper2 = ConferencePaper(2021, "A Survey on Formal Verification for Solidity Smart Contracts")
paper2.addAuthor("Ikram Garfatta")
paper2.addAuthor("Kais Klai")
paper2.addAuthor("Walid Gaaloul")
paper2.addAuthor("Mohamed Graiet")

acsw2021 = Conference("ACSW", "Australian Computer Science Week")
acsw2021.addPaper(paper1)
acsw2021.addPaper(paper2)

print(paper1.getReference())
print(paper2.getReference())

# Task 4
print(isinstance(paper1,ConferencePaper))
print(isinstance(paper1,JournalArticle))
print(isinstance(acsw2021,Conference))
print(isinstance(article1,JournalArticle))
print(isinstance(article1,AcademicPublication))

print(type(paper2).__name__)
print(type(article1).__name__)
print(type(acsw2021).__name__)