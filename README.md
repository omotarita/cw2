# Coursework 2

## **Requirements**

Requirements engineering is an iterative process in software engineering in which the expected capabilities of a finished product are discovered (or elicited), made more specific, validated and possibly changed. It plays an integral role in the development of a product, as these requirements come to shape the product goals which engineers, product managers and designers refer back to throughout development to ensure the product, once built, meets stakeholders' expectations. 

The innate complexity of software engineering projects is facilitated by the dividing up the work across different roles carried out by various team members. However, this "split" introduces complexities of its own such as fractionated progress due to individual interpretations of product goals. Requirements help manage this, as they ensure team members share a united perspective on the expectations of the finished product. This reduces project cost, as it mitigates the risk of building unsuccessful products.

 

### **Requirements identification methods**

The BABOK Guide (Business Analysis Body of Knowledge) provides a number of techniques that can be used to elicit requirements for software engineering projects. As a project is fundamentally underpinned by a need to serve users, they serve as the most useful source for discovering (or gathering) requirements.

Although the requirements identification methods available for this project are limited to solely brainstorming, if this were a real-world project, I believe focus groups, user interviews and observation would also be useful methods to undertake, as they embody a user-centred design focus by provide a deeper insight into users' needs.

To ensure I gathered a diverse range of requirements through brainstorming, I followed divergent design thinking principles to arrive at a number of ideas. Here's a few examples of some of the basic requirement ideas I came up with:

- Login/Create Account functionality
- Users with accounts can indicate what movies they've watched already
- Filter by streaming platform option


### **Requirement specification method**

After identifying a number of requirements, I formalised each of these into user stories. I chose this specification method as it uses natural language, thus ensuring widespread comprehensibility, and it goes even further by providing an insight into the rationale behind each user requirement, which the traditional "shall" natural language specification does not. User stories are also commonly used by Agile teams to specify requirements, so this method seemed appropriate given that this project is underpinned by the Data-driven Scrum methodology (which is an Agile framework). 

In specifying my requirements into user stories, I was also able to identify three individual user types for this web-app. Each of these user-types has a unique end-goal for their use of this web-app, described by their type title:

