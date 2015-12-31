// var request = new XMLHttpRequest();
// request.open('GET','txt/data.txt',false);
// request.send();
// if(request.status===200){
// 	console.log(request);
// 	document.writeln(request.responseText)
// }
console.log("loaded javascript");
$(document).ready(function(self){
  $('#Button').on("click",handleClick);
});
function handleClick(self){
  console.log('i am in handleClick')
  $.ajax('/',{
    type:'GET',
    data:{
      fmt:'json'
    },
    success:showData
  });
};
function showData(Data){
  console.log(Data.name)
  $('#results').html(Data.name)
}