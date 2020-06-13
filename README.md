# Login API Application

The aim of this project is to create an app where I can demonstrate how we could implement a big application in Django. 
### Features

-   Repository-level layout and organization
-   Project-level layout and organization
-   Use of features, user stories, acceptance criteria
-   Use of BDD methodologies
-   Use the followings frameworks:
    - Django
    - Django Rest Framework
    - Behave
    - Behave Django
    - Drf Yasg 
    
    *Note: This app demonstrates how to use the frameworks mentioned before.*

### Environment Setup

This process assumes a basic knowledge of the Python ecosystem. You need to be familiar with Pip, Virtualenv, and its counterpart Virtualenvwrapper.

-   Make sure you have everything installed and working:
    - virtualenv
    - virtualenvwrapper
    
- Clone this repository 

     git clone https://github.com/macurandb/login-api-app.git
 
- Set up your Python virtual environment
    - Install virtualenvwrapper
        ```
         $ pip install virtualenvwrapper
        ```
    - Configure folder of projects  
        ```
        $ export WORKON_HOME=~/.virtualenvs
        ```
    - Add virtualenvwrapper.sh to .bashrc
      ``` 
      $ /usr/local/bin/virtualenvwrapper.sh
      ```
    - Create a new virtualenv
        ```
        $ which python3 #Output: /usr/bin/python3
        $ mkvirtualenv --python=/usr/bin/python3 loginTestApp
        ```
    - Activate environment
        ```
         $ workon loginTestApp
        ```  
- Install requirements
    ```
     $ pip install -r requirements.txt 
    ```
- Check all code
    ``` 
    $ python manager check 
    ```
- Run migrations
    ```
    $ python manager migrate
    ```
- Create superuser
   ```
   $ python manage.py createsuperuser
  ```  
### Running Tests
- To run a unit tests, please use 
    ```
    $ python manager test
    ```
- To run a BDD tests, please use
    ```
    $ python manager behave
    ```
  
  Output 
      
      Creating test database for alias 'default'...
            Feature: Allow users to login to API # features/login_user.feature:2
            
              Scenario Outline: Login successfully with email and password -- @1.1 Users  # features/login_user.feature:13
                Given the email is "test@example.com"                                     # features/steps/login/login_steps.py:6 0.001s
                And the password is "testpassword"                                        # features/steps/login/login_steps.py:10 0.000s
                When the user send data to login URL                                      # features/steps/login/login_steps.py:14 0.208s
                Then the system should response "200" and "OK"                            # features/steps/login/login_steps.py:26 0.000s
            
              Scenario Outline: Login successfully with email and password -- @1.2 Users  # features/login_user.feature:14
                Given the email is "sol@gmail.com"                                        # features/steps/login/login_steps.py:6 0.000s
                And the password is "solagel1333@gmail.com"                               # features/steps/login/login_steps.py:10 0.000s
                When the user send data to login URL                                      # features/steps/login/login_steps.py:14 0.163s
                Then the system should response "404" and "Not Found"                     # features/steps/login/login_steps.py:26 0.000s
            
            Feature: Register a user # features/register_user.feature:2
            
              Scenario Outline: Register user into the API successful -- @1.1 Users                   # features/register_user.feature:12
                Given the user put "Duany", "Baro", "macurandb@gmail.com",  "Macuran4955061233", "34" # features/steps/register/register_steps.py:6 0.177s
                When the user send data to register URL                                               # features/steps/register/register_steps.py:18 0.000s
                Then the system register "201" and "Created" and token                                # features/steps/register/register_steps.py:22 0.000s
            
              Scenario Outline: Register user into the API successful -- @1.2 Users    # features/register_user.feature:13
                Given the user put "Sol", "Battet", "sol@gmail.com",  "solagel1", "32" # features/steps/register/register_steps.py:6 0.170s
                When the user send data to register URL                                # features/steps/register/register_steps.py:18 0.000s
                Then the system register "201" and "Created" and token                 # features/steps/register/register_steps.py:22 0.000s
            
              Scenario: Register user into the API fail                                          # features/register_user.feature:15
                Given the user put "test1", "test111", "test@example.com",  "testpassword", "34" # features/steps/register/register_steps.py:6 0.005s
                When the user send data to register URL                                          # features/steps/register/register_steps.py:18 0.000s
                Then the system register "400" and "Bad Request"                                 # features/steps/register/register_steps.py:31 0.000s
            
            2 features passed, 0 failed, 0 skipped
            5 scenarios passed, 0 failed, 0 skipped
            17 steps passed, 0 failed, 0 skipped, 0 undefined
            Took 0m0.726s
            Destroying test database for alias 'default'..
      
### Run the project
     ```
    $ python manager runserver
    ```
## Check the documentation
  This example use the `drf_yasg` to generate the documentation. 
  You can see the documentation in the followings links:
  - http://localhost:8000/api/v1/docs
  - http://localhost:8000/api/v1/redocs

### Compatibility
* Python 3.0
* Django 3.0
* SQLite, PostgreSQL, MySQL

## Contact

Reach out to me at:

- LinkedIn : [linkedin.com/in/msc-duany-baró-menéndez-1a552a160/](https://www.linkedin.com/in/msc-duany-bar%C3%B3-men%C3%A9ndez-1a552a160/)
- Email : [macurandb@gmail.com](mailto:macurandb@gmail.com)

## License
[GPL](https://choosealicense.com/licenses/GPL/)

### TODO
- Integrate with Google, Facebook
- User CRUD
- Setup Production and CI environments  
- Others 
