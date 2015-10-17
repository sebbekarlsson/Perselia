function user_login(email, password){

    /* Creating our request object */
    var data = {};
    data.email = email;
    data.password = password;
    
    /* Sending our request */
    return json_request('/api/users.login', data, false, function(response) {
        response.responseText;
    });
}
