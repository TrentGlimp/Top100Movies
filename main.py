from imdb_scraper import scrape_top_100_movies
from movie_class import Movie

movies = scrape_top_100_movies()

def input_check(prompt, set):
    user_input = input(prompt)
    stringified_list = [str(item) for item in set]
    if user_input in stringified_list:
        return user_input
    else:
        print("Sorry the following input was invalid, please try again")
        input_check(prompt, set)

def filter_movies_by_attribute(movies, attribute_name, prompt_message, is_genre=False):
    if is_genre:
        genre_list = sorted(set(genre for movie in movies for genre in movie.genre_list))
        genre = input_check(f"{prompt_message}\n{genre_list}\n", genre_list)
        return [movie for movie in movies if genre in movie.genre_list]
    else:
        attributes = sorted(set(getattr(movie, attribute_name) for movie in movies))
        user_input = input_check(f"{prompt_message}\n{attributes}\n", attributes)
        return [movie for movie in movies if str(getattr(movie, attribute_name)) == user_input]

def main():
    print("Welcome to the Movie Recommendation Program!")
    run_again = True
    filtered_movies = []
    filter_options = {
        '1': ("year", "Enter 1 of the following years:"),
        '2': ("decade", "Enter 1 of the following decades:"),
        '3': ("maturity", "Enter 1 of the following maturity ratings:"),
        '4': ("genre", "Enter a genre:"),
        '5': ("rank", "Enter 1 of the following ranks:"),
        '6': ("runtime", "Enter 1 of the following runtimes:"),
        '7': ("rating", "Type 1 of the following ratings:")
    }

    while run_again:
        print("\nWhat would you like to filter movies by?")
        print("1. Specific Year")
        print("2. Specific Decade")
        print("3. Maturity Rating")
        print("4. Genre")
        print("5. Rank in Top 100 List")
        print("6. Runtime")
        print("7. Rating")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice in filter_options:
            attribute_name, prompt_message = filter_options[choice]
            is_genre = attribute_name == "genre"
            filtered_movies = filter_movies_by_attribute(movies, attribute_name, prompt_message, is_genre)
        else:
            print("Invalid choice. Please choose a valid option.")


        if filtered_movies:
            print("\nYour Recommended Movies:")
            for movie in filtered_movies:
                    print(movie)
            else:
                print("\nNo movies match the selected filters.")
            filtered_movies.clear()
        user_input = input("Would you like to use this again\n[y/n]\n")
        if user_input == 'n':
            run_again = False
            print("Thank you for using the movie reccommender!")

if __name__ == "__main__":
    main()
