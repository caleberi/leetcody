# ** Data type in Postgres  **

While creating table, for each column, you specify a data type, i.e., what kind of data you want to store in the table fields.
This enables several benefits −

- **Consistency** − Operations against columns of same data type give consistent results and are usually the fastest.

- **Validation** − Proper use of data types implies format validation of data and rejection of data outside the scope of data type.

- **Compactness** − As a column can store a single type of value, it is stored in a compact way.

- **Performance** − Proper use of data types gives the most efficient storage of data. The values stored can be processed quickly, which enhances the performance.

PostgreSQL supports a wide set of Data Types. Besides, users can create their own custom data type using CREATE TYPE SQL command .

The following table lists the data types supported by PostgreSQL.

**Numeric Types**
![numbers](images/postgresql-data-types-numeric.png)

**Monetary Types**
![ money](images/postgresql-data-types-money.png)

**Character Types**
![characters](images/postgresql-data-types-characters.png)

Others are Binary Types , Date/Time Types, Boolean Typs, and others.

**Schema and Table Creation**
Advantages of using a Schema
- It allows many users to use one database without interfering with each other.
- It organizes database objects into logical groups to make them more manageable.
- Third-party applications can be put into separate schemas so they do not collide with the names of other objects.
