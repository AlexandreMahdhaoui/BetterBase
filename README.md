# BetterBase

BetterBase is an API providing a namespace of database-adapters for 
microservices.

### Create a BetterBase instance from a BetterManager instance:
By accessing the BetterManager's instance namespace, BetterBase will 
retrieve its meta-configuration. From which it will not only bootstrap its
self configuration but also the configuration of the entire 
managed application.

### Adapter's class methods:
#### _one:
- find_one(filter, projection),
- insert_one(document),
- update_one(filter, update),
- delete_one(filter),

#### _many:
- find(filter, projection),
- insert_many(documents),
- update_many(filter, update),
- delete_many(filter)