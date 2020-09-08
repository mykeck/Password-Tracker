# Passwordlocker

## Built By [Mike Collins](https://github.com/mykeck)

## Description
password Locker is a Terminal run Python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials 
* Generate a password for a new credential/account

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Do you want to sign up or login : Click 's' to sign up or 'l' to login |
| Display prompt for creating an account | **Enter: cc** | Enter your username and password |
| Displays credentials | **Enter: vc** | Shows credentials |
| Display codes for navigation | **Enter fc** | find credentials|
| Display prompt for saving an already existing credential | **Enter: del** | Delete credentials|
| Exit application | **Enter: lo** | logout the current logged in account |

## SetUp / Installation Requirements
### Prerequisites
* python 3.6
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/mykeck/Password-Tracker
        $ cd Python

## Running the Application
* To run the application, in your terminal:

        $ chmod +x locker.py
        $ ./run.py
        
## Testing the Application
* to run the tests for the class file:

        $ python3.6 test_locker.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2020 [Mike Collins](https://github.com/mykeck/Password-Tracker/blob/master/LICENSE)
