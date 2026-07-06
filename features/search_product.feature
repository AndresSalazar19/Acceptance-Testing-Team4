# language: en
Feature: Search for a product in the inventory
  As a user of the Inventory Manager
  I want to search for a product by name
  So that I can quickly check whether it exists and its data

  Scenario Outline: Search for a product by name
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |
      | Sugar   | 5        |
    When the user searches for the product "<query>"
    Then the search result should be "<result>"

    Examples:
      | query  | result                         |
      | Coffee | found                          |
      | Salt   | No product found matching Salt |
