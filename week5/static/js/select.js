$(document).ready(function(){
    console.log("start")
    $("#MS").change(function (e) {
            $('#post').toggleClass('on off');
            $('#put').toggleClass('on off');
        }
    );
})