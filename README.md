# ℹ️ **Overview**

Welcome to The Cullinary Collective web application designed and developed by Sione Yerkovich. The purpose of this project is to improve upon the skills I have acquired during my studies and the development of previous personal projects, with the end result being a production ready application.

This application was designed as an interactive recipe forum/social media mesh, I set out to complete this project with one thing in mind; create an application that is production ready in only 4 weeks while successfully implementing the "business rules" outlined in the roadmap document. The website has implemented many features over its development, within the 4 week timeframe I was able to conclude the application with the core features being as follows:

1. Navigation Bar: Streamlined access to the core features of the website: Recipe category navigation, search feature, The Recipe Book and a dynamic Log in/ Log out button
2. The Recipe Book: Here users can upload their own recipes to the recipe book. Submitted recipes get added to "The Collective" and become available for other users to find when using the search feature. This is also where favourited recipes are stored
3. Search feature: Users can search for existing recipes across the collective, this includes keywords such as "dinner" and specifics such as "steak"
4. Log-in/registration menu's that validate user details against the database
5. A password recovery system for forgotten passwords
6. Like system: users can engage with the community by liking recipes, this is tallied and displayed with the recipe details
7. Review feature: Submit reviews for recipes you love, or think need some improvement
8. Favourites: Users can favourite recipes for quick access. These are added to the favourites section in The Recipe Book
9. Enhanced security features with user permissions and data protection.
10. User friendly UI

# 🚀 **Tech Stack**

I built this site using Bootstrap, HTML, CSS, Python and Django.

I utilised ***HTML*** to build the overall skeleton of every component/page. Django was used for object-relational mapping while integrating the database; Python was used to access and manipulate the data population for things such as conditional views.

***PYTHON*** programming logic was integrated to provide logic to these pages, including what elements are displayed and under what conditions. It allowed me to cross communicate with the ***Django*** framework for features such as database creation/manipulation, error handling and page views.

***CSS and BOOTSTRAP*** allowed me to create user-friendly designs that adhere to various design principles.

# 🌟 **Dependencies**

To run the application, you must install the following:
- asgiref==3.8.1
- dj-database-url==2.3.0
- Django==5.1.7
- django-heroku==0.3.1
- django-widget-tweaks==1.5.0
- gunicorn==23.0.0
- packaging==24.2
- pillow==11.1.0
- psycopg2==2.9.10
- python-decouple==3.8
- sqlparse==0.5.3
- typing_extensions==4.13.0
- tzdata==2025.1
- whitenoise==6.9.0

***Installing Dependencies***

When installing the dependencies for the project, it is highly recommended you perform this inside of a virtual environment to avoid package conflicts.

To install the dependencies, run the command: 'pip install -r requirements.txt' in a terminal of your choice.

# 📖 **Challenges and/or learnings**

This project presented many challenges, one of the biggest challenges involved the scale of the application. Navigating and understanding how every working part of the application linked together was a HUGE change of pace compared to my previous projects. It was clear from the outset that rules had to be put in place if I was going to do this efficiently.

Rule 1 Organisation:
With so many moving parts I had to develop with structure. The easiest way to cut down development time is by making navigation and comprehension simple, right? This came down to even the smallest details, such as name variables for my urls and views.
If I know that i'm creating a model containing objects with clear similarities, KEEP THE NAMING SIMILAR. For example my url paths, all the paths that would fall under the category of "Daily Recipes" have name variables assigned to them starting with "daily-recipes". This meant when i needed to utilize them to create a template or view redirection, i saved valuable time by not having to navigate to the url.py file to find the name variable. I could just think to myself "ok i know this page wants to redirect to the dinner template, so daily-recipes-dinner" etc. This rule had no limit and even helped me become efficient in writing fast, clear commit messages due to my templates having relative naming conventions, this rule was utilised wherever there were multiple relative parts.

Rule 2 Simplicity:
Keeping it simple was extremely helpful, I believe its easy to get overwhelmed in the details when working at scale (This applies to both developers and the end-user). I wanted to ensure that I incorporated the features without "scaring" off the user due to high complexity and screen clutter (im looking at you pb tech). I navigated this by utilising my skillset in design and logic, one example of this is deciding to hide buttons until the parent element is hovered. This was a method of reducing screen clutter while also retaining those features. Another example is the idea of a modal for displaying details, as it can be confusing for the user when lots of redirections are involved. The modals popup interface allows the user to get what they need without the confusion a redirection causes.

Rule 3 Planning:
It was clear from the outset that the sheer volume of features involved would require a planning strategy. It required in depth thinking about the challenges i'll face and how I tackle problems as an individual. I broke this down with the project management skills I have gained during my studies, creating a project roadmap that provided me with a quick reference whenever I was off track. The roadmap has been attached to this README below ()


# ✍️ **Relevant documentation**
1. User guide for new and existing users
[The Cullinary Collective (User guide).pdf](https://github.com/user-attachments/files/19543136/The.Cullinary.Collective.User.guide.pdf)


2. Developer guide for programmers
[The Cullinary Collective - FAQ's.pdf](https://github.com/user-attachments/files/19542648/The.Cullinary.Collective.-.FAQ.s.pdf)

3. The Cullinary Collective Roadmap
[The Cullinary Collective roadmap.docx](https://github.com/user-attachments/files/19675837/The.Cullinary.Collective.roadmap.docx)

