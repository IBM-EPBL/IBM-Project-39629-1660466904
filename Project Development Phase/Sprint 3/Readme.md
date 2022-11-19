### Sprint 3 - Getting News preferences from user

- New code added in
		app.py line 65
		templates/category.html (UI to get preferences)
		templates/test.html (To print update preferences of the user)
- This module will be executed on the first time login of the user or from the profile to change preferences
- The email id from session storage is used to INSERT/UPDATE records in user_data
- A string - list of preferences got in a specified format and used with the NewsAPI (Sprint 4)