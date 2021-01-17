# tic-tac-toe
A 2 player terminal Tic Tac Toe game

            XOXOXOXOXOXOXOXO----Tic Tac Toe----OXOXOXOXOXOXOXOX

            RULES :

            1. It is a two player game.
            2. The markers are a cross (X) and circle (O).
            3. The first player starts with a cross (X).
            4. To win you have to align your markers (X / O)
                either vertical, horizontal or diagonal thrice.
            5. You can use the Number-pad to assign your markers
                to the corresponding blocks as shown below.

                   |   |                  7 | 8 | 9
                ---+---+---              ---+---+---
                   |   |       ----->     4 | 5 | 6
                ---+---+---              ---+---+---
                   |   |                  1 | 2 | 3

            6. Press 0 to quit the game

            XOXOXOXOXOXOXOXO----Tic Tac Toe----OXOXOXOXOXOXOXOX

**Requirement to play**

Python 3 installed on your device.

**How to start playing**

Clone the repository to your device and run the following command in the command prompt/terminal :

            python <absolute_path>/tic-tac-toe.py                # python C:\Users\device_name\Desktop\rps.py
                                                                 # python /etc/mnt/c/Users/device_name/Desktop/rps.py
OR
If you opened the terminal in C directory type:

            python <relative_path>/tic-tac-toe.py                # python \device_name\Desktop\rps.py
                                                                 # python /device-name/Desktop/rps.py

OR

You can go to the location where the file is saved and you can open the command prompt/terminal there and just type:

            python tic-tac-toe.py

**Create an Application Extension (.exe) file and play**

**Requirements**

Python 3 installed
py2exe

To install py2exe just type the following in the terminal:

            pip install py2exe        Or      python -m pip install py2exe

After fulfilling above requirements

* Clone the repository

* Run the setup.py file by using the command :

            python setup.py py2exe              #you can run by any method given above

* It will create a folder named dist (you can rename this folder as Tic-Tac-Toe or TTT).

* Inside the dist folder there will be a file called "tic-tac-toe" which will be an Application Extension (.exe)

* Click on the file to play the game like any other application
