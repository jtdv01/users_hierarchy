# User Hierarchy

# Quick start

* Start a read-evaluate-print-loop (REPL) by typing in `make main`

```bash
➜  users_hierarchy ✗ make main
python3 src/user_hierarchy/main.py --users resources/users.json --roles resources/roles.json

Welcome to UserHierarchyDB!

Type in the user id of interest.
Information about subordinate users will then be showed.
To see this information again, type in `help`
To see the current state of the database type in `db`. WARNING! This can be large!


To quit type in `quit`


Type in User ID to query >

```

* The prompt will then ask for a user id.
* The program will then print out information about subordinate users under the queried user.

For example, querying the Admin (UserID = 1) will print out all users under this account.

```bash
Type in User ID to query >1

Found 4 users under UserID: 1 UserName: Adam Admin
{"user_id": 2, "user_name": "Emily Employee", "user_role": {"role_id": "4", "role_name": "Employee"}}
{"user_id": 3, "user_name": "Sam Supervisor", "user_role": {"role_id": "3", "role_name": "Supervisor"}}
{"user_id": 4, "user_name": "Mary Manager", "user_role": {"role_id": "2", "role_name": "Location Manager"}}
{"user_id": 5, "user_name": "Steve Trainer", "user_role": {"role_id": "5", "role_name": "Trainer"}}


```

# Dockerised deployment

Another `make` directive can be called to containerise the whole application. Use `make docker`

# Database Schema

```json

{
   "roles": {
       1: {"role_id": 1, "role_name": ...}
   },
   
   "users": {
       1: {"user_id": 1, "user_name": ..., "role_id": 1}
       2: {"user_id": 2, "user_name": ..., "role_id": 1}
   },
   
   "role_membership": {
       1: [1,2] # <-- Role 1 has users 1 and 2
   }

}

```

* The database is a simple in memory key-value store.
* In Python, this is a simple dictionary data structure.
* This was chosen for its simplicity and fast lookups on the requirements (user lookup).
* Working with this data structure in mind can it it possible to migrate to a cloud environment.
* A simple key-value store can also be extended beyond a single machine by adopting NoSQL databases such as DynamoDB. Global and secondary indexes can be utilised to speed up UserID and RoleID lookups.

# Recursive search
* Users are queried by an ID, which makes for a fast (O(1)) lookup against users.
* Recursive depth-first-search can be done on a `Role` to find out subordinate Roles.
* Worst case scenario it goes through `n` number of roles.
* Given that Roles do not grow as fast as users, this can be taken as a reasonable assumption.
* The `role membership` allows for decoupling the two entities while maintaining a connection.
* Subordinate users can be retried from the `Role membership`, which can be quickly queried again with a fast O(1) lookup per role.

