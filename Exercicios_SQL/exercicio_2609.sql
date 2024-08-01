SELECT c.name AS category_name, SUM(p.amount) AS total_amount
FROM products p
JOIN categories c ON p.id_categories = c.id
GROUP BY c.name
ORDER BY c.name;
