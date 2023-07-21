# Imagerestapidjango

Here are the various end points that I created in this project<br>
POST-http://127.0.0.1:8000/api/account/create/user/<br>
This endpoint is used to create user by providing the user details<br>
Body Request:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "string"<br>
}<br>
Responses:<br>
HTTP_201_CREATED<br>

Response Body:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>POST-http://127.0.0.1:8000/api/account/user/token/</h4><br>
This is used to generate the token for the user which can be used for the authentication<br>

Request Body:<br>

{<br>
  "email": "user@example.com",<br>
  
  "password": "string"<br>
}<br>

Responses:<br>

STATUS_200_OK<br>

Response Body:<br>

{<br>
    "token": "string"<br>
}<br>


<h4>GET-http://127.0.0.1:8000/api/account/user/manage/</h4><br>
It will retrieve the user information 
Request Body:<br>
In the headers of the request with the field name of authorization sending user's token<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
RESPONSES:<br>
STATUS:200<br>
RESPONSE_BODY:<br>
{<br>
    "email": "string",<br>
    "name": "string"<br>
}<br>

<h4>PATCH:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the user object partially<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>PUT:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the entire user object<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>GET-localhost:8000/api/image/</h4>

This endpoint is used to retrieve all the images in the database<br>
Request Body:<br>
No parameters<br>
Add the user token in the header<br>

Responses:<br>
STATUS:200<br>

Response Body:<br>

[<br>
{<br>
"id":0,<br>
"image":"string"<br>
}<br>

]<br>

<h1>POST:/api/image/</h1><br>

This API endpoint is used to post the single image to the server.In the request body send the  single image in the field of 'image'<br>
Add the Token to the header<br>
Request Body:<br>

{<br>
'image':"string"<br>
}<br>

RESPONSES:<br>
STATUS:201<br>
Respose Body:<br>
{<br>
  "id": 0,<br>
  "image": "string"<br>
}<br>



<h1>GET:/api/image/{id}/</h1><br>
This api endpoint is used to get the details of a particular image<br>
Add the token in the header 

Query Parameters:<br>
{<br>
'id':integer<br>
}<br>

Response:<br>

STATUS:200 OK<br>

Response Body:<br>
{<br>
  "id": 0,<br>
  "image": "string"<br>
}<br>

<h1>PUT:/api/image/{id}/</h1><br>
This api endpoint is used to update the details of a particular image object<br>
Add the token in the header
Query Parameters:<br>
{<br>
'id':integer<br>
}<br>


Request Body:<br>
{<br>
'image':'string'
}<br>

Response:<br>

STATUS:200 OK<br>

Response Body:<br>
{<br>
  "id": 0,<br>
  "image": "string"<br>
}<br>

<h1>PATCH:/api/image/{id}/</h1><br>
This api endpoint is used to update the certain fields of a particular image<br>
Add the token in the header 
Query Parms:<br>
{<br>
'id':integer<br>
}<br>

Request Body:<br>
{<br>
'image':'string'<br>
}<br>

Response:<br>

STATUS:200 OK<br>

Response Body:<br>
{<br>
  "id": 0,<br>
  "image": "string"<br>
}<br>


<h1>DELETE:/api/image/{id}/</h1><br>
This api endpoint is used to update the certain fields of a particular image<br>
Add the token in the header 
Query Parms:<br>
{<br>
'id':integer<br>
}<br>



Response:<br>

STATUS:204_NO_CONTENT<br>

Response Body:<br>
[]
<br>


























