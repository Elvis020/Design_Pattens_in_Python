# Introduction to Factory Pattern
* Factories are where things are created, hence it being a creational pattern
* Factory pattern defines an interface for creating an object and let subclasses decide which object to build
* It defers instantiation to the subclasses
* Factory pattern is aka the `Virtual Constructor`
* If you see plenty `if-elif-elif` try and write it in a better way
* There are 3 types of Factory Patter
  * Simple Factory
  * Full Factory
  * Abstract Factory
* Factory DP resolution include
  * Simple Factory Pattern Structure
    * Resolves the Open-close principle and Dependency Inversion Principle
    * Problem is, it is limited to one factory
  * Classic Factory or the Full Factory Pattern Structure
    * The Classic Factory or the Full Factory resolves the one-factory issue of the the simple factory
    * Adds an abstract factory base class
    * Many factories can be implemented
    * Implementations of factories may vary
    * A complex factory might use other patterns, like Builder pattern
  * Abstract Factory 
    * This pattern is a close cousin of FullFactory Pattern
    * Produces a family of classes
    * Enforces dependencies btn btn classes
    * Defers object creation to concrete subclasses
    * Abstract Pattern is aka the `Kit Pattern`
* Full Factory is great when you don't know which concrete classes you'll need
* Abstract Factory is useful when you have families of objects