$.ajax({
    method: 'GET',
    url: 'https://api.api-ninjas.com/v1/city?name=' + 'Pune',
    headers: { 'X-Api-Key': 'jrBHlDKqviKKbMOJXyN23w==0DfjRcyeluirjXlg'},
    contentType: 'application/json',
    success: function(result) {
        console.log(result);
    },
    error: function ajaxError(jqXHR) {
        console.error('Error: ', jqXHR.responseText);
    }
});

$.ajax({
    method: 'GET',
    dataType: 'json',
    url: 'https://api.api-ninjas.com/v1/city?name=' + city_name,
    headers: { 'X-Api-Key': 'jrBHlDKqviKKbMOJXyN23w==0DfjRcyeluirjXlg' },
    contentType: 'application/json',
    success: function(result) {
        console.log(result[0]);
        console.log(result[0].name);
        city_name = result[0].name;
        latitude = result[0].latitude;
        longitude = result[0].longitude;
        country = result[0].country;
        is_capital = result[0].is_capital;
        population = result[0].population;
        api_result = result[0];
        console.log("api result:", api_result.name);
        // city_details = {result[0].name,result[0].country,result[0].latitude,result[0].longitude,result[0].is_capital,result[0].population};
        city_details = {city_name,country};
        console.log(city_details);
        console.log(result[0].name,result[0].country,result[0].latitude,result[0].longitude,result[0].is_capital,result[0].population);
        return api_result;
    },
    error: function ajaxError(jqXHR) {
        console.error('Error: ', jqXHR.responseText);
    }
});

$.ajax({
    type: "POST",
    url: "/stats/tdata/",
    data: {
        // "cityname" : JSON.stringify(city_name),
        // "c_name" : city_name,
        "c_name" : api_result.name,
        // "lat" : JSON.stringify(latitude),
        // "lon" : JSON.stringify(longitude),
        "lat" : latitude,
        "lon" : longitude,
        "country" : country,
        "iscapital" : is_capital,
        "population" : population,
        "result" : JSON.stringify(api_result)
    },
    success: function(response)
    {
        $("#m").html("<h2>IP sent to backend.</h2>");
    }
});
return false;
