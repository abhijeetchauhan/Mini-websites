console.log("loaded javascript");
$(document).ready(function(self){
  $('#Button').on("click",handleClick);
});
function handleClick(self){
  console.log('i am in handleClick')
  $.ajax('https://api.idolondemand.com/1/api/async/recognizespeech/v1?url=https%3A%2F%2Fwww.idolondemand.com%2Fsample-content%2Fvideos%2Fhpnext.mp4&apikey=0075d733-b098-46f7-b919-4604d4d29f5f',{
    type:'GET',
    success:sendData
  });
};
function showData(Data){
  console.log(Data)
  $('#results').html(Data['actions'][0]['result']['document'][0]['content'])
}
function sendData(data){
    send=data['jobID']
    console.log(send)
    $.ajax('https://api.idolondemand.com/1/job/result/'+data["jobID"]+'?apikey=0075d733-b098-46f7-b919-4604d4d29f5f',{
      type:'POST',
      success:showData
    });
}