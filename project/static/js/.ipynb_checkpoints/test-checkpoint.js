// Heat Array Call

$.ajax({
    url: "https://data.cityofchicago.org/resource/85ca-t3if.json",
    type: "GET",
    data: {
      "$limit" : 2000,
      "$$app_token" : CHI_API_KEY
    }
}).done(function(response) {
  alert("Retrieved " + response.length + " records from the dataset!");
  console.log(response);

  var heatArray = [];

  for (var i = 0; i < response.length; i++) {
    var location = response[i].location;
    var hit_n_run = response[i].hit_and_run_i;
    if (hit_n_run === "Y") {
    if (location) {
      heatArray.push([location.coordinates[1], location.coordinates[0]]);
    }
  

  var heat = L.heatLayer(heatArray, {
    radius: 10,
    blur: 30
  }).addTo(hit_map);
    };
  };
});

$.ajax({
    url: "https://data.cityofchicago.org/resource/85ca-t3if.json",
    type: "GET",
    data: {
      "$limit" : 1000,
      "$$app_token" : CHI_API_KEY
    }
}).done(function(response) {
  alert("Retrieved " + response.length + " records from the dataset!");
  console.log(response);


//d3.json(newtry, function(response) {

  //console.log(response);
  for (var i = 0; i < response.length; i++) {
    var location = response[i].location;
    var fatalities = Number(response[i].injuries_fatal);
      console.log(fatalities);
      if (fatalities > 0) {
    if (location) {
      L.marker([location.coordinates[1], location.coordinates[0]]).addTo(myMap);
    }
  };
  };
}); 