1. **Binge-watcher** (these users have a need for speed and are driven by a desire to find and watch movies that moderately match their preferences as soon as possible)
2. **Host** (these users want to find and watch movies that suit a group of people's combined preferences)
3. **Aficionado** (these users are more particular about the movies they watch and are willing to spend more time deciding, as long as what they eventually choose to watch closely matches their preferences)

 Individuating users by type as opposed to conflating them all together helped inform my understanding of my users' potential desires and interactions; as such, I was able to come up with a few more requirements.


### **Prioritisation method**

To prioritise my requirements, I considered a number of methods commonly adopted across software engineering and its related disciplines; namely the MoSCoW method, the Relative Weighting method and the 100-point method ([find here a more exhaustive list of prioritisation methods](https://toolkits.dss.cloud/design/)). I selected these three methods due to their simple quantification and/or categorisation of requirements according to realistic criteria (such as feasibility, cost, benefit etc.), which allows for more rapid prioritisation by product owners and software engineers. 

Although the MoSCoW method is more commonplace in Agile applications, I preferred to use a method which quantifies requirements, as opposed to simply categorising them, as this facilitates the creation of hierarchy in the requirements backlog. Ultimately, I chose the **Relative Weighting method** as its quantification takes into account the predicted benefit, penalty, cost and risk of each requirement, thus making it a considerably informed prioritisation method. Conversely, the 100-point method wasn’t chosen as, in spite of also quantifying requirements, it effectively represents a voting poll, with each voter scoring requirements using independent, undocumented criteria; as such, I felt requirements' scores were somewhat inconsistent. 

### **Documented and prioritised requirements**

Find here the [full list of prioritised requirements](design_requirements.csv)


### Validation

I validated my set of requirements against the following criteria:

1. Validity - do they reflect the real, changing needs of the users?
2. Consistency - is there duplication or any contradictory constraints?
3. Completeness - do they include everything needed?
4. Realism - can they realistically be implemented in the technology, budget and time?
5. Verifiability - can they be tested?

Given the validation criteria and their relative weighting scores, I decided to implement the majority of the listed requirements, aside from last one (relating to integrating the data from users' streaming platform accounts) as it seemed relatively unrealistic and unfeasible compared to the other requirements, due to its complexity. Furthermore, it received the lowest relative weighting score, which indicates that it doesn't reflect users genuine needs.


## Design

### The Application Design

The application design process of any software development project is an substantial activity involving aspects of aesthetic design, such as user interface design and wireframing, experiential design, such as user experience design, and application architecture, building roadmaps and diagrams representing a high-level view of the code underlying the app. For this project, I took a multifaceted approach to application design, considering each of these aspects to ensure all aspects of the app's intended functionality were explored and exemplified.

#### Embodying The User

The user’s actions and thoughts underpin all aspects of the design of an application, therefore in the effort to build effective, intuitive software, it seemed apt to start by deeply exploring the user’s potential interactions with the system.

![Use Case Diagram](use_case_diagram.png)

#### MVC (Model-View-Controller)

As implied in the initial repository for this project, although this web-app has the potential for useful applications across all manner of movie streaming platforms, for this initial minimum viable product (MVP) version of the app, we will be focusing on streamlining it for use with Netflix specifically. However, as the goal remains for the app to be compatible with a wide variety of streaming platforms, scalability and flexibility of this software is imperative. The use of design patterns in its development will help support this, and they ensure ease of maintainability of code. 

For this project, the Model-View-Controller (MVC) pattern has been employed as it is scalable and relatively simple to understand (which ensures team members joining the project late are able to easily pick up wherever it's left off).

**Model: Class Diagram**

Using the use case diagram as a reference point, and following the Domain-Driven-Design (DDD) approach for further support, I developed the following class diagram to depict the app's classes and their interrelationships.

![Class Diagram](Application_Design/UML_class_diagram.png)

**View: Wireframes**

The “view” aspect of the MVC pattern represents the structure and appearance of the user interface (UI). Here, this is depicted using wireframing, as this method permits both a low-fidelity visualisation of the user interface and an understanding of the flow of web pages (i.e. how users navigate through the app/what happens when they click something) which supports the development of the information structures (such as classes, entities and data) underlying the UI.

According to a 2017 survey, 42% of people prefer to use their laptop or desktop to watch TV shows, compared to 13% for smartphone fans and 23% television traditionalists. Although the statistics would likely be quite different for movies, due to widespread appreciation for enjoying cinema on the "big screen", the results of the 2017 survey imply that people are substantially more likely to watch movies on their laptop/desktop than their phones. For this reason,  I decided to optimise the app for desktop use, as it seemed that it would be the most likely Internet-connected device of choice for movie-watchers. 

Here is a flow diagram depicting the interactions between the app's webpages.
![Flow Diagram](Application_Design/flow_diagram_wireframe.png)


<details>
  <summary>Expand this to view the wireframes illustrating the visual design for each of the app's webpages (as shown featured in the flow diagram)</summary>
  
  ### Homepage (Not Signed In) (01)
  <img src="Application_Design/Homepage_NSI_wireframe.png" name="Homepage (Not Signed In) (01)">

  ### Homepage (Signed In) (01*)
  <img src="Application_Design/Homepage_SI_wireframe.png" name="Homepage (Signed In) (01*)">

  ### Choose For Me (02)
  <img src="Application_Design/Choose_For_Me_wireframe.png" name="Choose For Me (02)">

  ### Results (03)
  <img src="Application_Design/Results_wireframe.png" name="Results (03)">

  ### Movie Listing (04)
  <img src="Application_Design/Movie_Listing_wireframe.png" name="Movie Listing (04)">

  ### Blend (05)
  <img src="Application_Design/Blend_wireframe.png" name="Blend (05)">

  ### Blend OTP Confirmation (06)
  <img src="Application_Design/Blend_OTP_wireframe.png" name="Blend OTP (06)">

  ### Create Account (07)
  <img src="Application_Design/Create_Account_wireframe.png" name="Create Account (07)">

  ### Sign In (08)
  <img src="Application_Design/Sign_In_wireframe.png" name="Login (08)">

  ### Settings (09)
  <img src="Application_Design/Settings_wireframe.png" name="Settings (09)">

  ### Saved Preferences (10)
  <img src="Application_Design/Saved_Preferences_wireframe.png" name="Saved Preferences (10)">
</details>

**Controllers (and Routes)**

In an MVC design pattern, the controllers represent the 'brain' of the app; upon receiving a webpage request (represented by the url **routes**), the controller effects the request by using the models to retrieve the data it needs to populate a webpage and the view that renders its visual representation.

Find below a table describing the routes for this application and their corresponding views and controller functions.

| Route | View Description ([Refer to Wireframes for Views](#wireframes)) | Controller Function |
| --- | --- | --- |
| '/' | Index/Homepage (01) | **index()** |
| '/users/<*username*>' | Profile for a given user | **display_profile(username)** |
| '/users/signup' | Create Account page (07) | **create_account()** |
| '/users/login' | Login page (08) | **login()** |
| '/movie/choose/"<*sessionID*>"' | Choose For Me (02) | **choose_for_me()** |
| '/movie/<*movieID*>' | Movie Listing page (04) | **display_movie_listing(movieID)** |
| '/movie/results/<*sessionID*>' | Results page (03) | **display_results(sessionID)** |
| '/users/blend/<*blendID*>' | Blend page (05) | **blend(blendID)** |
| '/users/settings/<*username*>' | Settings page (09) | **display_settings(username)** |
| '/users/saved/<*username*>' | Saved Preferences (10) | **display_saved(username)** |

Here is the complete MVC diagram, further demonstrating how the **models**, **views** and **controllers** work in tandem. I modelled the diagram in UML due to its widespread popularity which suggests the diagram should be understood by the vast majority of developers.
![Complete MVC Diagram](Application_Design/MVC_diagram.png)

### Relational database design

Relational databases contain the multitude of datapoints for every entity interacting with an application. For this application, the entities are the users, the movies, the users' movie choices and their 'blends'. The data for each and every one of the interactions carried out in an app is documented in its relational database; as such, these systems are highly complex and incredibly confusing. Relational database design helps manage this complexity. By representing the relationships between entities in a relational database, developers are able to understand and automate how different datapoints affect each other, reducing the potential for error when data points change. 

For these reasons, I developed an Entity Relationship Diagram (ERD) to represent the logical design stage of the relational database design of this application. See below.
![ER Diagram](Application_Design/ERD_diagram.png)

<details>
  <summary>More detailed entities including constraints for each attribute</summary>

  ### User Entity
  <img src="Application_Design/user_entity.png" name="User Entity">

  ### Movie Choice Entity
  <img src="Application_Design/movie_choice_entity.png" name="Movie Choice Entity">

  ### Movie Entity
  <img src="Application_Design/movie_entity.png" name="Movie Entity">

  ### Blend Entity
  <img src="Application_Design/blend_entity.png" name="Blend Entity">

  </details>


<details>
  <summary>Find here an early stage design documenting the conceptual database design considerations for this project</summary>

  ### Initial Conceptual Database Design
  <img src="Application_Design/Conceptual_ERD.png" name="Initial Conceptual Database Design">

  </details>


## Testing
When building software with numerous entities, classes and methods the code often tends to become relatively complex, in spite of taking steps like code quality considerations, eliciting and clearly specifying requirements and carrying out careful application design processes to prevent this. Testing represents one of the final software 'finetuning' processes; at this stage, developers are focused on verifying that their software behaves as intended and on finding bugs.

### Choice of unit testing library
To test the code in this project, I chose to use the **pytest** library over unittest, as the pytest format of constructing tests within Python functions allows for more compact code than unittest (which requires tests to be packaged within separate classes). Keeping my code as compact as possible is another complexity management precaution, which helps me maintain quality and accuracy in my code.

### Tests
I began developing my tests by thoroughly considering the methods of the class I chose to investigate, [user.py](user.py). I then listed out a vast range of arguments, some more fussy than others, and then wrote out the corresponding return values for each of these. After this I began writing my tests, following the Arrange, Act and Assert (AAA) testing pattern to help me structure them. Instead of commenting "arrange", "act" and "assert" before each section of code, which is repetitive and somewhat redundant, I used the Given-When-Then formula to represent the logic behind each of my tests.

Find my tests in the [test_user.py file](test/test_user.py) in the [test folder](test).

### Test results
![Test Results](test/test_results.png)


### Continuous integration
I attempted to set up a continuous integration pipeline using CircleCI. Here's a link to my [yml file](.circleci/config.yml)

See here the results of a build attempt using CircleCI.
![Build Image A](.circleci/build_6.png)
![Build Image B](.circleci/build_6b.png)


## Weekly progress reports

<details>
  <summary>Report 1</summary>

  **What I did in the last week:**

  I assessed the requirements for my app by breaking down users needs through writing user stories and categorising these into app features. I then specified these using the MoSCoW prioritisation technique


  **What I plan to do in the next week:**

  I'll visualise these requirements by designing wireframes for my app. I'll also go deeper into breaking down how I'll achieve each of these requirements using application architecture (and possibly UML)


  **Issues blocking my progress:**

  None
 
  </details>

<details>
  <summary>Report 2</summary>


  **What I did in the last week:**

  I explored some commonly-used design patterns for Flask (e.g. MVC and Facade) and designed wireframes for my app.


  **What I plan to do in the next week:**

  Next week I plan to further flesh out my work on the design for this web-app and explore aspects of database design.


  **Issues blocking my progress:**

  I've had to leave the country at short notice for familial reasons - as such, preparations for the trip and the long flight have meant that I've had less time than I'd have liked to make progress in the project. This won't be a problem in future sprints, as I plan to be back at the start of the week.

 
  </details>

<details>
  <summary>Report 3</summary>


  **What I did in the last week:**

  Learnt about code quality standards and applied this learning to my work


  **What I plan to do in the next week:**

  I plan to run some unit tests on my code


  **Issues blocking my progress:**

  Time spent abroad did impede my work slightly at the start of the week, but things are picking up

 
  </details>



<details>
  <summary>Report 4</summary>


  **What I did in the last week:**

  Unfortunately, I haven't been able to make any progress on the coursework project this week


  **What I plan to do in the next week:**

  Next week, I plan to practice running unit tests using the pytest tool and wrap up the coursework 


  **Issues blocking my progress:**

  I have been unwell for the past week, which has made it quite difficult to work. I can't predict when this will cease to be a problem, but hopefully, it will be soon.

 
  </details>



## References

Prioritzation Techniques Article. SimpliLearn. 2021 [Blog]. Available at [https://www.simplilearn.com/agile-prioritization-techniques-article](https://www.simplilearn.com/agile-prioritization-techniques-article)
 (Accessed on 17 November 2021)
 
 Non-Functional Requirements as User Stories. Mountain Goat Software. 2013 [Blog]. Available at [https://www.mountaingoatsoftware.com/blog/non-functional-requirements-as-user-stories](https://www.mountaingoatsoftware.com/blog/non-functional-requirements-as-user-stories)
 (Accessed on 27 November 2021)
 
 Types of Constraints. IBM. 2014 [Blog]. Available at [https://www.ibm.com/docs/en/ias?topic=constraints-types](https://www.ibm.com/docs/en/ias?topic=constraints-types) (Accessed on 8 January 2022)
