SELECT * FROM languages WHERE languages.lang = "Slovene";
SELECT * FROM languages
JOIN countries ON languages.country_id = countries.id WHERE languages.lang = "Slovene";



SELECT countries.name AS country_name, COUNT(cities.id) AS cities_count 
FROM countries JOIN cities ON countries.id = cities.country_id
GROUP BY country_name
ORDER BY COUNT(cities.id) DESC;



SELECT * FROM cities WHERE country_id = 136 AND population > 500000
ORDER BY population DESC;



SELECT languages countries