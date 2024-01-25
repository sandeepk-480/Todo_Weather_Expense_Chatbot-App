<h3>Todo App, Weather App, Expense App, Chatbot App Compliled in a Django Project.</h3><br>

This Project Consist of 4 apps-<br>
1) Todo:<br>
- We can add task Here<br>
- The added task is shown in the form of a table.<br>
- Table consist of- ID, Task Name, Date added, Status (inprogress or finished), and action column which has delete button and a finished button which changes the status to "finished".<br><br>

2) Weather App:<br>
- Here i have used openweather api fro getting th current weather.<br>
- We enter the name of the city in the input area and it displays the  current weather with icon and temperature below in the form of a card.<br><br>

3) Expense App: <br>
- This app homepage is divided into 2 parts-<br>
- left side contain a form to add the expense, forms conatins Amount, Category, and description field and all are required field.<br>
- Right Side shows all the Expense data added in the form of a table.
- Table consist of Sr.No, Amount, Category, Description, Date Added, And Action column with has a delete button.<br><br>

5) Chatbot App:<br>
- I have Used Spacy Python library, which is basically a NLP library.<br>
- App homepage consist of a Modal Button, which shows all the Questions you can ask.<br>
It has input area to Enter your input.
- All the inputs are shown in the form of a list below with delete functionality included<br><br>

<h2> How to Use the Project</h2>
1) Open any of your code editor (VsCode or Pycharm).<br>
2) Create a Virtual Environment (optional but recommended).<br>
3) In terminal write this code:<br>
- git clone https://github.com/sandeepk-480/Todo_Weather_Expense_Chatbot-App.git <br>
- cd Todo_Weather_Expense_Chatbot-App <br>
- pip install -r req.txt<br>
4) Since i will not include my Weather Api key better include your's or atleast create a ".env" file in the root directory of your project to prevent errors, and write this inside .env file-<br>
API_KEY=1234wgd56<br>
this is some random words<br>
5) Run the project-<br>
"python manage.py runserver"<br>
