Feature: Testing Amazon Functionality
    Scenario: Go to Amazon and search for a laptop
        Given I go to amazon.com
        When I enter "laptop" in the search bar
        Then I should see "laptop" in the search results
        When I click on an item in the search results
        # Then I should see the item's title
        # When I click the "Add to Cart" button
        # Then I should go to the cart