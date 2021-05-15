function clickTrEvent(trObj) {
    if (trObj.id == "btn_map"){
        if (parseFloat(document.getElementById('lat_id').value) > 90 || parseFloat(document.getElementById('lat_id').value) < -90 ){
            alert('lat_id 범위를 넘어갔습니다');
        }
        else if (parseFloat(document.getElementById('lon_id').value) > 180 || parseFloat(document.getElementById('lon_id').value) < -180 ){
            alert('lon_id 범위를 넘어갔습니다');
        }
        else{
            document.fr_map.submit();
        }
    }
}