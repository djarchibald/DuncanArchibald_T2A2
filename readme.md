### Duncan Archibald T2A2  
<br>

**R1: Identification of the problem you are trying to solve by building this particular app.**  

One of the biggest challenges faced by hobby photographers is the sheer expense of the kit involved. Top-end lenses especially can run into the thousands of dollars, and are usually backed by slick marketing and in-depth reviews that combine to convince the hobbyist that they *need* to have the latest lens in order to produce high quality images. 

There are two common scenarios in particular that my app aims to address. the first of these is where a photographer might want to try out a lens over a period of time and in different conditions before they commit thousands of dollars to buying it. The second is where a photographer plans a shoot that requires a very specific lens which would be too expensive to justify buying for a one-off (or rare-use) occasion. For example, a photgrapher more used to shooting landscape or street may not have the ideal lens for a portrait session, equally, a studio photographer may not have a long zoom lens to hand if they want to go and shoot some wildlife.

My app will let groups of photographers,  whether members of the same photography club, or even just an informal group of friends- list lenses they are willing to lend and others to see what lenses others have that they might be able to borrow.


**R2: Why is it a problem that needs solving?**  

Believe it or not, Gear Acquistion Sydnrome (GAS) is a widely-used, if slightly tongue-in-cheek, photography term that describes this problem. Hobby photographers in particular are  known to be chronic sufferers of GAS, which can get quickly out of hand as they end up spending huge amounts of money, convinced that the latest lens will see their pictures on the cover of Vogue or National Geographic. 


While a sadly incurable condition, my app will help mitigate its effects, with its ultimate aim being to save photographers money. If a photographer can try a lens before they buy, they can be sure that they are choosing a lens right for them and their photography before committing to a significant spend. They will be able to compare and contrast different options in a way they couldn't if they simply went out and bought a new lens immediately. The app will also allow photgraphers to borrow lenses for rare use occasions, for example if experimenting in a new genre, or if they require a specific spec of lens that they don't currently have. This will hopefully mean they won't be tempted to go out and spend thousands of dollars on a lens that will then largely sit unused.  

**R3: Why have you chosen this database system. What are the drawbacks compared to others?**  

**R4: Identify & Discuss the key functionalities and benefits of an ORM**

Object-relational mapping (ORM) allows developers to map objects in their code to the tables in a relational database. We can consider the ORM *"the layer that connects object-oriented programming (OOP) to relational databases...the ORM and ORM tools help simplify the interaction between relational databases and different OOP languages."* [^1]

This functionality brings a number of advantages for developers:

- **Speed:** because developers can use an ORM to handle the details of working with a database, they have to write less code, thus resulting in faster development. 
- **Abstraction:** hand in hand with speed, comes the mapping layer that I've referenced above. This allows developers a form of abstraction whihc means they can spend more time writing code that focusses on interacting with objects rather than database queries.
- **Flexible/Portable:** this abstraction in turn means that developers don't have to change their code if they find themselves working accross multiple databases, thus bringing further speed advantages to future projects if code can be reused.
- **Maintenance:** with an ORM, the code is often easier to read and understand than if an ORM was not being used. This gives a further advantage in terms of a developer's ability to modify and maintain the code over time, as well as contributing to many of the advantages already outlined. 
- **Security:** an ORM can help with an apps security by prevenmting an SQL injection attack. This is where an attacker might attempt to "inject" malicious SQL code into an apps input fields (e..g a search box, or login form) in an attempt to gain accsess to an application's database. They can be particularly dangerous as they can allow the attacker to bypass authentication, and have the ability to perform full CRUD operations on the data in the database. ORMs can help prevent this type of attack by provifing paramaterised queries (which passes user input as a parameter whic can be validated by the ORM), input validation (an in-built system to ensure input is within the expected range and format), automatic escaping (which prevents the database interpreting user input as SQL code) or using query builder methods (which allow developers to create SQL queries without having to write the raw code). These options give developers some assurance that theur code is les vuknerable to an injection attack.

**R6: ERD**  

**R7: Detail of any third party services used**  

**R8: Describe your project's models in terms of the relationships they have with each other**

**R9: Discuss the database relations to be implemented in your application**

**R10: Describe the way tasks are allocated and tracked in your project.**


[^1]: FreeCodeCamp.com https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/