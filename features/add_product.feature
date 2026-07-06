Feature: Add a product to the inventory
  As a user of the Inventory Manager
  I want to add new products
  So that they are registered in my stock

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"