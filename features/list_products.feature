# language: en
Feature: List all products in the inventory
  As a user of the Inventory Manager
  I want to list every stored product
  So that I can review my current stock
 
  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the products listing should be:
      | Product |
      | Coffee  |
      | Sugar   |
