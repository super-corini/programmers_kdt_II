const para_name = document.querySelector('#name');

para_name.addEventListener('click', updateName);


function updateName() {
    let name = prompt('Enter a new name');
    para_name.textContent = name != '' ? name : 'Empty';
}

const para_age = document.querySelector('#age');

para_age.addEventListener('click', alert_age);

function alert_age() {
    alert('어느새 25...')
}

const para_hobby = document.querySelector('#hobby');
para_hobby.addEventListener('click', strike_hobby);

function strike_hobby(event){
    if (event.target.checked){
        event.target.parentElement.style.setProperty("text-decoration", "line-through");
    }else{
        event.target.parentElement.style.setProperty("text-decoration", "none");
    }
}