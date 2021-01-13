To install all modules needed to run this server: 
- Open your terminal and type pip install -r requirements.txt

To run the server:
- python -m flask run 
- python run.py 
- FLASK_APP=run.py FLASK_DEBUG=1 flask run (with git bash)

Admin account:
- Admin account: admin@gmail.com
- Admin password: SpiderMan2@@1

User account Management:
- Disable account functions
    - users able to disable/ restore account
    - To after disable account go to login page
    - type the email and password for the account that was disabled
    - It should lead to a page asking if you want to restore account
    - Click restore account and type in email and password
    - It will log you back into the account and the account will be restored with all your previous information still saved

- Credit Card saving
    - Able to add/ delete/ edit 
    - If user adds an existing credit card it will show error

- Address Saving
    - if user adds an existing address that the user themself have already previously added it will also not allow user to add and show error
    
- Forget Password
    - Register with a valid and existing email that you can access
    - Go to Login page click on forget password
    - It will lead to a page asking user to enter email
    - It will send an email to the users email that has been entered
    - If an users enter an email that has not been registered yet it would not send the email and would show an error
    - Go to gmail and click on the reset password link to change password
    - If user takes more than 10 mins, the reset token will no longer be avaliable and users will no longer be able to change password (for security purposes)

- Viewing of logs
    - Login using the admin account 
    - click on the admin panel on the navigation bar 
    - navigate to the logs section on the admin panel 

- paypal account credentials 
    - Verify transactions on this url by logging into the following credentials listed below: 
        -> https://www.sandbox.paypal.com/sg/signin
    - Client account (customer):
        -> email: sb-x0efn2935844@personal.example.com
        -> password: pr{eC+4E
    - Merchant account (seller):
        -> email: prestigium@business.com
        -> password: VX7nz#40

- Our customer email:
    - On your machine, you would need to into the following credentials to forward 2fa requests, forget password requests
    -> email: testemailnyp@gmail.com
    -> password: ValentiaTest2@@1
    - Logged onto gmail to get notified of suspicious activities:









