from string import Template
'''
This is  a simple data output program it will output all the items in a users e-cart.
Here in this program 
i will create a template for the output then
fill it with the cart info
'''

def Main():
    cart  = []
    cart.append(dict(item="coke",price=8,quantity=2))
    cart.append(dict(item="cake",price=12,quantity=1))
    cart.append(dict(item="fish",price=32,quantity=5))
    t = Template("$quantity x $item = $price")

    total = 0
    print("cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total:" + str(total))

if __name__ == '__ main__':
    Main()
    