-- script that displays the average temperature (Fahrenheit).
SELECT city, AVG(`value`) AS average_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
