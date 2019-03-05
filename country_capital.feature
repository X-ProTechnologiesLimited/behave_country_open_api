# file:features/country_api.feature
Feature:Country_Capital

  Scenario Outline:Get capital of a country
  Given I want to get the capital of "<country>"
	When I send the API request
	Then response should return integer "http_response_code" : "200"
  Then response should return string "capital" : "<capital>"
  Then response should return string "region" : "<region>"



	Examples:Country, Capital
        | country      |capital    | region |
        | India        |New Delhi  | Asia |
        | Ireland      |Dublin     | Europe |
        | France       |Paris   | Europe |
        | Great Britain|London     | Europe |
