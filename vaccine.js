'use strict'

function ajaxGetRequest(path, callback) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState===4 && this.status ===200) {
      callback(this.response);
    }
  }
  request.open("GET", path);
  request.send();
}

function showBar(response) {
  let data=JSON.parse(response);
  let x_arr=data['x']
  let y_arr=data['y']
  var plot_data = [
    {
      x: x_arr,
      y: y_arr,
      type: 'bar'
    }
  ];
  var layout = {
    xaxis: {title: 'Location'},
    yaxis: {title: '% Fully Vaccinated'},
    barmode: 'relative',
    title: 'Fully Vaccinated By Location'
  };
  Plotly.newPlot('barDiv', plot_data, layout);
}

function showPie(response){
  let data = JSON.parse(response);
  let values_arr=data['values']
  let labels_arr=data['labels']
  var plot_data = [
    {
      values: values_arr,
      labels: labels_arr,
      type: 'pie'
    }
  ];
  var layout = {
    title: 'Vaccine Manufacturer Market Share',
    height: 400,
    width: 500
  };
  Plotly.newPlot('pieDiv', plot_data, layout);
}

function getData(){
  ajaxGetRequest('bar', showBar);
  ajaxGetRequest('pie', showPie);
}

function ajaxPostRequest(path, data, callback) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState===4 && this.status ===200) {
      callback(this.response);
      }
    }
  request.open("POST", path);
  request.send(data);
}

function showLine(response) {
  let data = JSON.parse(response);
  let x_arr=data['x'];
  let y_arr=data['y'];
  var trace1={
    x: x_arr,
    y: y_arr,
    type: 'scatter'
  };
  var trace2 = {
    x: [1, 2, 3, 4],
    y: [16, 5, 11, 9],
    type: 'scatter'
  };
  var plot_data = [trace1];
  var layout = {
    xaxis: {title: 'Date'},
    yaxis: {title: '% Fully Vaccinated'},
    title:'% Fully Vaccinated by Date'
  };  
  Plotly.newPlot('lineDiv', plot_data, layout);
}

function getLocData() {
  let input=document.getElementById('locText');
  let locText=input.value;
  input.value='';
  let locBlob=JSON.stringify({'locText': locText});
  ajaxPostRequest('loc', locBlob, showLine);
}

