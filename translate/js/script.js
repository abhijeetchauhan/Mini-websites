console.log("loaded javascript");
$(document).ready(function(self){
  $('#Button').on("click",handleClick);
});
function handleClick(self){
  console.log('i am in handleClick');
  input=$('#input').val();
  $.ajax('https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20150725T081815Z.d6344454352c9f52.cb3ae21a7f8976436e5304e28646abf270c6ff42&text='+input,{
    type:'POST',
    success:sendData
  });
};
function showData(Data){
  console.log(Data)
  $('#results').html(Data['text']);
  // $('#results').html(Data['actions'][0]['result']['document'][0]['content'])
}
function sendData(data){
    input=$('#input').val();
    send=data['lang'];
    $.ajax('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20150725T081815Z.d6344454352c9f52.cb3ae21a7f8976436e5304e28646abf270c6ff42&lang='+send+'-en&text='+input,{
      type:'POST',
      success:showData
    });
}
// -------------------------------------------getlang method-----------------------------------------------------
  // $.ajax('https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=trnsl.1.1.20150725T081815Z.d6344454352c9f52.cb3ae21a7f8976436e5304e28646abf270c6ff42',{
  //   type:'GET',
  //   success:showData
  // });
