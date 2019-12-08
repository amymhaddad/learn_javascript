


let runningTotal = 0;

// user types in nubmers and i need to keep track of them
let buffer = "0";

//Keep track of what user previously pressed ie,: 12 + -->need to keep track of the +
//null b.c nothing has been previously assigned 
let previousOperator = null;

const screen = document.querySelector('.screen');


//Listen at the top level, the container level
document
    .querySelector('.calc-buttons')
    .addEventListener("click", function(event) {
        //use innerText b/c intestested in what the button is BUT use value when you need to get the value from user input, for ex
        buttonClick(event.target.innerText);
});


//funciton defines the TYPES of button clicks
function buttonClick(value) {
    //IF number, do this. IF symbol, do that. SO need to see if the value is a number
    //use isNaN(), which says if value is NaN, then call the handleSymbol(value) fucntion
    if (isNaN(parseInt(value))) {
        handleSymbol(value);
        //Otherwise, handle the number by calling the handleNumber(value) function 
    } else {
        handleNumber(value);
    }
    rerender();
}

//IF buffer is a single number, reassign the var to the number. 
function handleNumber(value) {
    if (buffer === "0") {
        buffer = value;
        //OTHERWISE append the value to the buffer var (ie, 557)
    } else {
        buffer += value;
    }
    //call this function to get the numbers to show up 
    
}

//instead of a bunch of conditionals, use a switch statement 
//ex: take this value. If it's = to "C" do this..
function handleSymbol(value) {
    switch (value) {
        case 'C':
            buffer = "0";
            runningTotal = 0;
            break;
        case "=":
            //nul = absence of value 
            if (previousOperator === null) {
                return;
            }
            flushOperation(parseInt(buffer));
            previousOperator = null; 
            buffer = "" + runningTotal;
            runningTotal = 0
            break;
        case "˿":
            if (buffer.length === 1) {
                buffer = "0";
            } else {
                buffer = buffer.substring(0, buffer.length -1 )
            }
        default:
            handleMath(value)
            break;
    }
}


//this function writes out the buffer var to the calculator screen 
//screen is my class name in the html BUT I need to create a js const in order to grab the related info
function rerender() {
    screen.innerText = buffer 
}

