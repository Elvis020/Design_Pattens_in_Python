# Introduction to Builder Pattern
* Builder helps by separating the construct of a complex object
* Builder encapsulates object creation
* Allows for multistep construction process
* Implementations may vary, builder can be very flexible without changing the client interface
* Builder helps resolves the large parameter list
* Methods of resolving a DP using a builder
  1. Get rid of the constructor and expose the attributes(Gets rid of the constructors problem)
  2. To resolve the constructor proliferation problem we can use setting the attributes of fields in a class as the constructor
  3. Encapsulate the attributes of the said class
* Benefits of the Builder DP includes:
  * Separates the "How" from the "What"
  * Assembly separate from components
  * Encapsulates what varies
  * Permits different representations
  * Client creates Director object
  * Director uses concrete builder
  * Builder adds parts to the product