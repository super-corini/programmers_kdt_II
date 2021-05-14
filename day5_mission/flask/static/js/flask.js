var table = document.getElementById('table'),rIndex;
for (var i = 0; i < table.rows.length; i++)
{
    table.rows[i].onclick = function()
    {
        rIndex = this.rowIndex;
        console.log(rIndex);
        document.getElementById('lid').value =  rIndex;
        document.getElementById('lname').value = this.cells[1].innerHTML;
        document.getElementById('lstock').value = this.cells[2].innerHTML;
        if (document.getElementById('check')){
            document.getElementById('check').id = "uncheck";
        }
        this.id ="check";
    }
}


function clickclose(trObj) {
    clickdata.style.display = 'none';
}


var checked = true;
var clickdata = document.getElementById('clickdata');
function clickTrEvent(trObj) {
    if (trObj.id == "view"){
        clickdata.style.display = 'none';
        document.menus.submit();
    }
    if (trObj.id == "create"){
        checked = true;
        clickdata.style.display = 'block';
        document.getElementById('lid').value =  table.rows.length;
        document.getElementById('lname').value = "";
        document.getElementById('lstock').value = "";
    }
    if (trObj.id == "update"){
        checked = false;
        clickdata.style.display = 'block';
    }
    if (trObj.id == "delete"){
        clickdata.style.display = 'none';
        if (rIndex){
            document.sub1.action = "/weaponlist/delete";
            document.sub1.submit();
        }
    }
    if (trObj.id == "maker"){
        if (document.getElementById('lname').value == ""){
            alert('name을 입력해주세요');
        }
        else if (document.getElementById('lstock').value == ""){
            alert('stock를 입력해주세요');
        }
        else{
            if (checked){
                document.sub1.action = "/weaponlist/create";
                document.sub1.submit();
            }else{
                document.sub1.action = "/weaponlist/update";
                document.sub1.submit();
            }
                
        }
    }
}