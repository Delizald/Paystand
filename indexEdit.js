//Just a simple HTTP request program for the Paystand code challenge.
var myrequest = require('request');
var fs   = require('fs');
var myemail = 'david.elizalde.r.a@gmail.com';
var mytoken = "";
var myURL=""; //I've removed the URL for privacy purposes.

var ageAverage = 0;
var payload = "";
var mycode =""; 
var myPeopleArray = [];

var codeFile = "code.js";

mytoken = await getToken(mytoken);
console.log("My token is "+mytoken);

async function getToken(){
    const result = await myrequest(myURL+"?email="+myemail, function(err, response, body)  {
        if (err) { 
          return console.log(err); 
        }
        mytoken = JSON.parse(response.body); 
        mytoken = mytoken.token;
        
    });
    return result;
}