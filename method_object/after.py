'''
FROM: Martin Fowler
REPLACE FUNCTION WITH COMMAND
formerly: Replace Method with Method Object

The method `calculate_total` is too complicated. Replace it with a Command (Method Object).

1. Create an empty class for the function. Name it based on the function. 
2. Move the function to the empty class.
3. Keep the original function as a forwarding function until at least the end of the refactoring.
4. Follow any convention the language has for naming commands. If there is no convention, choose a generic name for the command's execute function, such as "execute" or "call".
5. Consider making a field for each argument, and move these arguments to the constructor.


OUTPUT
Items: table @ $100, chair @ $25
Discounts: 5, 9
Tax: 0.15
127.65
'''
class Order:
  def __init__(self, order_line_items=None,
               discounts=None, tax=0):
    if order_line_items:
      self._order_line_items = order_line_items
    else:
      self._order_line_items = []
    if discounts:
      self._discounts = discounts
    else:
      discounts = []
    self._tax = tax

  def order_line_items(self):
    return self._order_line_items

  def discounts(self):
    return self._discounts

  def tax(self):
    return self._tax

  ### MANY OTHER METHODS ###
  def calculate_total(self):
    # Call the new Command (Method Object) that was created
    return OrderTotalCalculator(self._order_line_items, self._discounts, self.tax()).compute()

  def __str__(self):
    items = ', '.join(map(str, self._order_line_items))
    discounts = ', '.join(map(str, self._discounts))
    return ("Items: %s\nDiscounts: %s\nTax: %.2f" %
            (items, discounts, self._tax))

class OrderLineItem:
  def __init__(self, name, price):
    self._name = name
    self._price = price
  def name(self):
    return self._name
  def price(self):
    return self._price
  def __str__(self):
    return ("%s @ $%s" %
            (self._name, self._price))

 ### NEW CODE ###
class OrderTotalCalculator:
  def __init__(self, order_line_items, discounts, tax):
    self.order_line_items = order_line_items
    self.discounts = discounts
    self.tax = tax

  def compute(self):
    subtotal = 0
    for line_item in self.order_line_items:
      subtotal += line_item.price()
    for discount in self.discounts:
      subtotal -= discount
    tax = subtotal * self.tax
    total = subtotal + tax
    return total



if __name__ == '__main__':
  order = Order([OrderLineItem("table", 100), OrderLineItem("chair", 25)], [5, 9], 0.15)
  print(order)
  print(order.calculate_total())