# connecting python with javascript by web sockets

-   this program has basic **echo** functionality.
-   For the communication between **client(javascript at browser) and server(python)** I use **websocket**.
-   this program is general demonstration of communication between two languages by the use of **json**

#

## working

-   for the client,

    -   open a websocket
    -   send message (I use json)
    -   receive for response (render as per response json's 'query' field)

-   for the server,
    -   start event loop
    -   receive websocket
    -   process as per (json's 'query field)

#

## testing

-   for testing this project, you need to follow some staps as discribed below

### client

-   open client/myView with vs code editors' live server **or**
-   `pyhton -m http-server` and <localhost:8000> **or**
-   node.js server

### server

-   `python server.py`
