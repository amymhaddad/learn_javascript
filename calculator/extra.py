<button class="button">Click me!</button>

<body>
    <script>
        const button = document.querySelector('.button');
        button.addEventListener('click', function () {
            alert("here!");
        });
    </script>

Key point:
-HTML 
-THEN JS


Original HTML -- before adding buttons:
<body>
<div>
    <div class="columns">
            <div class="calc-input">
                <div class="calculation">0</div>
            </div>

            <div class="calc-input">
                <div class="clear">C</div>
                <div class="operation arrow">&larr;</div>
                <div class="operation">&divide;</div>    
            </div>


            <div class="calc-input">
                    <div class="number">7</div>
                    <div class="number">8</div>
                    <div class="number">9</div>
                    <div class="operation">&times;</div>  
                </div>
    
                <div class="calc-input">
                    <div class="number">4</div>
                    <div class="number">5</div>
                    <div class="number">6</div>
                    <div class="operation">&minus;</div>  
                </div>
    
                <div class="calc-input">
                    <div class="number">1</div>
                    <div class="number">2</div>
                    <div class="number">3</div>
                    <div class="operation">&plus;</div>  
                </div>
    

            <div class="calc-input">
                <div class="number zero">0</div>
                <div class="number equals">&equals;</div>  
            </div>   
    </div>
</div>
</body>

</html>


const int = parseInt(number, 10);
        alert(int);

let ten = 0;
    const button = document.querySelector('.number');
    button.addEventListener('click', function() {
        ten += button;
        alert(ten);
    });





// let ten = 0;
// const button = document.querySelector('.number');
// console.log(button);

// The for loop goes outside of the addEventListener() b/c I need to do something to each element in the List 
// and need to apply AddEventListener() to each element.

let number = 0
const buttons = document.querySelectorAll('.number');
debugger

buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        let number = parseInt(button.innerHTML, 10);
        console.log(number);
    })
});




const buttons = document.querySelectorAll('.number');
buttons.forEach(function(button) {
    let numAsInt = parseInt(button.innerHTML, 10);
    button.addEventListener('click', function() {
        if (Number.isInteger(numAsInt)) {
            output.innerHTML = button.innerHTML;
        };
    });
});


Program that works:

let output = document.querySelector('.output');

let mathEquation = ''


const buttons = document.querySelectorAll('.number');
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        mathEquation += button.innerHTML;     
        output.innerHTML = mathEquation;
    });
});

const operations = document.querySelectorAll('.operation');
operations.forEach(function(operation) {
    operation.addEventListener('click', function() {
        mathEquation += operation.innerHTML;
    });
});

const evaluate = document.querySelector('.equals');
evaluate.addEventListener('click', function() {
    output.innerHTML = eval(mathEquation);
});



const clear = document.querySelector('.clear');
evaluate.addEventListener('click', function() {
    output.innerHTML = 0;
    mathEquation = '';
});



ORIGINAL:
<div>
        <div class="columns">
                <div class="calc-input">
                    <div class="output">0</div>
                </div>

                <div class="calc-input">
                    <div class="clear">C</div>
                    <div class="arrow">&larr;</div>
                    <div class="operation">&divide;</div>    
                </div>

                <div class="calc-input">
                        <div class="number">7</div>
                        <div class="number">8</div>
                        <div class="number">9</div>
                        <div class="operation">&times;</div>
                    </div>
        
                    <div class="calc-input">
                        <div class="number">4</div>
                        <div class="number">5</div>
                        <div class="number">6</div>
                        <div class="operation">&minus;</div>  
                    </div>
        
                    <div class="calc-input">
                        <div class="number">1</div>
                        <div class="number">2</div>
                        <div class="number">3</div>
                        <div class="operation">&plus;</div>  
                    </div>
        
                <div class="calc-input">
                    <div class="number zero">0</div>
                    <div class="equals">&equals;</div>  
                </div>   
        </div>
    </div>



.button {
    color: blue;
}

.columns {
    display: flex;
    flex-direction: column;
    width: 30%; 
    padding-left: 30%;  
    padding-top: 5%;
}

.calc-input {
    display: flex;
}

.output {
    order: 3;
    border: 1px black solid;
    width: 100%;
    display: flex;
    justify-content: flex-end;
    background-color: black;
    color: white;
}

.clear {
    order: 1;
    border: 1px black solid;
    width: 50%;
    display: flex;
    justify-content: center;
    background-color: #d3d3d3;
    color: black;
}

.arrow {
    order: 2;
    border: 1px black solid;
    width: 25%;
    background-color: #808080;
    color: black;
    order: 3;
    border: 1px black solid;
    width: 25%;
    display: flex;
    justify-content: center;
    background-color: orange;
    color: white;
}

.operation {
    order: 3;
    border: 1px black solid;
    width: 25%;
    display: flex;
    justify-content: center;
    background-color: orange;
    color: white;
}

.number {
    border: 1px black solid;
    width: 25%;
    display: flex;
    justify-content: center;
    background-color:#d3d3d3;
}

.zero {
    order: 1;
    border: 1px black solid;
    width: 75%;
}

.equals {
    order: 3;
    border: 1px black solid;
    width: 25%;
    border: 1px black solid;
    width: 25%;
    display: flex;
    justify-content: center;
    background-color:#d3d3d3;
}


let output = document.querySelector('.calc');

let mathEquation = ''

const buttons = document.querySelectorAll('.number');
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        mathEquation += button.innerHTML;     
    output.innerHTML = mathEquation;
    });
});

const operations = document.querySelectorAll('.operation');
operations.forEach(function(operation) {
    operation.addEventListener('click', function() {
        mathEquation += operation.innerHTML;
    });
});

const evaluate = document.querySelector('.equals');
evaluate.addEventListener('click', function() {
    output.innerHTML = eval(mathEquation);
});

const clear = document.querySelector('.clear');
clear.addEventListener('click', function() {
    output.innerHTML = 0;
    mathEquation = '';
});

const arrow = document.querySelector('.arrow');
arrow.addEventListener('click', function() {
    mathEquation = mathEquation.substring(0, mathEquation.length - 1);
    output.innerHTML = mathEquation;
});
