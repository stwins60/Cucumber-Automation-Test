Feature: Testing API functionality

    Scenario: Getting the latest movie, and getting movie rating
        Given I have a valid API key and I go to the API endpoint
        Then I should get the latest movie
        # Given A number as the movie_id
        Given I post a movie rating
        Then I should get the movie rating
        # Given I enter an invalid movie_id
        # Then I should get a 404 error




