Feature: Remove a product from the inventory
  As a user of the Inventory Manager
  I want to remove a product
  So that discontinued items disappear from my stock

  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"
    But the inventory should contain "Sugar"