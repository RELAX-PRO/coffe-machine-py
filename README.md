# Coffee Machine Python

A simple coffee machine simulator written in Python that allows users to order different coffee drinks, manage resources, and handle payments.

## Features

- **Multiple Coffee Options**: Choose from espresso, latte, or cappuccino
- **Resource Management**: Tracks water, milk, coffee, and money
- **Payment System**: Accepts coins (quarters, dimes, nickels, pennies) with change calculation
- **Resource Reporting**: Check current resource levels
- **Simple CLI Interface**: Easy-to-use command-line interface

## Coffee Menu

| Drink | Water (ml) | Milk (ml) | Coffee (g) | Price ($) |
|-------|------------|-----------|------------|-----------|
| Espresso | 50 | - | 18 | 1.50 |
| Latte | 200 | 150 | 24 | 2.50 |
| Cappuccino | 250 | 100 | 24 | 3.00 |

## How to Run

1. Make sure you have Python 3 installed
2. Run the coffee machine:
   ```bash
   python3 "3.Coffe machine.py"
   ```

## Usage

- Type `espresso`, `latte`, or `cappuccino` to order a drink
- Type `report` to check current resource levels
- Type `off` to turn off the machine
- Follow the prompts to insert coins when ordering

## Example

```
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
How many quarters?: 6
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your espresso ☕️. Enjoy!
```
