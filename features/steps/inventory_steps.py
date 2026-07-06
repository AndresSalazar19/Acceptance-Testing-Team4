"""
Step definitions for the Inventory Manager acceptance tests.

Every step drives the real InventoryManager class defined in
Inventory_manager/inventory.py. Nothing is faked here: the assertions
check the actual state and return values produced by the application.

Behave gives each scenario a fresh `context`, so the InventoryManager
instance created in a Given step does not leak into other scenarios.
"""

from inventory import InventoryManager


# ---------------------------------------------------------------------------
# GIVEN
# ---------------------------------------------------------------------------

@given('the inventory is empty')
def step_impl(context):
    context.manager = InventoryManager()


@given('the inventory contains products:')
def step_impl(context):
    context.manager = InventoryManager()
    for row in context.table:
        name = row['Product']
        # Quantity is optional: some tables only carry the Product column.
        quantity = row['Quantity'] if 'Quantity' in row.headings else 0
        context.manager.add_product(name, quantity=quantity)


# ---------------------------------------------------------------------------
# WHEN
# ---------------------------------------------------------------------------

@when('the user adds a product "{product}"')
def step_impl(context, product):
    context.manager.add_product(product)


@when('the user lists all products')
def step_impl(context):
    context.listing = context.manager.list_products()


@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    context.message = context.manager.update_quantity(product, quantity)


@when('the user removes the product "{product}"')
def step_impl(context, product):
    context.message = context.manager.remove_product(product)


@when('the user searches for the product "{product}"')
def step_impl(context, product):
    context.search_result = context.manager.search_product(product)


# ---------------------------------------------------------------------------
# THEN
# ---------------------------------------------------------------------------

@then('the inventory should contain "{product}"')
def step_impl(context, product):
    names = [item['name'] for item in context.manager.list_products()]
    assert product in names, f'Product "{product}" not found in the inventory'


@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    names = [item['name'] for item in context.manager.list_products()]
    assert product not in names, f'Product "{product}" was unexpectedly found'


@then('the products listing should be:')
def step_impl(context):
    expected = [row['Product'] for row in context.table]
    actual = [item['name'] for item in context.listing]
    assert actual == expected, f'Expected {expected} but got {actual}'


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    found = context.manager.find_product(product)
    assert found is not None, f'Product "{product}" not found in the inventory'
    assert found['quantity'] == int(quantity), (
        f'Expected quantity {quantity} but got {found["quantity"]}'
    )


@then('the search result should be "{expected}"')
def step_impl(context, expected):
    result = context.search_result
    if expected == "found":
        assert isinstance(result, dict), f'Expected a product, got: {result!r}'
    else:
        assert result == expected, f'Expected "{expected}" but got "{result}"'
