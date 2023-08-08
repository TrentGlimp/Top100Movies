class Movie:
    def __init__(self, rank, title, year, rating, runtime, maturity, genre_list):
        self.rank = int(rank)
        self.title = title
        self.year = int(year)
        self.decade = int(f"{year[:3]}0")
        self.rating = float(rating)
        self.runtime = int(runtime)
        self.maturity = maturity
        self.genre_list = genre_list
    
    def __str__(self):
        attributes = [
            f"Rank: {self.rank}",
            f"Title: {self.title}",
            f"Year: {self.year}",
            f"Rating: {self.rating}",
            f"Runtime: {self.runtime} mins",
            f"Maturity: {self.maturity}",
            f"Genres: {', '.join(self.genre_list)}",
            ]
        max_length = max(len(attr) for attr in attributes)
        separator = f"+{'-' * (max_length + 2)}+"
        output = f"{separator}\n"
        for attribute in attributes:
            output += f"| {attribute:<{max_length}} |\n"
        output += separator
        return output
    

