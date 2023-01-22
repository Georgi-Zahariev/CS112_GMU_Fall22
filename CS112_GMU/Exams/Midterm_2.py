def positive_indices(some_list):
	new_list = []
	for i in range(len(some_list)):
		if some_list[i]>0:
			new_list.append(i)
			
	return new_list

def make_dict(key_lst, val_tuple):
	new_dict = dict()
	for i in range(len(key_lst)):
		new_dict[key_lst[i]] = val_tuple[i]
		
	return new_dict

def get_set(pos_list, def_dict = {}):
	final_set = set()
	lst_set = set(pos_list)
	lst2 = []
	if len(def_dict) != 0:
		for i in def_dict.values():
			lst2.append(i)
		
	lst2_set = set(lst2)
	
	final_set = lst_set.difference(lst2_set)
	
	return final_set