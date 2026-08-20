#25. Create sets representing products belonging to different categories. Find products that belong to both categories.

cat1_products = {"Laptop", "Smartphone", "Headphones", "Smartwatch"}
cat2_products = {"Smartwatch", "Camera", "Headphones", "Tablet"}

common_products = cat1_products.intersection(cat2_products)
print("Products belonging to both categories:", common_products)
