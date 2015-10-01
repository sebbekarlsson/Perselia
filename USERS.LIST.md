## users.list
> This function is used to get a list of users.

#### JSON:
    
        {
            'offset': '64'
            'max': '500'
        }

> The values should be pretty obvious.

#### JSON-RESPONSE:

        {
            'users':[
            {
                'firstname: 'John',
                'lastname': 'Doe',
                'email': 'john.doe@doecompany.com',
                'avatar_url': 'http://demo.geekslabs.com/materialize/v2.1/layout01/images/avatar.jpg',
                'id': '285902754',
                'created': '2015-04-06-21:30',
                'updated': '2015-05-06-22:30'
                
                custom_fields:[
                    {'key': 'birth', 'value': '1991-01-05'},
                    {'key': 'gender', 'value': 'male'}
                ]
            },
            {
                'firstname: 'Sarah',
                'lastname': 'Cliff',
                'email': 'sarah.cliff@doecompany.com',
                'avatar_url': 'null',
                'id': '235955754',
                'created': '2015-07-02-10:30',
                'updated': '2015-09-06-06:21'
                
                custom_fields:[
                    {'key': 'birth', 'value': '1996-08-05'},
                    {'key': 'gender', 'value': 'female'}
                ]
            },
            {
                'firstname: 'Tom',
                'lastname': 'Haralds',
                'email': 'tom.haralds@doecompany.com',
                'avatar_url': 'http://demo.geekslabs.com/materialize/v2.1/layout02/images/avatar.jpg',
                'id': '185906664',
                'created': '2015-02-03-01:45',
                'updated': '2012-05-06-12:36'
                
                custom_fields:[
                    {'key': 'birth', 'value': '1989-05-01'},
                    {'key': 'gender', 'value': 'male'}
                ]
            }
        ]
    }