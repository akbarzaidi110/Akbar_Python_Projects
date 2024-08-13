Feature: Change Password

  @changepwdgrid
  Scenario: Change password of market admin user from user grid
    Given logged in with nimda user
    When changing the password of market admin user
    Then market admin user logged in successfully

  @changepwdvalidations
  Scenario: Checking of change password validations
    Given user logged in successfully
    When changing the password by entering less than 8 characters
    And when changing the password by entering incorrect combination
    And when changing the password by entering from previously entered 24 passwords
    And when changing the password by entering password which is obtain through personal information
    And when changing the password by entering password which contains simple keyboard combinations
    Then validation error appears

  @changepwdsettings
  Scenario: Change password of market admin user from settings page
    Given logged in with market admin user
    When changing the password of available market admin user
    Then market admin user logged in with changed password