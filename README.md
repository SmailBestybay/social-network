# Country Finder
#### Video Demo:  https://youtu.be/CiHE0b10Jog
#### Description:
Country Finder is a web app that searches Netflix catalog across the globe.
The search result returns a list of netflix titles with flags of countries where that title is available.

It uses [unogsNG database](https://rapidapi.com/unogs/api/unogsng) through RapidApi.

Flask is the backend framework. 

The backend tasks are:
- make API calls to unogsNG database.
- parse over JSON response and convert it into Python dict
- manipulate the converted JSON to extrapolate country names list
- render templates with JINJA

Frontend technologies are HTML, CSS, Bootstrap, [MDB flags](https://mdbootstrap.com/docs/standard/content-styles/flags/).

For Card styling I referenced [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Card).

I used Visual Studio Code IDE in a virtual environment. 

In the future, there are multitude of features I would like to add, and improve general user experience with better styling and layout.
An example of that would be to make each card a link to a pop up page that would show more details about a particular search result. 

Description of each file in the project:
- **app.py** is the main back end file that contains the routes, manipulates converted JSON, and passes arguments to JINJA.
- **helper.py** contains the function to make the API call to unogsNG database.
- **templates** folder contains html templates.
- **static** folder contains css folder which contains styles.css file.
- **styles.css** is the stylesheet for the web app, mainly for card layout of the results page.
- **requierments.txt** is flask requirements file.

#### Development journey and decisions:

I wanted to create a tool for VPN users to search easily for titles in different countries.
During the time of isolation, people were able to connect with others thanks to software tools like Netflix Party.
Netflix Party lets users stream movies and shows in sync. Hence my idea would help people connect further by discovering more options in the global Netflix catalogue.

From research I found [unogs.com](https://unogs.com/), it is exactly what I had in mind. 
While looking at how that website was built I learned that they also provide an API to their database. 
This was a great opportunity for me to learn how to use the REST API. After I understood how to use the endpoints, I had to learn how to parse JSON. 
I had to learn that the requests library has its own json() method, but it was not enough. 
One of json response sub objects (the key value pair object of country codes and names) would not convert to a python dictionary...
So I had to concatenate that object with a missing pair of curly brackets, then use json.loads() method to turn it into a python dictionary.
Once I was able to access all the values of the JSON response with python, it became much easier. 

In order to programmatically generate appropriate country flags per search result, I had to use python's string manipulation techniques. 
This is where I am so glad that I was able to use python for this project. String manipulation with python is very intuitive. 

On the front end side of this project, I had to learn a lot about CSS and HTML. I have gained a lot of respect for CSS over the course of this final project.
I found it tremendously difficult to layout or size elements as I wanted. There are so many things about this project that I would like to improve from a CSS perspective.
However, I'm afraid it's beyond my scope of knowledge at this point. 




