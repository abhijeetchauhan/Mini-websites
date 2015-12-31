console.log("loaded javascript");
$(document).ready(function(self){
   if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
});
function showPosition(position) {
    var x = document.getElementById("coords");
    x.innerHTML = position.coords.latitude + 
    "," + position.coords.longitude; 
}
