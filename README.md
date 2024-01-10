# Phase 3 Project
## Overview
This application acts as a client databse manager for a non-profit organization that helps immigrants from different countries in the world.

This is inspired by my wife who works for one of these organizations so I decided to make a mock version of their database of clients. This has less information than the real database but is functions to get some of the important aspects of each client seeking help.



***cli.py***

The direct interaction the user has with the database. This is done by editing, adding and removing data as well as just getting related groups of data. The first half of the options involve interacting with the *clients.py* file and its functions. The second half of the options deal with interacting with the *countries.py* file and its functions.

***clients.py***

Holds the Client model and its functions for creating, searching and updating the database. It uses the datetime module to enter the date of when people join the organization. SQLITE does not support data for having a date in the database so it had to be converted to a string. It also uses countryinfo module to make sure that a country of origin is an actual place. This is the many of the one-to-many relationship.

When creating a new client it verifies that the country of origin has already been created in the coutnries database with the origin setter.

***countries.py***

Contains the Countries model and all the functions for creating, searching and updating the database for countries. This uses the countryinfo module and pycountry module that both work together to make sure that a country being added is a real country and also to get the primary language of said country. This is the one side of the one-to-many relationship.



### Modules Used
**datetime** A built in module that manages time, dates and intervals. I use it in this application to create the date people joined. Due to the fact that when the seed file is run the clients are created at the same time, many have the same date but it was a good experience learning how to work with the *datetime* module.

Though it was useful to learn, the sqlite program doesn't accept dates as a data type so I learned to use some built in functionallity to make it a string. 

**countryinfo** I needed a module that has information on all the world countries. This one was very useful. A country as capitol, location, bordering countries and so many more bits of information to pull from the country. It can also tell me the country's primary language, which is exactly what I needed. The only drawback is that the language was in the alpha 2 version, meaning it was the abbreviation of the language (i.e., english is EN). Some languages would be difficult to figure out by their abbreviation, especially for smaller countries with lesser known languages. Which leads me to my next module.

**pycountry** pycountry has a less information on specific data from countries, like what language one speaks, but a wider range of similar information. It has some information on countries, languages, language scripts and even currencies. I only needed the languages available to me. Using the abbreviation given to me by countryinfo, which is its alpha_2, I can search the languages for the correct one and get the name of what the alpha_2 returns. *pycountry* seems to have a lot of variety of information but not a great way to connect them, as in finding out what currency or language a country uses.

### Concluding

This project offers a simulated client database management system for a non-profit organization, drawing inspiration from real-world scenarios.