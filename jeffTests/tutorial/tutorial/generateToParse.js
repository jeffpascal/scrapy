
// require fs
var fs = require('fs');

// read json file
var json = fs.readFileSync('imobiliare.ro_2022-05-29T10-25-00_toateAnunturiTimisoara_urls.json', 'utf8');
console.log(json)
// for each entry in array, print url to file
var jsonObj = JSON.parse(json);
var i = 0;
for (i = 0; i < jsonObj.length; i++) {
    var url = jsonObj[i].url;
    console.log(url);
    fs.appendFileSync('imobiliare.ro_2022-05-29T10-25-00_toateAnunturiTimisoara_urls2', "\"" + url + '\",\n');
}