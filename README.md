# User Hierarchy

# Quick start

* Start a read-evaluate-print-loop (REPL) by typing in `make main`

```bash
➜  users_hierarchy ✗ make main

Welcome to UserHierarchyDB! Author: JTY 2019

Type in the user id of interest.
Information about subordinate users will then be printed out.
To see the current state of the database type in `db`. WARNING! This can be large!


To quit type in `quit`.


To see this information again, type in `help`.

Type in User ID to query > _______

```

* The prompt will then ask for a user id.
* The program will then print out information about subordinate users under the queried user.

For example, querying the Admin (UserID = 1) will print out all users under this account.

```bash

# Admin commands everyone else
Type in User ID to query >1
Found 4 users under UserID: 1 UserName: Adam Admin
{"user_id": 2, "user_name": "Emily Employee", "user_role": {"role_id": "4", "role_name": "Employee"}}
{"user_id": 3, "user_name": "Sam Supervisor", "user_role": {"role_id": "3", "role_name": "Supervisor"}}
{"user_id": 4, "user_name": "Mary Manager", "user_role": {"role_id": "2", "role_name": "Location Manager"}}
{"user_id": 5, "user_name": "Steve Trainer", "user_role": {"role_id": "5", "role_name": "Trainer"}}


# Sam commands Employees and Trainers
Type in User ID to query >3
Found 2 users under UserID: 3 UserName: Sam Supervisor
{"user_id": 2, "user_name": "Emily Employee", "user_role": {"role_id": 4, "role_name": "Employee"}}
{"user_id": 5, "user_name": "Steve Trainer", "user_role": {"role_id": 5, "role_name": "Trainer"}}

# Emily has no one under her
Type in User ID to query >2
Found 0 users under UserID: 2 UserName: Emily Employee
```

# Dockerised deployment

Another `make` directive can be called to containerise the whole application. Use `make docker`

One should see this on a successful build:

```
sudo make docker

docker build -t user_hierarchy:1.0.0 . && docker run -ti user_hierarchy:1.0.0
Sending build context to Docker daemon    407kB
Step 1/5 : FROM python:3.6
 ---> xxxx
Step 2/5 : WORKDIR /opt/user_hierarchy
 ---> Using cache
 ---> xxx
Step 3/5 : COPY . /opt/user_hierarchy
 ---> xxx
Step 4/5 : RUN python3 src/user_hierarchy/tests.py
 ---> Running in xxx
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
Test that employee and trainee do not have anyone under them: OK
Test empty: OK
Test that Root is above all others: OK
Test Location Manager: OK
Test that only Adam Admin has the only role role: OK
Removing intermediate container 987f42d46e14
 ---> xxx
Step 5/5 : ENTRYPOINT ["make", "main"]
 ---> Running in 533e5dfb05f3
Removing intermediate container 533e5dfb05f3
 ---> xxx
Successfully built xxx
Successfully tagged user_hierarchy:1.0.0
python3 src/user_hierarchy/main.py --users resources/users.json --roles resources/roles.json


Welcome to UserHierarchyDB! Author: JTY 2019

Type in the user id of interest.
Information about subordinate users will then be printed out.
To see the current state of the database type in `db`. WARNING! This can be large!


To quit type in `quit`.


To see this information again, type in `help`.


Type in User ID to query > ____
```

# Database Schema

See `src/user_hierarchy/db.py`

```

{
   "roles": {
       "1": {"role_id": 1, "role_name": ...}
   },
   
   "users": {
       "1": {"user_id": 1, "user_name": ..., "role_id": 1}
       "2": {"user_id": 2, "user_name": ..., "role_id": 1}
   },
   
   "role_membership": {
       1: [1,2] # <-- Role 1 has users 1 and 2
   }

}

```

* The database is a simple in memory key-value store.
* In Python, this is a simple dictionary data structure.
* This was chosen for its simplicity and fast lookups on the query requirements (user and role id lookups).
* Working with this data structure in mind, it is still possible to migrate to a cloud environment.
* A simple key-value store can also be extended beyond a single machine by adopting NoSQL databases such as DynamoDB.
* Global and secondary indexes can be utilised to speed up UserID and RoleID lookups.

# Recursive search

See `src/user_hierarchy/subordinate_search.py`

* Users are queried by an ID, which makes for a fast (O(1)) lookup against users.
* Recursive depth-first-search can be done on a `Role` to find out subordinate Roles.
* Worst case scenario it goes through `n` number of roles.
* Given that Roles do not grow as fast as users, this can be taken as a reasonable assumption.
* The `role_membership` allows for decoupling the two entities of Roles and Users while maintaining a connection.
* Subordinate users can be queried from the `role_membership` entity, which can be quickly queried again with a fast O(1) lookup per role.
*


# Unit testing

See `src/user_hierarchy/tests.py` for the extensive unittesting.

# Possible extensions

To build more confidence on testing, try property based tests using Hypothesis: https://hypothesis.readthedocs.io/en/latest/ 
