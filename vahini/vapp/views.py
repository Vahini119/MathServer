from django.shortcuts import render
def calculate_total(request):
	p=float(request.POST.get('price','0'))
	G=float(request.POST.get('GST','0'))
	total = p+(p*G/100) if request.method=='POST' else 0
	print("price=",p)
	print("GST=",G)
	print("total=",total)
	return render(request,'vapp/total.html',{'p':p,'G':G,'total':total})

 
