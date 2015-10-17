function json_request(url, data, sync, callback){

    var x = new XMLHttpRequest();

    var string = JSON.stringify(data);

    x.open('POST', url, sync);
    x.setRequestHeader('Content-type','application/json; charset=utf-8');

    x.onload = function() {
        callback(x.responseText);
    }

    x.send(string);

    return x.responseText;
}