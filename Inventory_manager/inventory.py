class InventoryManager:
    def __init__(self):
        self._catalog = []

    def _make_entry(self, name, quantity=0, price=0.0, category="General"):
        return {
            "name": name,
            "quantity": int(quantity),
            "price": float(price),
            "category": category,
        }

    def add_product(self, name, quantity=0, price=0.0, category="General"):
        """Add a new product to the inventory."""
        entry = self._make_entry(name, quantity, price, category)
        self._catalog.append(entry)
        return entry

    def list_products(self):
        """Return all products currently in the inventory."""
        return self._catalog

    def find_product(self, name):
        """Return the product dict matching `name`, or None."""
        for entry in self._catalog:
            if entry["name"] == name:
                return entry
        return None

    def update_quantity(self, name, quantity):
        """Update the quantity of an existing product."""
        selected = self.find_product(name)
        if selected is None:
            return f'Product "{name}" was not found'
        selected["quantity"] = int(quantity)
        return f'Product "{name}" updated to quantity {quantity}'

    def remove_product(self, name):
        """Remove a product from the inventory."""
        selected = self.find_product(name)
        if selected is None:
            return f"Product {name} was not found"
        self._catalog.remove(selected)
        return f"Product {name} was removed"

    def search_product(self, name):
        """Search for a product by (exact) name."""
        selected = self.find_product(name)
        if selected is None:
            return f"No product found matching {name}"
        return selected


# ---------- Command Line Interface ----------

def print_menu():
    print("\n=== Inventory Manager ===")
    print("1. Add product")
    print("2. List products")
    print("3. Update quantity")
    print("4. Remove product")
    print("5. Search product")
    print("6. Exit")


def main():
    controller = InventoryManager()
    while True:
        print_menu()
        option = input("Select an option: ").strip()

        if option == "1":
            name = input("Product name: ").strip()
            quantity = input("Quantity: ").strip() or 0
            price = input("Price: ").strip() or 0.0
            category = input("Category: ").strip() or "General"
            controller.add_product(name, quantity, price, category)
            print(f'Product "{name}" added.')

        elif option == "2":
            items = controller.list_products()
            if not items:
                print("Inventory is empty.")
            else:
                print("Products:")
                for item in items:
                    print(
                        f'- {item["name"]} | Qty: {item["quantity"]} | '
                        f'Price: {item["price"]} | Category: {item["category"]}'
                    )

        elif option == "3":
            name = input("Product name: ").strip()
            quantity = input("New quantity: ").strip()
            print(controller.update_quantity(name, quantity))

        elif option == "4":
            name = input("Product name: ").strip()
            print(controller.remove_product(name))

        elif option == "5":
            name = input("Product name to search: ").strip()
            result = controller.search_product(name)
            print(result)

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()