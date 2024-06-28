let promise = new Promise((resolve , reject) => {
          console.log("I am a promise");
          // resolve("success");
          reject("some error");
});

console.log(promise);


























// function getData(dataId,getNextData){
//           setTimeout( () => {
//                     console.log("data" , dataId);
//                     if(getNextData){
//                     getNextData();
//                     }
//           },2000);

// }

// //call back hell -> not good way of programming 
// getData(1 , () => {
//           console.log("getting data 2....");
//           getData(2  ,() => {
//                     console.log("getting data 3....");
//                     getData(3 , () => {
//                               console.log("getting data 4....");
//                               getData(4);
//                     });
//           });
// });

