# Created by duany at 6/11/20
Feature: Allow users to login to API
  # Enter feature description here

  Scenario Outline: Login successfully with email and password
    Given  the email is "<email>"
    And the password is "<password>"
    When the user send data to login URL
    Then  the system should response "<status_code>" and "<status_text>"

    Examples: Users
      | email                |  password              | status_code  | status_text |
      | test@example.com     | testpassword           | 200          | OK          |
      | sol@gmail.com        | solagel1333@gmail.com  | 404          | Not Found   |

