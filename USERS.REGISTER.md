## users.register
> This function is used to register a new user.

#### JSON:

        {
            "users":[
                {
                    "firstname": "John",
                    "lastname": "Doe",
                    "email": "john.doe@doecompany.com",
                    "avatar_url": "http://demo.geekslabs.com/materialize/v2.1/layout01/images/avatar.jpg",
                    "password": "joedoe123",
                    
                    "custom_fields":[
                        {"key": "birth", "value": "1991-01-05"},
                        {"key": "gender", "value": "male"}
                    ]
                }
            ]
        }
        
> Note: this function takes an array of users, if you only want to register one single user, just put one object inside of the array.

## Updating a user
> To update a user, the JSON should look exactly the same but you need to include the id of the chosen user.
> Like this:

        {
            "users":[
                {
                    ...

                    "id": "937471916"
                }
            ]
        }