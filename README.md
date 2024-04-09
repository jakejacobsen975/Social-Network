# If not installed yet, install pyfiglet with the following command:
pip install pyfiglet

# To run the tests for this social network, first run:
./make_data # This creates the database
# Then run:
./populateTables # This runs a script to fill the tables of the database with information

# The database should be created and filled in now. Now run:
./soc_media interact # You will see a welcome message with a prompt to either create an account or login

# Now run:
./soc_media create # An account has been created

# Now run:
./soc_media login username # This will make sure you are logged in as the current user

# To follow someone, first run:
./soc_media follow # A list of names will appear and you will be prompted to select one person to follow by typing in a name as displayed in the list. You will be added to their followers list as they are added to your follows list.
