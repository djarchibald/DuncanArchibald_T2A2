### Duncan Archibald T2A2  
<br>

**R1: Identification of the problem you are trying to solve by building this particular app.**  

One of the biggest challenges faced by hobby photographers is the sheer expense of the kit involved. Top-end lenses especially can run into the thousands of dollars, and are usually backed by slick marketing and in-depth reviews that combine to convince the hobbyist that they *need* to have the latest lens in order to produce high quality images. 

There are two common scenarios in particular that my app aims to address. The first is where a photographer might want to try out a lens over a period of time and in different conditions before they commit thousands of dollars to buying it. The second is where a photographer plans a shoot that requires a very specific lens which would be too expensive to justify buying for a one-off (or rare-use) occasion. For example, a photgrapher more used to shooting landscape or street may not have the ideal lens for a portrait session, equally, a studio photographer may not have a long zoom lens to hand if they want to go and shoot some wildlife.

My app will let groups of photographers,  whether members of the same photography club, or even just an informal group of friends- list lenses they are willing to lend and others to see what lenses others have that they might be able to borrow.


**R2: Why is it a problem that needs solving?**  

Believe it or not, Gear Acquistion Sydnrome (GAS) is a widely-used, if slightly tongue-in-cheek, photography term that describes this problem. Hobby photographers in particular are  known to be chronic sufferers of GAS, which can get quickly out of hand as they end up spending huge amounts of money, convinced that the latest lens will see their pictures on the cover of Vogue or National Geographic. 


While a sadly incurable condition, my app will help mitigate its effects, with its ultimate aim being to save photographers money. If a photographer can try a lens before they buy, they can be sure that they are choosing a lens right for them and their photography before committing to a significant spend. They will be able to compare and contrast different options in a way they couldn't if they simply went out and bought a new lens immediately. The app will also allow photgraphers to borrow lenses for rare use occasions, for example if experimenting in a new genre, or if they require a specific spec of lens that they don't currently have. This will hopefully mean they won't be tempted to go out and spend thousands of dollars on a lens that will then largely sit unused.  

**R3: Why have you chosen this database system. What are the drawbacks compared to others?**  

I chose to use PostgreSQL. It is an extremely popular and widely used database with a number of advantages when compared to some of the (many) alternative DBMS's such as MySQL or Oracle Database.  

From my perspective as a new developer, some of its key strengths are:

- It is widely compatible. I knew that by using PostgreSQL I was unlikely to have to worry too much that I would not be able to run it on my machine or have any challenges with the various packages that I knew I would be making use of in building my app.
- On a related note, PostgreSQL's large community of users is a huge strength for a newcomer to the field. There are - I can confirm from personal experience(!) -  a wealth of resources available online including tutorial videos, questions and answers in forums and lengthy documentation on almost every aspect of the DBMS.
- The first two examples listed can in part by explained by the fact PostgreSQL is open-source. It is therefore freely available and if required can be customised. While customisation was not neccesarily on my shortlist of things I needed from a DBMS for this project, the fact that it was freely available and well supported, definitely was. I was reasonably confident going into the project that I would make heavy use of the online support available; a prediction which was borne out when it came to building my app.
- PostgreSQL is known to be a secure DBMS with multiple options such as role-based access and SSL encryption which are useful when considering data protection. While not necesarily a fundamental reason I chose it for this project, it would be a consideration should this app ever get to a stage where it is deployed.
- Data integrity is key to any database, and was not something that I wanted to have any concerns about in this project. PostgreSQL is known for its strong support of ACID compliance which ensures data is reliably and consistently stored and retrieved. 
- Finally, PostgreSQL is widely held to be both scalabale and extensible. It is able to handle huge amounts of data easily and can be used with a number of extensions and tools (over and above its already strong suite of functions) where neccesary. This links to the point I made earlier about the wide and active user-base, as many users have developed their own tools that can be easily plugged into PostgreSQL.  

So we can see that there are compelling reasons for any developer to choose to use PostgreSQL. It does howver have some drawbacks compared to its competitors:

