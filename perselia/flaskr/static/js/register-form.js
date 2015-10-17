function register(form){

    /* Creating our request object */
    var data = {};
    data.users = [];
    var user = {};

    /* Creating a user */
    user.firstname = form.firstname.value;
    user.lastname = form.lastname.value;
    user.email = form.email.value;
    user.avatar_url = form.avatar_url.value;
    user.password = form.password.value;
    user.password_confirm = form.password_confirm.value;
    user.master = 1;
    user.custom_fields = [];

    /* Pushing the user to our request object */
    data.users.push(user);
    
    /* Sending our request */
    json_request('/api/users.register', data, true, function(response) {
        resp = JSON.parse(response);
        statusmessage = document.getElementById('statusmessage');

        if(resp.errors != null){

            /* Printing errors if there are any */
            statusmessage.textContent = resp.errors;
        }else{

            /* Everything went OK */
            statusmessage.textContent = 'Registration Complete!';
        }
    });

    /* Preventing default behaviour of the form button */
    return false;
}