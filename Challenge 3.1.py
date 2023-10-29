#Write a function called linear_search_produc that takes the list of products and a target product name as input. The function shoud preform a linear search to find thetarget product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_search_product(product_list, target_product):
  indices = []
  for i, product in enumerate(product_list):
      if product == target_product:
          indices.append(i)
  return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
if result:
  print(f"The product '{target_product}' was found at indices: {result}")
else:
  print(f"The product '{target_product}' was not found in the list.")