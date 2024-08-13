Feature: User Creation

  @adminusercreation
  Scenario: Market Admin can be created through NIMDA user
    Given NIMDA user logged in with valid credential
    When created a Market Admin user
    Then User created successfully