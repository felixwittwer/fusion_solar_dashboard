// file: scripts.js
// This file is necessary to create the arc diagrams in the dashboard.
// (c)2024 Felix Wittwer

// Your IDE is probably showing an error in lines 
// 21; 22; 55; 56; 87; 88
// It's fine. This is a template file and the variables sourrounded with curly brackets will be replaced by the create_page.py script.

// arcs start at 0.9 * Math.PI and end at 2.1 * Math.PI
var accent_color = '#055d3d'

// middle arc
var startAngle = 0.9 * Math.PI;
var radius = 220;
var counterClockwise = false;

var canvas = document.getElementById('current_power_canvas');
var ctx = canvas.getContext('2d');
var x = canvas.width / 2;
var y = canvas.height / 2;
var endAngle = 2.1 * Math.PI;

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 55;

ctx.strokeStyle = '#dcdcdc';
ctx.stroke();

var max_power = {{max_power}}; // in kW
var percentage = ({{current_power}}/max_power)*100;
if (percentage > 100) {
    percentage = 100;
}
var endAngle = (0.9+(1.2*(percentage/100))) * Math.PI; // maximum value is 2.1

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 55;

ctx.strokeStyle = accent_color;
ctx.stroke();

// left arc
var startAngle = 0.9 * Math.PI;
var radius = 180;
var counterClockwise = false;

var canvas = document.getElementById('today_power_canvas');
var ctx = canvas.getContext('2d');
var x = canvas.width / 2;
var y = canvas.height / 2;
var endAngle = 2.1 * Math.PI;

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 40;

ctx.strokeStyle = '#dcdcdc';
ctx.stroke();

var day_goal = {{day_goal}}; // in kWh
var percentage = ({{today_power}}/day_goal)*100;
if (percentage > 100) {
    percentage = 100;
}
var endAngle = (0.9+(1.2*(percentage/100))) * Math.PI;

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 40;

ctx.strokeStyle = accent_color;
ctx.stroke();

// right arc
var startAngle = 0.9 * Math.PI;
var radius = 180;
var counterClockwise = false;

var canvas = document.getElementById('month_power_canvas');
var ctx = canvas.getContext('2d');
var x = canvas.width / 2;
var y = canvas.height / 2;
var endAngle = 2.1 * Math.PI;

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 40;

ctx.strokeStyle = '#dcdcdc';
ctx.stroke();

var month_goal = {{month_goal}}; // in kWh
var percentage = ({{month_power}}/(month_goal/1000))*100;
if (percentage > 100) {
    percentage = 100;
}
var endAngle = (0.9+(1.2*(percentage/100))) * Math.PI;

ctx.beginPath();
ctx.arc(x, y, radius, startAngle, endAngle, counterClockwise);
ctx.lineWidth = 40;

ctx.strokeStyle = accent_color;
ctx.stroke();
