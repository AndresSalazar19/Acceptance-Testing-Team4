# Inventory Manager — Acceptance Testing (Team 4)

Command-line Inventory Manager validated with **Behave** (BDD / Gherkin)
acceptance tests. Software Engineering II — I Term 2026, ESPOL.

## Structure
```
Inventory_manager/inventory.py   # Application logic (InventoryManager + CLI)
features/*.feature               # 5 Gherkin features / 5 scenarios
features/steps/inventory_steps.py# Step definitions (drive the real class)
features/environment.py          # Makes InventoryManager importable
```

## Setup & run
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

python Inventory_manager/inventory.py   # run the app
behave                                  # run the acceptance tests
```

## Product attributes
name, quantity, price, category

## Features / Scenarios
1. Add a product        2. List all products     3. Update quantity
4. Remove a product     5. Search a product (added — includes a not-found case)
