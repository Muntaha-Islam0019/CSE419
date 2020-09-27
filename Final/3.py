def find_triplets(the_list, length): 

	check_validity = True
    
	for i in range(0, length - 2): 
		for j in range(i + 1, length - 1): 
			for k in range(j + 1, length): 

				if (the_list[i] + the_list[j] + the_list[k] == 0): 
					print(the_list[i], the_list[j], the_list[k]) 
					check_validity = True
	
	if (check_validity == False): 
		print("No answer.") 


inputs = list(map(int, input().rstrip().split()))
find_triplets(inputs, len(inputs))
