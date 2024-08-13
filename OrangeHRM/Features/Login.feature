Feature: Admin market user login


  @login
  Scenario: verifying admin user login
    When a user provides valid login credential
    Then user should be able to login