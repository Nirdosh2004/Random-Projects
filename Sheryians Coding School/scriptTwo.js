// es5(older version of javascript) and es6(newer version of javascript)

function abcd(){
          for(var i=0 ;i<5;i++){
                    console.log(i);
          }
          console.log(i)
}
console.log(abcd());


function calculateMarks(sum,marks){
          for(let i=0;i<marks.length;i++){
                    sum = sum+marks[i];
          }
          return sum;
}

let sum = 0;
let marks = [98,78,89,88,67,90];
console.log(calculateMarks(sum,marks));
let percentage = (calculateMarks(sum,marks)/600)*100;
console.log(percentage + "%");


function abcd(){   //parent function 
          var a = 17;
          function def(){  //child function of abcd()
                    var b = 29;  //abcd() can access def() but not elements of def() like "var b"
          }
}

let a = [1,2,3,4,5];
let b = [...a];    //copy by value "pass by value"

a.pop();
console.log(a);
console.log(b);

let obj = {
          name : "nirdosh" ,
          class : "BCA" ,
          section : "B" ,
};

console.log(obj);
let copyObj = {...obj};   //copy an object " pass by value"
console.log(copyObj);
copyObj.name = "Rishabh Kushwaha";  //can change the values of variables 
console.log(copyObj);


if(9){  //other than 0 means truthy value
          console.log("hello");
}
else{
          console.log("hey ");
}

if(0){   //0 -> falsy value
          console.log("hello");
}
else{
          console.log("hey ");
}


switch(2){  //we don't really use in js
          case 1:
                    {

                    }
}


//for each loop
let arr = [3 ,5,6,6,7,4,4,3,2,5,66,7,8];
//for each actual value pe impace nhi dalta okii 
arr.forEach(function(val){  // value -> variable  // add some value  in each value 
          console.log(val+2);  // we are adding 2 here
});

console.log(arr);  


let obj = {
          name : "Harshit" , class : 5 , age : 44 , 
};
//for in loop 
for (let key in obj){
          console.log( key +  " -> " + obj[key]);
}

//asynchronous javascript 
//also called "callback function" 
console.log("Hello broo");
setTimeout(function(){
          console.log("2 sec baad chalao");
},2000);  //2000 is in mili-seconds "means "2sec""

