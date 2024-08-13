Feature: User creation through import file

  @userimport
  Scenario: Checking the user import functionality
    Given logged in from admin user
    When file imported with user unique data
    Then user created/imported successfully