- PostgreSQL is complex, and can be difficult for new users. I found it a very steep learning curve, particularly when getting to grips with some o the syntax required which at several points in this assignment brought me to complete halts for extended periods.
- I spoke earlier about the large and engaged community of users that provide a great resource for others. That being said some of the alternatives such as the DBMS' developed by heavyweights like Oracle and Microsoft do have considerable commercial support - with huge amounts of software and tools available for purchase. This was less of an issue in this specific assignment but clearly could be a signifcant concern in a profesional setting.
- Some argue that PostgreSQL is also resource-intensive in comaprison to its alternatives, especially if using a large dataset.
- In a similar vein PostgreSQL can perform slowly in certain scenarios, especially where some of its strengths (such as it being so flexible) actually hold it back slightly, and result in poor(er) performance when dealing with complex queries e.g. over multiple tables or joins.

**R4: Identify & Discuss the key functionalities and benefits of an ORM**


Object-relational mapping (ORM) allows developers to map objects in their code to the tables in a relational database. We can consider the ORM *"the layer that connects object-oriented programming (OOP) to relational databases...the ORM and ORM tools help simplify the interaction between relational databases and different OOP languages."* [^1]

This functionality brings a number of advantages for developers:

- **Speed:** because developers can use an ORM to handle the details of working with a database, they have to write less code, thus resulting in faster development. 
- **Abstraction:** hand in hand with speed, comes the mapping layer that I've referenced above. This allows developers a form of abstraction whihc means they can spend more time writing code that focusses on interacting with objects rather than database queries.
- **Flexible/Portable:** this abstraction in turn means that developers don't have to change their code if they find themselves working accross multiple databases, thus bringing further speed advantages to future projects if code can be reused.
- **Maintenance:** with an ORM, the code is often easier to read and understand than if an ORM was not being used. This gives a further advantage in terms of a developer's ability to modify and maintain the code over time, as well as contributing to many of the advantages already outlined. 
- **Security:** an ORM can help with an apps security by prevenmting an SQL injection attack. This is where an attacker might attempt to "inject" malicious SQL code into an apps input fields (e..g a search box, or login form) in an attempt to gain accsess to an application's database. They can be particularly dangerous as they can allow the attacker to bypass authentication, and have the ability to perform full CRUD operations on the data in the database. ORMs can help prevent this type of attack by provifing paramaterised queries (which passes user input as a parameter whic can be validated by the ORM), input validation (an in-built system to ensure input is within the expected range and format), automatic escaping (which prevents the database interpreting user input as SQL code) or using query builder methods (which allow developers to create SQL queries without having to write the raw code). These options give developers some assurance that there code is les vulnerable to an injection attack.  
  
**R5: Document all endpoints**  

**Home**

```
@home.get("/")
def get_home_page():
    return {"message": "Welcome to the Lens Library!"}
```  
As you can see from the code snippet above, the home endpoint acts as the landing page and should return the message "welcome to the Lens Library"

**User endpoints**   

```
@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users) 

@user.get("/<int:id>")
def get_user(id):
    user = User.query.get(id)
    if not user:
        return {"message": "That user doesn't exist"}
    
    return user_schema.dump(user) 

@user.post("/")
def create_user():
    try:
        user_fields = user_schema.load(request.json)

        user = User(**user_fields)
           
        db.session.add(user)
        db.session.commit()
    except:
        return {"message": "Your information is incorrect" }
    return user_schema.dump(user)  
```
You can see in the above the GET endpoints will return either all users or a specific user searched for by ID, or return an appropriate message if unable to.

The post endpoint allows you to add a user to the database (and again provides an appropriate error message if unable to).  

**Lens endpoints**  
```
@lens.get("/")
def get_lenses():
    lenses = Lens.query.all()
    return lenses_schema.dump(lenses) 

@lens.get("/<int:id>")
def get_lens(id):
    lens = Lens.query.get(id)
    
    if not lens:
        return {"message": "That lens isn't in the library"}
    
    return lens_schema.dump(lens)

@lens.post("/")
def create_lens():
    try:
        lens_fields = lens_schema.load(request.json)

        lens = Lens(**lens_fields)
           
        db.session.add(lens)
        db.session.commit()
    except:
        return {"message": "Your information is incorrect" }
    
    return lens_schema.dump(lens)  
```  
Similarly to the user endpoints you can see from the above code that the lens GET endpoints allow you to search the database for a list of all lenses or a specific lens by ID. This should also return information on the lens owners.

