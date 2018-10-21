console.log('asdasda');

function run() {
  var myform = document.getElementById("imgForm");
  var data = new FormData(myform);

  console.log('submiting data');
  console.log(data);

  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://api.imgur.com/3/image",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer 54235d35006443061c54158f2e13e6327fd5a778"
    },
    "processData": false,
    "contentType": false,
    "mimeType": "multipart/form-data",
    "data": data
  };

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
}




// var form = new FormData();
// form.append("image", "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7");
//
