# Created by duany at 6/11/20
Feature: Register a user
  # Enter feature description here

  Scenario Outline: Register user into the API successful
    Given the user put "<first_name>", "<last_name>", "<email>",  "<password>", "<age>"
    When the user send data to register URL
    Then the system register "<status_code>" and "<status_text>" and token

    Examples: Users
      | first_name  | last_name   | email                |  password               | age  | status_code  | status_text |
      |  Duany      |  Baro        | macurandb@gmail.com  | Macuran4955061233      | 34    |   201  | Created |
      |  Sol        |  Battet      | sol@gmail.com        | solagel1               | 32    |   201  | Created |

  Scenario: Register user into the API fail
    Given the user put "test1", "test111", "test@example.com",  "testpassword", "34"
    When the user send data to register URL
    Then the system register "400" and "Bad Request"
