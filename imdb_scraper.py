import requests
from bs4 import BeautifulSoup
from movie_class import Movie
import re

def extract_year(year_string):
    match = re.search(r'\((\d{4})\)', year_string)
    if match:
        return match.group(1)
    return None

def scrape_top_100_movies():
    one_fifty_url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
    fifty_one_one_hundred_url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt"
    one_fifty_response = requests.get(one_fifty_url)
    fifty_one_one_hundred_response = requests.get(fifty_one_one_hundred_url)
    one_fifty = BeautifulSoup(one_fifty_response.content, "html.parser")
    fifty_one_one_hundred = BeautifulSoup(fifty_one_one_hundred_response.content, "html.parser")

    titles = [movie.find('a').string for movie in one_fifty.find_all("h3", class_="lister-item-header")] + [movie.find('a').string for movie in fifty_one_one_hundred.find_all("h3", class_="lister-item-header")]
    ratings = [rating.find("strong").string for rating in one_fifty.find_all("div", class_="inline-block ratings-imdb-rating")] + [rating.find("strong").string for rating in fifty_one_one_hundred.find_all("div", class_="inline-block ratings-imdb-rating")]
    years = [extract_year(year.string) for year in one_fifty.find_all("span", class_="lister-item-year text-muted unbold")] + [extract_year(year.string) for year in fifty_one_one_hundred.find_all("span", class_="lister-item-year text-muted unbold")]
    maturities = [maturity.string for maturity in one_fifty.find_all("span", class_="certificate")] + [maturity.string for maturity in fifty_one_one_hundred.find_all("span", class_="certificate")]
    runtimes = [runtime.string[:3] for runtime in one_fifty.find_all("span", class_="runtime")] + [runtime.string[:3] for runtime in fifty_one_one_hundred.find_all("span", class_="runtime")]
    genre_list = [genres.string.strip().split(', ') for genres in one_fifty.find_all("span", class_="genre")] + [genres.string.strip().split(', ') for genres in fifty_one_one_hundred.find_all("span", class_="genre")]


    movies = [Movie(i+1, titles[i], years[i], ratings[i], runtimes[i], maturities[i], genre_list[i]) for i in range(100)]
    return movies