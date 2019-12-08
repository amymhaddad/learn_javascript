let output = document.querySelector('.screen');

let mathEquation = ''

const numbers = document.querySelectorAll('.number');
numbers.forEach(function(number){
    number.addEventListener('click', function() {
        mathEquation += number.innerHTML;
    output.innerHTML = mathEquation;
    });
});



// numbers.forEach(function(number) {
//     number.addEventListener('click', function() {
//         mathEquation += number.innerHTML;    
//         console.log(mathEquation) 
//     output.innerHTML = mathEquation;
//     });
// });





// const operations = document.querySelectorAll('.operation');
// operations.forEach(function(operation) {
//     operation.addEventListener('click', function() {
//         mathEquation += operation.innerHTML;
//     });
// });

// const evaluate = document.querySelector('.equals');
// evaluate.addEventListener('click', function() {
//     output.innerHTML = eval(mathEquation);
// });

// const clear = document.querySelector('.clear');
// clear.addEventListener('click', function() {
//     output.innerHTML = 0;
//     mathEquation = '';
// });

// const arrow = document.querySelector('.arrow');
// arrow.addEventListener('click', function() {
//     mathEquation = mathEquation.substring(0, mathEquation.length - 1);
//     output.innerHTML = mathEquation;
// });
