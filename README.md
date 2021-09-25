# trelloEndpoint
an endpoint to create tickets using the Trello REST API

This is an application I made as a challenge in my attempt to get a job at NaNLabs. In order to run it you must follow these steps, assuming you've already cloned this repository:

- Install Python **3.6** (or later). You can download it [here](https://www.python.org/downloads/)
- Run `$ pip install -r requirements.txt` to install all required libraries.
- Generate an authtoken at https://trello.com/app-key . **Remember _not to share_ this token as it grants access to your user's data.**
- Once you've generated the authtoken, open set_board.py with a text editor and replace the value of API_TOKEN (Line 6)
- Run app.py to start the application. Read challenge.pdf as to know how to use it!

Keep in mind that the management team is responsible for creating the tickets, but they won't complete them. So, when creating a "bug" ticket, the application will asign it to a random member of the board, excluding the admin (management team). If your board has no members but yourself (meaning you're the admin) it won't assign the ticket to you.
To change this, go to **set_board.py** and inside the `get_members_id` function, change the *"filter"* value in `jsonObj` from *"normal"* to *"all"*.
