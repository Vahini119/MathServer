# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
total.html

<html>
<head>
<title>GST Bill Calculator</title>

<style>
.box {
    width:500px;
    height:320px;
    border:dashed 3px black;
    padding:10px;
    position:fixed;
    top:190px;
    left:500px;
    text-align:center;
    background-color:rgb(123, 216, 131);
}
</style>

</head>

<body bgcolor="lightblue">

<div class="box">

<h1>Price calculator</h1>
<h3>VAHINI(25018547)</h3>

<form method="POST">
{% csrf_token %}

<div>
<label>Price</label>
<input type="text" name="price" value="{{p}}" >
</div>
<br>

<div>
<label>GST</label>
<input type="text" name="GST" value="{{G}}">
</div>
<br>

<div>
<input type="submit" value="Calculate">
</div>
<br>

<div>
<label>Total Bill (₹)</label>
<input type="text" value="{{total}}">
</div>

</form>
</div>

</body>
</html>
```
```
views.py

from django.shortcuts import render
def calculate_total(request):
	p=float(request.POST.get('price','0'))
	G=float(request.POST.get('GST','0'))
	total = p+(p*G/100) if request.method=='POST' else 0
	print("price=",p)
	print("GST=",G)
	print("total=",total)
	return render(request,'vapp/total.html',{'p':p,'G':G,'total':total})

 

```
```
urls.py

from django.contrib import admin
from django.urls import path
from vapp import views
urlpatterns = [
    path('', views.calculate_total, name='calculate_total'),
    ]

```
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (47).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (48).png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
