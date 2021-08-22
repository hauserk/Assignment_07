#----------------------------------------------#
# Title: CDInventory.py
# Desc: Working with structured error 
#       handling and pickling.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KHauser, 2021-Aug-20, Modified Assignment 6
# KHauser, 2021-Aug-21, Added Error Handling
# KHauser, 2021-Aug-22, Added Pickling
#----------------------------------------------#

import pickle

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    """Processing the data in list of dicts internal data structure"""
    
    @staticmethod
    def add_cd(ID, title, artist, table):
        """Function to manage internal data structure to add items to list of dicts

        Processes user entered data and adds information as dict to 2D table (list of dicts).

        Args:
            ID (string): CD ID from user input
            title (string): the CD title from user input
            artist (string): the CD artist name from user input          
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            intID = int(ID)
            dicRow = {'ID': intID, 'Title': title, 'Artist': artist}
            table.append(dicRow)
        except ValueError:
            print('Oops! ID must be an integer. Please try again')
        except:
            print('Oops! Cannot add CD')
    
    @staticmethod
    def delete_cd(table):
        """Function to manage internal data structure to delete items to list of dicts

        Processes user entered data and deletes information as dict from 2D table (list of dicts).   

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        intRowNr = -1
        blnCDRemoved = False
        try:
            for row in table:
                intRowNr += 1
                if row['ID'] == int(intIDDel):
                    del table[intRowNr]
                    blnCDRemoved = True
        except ValueError:
            print('Oops! ID must be an integer. Please try again.')
            blnCDRemoved = ''
        except:
            print('Oops! Cannot delete CD')
        return blnCDRemoved

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from pickled file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Data (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        data = []
        try:
            with open(file_name,'rb') as fileobj:
                data = pickle.load(fileobj)
            return data
        except FileNotFoundError:
            print('Oops! No such file or directory: ', file_name)
        except:
            print('Oops! Problem with reading file:', file_name)

    @staticmethod
    def write_file(file_name, table):
        """Function to manage saving serialized data via pickle from list of dictionaries to file

        Writes the data from 2D table (list of dicts) table into serialized file identified by file_name 
        one dictionary row represents one row of data in table
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            with open(file_name,'wb') as fileobj:
                pickle.dump(table, fileobj)
        except FileNotFoundError:
            print('Oops! No such file or directory: ', file_name)
        except:
            print('Oops! Problem with writing to file:', file_name)


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def delete_cd_message(outcome):
        """Displays message if CD was removed successfully or not

        Args:
            None.

        Returns:
            None.
        """
        if outcome == True:
            print('The CD was removed\n')
        elif outcome == False:
            print('Could not find this CD!\n')
        
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        try:
            for row in table:
                print('{}\t{} (by:{})'.format(*row.values()))
        except:
            print('\n')
        print('======================================\n')

    @staticmethod
    def get_cd_info():
        """Get User Input for CD ID, Album, Artist

        Args:
            None.
            
        Returns:
            ID (string): CD ID from user input
            title (string): the CD title from user input
            artist (string): the CD artist name from user input

        """
        ID = input('Enter ID: ').strip()
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return ID, title, artist


# 1. When program starts, read in the currently saved Inventory
lstTbl = FileProcessor.read_file(strFileName)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileProcessor.read_file(strFileName)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
        
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.get_cd_info()
        # 3.3.2 Add item to the table
        DataProcessor.add_cd(strID, strTitle, strArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
        
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = input('Which ID would you like to delete? ').strip()
        # 3.5.2 search thru table and delete CD
        result = DataProcessor.delete_cd(lstTbl)
        IO.delete_cd_message(result)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
        
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
        
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




