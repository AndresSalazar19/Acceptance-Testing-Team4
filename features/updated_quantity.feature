Feature: Update the quantity of a product
  As a user of the Inventory Manager
  I want to change the quantity of a product
  So that the stock reflects reality

  Background:
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |

  Scenario: Update the quantity of a product
    When the user updates product "Coffee" to quantity "25"
    Then the inventory should show product "Coffee" with quantity "25"