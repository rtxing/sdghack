# sdghack
Contributers and Contact Information: Tiruvenganna Rao R
Problem Statement addressed (or explain your own): 
Enable Search For United Nations Sustainable Development Goals

##Description:
Explain what your project is trying to accomplish and how you utilized graph technology to achieve those goals. Describe how your submission is relevant to the problem statement and why it is impactful to the world. Remember to link your submission video here.
Our project provides a holistic view of the UN SDG’s and their relationships.
And enables coordination between the stakeholders.
We captured the business requirements and modelled the processes in Tiger Graph Database. Our approach to solving the problem is by using Knowledge Graph, Design Thinking and Value Chain Analysis.  A knowledge graph, also known as a semantic network, represents a network of real-world entities—i.e. objects, events, situations, or concepts—and illustrates the relationship between them. This information is usually stored in a graph database and visualized as a graph structure.
Some of the challenges in achieving the UN SDG’s are 

Impact
The United Nations Sustainable development goals have complex implementation challenges like financial, socio-economic, inequality, globalization, environmental degradation, population diversity and siloed information. These common challenges are an urgent call of action by each and every country. There are a lot of interconnections between different goals like ending poverty and other deprivations must go hand-in-hand with strategies that improve health and education, reduce inequality, and spur economic growth – all while tackling climate change and working to preserve our oceans and forests. If we are able to lay out all the interconnections between different sustainable development goals, it would be incredibly beneficial for all our stakeholders to achieve multiple goals with just one solution. That is what our project Global Goals Graph does uses the power of Graph technology. Our potential stakeholders for the UN SDGs are the general public, governments, conscious businesses, NGOs and civil -societies. Our solution showcases the Knowledge graph for the development goals. We use a holistic approach for our knowledge graph which enables coordination among stakeholders thereby addressing some of the above problems.
The social benefit includes saving the environment, maximizing resources for the world, improving quality of living, and good health. The economic benefit includes betterment of wages for lower-income, efficient use of resources and increased productivity, Our solution positively impacts the environment, increases the quality of life of people from different walks of life, from different communities, efficient use of resources, reduces poverty, better health and sustainable living. So our solution would prove to be a step toward achieving all the development goals and help the society sustain itself. It proves to be effective in helping create more understanding of the interconnections between all the 17 SDGs so that stakeholders can target multiple goals with one step which will increase the efficiency of the steps taken for achieving the goals and hence help in the betterment of our society and planet earth.
Innovative use case of graph
Our project has a complex implementation. It involves intensive Tiger Graph, Our approach for achieving the United Nations Sustainable development goals is through using Knowledge Graphs and Design Thinking. A knowledge graph, also known as a semantic network, represents a network of real-world entities—i.e. objects, events, situations, or concepts—and illustrates the relationship between them. This information is usually stored in a graph database and visualized as a graph structure.
In the context of the UN SDGs, achieving the goals would require a deep understanding of the challenges, value chain propositions, and looking into what frameworks would fit in to solve the root of the problems. Our Knowledge graph and design-thinking approach enable a holistic view of the entities and their relationships and coordination between the stakeholders. The approach is inherently suited to handle this type of complexity.
A graph's inherent properties of relationships among entities capture the requirement of what needs to be modelled and are well suited to handle the size and complexity of this nature. We analyzed the nature of the problem and similar problems, studied the existing practices, technologies and frameworks, and came up with the Knowledge Graph. After evaluating the different solutions, their features, offerings, pros & cons, we matched the requirements against the potential solutions and finalized Knowledge Graph. After implementing the tiger graph, we created a python-based server in Django, where we created a basic frontend using bootstrap, after which we integrated the Tiger Graph database with the frontend which resulted in a fully functional dynamic website. 

