# Data Acquisition RIT COVID Dashboard
This is script that pulls data from RIT COVID-19 dashboard, such as positive cases for Students and Employees, and creates 
a graph with trend line. Moreover, it collects the data in the CSV file and captures screenshots of the data on the website.

The script further sends the generated graph with a message to users/groups on Telegram.
___
Packages: 
1. Selenium
2. Webdriver Manager
3. Beautiful Soup 4
4. Pandas
5. Numpy
6. Matplotlib
7. pyTelegramBotAPI
8. Pillow
___

> Run `application.exe` to get updated data csv, graph, and screenshots.
> 
> If the `exe` file does not work, use a pyinstaller or auto-py-to-exe to 
> generate a new exe file.
> Create an info.txt file in `src` directory with this information:
> 1. bot_token retrieved using @BotFather on Telegram
> 2. control chat_id (yourself/the person you are wanting to send the info to)
> 3. send chat_id* (the person you are wanting to send the info to)
> 4. send_group chat_id* (the group you are wanting to send the info to)
> 
> *These can be placeholder `int` numbers.
> 
> Lines 36 and 38 are currently set to ***control chat_id***. 
> Change these lines depending on whom you want to send the information to.
> 
> The chats with the sender must be initiated for it to send the information.
> 
> Command for pyinstaller:
> - pyinstaller -F [~\data-acquisition-rit-covid-dashboard\src\application.py]
> 
>  *exe file must be placed inside the main directory, data-acquisition-rit-covid-dashboard*

Author: Maksim Pikovskiy Email: pikmak2001@gmail.com
