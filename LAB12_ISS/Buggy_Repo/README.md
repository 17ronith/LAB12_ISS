### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies  

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Name : Roll Number

### Table to keep track

| ID  | Issue Description                        | Identified By | Fixed By     |
|-----|------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                  |       Narain |     Whole Team     |
| 2   |Wrong script path in profile.html (styles/ instead of scripts/)    |Saharsh        |Saharsh        |
| 3   |Home.js is a completely unused file       |Saharsh       |Saharsh        |
| 4   |Missing quiz link in other HTML pages' navigation         |Saharsh          |Saharsh        |
| 5   |Missing news link in quiz.html navigation |Saharsh        |Saharsh       |
| 6   |Missing analytics link in quiz.html navigation       |Saharsh               |Saharsh              |
| 7   |Missing nav menu is analytics.html                                          |               |              |
| 8   |Missing container in items.html           |Saharsh        |Saharsh              |
| 9   |fixed models.py, error in var type                   | Aakarsh|      Aakarsh        |
| 10  |hardcoded users in analytics.py           |        Aakarsh       |       Aakarsh       |
| 11  |names should be name and usernames should be username in analytics.py|  Aakarsh|   Aakarsh        |
| 12  |no plot key returned in analytics.py      |     Aakarsh      |        Aakarsh      |
| 13  |changed API Based URL from 8001 -> 8000   | Ronith        | Ronith             |
| 14  | HTTP Method Fix: Changed the deleteItem function's method from "POST" to "DELETE" to follow RESTful standards.                                      |Ronith               |   Ronith           |
| 15  |    Content-Type Header Update: Updated "Content-Type" from "application/html" to "application/json" to properly send JSON payloads                                      |    Ronith           |      Ronith        |
| 16  |     Search Feature Added: Implemented a search input to filter quiz attempts by username.                                     |  Ronith             |  Ronith            |
| 17  |      Score Update Logic: Modified logic to increase score for correct answers and update high score if needed.                                    |  Ronith             | Ronith             |
| 18  |Game Over Condition: Added functionality to end the game after the first wrong answer.                                       |Ronith               | Ronith             |
| 19  |Reset Button Added: Introduced a reset button to restart the quiz and clear current state.                                       | Ronith              | Ronith             |
| 20  |  Changed /home to /: Simplified the root endpoint to make the base URL cleaner and more intuitive.                                        |  Ronith             | Ronith             |
| 21  | Added CORS Middleware: Enabled CORS to allow frontend-backend communication across different origins.                                         | Ronith              | Ronith             |
| 22  | Corrected router = {} to APIRouter(): Properly initialized the router to enable route registration.|Ronith               |  Ronith           |
| 23  | Fixed async DB init call: Made init_db() asynchronous to correctly await database initialization.                                         |Ronith               | Ronith             |
| 24  |      main.py in the FAST API APP, user_router was not included so we include i    |    akshith           |        akshith      |
| 25  |  Simplified delete to handle one ID cleanly: Updated delete logic to delete a single item by ID, improving clarity and correctness                                  |       durga        |       durga       |
| 26  |Replaced duplicate @router.post("/"): Removed redundant route to prevent conflict and ambiguity.                                          |     durga          |              |
| 27  |    Fixed duplicate @router.post("/") conflict
→ Ensured there's only one POST route to avoid ambiguity when creating or retrieving users.                                      |        durga       |           durga   |
| 28  |  Corrected async DB call
→ Used await init_db() to properly handle asynchronous MongoDB connection initialization.                                        |   durga            |         durga     |
| 29  |            Replaced erroneous delete_all() with delete_one()
→ Switched to delete_one({"_id": ObjectId(user_id)}) to accurately delete a specific user instead of attempting a non-existent bulk delete method.                              |     durga          |       durga       |
| 30  |  routs/quiz.py get question was always giving question[1]. changed it to give a random question                                        |    durga           |   durga           |