•	Ambitious and complex graph
Our solution requires modelling data from various diversified sources such as scientific, industry, governments and all kinds of projects. The tool that captures information & interactions among the data from all the above sources requires a complex graph such as Tiger Graph. Our Knowledge graph solution composes of 13 vertices and 13 edges. We started by first studying the UN SDGs. We studied how to dissect the value chain. The information present in each goal, target and indicator is transformed into a semantic representation. We identified the gaps in the value chain through gap analysis. We then wrote the functional requirements and then modelled the requirements into database design and user interfaces, developed queries, and built the frontend and backend.
Some functional features we targeted are speed, scaling, analytics, built-in REST APIs, and GSQL. We tried to have the platform as smooth and seamless as possible thus we targeted to have a high speed, we used the best and the fastest options for the frontend like bootstrap, and Django for the backend as it had a high compatibility speed with Tiger Graph. The website is also scalable and can be accessed from any form of device that has a connection to the internet. We show very detailed analytics on our frontend, after all the data gets processed by the database, it generates precise values that we show on our frontend as you must have seen on the Matrix page in the video. We also used several built-in REST APIs and also created our own multiple custom REST APIs for the dataset fetching and integration process. We wrote several GSQL queries to integrate the data into the database. We used GSQL because it is the fastest and most scalable query language for graph databases. That briefly summarises how we went about this project technically.
•	Applicable graph solution
The stakeholders of our solution are the general public, governments, businesses, NGOs and civil -societies. In particular, for example for SDG no. 11, stakeholders would be city residents, municipalities & residential societies. Most of the stakeholder's systems are providing information through Public access data portals, APIs, messengers, and bots which can be integrated into our system. Integrating the above systems /applications with our solution is easy. The backend data is modelled as per the requirements of the real-world processes and their inter-relationships are also captured. The solution accepts data from heterogeneous sources. Depending on the goal we are addressing, solutions can be adapted as needed. First, we Identify which goal, targets/or indicators we want to handle first and identify the systems like stakeholders systems, government systems, and private businesses. Next mapping the data, loading in our systems. Release the project as a pilot to a small set of users. Then take feedback and close the loop.
The size of the market depends on the goal. For example Goal no. 11: Sustainable Cities and Communities is around 700 bn. The market size for the Global climate change consulting market generated revenue of US$ 5.3 billion in 2017. The market size for the global renewable energy market was valued at $881.7 billion in 2020. Since UN Sustainable development goals are an urgent call of action by each and every country, the target and the impacted audience are huge. This being the need of the hour, has a wide potential to be applicable/implemented in today's world

Other additions:
•	Data: The data and Tiger Graph schema, data mapping and queries are present in the data folder
•	Technology Stack: Python, Django, Bootstrap, Tiger Graph 
•	Visuals: 
       
•	Link to our Website where the solution is hosted:
https://rtrao99.pythonanywhere.com/ 
Dependencies
The dependencies are mentioned in the requirements.txt file.
The project requires Python 3.8.10
Installation
Please give detailed instructions on installing, configuring, and running the project so judges can fully replicate and assess it.
This can include:

This app is built with Python 3.8.10, Django 3.2

Clone the repository:

git clone https://github.com/rtxing/sdghack.git

You can download at Python from : https://www.python.org/downloads/

After installing Python and adding the path to environment variables,

You can install virtualenv by  running below command

python -m pip install virtualenv




Access permissions have been given to TigerGraph-MDC  and devposttesting

To run the project From command line run the below commands:

>>> virtualenv tgenv
>>> cd tgenv/bin
>>> source activate

>>> pip3 install -r requirements.txt

>>> cd sdghack/
>>> python manage.py runserver

The server will be running at : http://127.0.0.1:8000/

The data and Tiger Graph schema, data mapping and queries are present in the data folder 
Known Issues / Limitations
Some queries are not optimized and take a little longer to execute.
Not all features of Knowledge Graph are implemented.
Future Enhancements
 We want to integrate our solution with blockchain and provide tokens / incentivization for good social behavior.
We want to show the SDG visually more dynamically.
Reflections
We did requirements analysis, designing the user interfaces, database design , front end and backend development. We used datasets from UN open data sets. The is scope to optimise the database design and capture requirements better.
References
Some reference links:
https://www.researchgate.net/publication/314450804_Achieving_Sustainable_Development_through_Value_Chain
https://knowsdgs.jrc.ec.europa.eu/interlinkages-visualization



