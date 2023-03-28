# Introduction to Prototype Pattern
* uses a given instance as prototype
* creates a clone of the prototype
* Clones can have different attributes
* Reduces the number of classes
* Run-time inheritance
* Resolves some issues of the Abstract Factory DP
* There are 3 ways of using the prototype DP: Shallow cloning, Deep cloning and Manager
* Shallow copying
  * This constructs a new compound object and then inserts a reference into it to the object found in the original
  * Using shallow copying in cloning for prototypes has a problem 
  * The resolution is to use deep cloning
* Deep copying
  * Recursively copies objects found in the original
  * You have to be careful when using deep cloninng technique, cuz it can cause recursive loops
  * Note that you don't always have to use deep cloning
  * Use deep cloning with care
* Prototype Manager
  * In a system with a large number of prototypes, a prototype manager helps keep things organized
  * You can use a dictionary
  * Basically you create clones from the prototype manager which is a dictionary
  * With the manager, you are able to create clones for both shallow clones and deep clones
  * The prototype manager helps you separate the building concerns of building and cloning the prototypes
* You can use a combination of both Deep and Shallow implementations