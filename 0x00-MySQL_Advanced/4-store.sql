-- creates a trigger that decreases the quantity of an item after adding a new order.

UPDATE items SET quantity = quantity - (
	SELECT SUM(orders.number)
	FROM orders
	WHERE orders.item_name=items.name
)
WHERE items.name IN (SELECT item_name FROM orders);
