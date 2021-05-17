const canvas = document.querySelector("canvas");


canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const ctx = canvas.getContext('2d');

let ALPHA = 0.5;
let color = [`rgba(0,255,255,${ALPHA})`,`rgba(255,0,255,${ALPHA})`,`rgba(255,255,0,${ALPHA})`,`rgba(0,0,0,${ALPHA})`];

let mouse={
    x : undefined,
    y : undefined
};

let AREA = 50;
let MAX_R = 80;

const CIRCLE_NUM = 600;
let circle = [];


function handleMouse(event){
    mouse.x = event.x;
    mouse.y = event.y;
}

function Circle(x,y,r,vx,vy,indexColor){

    this.x = x;
    this.y = y;
    this.r = r;
    this.vx = vx;
    this.vy = vy;
    this.minR = r;

    this.draw = function() {

        ctx.beginPath();
        ctx.arc(this.x,this.y,this.r,0,Math.PI*2,false);
        ctx.fillStyle = `${color[indexColor]}`;
        ctx.font = "15px malgun gothic";
        text = '안녕하세요! 저는 김현우입니다 :)';
        ctx.fillText(text, canvas.width/5*2.18, canvas.height/2);
        ctx.fill();
    }

    this.update = function(){
        if( this.x+this.r > canvas.width || this.x-this.r < 0){
            this.vx = -this.vx;
        }
        if( this.y+ this.r > canvas.height || this.y-this.r < 0){
            this.vy = -this.vy;
        }

        // ABsoulute Value 절대값 
        if(Math.abs(mouse.x - this.x) < AREA && Math.abs(mouse.y - this.y )< AREA){
            if(this.r < MAX_R){
                this.r += 2;
            }
        }
        else{
            if(this.r > this.minR){
                this.r -= 2;
            }
        }

        this.x+=this.vx;
        this.y+=this.vy;

        this.draw();
    }
}


function init(){

    circle = [];

    for(let i = 0; i < CIRCLE_NUM; i ++){


        let r = Math.random() * 8 + 3;
        let x = Math.random() * (canvas.width - r*2) + r;
        let y = Math.random() * (canvas.height- r*2) + r;
    
        let vx = (Math.random()-0.5) * 2;
        let vy = (Math.random()-0.5) * 2;

        let whichColor = Math.floor(Math.random()*4);
    
        circle.push(new Circle(x,y,r,vx,vy,whichColor));
        //circle[i] = new Circle(x,y,r,vx,vy);
    }

}

function moveCircle(){

    requestAnimationFrame(moveCircle);

    ctx.clearRect(0,0,canvas.width,canvas.height); /* clearRect는 fillRect와 반대 개념으로 동일하게 x,y,가로사이즈,세로사이즈 */
    for(let i = 0; i < CIRCLE_NUM; i ++){
        circle[i].update();
    }
}

canvas.addEventListener("mousemove",handleMouse);
window.addEventListener("resize",function(event){
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();

});

init();
moveCircle();
