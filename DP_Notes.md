 # Introduction to Design Patterns
 * We need design patterns for consistency,reliability and understanding
 * DP, makes our work easily understandable
 * Gang of 4 published the first book on DP in 1994
 * DP falls into 3 basic categories
   * Creational(Object creation)
     * Factory(Simple,Full Factory and Abstract), Builder, Prototype, Singleton
   * Structural(Object Composition)
   * Behaviour(Object interaction and responsibility)
 * SOLID
   * Single Responsibility
     * A class should have only one responsibility
   * Open-Closed
     * A class should be open for extension but closed for modification
   * Liskov Substitution
     * Named after Babara Liskov  
     * Some classes should be able to stand in for their parents in a program without breaking anything
   * Interface Segregation
     * Many specific interfaces are better than a do it all interface
   * Dependency Inversion
     * We should program towards abstractions and not implementations
     * Implementations can vary but abstractions do not
* Python does not have an interface so we use an ABC instead
* If you forget to implement an abstract method, Python catches Missing Implementations