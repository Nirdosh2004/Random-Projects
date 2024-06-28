// stack = primitive (means pass by value (copied value))
// head = non-primitive (pass by reference (exact value))


// stack
let one = "hello";
let two = one;
two = "what is your name";
 console.log(one);
 console.log(two);


// heap
let userOne = { 
          email : "nirdoshkushwaha75@gmail.com" , 
          name : "Nirdosh",
};

console.log(userOne.email);
userOne.email = "hrishabhkushwaha73@gmail.com";
console.log(userOne.email);

const name = "Rishabh kushwaha";
let age = 20;
console.log(`hello my name is ${name} \nand my age is ${age}`);

console.log(typeof(name));
console.log(typeof age);

let namee = "Nirdosh kushwaha";
for(let i=0;i<namee.length;i++){
          console.log(namee[i]);
          console.log(namee[i].toUpperCase());
          console.log(namee[i].toLowerCase());
};

