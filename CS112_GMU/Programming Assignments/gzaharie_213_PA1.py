#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 1
#Due Date: 09/05/2022
#-------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
#Comments and Assumptions: A note to the grader as to any problems or
#uncompleted aspects of the assignment, as well as any assumptions about the #
#meaning of the specification. You can write in N/A if you don’t have any
#comments/assumptions.
#-------------------------------------------------------------------------------
#NOTE: width of source code should be <=80 characters to be readable on-screen.
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

print("Pet Love Vet Weekly Profit Calculator")

#input information and making it the proper type (int/float in our case)
patients = int(input("Total patients this week: "))
total_charged_pp = float(input("Total charged per patient: "))
wage = float(input("Part timer's hourly pay: "))
workers = int(input("Number of part-timers: "))
total_hours = int(input("Part-timers total hours worked: "))
total_supply_cost = float(input("Total supply costs: "))
fees = float(input("Overhead fees: "))
print()

#gross made amount 
gross = patients * total_charged_pp

#regular hours are these paid on normal wage and they are 20 a week per worker
#extra hours are every hour above the regular hours and are paid - wage*1.5
regular_hours = workers*20
extra_hours = total_hours - regular_hours
total_paid = (regular_hours*wage) + extra_hours*(wage*1.5)

#15% taxes on the gross made
taxes = 0.15 * gross

#profit calculations
profit = gross - (taxes + total_paid + total_supply_cost+fees) 

#print all needed using round for the values
print(f'Gross Made:	{gross}')
print(f'Total paid to Part-Timers:	{total_paid}')
print(f'Total tax paid:	{taxes}')
print(f'Net Profit for the Week:	{profit}')
