import requests
import json
from bs4 import BeautifulSoup

def get_ingredients_string(number_of_ingredients):
    if number_of_ingredients == 1 :
        ingredients_string = input("Enter ingredient: ")
    else:
        ingredients_string = ""
        for j in range(number_of_ingredients):
            ingredient = input(f"Enter ingredient {j+1}: ")
            if j < number_of_ingredients -1:
                ingredients_string = ingredients_string + ingredient + ","
            else:
                ingredients_string = ingredients_string + ingredient
    return ingredients_string

def get_format():
    f = ""
    while f not in ["json", "xml"]:
        f = input("Enter a valid format (json or xml): ")
    return f

number_of_ingredients = int(input("Enter the number of ingredients: "))

i = get_ingredients_string(number_of_ingredients)

q = input("Enter the search query: ")

p = input("Enter the maximal number of pages: ")

f = get_format()

url = f"http://www.recipepuppy.com/api/?i={i}&q={q}&p={p}&format={f}"

response = requests.get(url)

if f == "json":
    data = response.json()
    results = data['results']
    #print(results)

    k = 1
    for d in results:
        title = d['title']
        href = d['href']
        ingredients = d['ingredients']
        thumbnail = d['thumbnail']

        print(title, href, ingredients, thumbnail)

        sql = f"INSERT INTO RECIPES(title, href, ingredients, thumbnail) \
        VALUES ({title},{href},{ingredients},{thumbnail});"

        # execute sql

        print(f"INSERT number {k} OK")
        k+=1

else:
    soup = BeautifulSoup(response.content, "lxml")
    recipe_list = soup.find_all("recipe")
    k = 1
    for r in recipe_list:
        title = r.find("title").text
        href = r.find("href").text
        ingredients = r.find("ingredients").text

        print(title, href, ingredients)

        sql = f"INSERT INTO RECIPES(title, href, ingredients) \
            VALUES ({title},{href},{ingredients});"
            
        # execute sql
        print(f"INSERT number {k} OK")
        k += 1
        