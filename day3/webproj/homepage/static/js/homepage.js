var typingBool = false; 
    var typingIdx=0; 
    var typingTxt = document.getElementsByClassName("typewriter")[0].textContent;
    console.log(typingTxt);
    typingTxt=typingTxt.split("");
    if(typingBool==false){ 
       typingBool=true; 
       
       var tyInt = setInterval(typing,300);
     } 
     
     function typing(){ 
       if(typingIdx<typingTxt.length){ 
            document.getElementsByClassName("typing")[0].append(typingTxt[typingIdx]);
            typingIdx++; 
       } else{ 
         clearInterval(tyInt);
       } 
     }  