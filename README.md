### NOTE - this code is not maintained, and not guaranteed to work with newer versions of rdflib!

For RDBMS based persistence for RDFLib we recommend you use 

https://github.com/RDFLib/rdflib-sqlalchemy

---

MySQL implementation of FOPL Relational Model as an RDFLib Store.

The MySQL store’s relational schema incorporates hashes of terms for efficient interning as well as other normalizations. Very little of it is written specifically for MySQL and thus theoretically it can be very easily ported to other back-ends (with the possible exception of issues with its use of foreign keys).

Note: Python 2.X only.
