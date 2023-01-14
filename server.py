"""Server for Debugging Lab."""

from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.secret_key = "this-should-be-something-unguessable"

COFFEE_PRICE = 2.50
TEA_PRICE = 1.50

menu_items = [
    "Regular Coffee",
    "Dark Roast Coffee",
    "Decaf Coffee",
    "Black Tea",
    "Green Tea",
    "Herbal Tea",
]

# One thing I'm noticing without reading the debugging directions is that 
# menu_items is not being passed as template data to the index.html template
@app.route("/")
def homepage():
    """Display the homepage."""

    session["cart"] = {}
    session["order_total"] = 0

    return render_template(
        "index.html", menu_items = menu_items, coffee_price=COFFEE_PRICE, tea_price=TEA_PRICE
    )


@app.route("/update-cart.json")
def update_cart():
    """Add a new item to the cart.

    Return updated cart as JSON.
    """

    item = request.args.get("item")
    # potential key error

    # The below commented out lines are wrong, and then the lines below that 
    # is correct:
    # session["cart"][item] += 1
    session['cart'].get('item', 0) + 1

    # session["order_total"] += get_item_price(item)
    session.get('order-total', 0 ) + get_item_price(item)

    return jsonify({"cart": session["cart"], "total": session["order_total"]})


def get_item_price(item_name):
    """Get the price of an item by name. DO NOT MODIFY this function."""

    if "Coffee" in item_name:
        return COFFEE_PRICE
    else:
        return TEA_PRICE


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
