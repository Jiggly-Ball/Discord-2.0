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


### Installation
This project only requires **pymongo (4.3.2)** to be installed.
You can either execute-
```
pip install pymongo==4.3.2
```
Or-
```
pip install -r requirements.txt
```
In your terminal.


### Setting up MongoDB
You can register / login to your account for MongoDB here: https://account.mongodb.com/account/login
After setting up your account and creating a database in your cluster, paste your token in `seceret.py` under the `token` key value.

Finally run **main.py**

Incase the **server.py** can't connect to the database, uncomment the lines 4, 5 & 6 in **server.py**
