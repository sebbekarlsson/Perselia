function login(form){

    /* Collecting statusmessage element */
    statusmessage = document.getElementById('statusmessage');

    /* Validate user data */
    if(form.email.value == "" || form.password.value == ""){
        statusmessage.textContent = 'Data is not valid';

        return false;
    }

    /* Sending our request */
    json = user_login(form.email.value, form.password.value);

    resp = JSON.parse(json);
    console.log(resp);

    if(resp.errors != null){

        /* Printing errors if there are any */
        statusmessage.textContent = resp.errors;
    }else{

        /* Everything went OK */
        statusmessage.textContent = 'Login Success!';
    }

    /* Preventing default behaviour of the form button */
    return false;
}