alert("hello")

let arr = [1,2,3,2,4,"hello "];
console.log(arr);
for(let i=0;i<=arr.length ;i++){
          console.log(arr[i]);
}

 arr.forEach(function(val){
         console.log(val + " what");
 })

arr.forEach(function (cal){   //means in every element of array 
          console.log(cal + 3);
})

let ans = arr.map(function (val){
          return (val + 2);
})

console.log(ans)

let newarr = arr.filter(function(val){
          if(val % 2 == 0){
                    return true;
          }
          else return false;
})

console.log(newarr);