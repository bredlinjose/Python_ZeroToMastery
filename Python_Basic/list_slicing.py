amazon_cart = ['notebook', 'glass', 'toys', 'apples']
print(amazon_cart)

amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart
new_cart[0] = 'gun'
# change both new_cart[0] and amazon_cart[0] to gun

# new_cart = amazon_cart[:]   # amazon_cart.copy() both are same
# new_cart[0] = 'gun'
# change only the new_cart[0] to gun

print(new_cart)
print(amazon_cart)
