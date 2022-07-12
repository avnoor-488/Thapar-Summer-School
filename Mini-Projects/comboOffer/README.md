
# Find Combo Offers within  a given range

A Django Based Web-App to predict the possible combinations of the entities in a csv.

### Built with
* [Django 3.2.9](https://www.djangoproject.com/)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file , this file has to be made in the same directory in which settings.py is there .

`EMAIL_HOST_USER = " email from which you'll send the results " `
* Do not enter the gmail password here
For generating password for mail system [click here](https://myaccount.google.com/apppasswords?rapt=AEjHL4PfI3cfF1f8D8WYpMN7uWSNu6nNpr9bneiUYYT-LWL-xqk-L4ftpDHOesxZrboomyXAhCW52c1Ggwk2YSL5RPvNNGZreg) , select the app as Mail and device as Windows Computer and Replace your password with the 16-character password shown above  

`EMAIL_HOST_PASSWORD = "16 - character code generated "`

## Run Locally

#### Open Windows PowerShell and Run these commands


Clone the project

```bash
  git clone https://github.com/avnoor-488/Thapar-Summer-School.git

```

Go to the project directory

```bash
  cd Thapar-Summer-School/Mini-Projects/comboOffer/
```
Create a virtual environment to install dependencies in and activate it:

```bash
  python -m venv venv
  venv\Scripts\activate 
```
You'll see like this on PowerShell

```bash
(venv) PS C:\Users\dead-hacker\Desktop\Thapar-Summer-School\Mini-Projects\comboOffer>

```

Now, Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

#### Also access this app by [clicking here](https://combo-offer.dead-hacker.tech/)
 

## Contributors

- [@Avnoor Singh](https://www.github.com/avnoor-488)
