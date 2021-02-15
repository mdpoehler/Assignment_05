#------------------------------------------#
# Title: CDInventory.py
# Desc: Script that asks user to add CD information to an inventory and then save to a file when ready.
# Change Log: (Who, When, What)
# MPoehler, 2021-Feb-10, Retrieved File created by DBiesinger
# MPoehler, 2021-Feb-11, Replaced TODOs from DBiesinger with code.
# MPoehler, 2021-Feb-12, Added formating to the printing of the inventory
# MPoehler, 2021-Feb-12, Added to save-to-file portion allowing user to append or overwrite information in txt file
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
# Choice system results and output
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l': # no elif necessary, as this code is only reached if strChoice is not 'exit'
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow) # loading existing data
        objFile.close()
        pass
    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('{:6}{:20}{:20}'.format('ID', 'CD Title','Artist')) # Formatting from the advice recieved on previous assignment by DKlos
        for row in lstTbl:
            print('{:<6}{:20}{:20}'.format(*row.values())) # Formatting from the advice recieved on previous assignment by DKlos
    elif strChoice == 'd':
        print('[e] Delete latest entry \n[t] Delete current inventory')
        delChoice = input('e or t: ')
        if delChoice.lower() == 'e':
            lstTbl.pop() # deleting latest entry
        pass
        if delChoice.lower() == 't':
            lstTbl.clear() # deleting current inventory
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        print('Would you like to: \n[o] Overwrite data in file with current inventory\n[n] Append data in file with current inventory')
        sveChoice = input('o or n: ')
        if sveChoice.lower() == 'o':
            objFile = open(strFileName, 'w')
        pass
        if sveChoice.lower () == 'n':
            objFile = open(strFileName, 'a')
        pass
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')