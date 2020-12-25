var add_onoff = document.getElementsByClassName('btn_add')[0];
var add_coffee = document.getElementsByClassName('add_coffee')[0];
var put_onoff = document.getElementsByClassName('btn_put');
var edit_onoff = document.getElementsByClassName('btn_controll')[0];
var edit_btns = document.getElementsByClassName('btns');
add_onoff.onclick = function(){
    if (add_coffee.style.display == '' ||
                add_coffee.style.display == 'none') {
        add_coffee.style.display = 'block';
    }
    else {
        add_coffee.style.display = 'none';
    }
};

var i;
for (i = 0; i < put_onoff.length; i++) {
    put_onoff[i].addEventListener('click', function(event){
        var put_coffee = event.target.parentElement.parentElement.nextElementSibling;
        if (put_coffee.style.display == '' ||
                    put_coffee.style.display == 'none') {
            put_coffee.style.display = 'block';
        }
        else {
            put_coffee.style.display = 'none';
        }
    });
}

edit_onoff.addEventListener('click', function(){
    for (i = 0; i < edit_btns.length; i ++) {
        edit_btn = edit_btns[i]
        if (edit_btn.style.display == '' ||
                edit_btn.style.display == 'none') {
            edit_btn.style.display = 'block';
        }
        else {
            edit_btn.style.display = 'none';
        }
    }
})