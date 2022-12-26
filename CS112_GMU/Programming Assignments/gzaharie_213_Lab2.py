car_msrp = float(input('MSRP: '))
car_year = int(input('Manufacture Year: '))
car_miles = float(input('Miles Driven: '))
car_accidents=int(input('Number of Accidents: '))

total_amount = car_msrp

#10% less because of the accident
if car_accidents>=1 :
	less=car_msrp * 0.1
	total_amount-= car_accidents * less

#based on year	
if car_year<=2019:
	years = 2022 - car_year
	total_amount -= years*500

#based on miles
thousands = car_miles/1000

if car_miles <50000:
	total_amount -= thousands * 50
else:
	total_amount -= thousands * 100
	
print(f'Value of vehicle: ${total_amount}')
	
	
	