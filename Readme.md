
# -:Scrape data for Mars:-

By Suvrangshu Ghosh

The homework consists of the following sections:
1. Scraping multiple websites and gathering data.
2. Creating database in Mongodb.
3. Creating Listings under mongo database.
4. Use MongoDb with Flask templating to create HTML page that displays all of the information that was scrapped from the various websites.

##### Scraping using Jupyter notebook - **mission_to_mars.ipynb**
##### python script for scraping - **scrapes_mars.py**

##### Mongodb database:

Screen capture showing Mongodb created the following:
Database = **mars_db**

![mongo](images/Mongo1.png) 

Under database mars_db collection mars_list is created 
![Collections - mars_list](images/mongo2.png)




##### Website screen shots:
![](images/web1.png)
**______________________________________________________________________________**
**Note:** *Please be informed that at times the webites from where I’m scraping data can be extra slow resulting in errors, to avoid that I have put time.sleep() at various places to slow down the scraping process and avoid issues.Sometimes the web can be down too.*
**_____________________________________________________________________________**

##### To start the process:
-	Go to the directory where the app.py is located
-	Open gitbash and cd to the directory.
-	Execute python app.py
-	You should see devtools starting:
![Command_prompt](images/commandprompt.png)

-	Open Web (Google Chrome browser) and type: ## http://127.0.0.1:5000/
**_______________________________________________________________________________**
*<u>**Note on Mars weather Twit:**</u>
Please be informed that the website(https://twitter.com/marswxreport?lang=en) is temporarily not giving latest weather details, soon they will start again. Once the details are available, the scraping code will automatically scrape the correct data.*
**_______________________________________________________________________________**

To start scraping, please press the button called “Press to Scrape for Mars”
This is a single page, kindly **scroll** down to see more details:

![MainPage](images/MainWeb.png)

![Page2](images/web2.png)