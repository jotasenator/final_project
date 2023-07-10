# Capstone App

This is about a web application that will allow the IT department in a company to manage control of desktop computers and their peripherals, as well as have information about users who are responsible for them.

## Distinctiveness and Complexity

It is well known that in a company where there are several departments and numerous computer and peripheral devices, it is necessary to keep track of all of them to avoid problems associated with lack of control (theft, parts replacement, etc.).

In companies where there is no app like this, the process of inventorying the devices must be done by writing in files that contain paper forms, and this brings with it several problems because this information can deteriorate, not be available for some reason, and it is very useful to always have the information at hand. In addition, it becomes a real nightmare to collect information in this way.

This app offers advantages such as having the information available from any device, with the correct credentials, being able to edit it briefly, as well as giving users the possibility to report problems avoiding other means that are used for these purposes. Another advantage it offers is its versatility when performing an inventory on a PC or peripherals of interest, or an audit because it is more comfortable to do it from a cell phone or tablet.

In the admin.html template or in the app with user “admin” in Home it is explained what the different options that appear in the navigation bar do. The text will be transcribed here:

While I was doing this app I based myself on the knowledge provided in the course and after doing the indicated exercises I am certain that it does not resemble any of the assigned projects. It is simply an app that solves a different problem.

As you can imagine, making this application brought with it several challenges, both with logic and with the IDE I use (VSC), I will enumerate them:

1. I have problems when formatting templates because {% %} get disorganized and can result in errors. I haven’t been able to fix it.

2. My biggest problem was when I was doing the logic to edit the user profile because I was using taking information from the inputs and saving it and everything seemed to be ok, but it wasn’t saving the user on the server. Finding this simple line of code kept me busy for too long:

```python
   def edit_user(request, username):
       # ...
       user.username = username
       user.save()
       # ...
```

3. At first the app had register.html and register logic like the course exercises but after studying and implementing validators.py I changed the way it works leaving less freedom to normal users and ended up eliminating the implementation, as shown in the git history of the app.

4. Defining the path and how to save different images that can be loaded into the app ended up defining them like this in settings.py:

```python
# Set the location for storing uploaded files
MEDIA_ROOT = BASE_DIR / “media”
MEDIA_URL = “/media/”
```

5. Find a way to conditionally render an element other than {%if %}{%else%}:

```python
href=“{{ company_intranet|default:‘#’}}”
```

- or this:

```python
target=“{{ company_intranet|yesno:‘blank’}}”
```

- This yesno syntax makes me smile and that’s a good thing.

6. Being able to give “admin” user ability to edit footer information, since I was only passing it to footer in one view and needed it in all views and found solution context_processors.py which is like react context and thought it was great.

7. When I use the built in form.as_p I needed to check how the bootstrap was inplemented in the input fields I already had in the app so I check the boostrap.css files for copying the styles.

Basically this app is about entering information, storing it, being able to modify it and delete it if necessary, which does not mean that it does not have levels of complexity that required being overcome. I could add that at least in the companies where I have worked all these years many problems could have been solved if we had had it and been able to use it and until now I have not seen this tool anywhere. You could say that today’s me made this app for yesterday’s me, and yesterday’s me likes it!

## File Structure

### Python files

- `admin.py`: Registers the classes from models.py so they can be displayed in the admin interface.
- `apps.py`: Default configuration file created when creating the capstone app.
- `context_processors.py`: Allows obtaining values from classes that can be used globally.
- `forms.py`: Used to create forms with multiple input fields in a built-in way.
- `models.py`: Defines the characteristics of the database using classes.
- `urls.py`: Defines the URL patterns, linking the function, the template, and the name, and specifying whether it is dynamic or not.
- `views.py`: Contains all the functions that handle requests and deliver variable values and messages.

### HTML files

- `admin.html`: Describes the app’s characteristics and provides information about the different navbar options.
- `create_pc.html`: Form for creating a PC profile.
- `create_user.html`: Form for creating a user profile.
- `customize_app.html`: Form that allows the user to customize some parts of the app.
- `edit_pc.html`: Form for editing an already created PC profile.
- `edit_user.html`: Form for editing an already created user profile.
- `footer.html`: Footer that displays information that can be modified by the user.
- `index.html`: A template switcher that redirects to different information depending on the user type.
- `layout.html`: Template that contains the navbar and is included in most other templates.
- `login.html`: Displays the login interface for accessing the app.
- `pc_profile.html`: Shows information about an already created PC, with options to edit and delete it.
- `pcs.html`: Displays all already created PCs, ordered by department and sorted alphabetically.
- `reports.html`: Shows reports sent by users to the IT department.
- `user_profile.html`: Shows information about an already created user, with options to edit and delete it.
- `user.html`: Form for creating a report and sending it to the server. This is the only action available to non-admin users.
- `users.html`: Displays all non-admin users, sorted alphabetically.

## Installation

To run Capstone App, follow these steps:

1. Install the required dependencies, if needed:

   - pip install -r requirements.txt

2. Run the following command to set up the database:
   - python manage.py makemigrations
   - python manage.py migrate

## Usage

To run Capstone App, use the following command:

3. Run the following command
   - python manage.py runserver

Then, open a web browser and navigate to `http://localhost:8000` to access the app.

## Additional Information / Issues

When creating a user profile, I implemented a library for the phone input field that includes country codes and validations. However, the countries are sorted alphabetically and Åland Islands appears last on the list. I wanted to sort the list ignoring non-Latin letters, but I couldn’t find a way to obtain the values and do it.

## Support

If you have any questions or need help with Capstone App, please contact me at jotasenator@gmail.com.