The POST end point allows you to add a lens to the database. Both GET and POST endpoints have error messages if they are unable to handle the request.  

**Comment endpoints**  

```
@comment.get("/")
def get_comments():
    comments = Comment.query.all()
    return comments_schema.dump(comments) 

@comment.get("/<int:id>")
def get_comment(id):
    comment = Comment.query.get(id)
    
    if not comment:
        return {"message": "I can't find that comment"}
    
    return comment_schema.dump(comment)

@comment.post("/")
def create_comment():
    try:
        comment_fields = comment_schema.load(request.json)

        comment = Comment(**comment_fields)
           
        db.session.add(comment)
        db.session.commit()
    except:
        return {"message": "Hmm. I can't seem to post that comment. Check the information is correct." }
    
    return comment_schema.dump(comment)
```

You can see in this code that the comment end GET and POST points allow you to list all comments, or by ID, as well as create a new comment and add it to the DB. all have error messages if needed.  

**Borrows**  

```
@borrow.get("/")
def get_borrows():
    borrows = Borrow.query.all()
    return borrows_schema.dump(borrows) 

@borrow.get("/<int:id>")
def get_borrow(id):
    borrow = Borrow.query.get(id)
    
    if not borrow:
        return {"message": "I can't find that borrow transaction"}
    
    return borrow_schema.dump(borrow)

@borrow.post("/")
def create_borrow():
    try:
        borrow_fields = borrow_schema.load(request.json)

        borrow = Borrow(**borrow_fields)
           
        db.session.add(borrow)
        db.session.commit()
    except:
        return {"message": "Hmm. I can't seem to create that borrow transaction. Check the information is correct." }
    
    return borrow_schema.dump(borrow)
```

As with the previosu endpoints, you can see from the code here that he GET and POST endpoints allow you to list all comments on the database or by comment ID. You can also create a new comment and add it to the DB. There are appropriate error messages if needed.  

**R6: ERD**  
This is the ERD that I pitched in my initial app proposal. Based on feedback, I will likely rename the 'Lends' table to avoid any confusion and to speed up my coding. The relationships are discussed in R9.  

![Proposed ERD](docs/Proposed%20ERD.png)





**R7: Detail of any third party services used**  

I'm not certain what third party services includes. I have included a requirments.txt file as part of my code which lists the various packages that should be used to in order for the app to function. These are also listed below for completeness. I also made heavy use of insomnia during the development of this app.  

```
blueprint==3.4.2
click==8.1.3
Flask==2.2.3
Flask-JWT-Extended==4.4.4
flask-marshmallow==0.14.0
Flask-SQLAlchemy==3.0.3
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
marshmallow==3.19.0
marshmallow-sqlalchemy==0.29.0
packaging==23.0
psycopg2==2.9.5
psycopg2-binary==2.9.5
PyJWT==2.6.0
python-dotenv==1.0.0
six==1.16.0
SQLAlchemy==2.0.5.post1
typing_extensions==4.5.0
Werkzeug==2.2.3 
```
**R8: Describe your project's models in terms of the relationships they have with each other**

I found establishing the relationships between my models to be an exceptionally challenging part of this assignment. There is a functioning two way one-to-many relationship between the user and lens models (i.e. it is possible to interrogate the database to see what lenses a particular user has listed, and vice versa, to search for lenses and see easily which user they are associated with.)  

That is to say it is possible to post a user, and to post lenses that are associated with that user's ID. You can then perform a get command to list the users (or a specific user), and within that will be able to see the lenses that they are associated with. And this works in reverse in that a get command for lenses will also display the users they are associated with (i.e. who owns them).

As you can see from the ERD and in the code of the models themselves, the database relies on a series of one-to-many relationships. I have used a number of constraints in each model  - with primary and foreign keys being defined which are intended to help maintain the integrity and consistency of the data in the databse, and would be a part of the relationships between the models. There are limited relationships in place in that you can see the foreign keys when using get commands in insomnia, but it was my intent to develop on these, using the relationship function, alongside the foreign keys (as I implemented for user-lens relationship). Unfortunately I was unable to successfully implement these for the other relationships, and took the view to just remove them, rather than include half-written code blocks that didn't work and risked causing the app to break. Developing my understanding of this function is a key learning point for me in this project.




