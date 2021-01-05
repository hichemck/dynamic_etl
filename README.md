# Dynamic ETL Job

ETL job that fetches dynamically data from the API

## Task

The API [recipepuppy](http://www.recipepuppy.com/about/api/) provides data about different recipes depending on multiple ingredients. The results in the response include title, href, ingredients and the thumbnail.

My ETL script takes the information (number of ingredients, ingredients, search query, format, number of pages) interactively and returns different recipes that correspond to the input information. For each recipe following information is returned:
- Recipe name
- Link to the recipe
- Ingredients list
- Thumbnail

Further, the script contains an SQL insert query that can be used to insert the recipes in an sql table.