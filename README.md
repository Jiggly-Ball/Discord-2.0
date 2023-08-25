# Discord-2.0

This is just a test project to learn about MongoDB's API and decided to implement it in a chat app similar to discord which also uses a database to store messages.
Because of that I don't need to code much of server (database) side code and very little client side code.

This is a very bad replica of discord as there are still some bugs which need to be fixed but I won't since this was just a test project related to MongoDB. But can still check out the code and maybe give me some suggestions. I will check them out.

There are some advantages and disadvantages of using this approach-
| Advantages                            | Disadvantages                     |
| -----------                           |   -----------                     |
| Lesser server & client side code      |       Slow                        |
| Fairly secure                         | Need to maintain a large Database |

There are probably more points to this but I'm lazy to list them all.


### Install packages
This project only requires **pymongo (4.3.2)** to be installed.
You can either execute-
```
py pip install pymongo==4.3.2
```
Or-
```
py pip install -r requirements.txt
```
In your terminal.


### Setting up MongoDB
You can register / login to your account for MongoDB here: https://account.mongodb.com/account/login
After setting up your account make a new Project and follow the steps below-

#### Click on Connect
![md1](https://github.com/Krishpy-Chips/Discord-2.0/assets/101330162/317b579c-4f47-4ce1-9f56-89414abe29ad)

#### A window will pop up and select Drivers
![md2](https://github.com/Krishpy-Chips/Discord-2.0/assets/101330162/77eafad9-0793-43f7-b4a5-18b4fe81853c)

#### Select the Driver as Python and its version as 3.6
![md3](https://github.com/Krishpy-Chips/Discord-2.0/assets/101330162/741433c1-f845-430f-b8fa-7575dae34996)
A link will appear at the bottom. Copy it and replace the empty string of **token** in **secret.py**.
After pasting, replace **<password>** with your Project's password (Remove the greater than and less than symbols when replacing the password).

Finally run **main.py**

Incase the **server.py** can't connect to the database, uncomment the lines 4, 5 & 6 in **server.py**
