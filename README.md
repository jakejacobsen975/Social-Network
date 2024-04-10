![Screenshot 2024-04-09 200054](https://github.com/jakejacobsen975/Social-Network/assets/122470500/83db5a0c-2167-4289-9e64-ea3f45480f5a)
# Genral inforamtion
This Harry Potter-Inspired Social Network is a platform developed as part of a Database Systems course. Conceived by myself and Ryan Rampton, this unique social network draws inspiration from the enchanting world of Harry Potter. It is based on a command line interface.

The platform offers a myriad of features, including user authentication allowing individuals to sign in.

Another features is the ability to join a Hogwarts house, echoing the cherished tradition in J.K. Rowling's universe. Users can align themselves with Gryffindor, Slytherin, Ravenclaw, or Hufflepuff, forging bonds with fellow housemates.

Moreover, our social network facilitates seamless interaction between users, enabling them to follow each other. Users can engage in lively discussions, express their thoughts, and share their magical experiences through comments, with the option for nested threads to delve deeper into conversations.

Through meticulous database design and implementation, we ensured robust data management, guaranteeing the smooth functioning of the platform. From user profiles to house affiliations and interactive features, our database system underpins the entire social network, providing a reliable foundation for its enchanting experience.

# Intallation Guide 
Download or clone the repository 
```
git clone https://github.com/jakejacobsen975/Social-Network.git
```

### If not installed yet, install pyfiglet with the following command:
```
pip install pyfiglet
```

### To run the tests for this social network, first run:
```
./make_data
```
# This creates the database
if this fails with an error like ``` /usr/bin/env: ‘python3\r’: No such file or directory```
try using 
```
dos2unix make_data
```
if any more following steps fail run command with ```dos2unix``` infront
### Then run:
```
./populateTables
```
# This runs a script to fill the tables of the database with information

### The database should be created and filled in now. Now run:
```
./soc_media interact
```
# You will see a welcome message with a prompt to either create an account or login

### Now run:
```
./soc_media create
```
# An account has been created

### Now run:
```
./soc_media login username
```
# This will make sure you are logged in as the current user

### To follow someone, first run:
```
./soc_media follow
```
# A list of names will appear and you will be prompted to select one person to follow by typing in a name as displayed in the list. You will be added to their followers list as they are added to your follows list.
