function json_request(url, data, callback){

    var x = new XMLHttpRequest();

    var string = JSON.stringify(data);

    x.open('POST', url, true);
    x.setRequestHeader('Content-type','application/json; charset=utf-8');

    x.onload = function() {
        callback(x.responseText);
    }
    
    x.send(string);
}