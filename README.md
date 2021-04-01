# Anorak - Server

## Resources
* Users
* Auth tokens
* Whiskeys
* User Whiskeys
* Tags

### Running the server
In the terminal, run the commands (It is necessary to install python and pipenv prior to running these commands): 
```javascript
git clone https://github.com/NotThatPatrickStewart/anorak-server.git
cd anorak-server
pipenv shell
python3 manage.py runserver
```
The last command will start running ther server at port localhost:8000

**NOTE**
All requests will require the following header:
`'Authorization': 'Token (insert user token here)'`
all POST requests will also require the header `'Content-Type': 'application/json'`

### Whiskeys
Methods supported:
* GET

As whiskeys are only used in the user search, only GET methods are supported.

#### List all whiskeys
Make a GET request to `http://localhost:8000/whiskeys`

This will return a list of JSON strings in the following format:
```JSON
{
    "id": 396,
    "title": "Maker's Mark",
    "list_img_url": "https://res.cloudinary.com/dt4sawqjx/image/upload/v1463683068/liwwdkkor7uepkwm5xwc.jpg",
    "region": "Bourbon",
    "price": 21.0
}
```

#### Get single whiskey by id
Make a GET request to `http://localhost:8000/whiskeys/1`, the number after `whiskeys/` being the id of the desired whiskey.

#### Get single whiskey by name
Make a GET request to `http://localhost:8000/whiskeys?searchterm=Chivas%20Regal%2012`, the spaces within the name of the whiskey are replaced by `%20`.

### User Whiskeys
Methods supported:
* GET
* POST
* UPDATE
* DELETE

#### List all user whiskeys
Make a GET request to `http://localhost:8000/userwhiskeys`

This will return a list of JSON strings in the following format:
```JSON
{
        "id": 34,
        "title": "Eagle Rare 17 2013",
        "list_img_url": "https://res.cloudinary.com/dt4sawqjx/image/upload/v1463682939/aryukfusjxrfz7tzfju8.jpg",
        "notes": "fantastic",
        "rating": 93,
        "whiskey_id": 197,
        "user": {
            "id": 3,
            "password": "pbkdf2_sha256$216000$G0lX7psUnmdP$CMnH7b622x3V3Fx3xsZkO2853kptLvzQ3/JoJ5XQ5fE=",
            "last_login": null,
            "is_superuser": false,
            "username": "anorak@user.com",
            "first_name": "",
            "last_name": "",
            "email": "anorak@user.com",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2021-03-25T15:53:24.662254Z",
            "groups": [],
            "user_permissions": []
        }
    }
```

#### Get single user whiskey
Make a GET request to `http://localhost:8000/userwhiskeys/3`, the number after `userwhiskeys/` being the id of the desired user whiskey.

#### Create new user whiskey
Make a POST request to `http://localhost:8000/userwhiskeys`
The body of the request must be in JSON format and include the name of the envelope and budget.
e.g. 
```JSON
  {
        "title": "Aberlour A'bunadh batch #36",
        "list_img_url": "https://res.cloudinary.com/dt4sawqjx/image/upload/v1463682979/przkj3phtkchoyozalzj.jpg",
        "notes": "Need to try",
        "rating": null,
        "whiskeyId": 27
    }
```
The returned data will look like this:
```JSON
{
    "id": 37,
    "title": "Aberlour A'bunadh batch #36",
    "list_img_url": "https://res.cloudinary.com/dt4sawqjx/image/upload/v1463682979/przkj3phtkchoyozalzj.jpg",
    "notes": "Need to try",
    "rating": null,
    "whiskey_id": 27,
    "user": {
        "id": 2,
        "password": "pbkdf2_sha256$216000$qMRH8szID7Z8$Vljya2V3XfruOHuvx1hGz9ZyKg4bxbw7rc2WO0gTR7I=",
        "last_login": null,
        "is_superuser": false,
        "username": "whiskey@whiskey.com",
        "first_name": "Mr.",
        "last_name": "Whiskey",
        "email": "whiskey@whiskey.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-03-24T21:25:48.259041Z",
        "groups": [],
        "user_permissions": []
    }
}
```
#### Edit user whiskey
Make a PUT request to `http://localhost:8000/userwhiskeys/2`, the number after `userwhiskeys/` being the id of the desired user whiskey.
The body should contain the same data as the for the POST request. For example, if we were to change the rating fron null to 58 and change the note for the above created user whiskey, we would make a PUT request to `http://localhost:8000/userwhiskeys/2`:

```json
  {
        "title": "Aberlour A'bunadh batch #36",
        "list_img_url": "https://res.cloudinary.com/dt4sawqjx/image/upload/v1463682979/przkj3phtkchoyozalzj.jpg",
        "notes": "Decent",
        "rating": 58,
        "whiskeyId": 27
    }
```
#### Delete user whiskey
Make a DELETE request to `http://localhost:8000/userwhiskeys/2`, the number after `userwhiskeys/` being the id of the desired user whiskey.

### Tags
Tags are the flavor profiles of each whiskey. There are 66 total flavor profile tags that each whiskey is ranked on, with a count for how many times each flavor appears in reviews for that whiskey.

Methods supported:
* GET

As tags are only used in the user search, only GET methods are supported.

#### List all tags
Make a GET request to `http://localhost:8000/tags`
The body should be structured as follows:
```JSON
 {
        "id": 1,
        "title": "caramel",
        "relatedtag": [
            {
                "id": 1,
                "normalized_count": 111,
                "whiskey": 27,
                "tag": 1
            }, ...
```
**NOTE**
Since this will return a unique relatedTag array for every instance of that tag, there are dozens of results for each tag. Due to space constraints I did not list the full result above.

#### Get single tag
Make a GET request to `http://localhost:8000/tags/1`, the number after `tags/` being the id of the desired tag.
