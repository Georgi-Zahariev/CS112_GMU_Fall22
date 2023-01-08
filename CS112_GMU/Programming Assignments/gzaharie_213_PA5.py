#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 5
#Due Date: 10/19/2022
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

#1
def findRecommendations(matches):
	#making deep copy
	info = []
	for i in range(len(matches)):
		info.append(matches[i])
	#empty list
	matches.clear()
	highest_index = -1
	cnt = -1
	max_value = -1
	
	#checking only the numbers
	for num in range(2,len(info),3):
		#if the number meets the requirements 
		if info[num] >= 80 :
			cnt += 1
			#appending the information that is connected with the number
			matches.append([info[num-2], info[num-1], info[num]])
			#highest number and its index in the new list
			if info[num] > max_value:
				max_value = info[num]
				highest_index = cnt
	
	#appending the heart emoji where is the highest number
	if len(matches)>0:
		matches[highest_index].append("\u2665")

#2
def compressInfo(datingTrack):
	#making deep copy
	info = []
	for i in range(len(datingTrack)):
		info.append(datingTrack[i])
	#helpful list
	temporary = []
	#make the list empty
	datingTrack.clear()
	
	#making helpful list only with the unique IDs
	for element in info:
		if element[0] not in temporary:
			temporary.append(element[0])
	
	id_count = 0
	#checking how many times each ID occurs
	for name in temporary:
		for num in range(len(info)):
			if info[num][0] == name:
				id_count += 1
		#appending the needed information - ID, count
		datingTrack.append((name,id_count))
		id_count = 0

#3
def combineInfo(profileInfo, datingTrack):
	#making deep copy
	profiles = []
	for i in range(len(profileInfo)):
		profiles.append(profileInfo[i])
	
	#going through the elements of profile (profileInfo)
	for num in range(len(profiles)):
		#going through the dating track elements
		for data in datingTrack:
			#checking if profiles ID is equal to ID in dating track
			#if yes, adding the number from dating track 
			if profiles[num][1] == data[0]:
				profileInfo[num].append(data[1])

#4
def setofNames(profiles, location):
	#empty set
	result = set()
	# reaching the value (list) of every element of the set
	for key, value in profiles.items():
		#checking if the element's location is equal as the given
		if value[2] == location:
			result.add(value[0])
	
	return result


