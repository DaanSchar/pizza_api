from extensions import db
from models.model import Pizza, Topping, Drink, Deliverer, Dessert

def init(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        pizzas = [
            Pizza(name='Margherita', price=4.99),
            Pizza(name='Marinara', price=3.99, ),
            Pizza(name='Quattro Stagioni', price=4.49, ),
            Pizza(name='Carbonara', price=3.99),
            Pizza(name='Frutti di Mare', price=3.99),
            Pizza(name='Quattro Formaggi', price=6.99),
            Pizza(name='Crudo', price=3.99),
            Pizza(name='Napoletana or Napoli', price=4.49),
            Pizza(name='Pugliese', price=3.99),
            Pizza(name='Montanara', price=5.99),
            Pizza(name='Emiliana', price=3.99),
            Pizza(name='Romana', price=3.99),
            Pizza(name='Fattoria', price=4.49),
            Pizza(name='Schiacciata', price=5.49),
            Pizza(name='Americana', price=2.99),
        ]

        toppings = [
            Topping(name='Tomato sauce', price=0.49, vegetarian=True),
            Topping(name='mozzarella', price=0.79, vegetarian=True),
            Topping(name='oregano', price=0.39, vegetarian=True),
            Topping(name='garlic', price=0.49, vegetarian=True),
            Topping(name='basil', price=0.29, vegetarian=True),
            Topping(name='mushrooms', price=0.89, vegetarian=True),
            Topping(name='ham', price=1.29, vegetarian=False),
            Topping(name='artichokes', price=1.99, vegetarian=True),
            Topping(name='olives', price=0.69, vegetarian=True),
            Topping(name='parmesan', price=0.69, vegetarian=True),
            Topping(name='eggs', price=0.99, vegetarian=True),
            Topping(name='bacon', price=1.59, vegetarian=False),
            Topping(name='seafood', price=3.99, vegetarian=True),
            Topping(name='gorgonzola cheese', price=0.99, vegetarian=True),
            Topping(name='Parma ham', price=1.99, vegetarian=False),
            Topping(name='anchovies', price=1.99, vegetarian=True),
            Topping(name='onions', price=0.59, vegetarian=True),
            Topping(name='pepperoni', price=1.59, vegetarian=False),
            Topping(name='Stracchino', price=1.99, vegetarian=True),
            Topping(name='eggplant', price=0.99, vegetarian=True),
            Topping(name='boiled potatoes', price=0.99, vegetarian=True),
            Topping(name='sausage', price=1.99, vegetarian=False),
            Topping(name='capers', price=0.79, vegetarian=True),
            Topping(name='peppers', price=1.39, vegetarian=True),
            Topping(name='peas', price=0.59, vegetarian=True),
            Topping(name='porchetta', price=1.39, vegetarian=False),
            Topping(name='Olive oil', price=0.29, vegetarian=True),
            Topping(name='rosemary', price=0.49, vegetarian=True),
            Topping(name='french fries', price=1.59, vegetarian=True)
        ]


        def get(topping):
            for i in toppings:
                if i.name == topping:
                    return i


        for pizza in pizzas:
            pizza.toppings.append(get('Tomato sauce'))

        pizzas[0].toppings.append(get('mozzarella'))
        pizzas[0].toppings.append(get('oregano'))

        pizzas[1].toppings.append(get('garlic'))
        pizzas[1].toppings.append(get('basil'))

        pizzas[2].toppings.append(get('mozzarella'))
        pizzas[2].toppings.append(get('mushrooms'))
        pizzas[2].toppings.append(get('ham'))
        pizzas[2].toppings.append(get('artichokes'))
        pizzas[2].toppings.append(get('olives'))
        pizzas[2].toppings.append(get('oregano'))

        pizzas[3].toppings.append(get('mozzarella'))
        pizzas[3].toppings.append(get('parmesan'))
        pizzas[3].toppings.append(get('eggs'))
        pizzas[3].toppings.append(get('bacon'))

        pizzas[4].toppings.append(get('seafood'))

        pizzas[5].toppings.append(get('mozzarella'))
        pizzas[5].toppings.append(get('parmesan'))
        pizzas[5].toppings.append(get('gorgonzola cheese'))
        pizzas[5].toppings.append(get('artichokes'))
        pizzas[5].toppings.append(get('oregano'))

        pizzas[6].toppings.append(get('mozzarella'))
        pizzas[6].toppings.append(get('Parma ham'))

        pizzas[7].toppings.append(get('mozzarella'))
        pizzas[7].toppings.append(get('oregano'))
        pizzas[7].toppings.append(get('anchovies'))

        pizzas[8].toppings.append(get('mozzarella'))
        pizzas[8].toppings.append(get('oregano'))
        pizzas[8].toppings.append(get('onions'))

        pizzas[9].toppings.append(get('mozzarella'))
        pizzas[9].toppings.append(get('mushrooms'))
        pizzas[9].toppings.append(get('pepperoni'))
        pizzas[9].toppings.append(get('Stracchino'))

        pizzas[10].toppings.append(get('mozzarella'))
        pizzas[10].toppings.append(get('eggplant'))
        pizzas[10].toppings.append(get('boiled potatoes'))
        pizzas[10].toppings.append(get('sausage'))

        pizzas[11].toppings.append(get('mozzarella'))
        pizzas[11].toppings.append(get('anchovies'))
        pizzas[11].toppings.append(get('capers'))
        pizzas[11].toppings.append(get('oregano'))

        pizzas[12].toppings.append(get('mozzarella'))
        pizzas[12].toppings.append(get('peppers'))
        pizzas[12].toppings.append(get('peas'))
        pizzas[12].toppings.append(get('porchetta'))

        pizzas[13].toppings.append(get('Olive oil'))
        pizzas[13].toppings.append(get('rosemary'))

        pizzas[14].toppings.append(get('mozzarella'))
        pizzas[14].toppings.append(get('sausage'))
        pizzas[14].toppings.append(get('french fries'))

        desserts = [
            Dessert(name='Tiramisu', price=3.99),
            Dessert(name='Chocolate mousse', price=2.49),
            Dessert(name='Amaretto cheesecake', price=3.39),
            Dessert(name='Banana Split', price=5.29),
            Dessert(name='Apple pie', price=2.99),
            Dessert(name='Dame blanche', price=3.59),
        ]

        drinks = [
            Drink(name='Coca cola', price=1.99),
            Drink(name='Coffee', price=2.29),
            Drink(name='Fanta', price=1.99),
            Drink(name='Fristee', price=1.99),
            Drink(name='Orange juice', price=1.99),
            Drink(name='Hot chocolate', price=2.19),
            Drink(name='Milk', price=1.59),
            Drink(name='Tea', price=1.59),
        ]

        deliverers = [
            Deliverer(deliverer_id='1', zip_code='6114'),
            Deliverer(deliverer_id='2', zip_code='6116'),
            Deliverer(deliverer_id='3', zip_code='6118'),
            Deliverer(deliverer_id='4', zip_code='6120'),
            Deliverer(deliverer_id='5', zip_code='6122'),
        ]

        db.session.add_all(deliverers)
        db.session.add_all(drinks)
        db.session.add_all(desserts)
        db.session.add_all(pizzas)
        db.session.add_all(toppings)
        db.session.commit()