**R9: Discuss the database relations to be implemented in your application**

**ERD**
![Proposed ERD](docs/Proposed%20ERD.png)

**Relationships:**  
As you can see from the above ERD my database comprises four tables that allow the app to track the lenses available, the users, any comments they make and any 'lends' (which for my database can be considered an individual borrow transaction)  As noted in R6 above, I will likely re-name the lends table to avoid unnecesary confusion and (hopefully!) speed up my coding. While I will decide on the final name when writing the code, for the purposes of this answer I will refer to it as the 'Borrow' table. The relationships will be:

**User Table**  
**Primary Key:** User ID.  

The User table will have a one-to-many relationship with the lens table. Each user can list 0 or more lenses to be borrowed, but each lens can only be owned by a single user. Similarly, the User table will have a one-to-many relationship with the Borrow table. Each user can borrow 0 or more lenses, but each borrow transaction can only be made by a single user. Finally the User table will have a one-to-many relationship with the Comment table. A user can make 0 or more comments, but each comment can only be made by a single user. 

**Lens Table**  
**Primary Key:** Lens ID   
**Foreign Key:** User ID

The lens table will have a one-to-many relationship with the borrow table. Each lens can be borrowed 0 or more times, but each single borrow transaction can only apply to a single lens (even in a scenario where a single user was borrowing multiple lenses at the same time - this would be multiple transactions). It will also have a one-to-many relationship with the comment table. Each lens can have 0 or more comments atatched to it, but each comment can only apply to a single lens. 

**Comment Table**  
**Primary Key:** Comment ID
**Foreign Keys:** USer ID, Lens ID.

We can consider the comment table will have the reverse of the lationships set out above. This means it will have a many-to-one relationship with the Lens table as 0 or more comments can be made on each individual lens. Similarly with the User table, the Comment table will have a many-to-one relationship each individual user can make 0 or more comments, but each comment is only made by an individual.

**Borrow Table**  
**Primary Key** When initially conceived I had not thought this table would need a primary key. Re-visiting it now as I draft this answer, I will likely consider creating a 'Borrow ID' to act as the primary key, which would, I think, be a straightforward way of tracking each single transaction.
**Foreign Keys:** Lens ID, User ID (lender), User ID (borrower).

As with the Comment table, the Borrow table can be considered to have the reverse of the relationships set out under the Lens and USer table descriptions. This means it will have a many-to-one relationship with the User table. An individual user can either list or borrow 0 or more lenses, but each lens can only have a single user as either the owner or borrower. Similarly it will have a many-to-one relationship with the Lens table. Each lens can be borrowed 0 or more times, but each borrow transaction only applies to a single lens. 

**R10: Describe the way tasks are allocated and tracked in your project.**

I have attempted to use Flask Blueprints as a way to organise and group related functionalities within my app. You can see the Blueprints established in each of the controller files. An example taken from the users controller is:  

```user = Blueprint('user', __name__, url_prefix="/users")```
You can see in the above example that the Blueprints have the endpoints defined. later in the code I then set out the different tasks at each end point...get, post etc. 

As I was attempting to follow the MVC paradigm where possible in building this app, I found that Blueprints helped me organise my various snippets of code and contributed to the overall modularity of the app.

As a new developer, a large (by my standards at least!) flask app is fairly overwhelming, and I found using Blueprints (alongside MVC structure) helped my try to break my app into smaller pieces, that I found ore manageable to work with. In a similar vein, using the URL prefixes helped me create mutliple componets and work on them separately from each other.  This contributed to helping with my testing, as I was able to use insomnia to test the various functionalities in isolation. They were also extremely helpful in that having defined a Blueprint, I could reuse it accross the app, which helped save me time in an already tight deadline. Finally, I found Blueprints helped speed up my development - which is not quick at the best of times - and did increase my understanding of how the various sections plugged together.

[^1]: FreeCodeCamp.com https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/