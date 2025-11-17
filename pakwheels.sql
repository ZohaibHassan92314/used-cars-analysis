CREATE DATABASE pakwheels_db;
USE pakwheels_db;

select * from used_cars;
SELECT * FROM used_cars ORDER BY price DESC LIMIT 10;
SELECT city, COUNT(*) AS total_cars FROM used_cars GROUP BY city ORDER BY total_cars DESC;
SELECT year, AVG(price) AS avg_price
FROM used_cars
GROUP BY year
ORDER BY year;

SELECT 
    CASE 
        WHEN price < 1000000 THEN 'Below 1M'
        WHEN price BETWEEN 1000000 AND 3000000 THEN '1M-3M'
        WHEN price BETWEEN 3000000 AND 5000000 THEN '3M-5M'
        ELSE 'Above 5M'
    END AS price_range,
    COUNT(*) AS total_cars
FROM used_cars
GROUP BY price_range;



