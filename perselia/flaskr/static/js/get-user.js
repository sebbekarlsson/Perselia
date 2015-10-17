function get_user(email){

    /* Creating our request object */
    var data = {};
    data.email = email;
    
    /* Sending our request */
    return json_request('/api/users.get', data, false, function(response) {
        response.responseText;
    });
}
