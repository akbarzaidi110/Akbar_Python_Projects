Feature: User login

  @validcred
  Scenario: Admin user Login
    When user logged in with valid credential
    Then user should be logged out successfully

  @invalidcred
  Scenario: Admin user not Logged in
    When user tries to login with invalid credential
    Then user should not be logged in