"""
menu_maker.py
Modify this, move to root directory, and run `python menu_maker.py` to change the menu
Place pictures of items (.jpg or .png) in the static folder

Created by Duncan Stothers in 2018 at Harvard University for Cabot Cafe
Licensed under MIT License
"""

import json

### Hot Drinks
hot_drinks = {}

# hot coffees
hot_drinks["Hot Coffees"] = [\
("Americano",2.50,"americano.jpg"),\
("Latte",3.00,"latte.jpg"),\
("Mocha",3.50,"mocha.jpg"),\
("Nutella-Me-More",4.00,"nutella.jpg"),\
]

# hot teas
hot_drinks["Hot Teas"] = [\
("Tea Pot",5.00,"teapot.jpg"),\
("Tea Cup",2.00,"teacup.jpg"),\
("Matcha Latte",3.50,"matcha.jpg"),\
("Chai Love Lucy",3.00,"chailovelucy.jpg"),\
("Pinkberry",3.00,"pinkberry.jpg"),\
("London Fog",3.50,"londonfog.jpg"),\
("Hot Shot",3.50,"hotshot.jpg"),\
("Dark Chai",4.00,"darkchai.jpg"),\
]

# Other
hot_drinks["Other"] = [\
("Apple Cider",2.00,"applecider.jpg"),\
("Hot Chocolate",2.50,"hotchocolate.jpg"),\
("Vanilla Steamer",2.50,"vanillasteamer.jpg"),\
("Cloud 9",3.00,"cloud9.jpg"),\
]

### Cold Drinks
cold_drinks = {}

# Iced Coffees
cold_drinks["Iced Coffees"] = [\
("Iced Latte",3.50,"icedlatte.jpg"),\
("Iced Mocha",3.50,"icedmocha.jpg"),\
("Thin Mint",4.50,"thinmint.jpg"),\
("Queen Bee Frappe",4.50,"queenbee.jpg"),\
]

# Iced Teas
cold_drinks["Iced Teas"] = [\
("Blood Orange",2.00,"bloodorange.jpg"),\
("Flower Power",2.00,"flowerpower.jpg"),\
("Tai Chi Chai Tea",3.00,"taichichaitea.jpg"),\
("Iced Matcha",4.00,"icedmatcha.jpg"),\
("Matcha Do About Nothing",4.50,"matchado.jpg"),\
]

# Lemonades
cold_drinks["Lemonades"] = [\
("Plain Jane",2.00,"plainjane.jpg"),\
("Blueberry Lemonade",2.50,"blueberrylemonade.jpg"),\
("Ondo Sunshine",2.50,"ondosunshine.jpg"),\
("Ultraviolet",4.00,"ultraviolet.jpg"),\
]

### Food
food = {}

# Savory
food["Savory"] = [\
("Bagel With Cream Cheese",2.00,"bagel.jpg"),\
("Hot Pocket",3.00,"cafe_logo_big.jpg"),\
("Mac N Cheese",3.00,"cafe_logo_big.jpg"),\
]

# Sweet
food["Sweet"] = [\
("Chocolate Chip Cookie",2.00,"cafe_logo_big.jpg"),\
("Coconut Macaroon",2.00,"cafe_logo_big.jpg"),\
("Muffin of the Day",2.50,"cafe_logo_big.jpg"),\
("Bear Claw",3.00,"cafe_logo_big.jpg"),\
("Scone of the Day",3.00,"cafe_logo_big.jpg"),\
("Chocolate Croissant",3.50,"cafe_logo_big.jpg"),\
("Almond Croissant",3.50,"cafe_logo_big.jpg"),\
("Lemon Poppyseed Cake",2.00,"cafe_logo_big.jpg"),\
]

### Favorites
favorites = {}

# Favorites
favorites["favorites"] = [\
("Tai Chi Chai Tea",3.00,"taichichaitea.jpg"),\
("Chai Love Lucy",3.00,"chailovelucy.jpg"),\
("Iced Matcha",4.00,"icedmatcha.jpg"),\
("Matcha Latte",3.50,"matcha.jpg"),\
("Hot Pocket",3.00,"cafe_logo_big.jpg"),\
]

### Save
j = json.dumps(cold_drinks)
f = open("menu/cold_drinks.json","w")
f.write(j)
f.close()

j = json.dumps(hot_drinks)
f = open("menu/hot_drinks.json","w")
f.write(j)
f.close()

j = json.dumps(food)
f = open("menu/food.json","w")
f.write(j)
f.close()

j = json.dumps(favorites)
f = open("menu/favorites.json","w")
f.write(j)
f.close()












