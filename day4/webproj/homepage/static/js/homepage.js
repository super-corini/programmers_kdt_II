var typingBool = false; 
var typingIdx=0; 
var typingTxt = document.getElementsByClassName("typewriter")[0].textContent;
var coffee = document.getElementsByClassName("coffee")[0];

typingTxt=typingTxt.split("");
if(typingBool==false){ 
    typingBool=true; 
    
    var tyInt = setInterval(function(){
      typing(typingTxt,'typing')
    },280);
} 

function typing(typingTxt,tbox){ 
  if(typingIdx<typingTxt.length){ 
      document.getElementsByClassName(tbox)[0].append(typingTxt[typingIdx]);
      typingIdx++;
  } 
  else {
    coffee.style.visibility = 'visible';
    clearInterval(tyInt);
  } 
}  