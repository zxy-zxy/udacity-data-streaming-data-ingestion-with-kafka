### Glossary

* DSL - Domain Specific Language. A metaprogramming language for specific tasks, 
such as building database queries or stream processing applications.
* Dataclass (Python) - A special type of Class in which instances are meant to represent data, 
but not contain mutating functions
* Changelog - An append-only log of changes made to a particular component. 
In the case of Faust and other stream processors, this tracks all changes to a given processor.
* Processor (Faust) - Functions that take a value and return a value. Can be added in a pre-defined 
list of callbacks to stream declarations.
* Operations (Faust) - Actions that can be applied to an incoming stream to create an intermediate 
stream containing some modification, such as a group-by or filter