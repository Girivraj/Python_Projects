# Coffee Machine Simulator

This Python script simulates a basic coffee vending machine offering three coffee types: espresso, latte, and cappuccino. Each drink requires specific quantities of water, milk, and coffee beans, with an associated cost.

## Features

- Tracks available resources (`water`, `milk`, and `coffee`).
- Checks resource availability before processing an order.
- Accepts coin payments (quarters, dimes, nickels, pennies) and calculates total amount inserted.
- Handles transactions by verifying payment, providing change if necessary, and updating profit.
- Displays resource reports and handles user commands like turning off the machine.
- Provides user prompts and messages in Marathi for a localized experience.

## Usage

Run the script and follow the on-screen prompts to order coffee, view resources, or turn off the machine.

Example commands:
- `espresso`
- `latte`
- `cappuccino`
- `report` — displays current resources and profit
- `off` — shuts down the machine

## How it works

The program runs an input loop that processes user choices. It validates resource availability, processes coins, updates resources and profit, and serves the selected coffee.

## Requirements

- Python 3.x

---

This project is a great introduction to Python basics, including loops, functions, conditionals, and user input handling.

Enjoy brewing your virtual coffee! ☕
