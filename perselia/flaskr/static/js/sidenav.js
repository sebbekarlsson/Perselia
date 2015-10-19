/* Fetching the element */
var side_nav = document.getElementById("side-nav");

/* Setting the attribute 'open' to false by default */
side_nav.setAttribute('open', 'false');
side_nav.style.left = '-25%';

function animateRight(obj, from, to, speed){
   if(from >= to){         
       return;  
   }
   else {
       var box = obj;
       box.style.left = from + "px";
       setTimeout(function(){
           animateRight(obj, from + speed, to, speed);
       }, 0) 
   }
}

function animateLeft(obj, from, to, speed){
   if(from <= to){         
       return;  
   }
   else {
       var box = obj;
       box.style.left = from + "px";
       setTimeout(function(){
           animateLeft(obj, from - speed, to, speed);
       }, 0)
   }
}

/**
* This function opens the side navigation.
*/
function open_sidenav(){

    /* Fetching the element */
    var side_nav = document.getElementById("side-nav");
    
    /* Setting the left */
    animateRight(side_nav, -500, 0, 12);

    /* Setting the opacity of the backdrop */
    backdrop.style.opacity = 100;

    /* Setting display of the backdrop */
    backdrop.style.display = 'block';

    /* Setting the 'open' attribute of the element */
    side_nav.setAttribute('open', 'true');
}

/**
* This function closes the side navigation.
*/
function close_sidenav(){

    /* Fetching the element */
    var side_nav = document.getElementById("side-nav");

    /* Setting the left */
    animateLeft(side_nav, 0, -500, 12);

    /* Setting the opacity of the backdrop */
    backdrop.style.opacity = 0;

    /* Setting display of the backdrop */
    backdrop.style.display = 'none';

    /* Setting the 'open' attribute of the element */
    side_nav.setAttribute('open', 'false');
}

/**
* This function toggles the side navigation between closed and open.
*/
function toggle_sidenav(){

    /* Fetching the element */
    var side_nav = document.getElementById("side-nav");

    /* Fetching the backdrop element */
    var backdrop = document.getElementById("backdrop");

    /* Fetching the attribute 'open' value */
    var open = side_nav.getAttribute('open');

    if (open == 'false'){
        open_sidenav();
    }else{
        close_sidenav();
    }

}