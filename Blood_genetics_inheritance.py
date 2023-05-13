def calculate_child_blood_types(parent1, parent2):
# resolve the parents with OO blood alleles
	alleles = {
		'A': ['A', 'O'],
		'B': ['B', 'O'],
		'AB': ['A', 'B'],
		'O': ['O']
	}

	parent1_alleles = alleles[parent1[0]] + alleles[parent1[1]]
	parent2_alleles = alleles[parent2[0]] + alleles[parent2[1]]

	if parent1[1] != 'O':
		parent1_alleles = parent1_alleles[:-1]
	if parent2[1] != 'O':
		parent2_alleles = parent2_alleles[:-1]
        
	child_blood_types = {
		'A': 0,
		'B': 0,
		'AB': 0,
		'O': 0
	}


	for allele1 in parent1_alleles:
		for allele2 in parent2_alleles:
			if allele1 == 'A' and allele2 == 'B':
				child_blood_types['AB'] += 1
			elif allele1 == 'A' and allele2 == 'A':
				child_blood_types['A'] += 1
			elif allele1 == 'B' and allele2 == 'B':
				child_blood_types['B'] += 1
			elif allele1 == 'O' and allele2 == 'O':
				child_blood_types['O'] += 1
			elif allele1 == 'A' and allele2 == 'O':
				child_blood_types['A'] += 1
				child_blood_types['O'] += 1
			elif allele1 == 'B' and allele2 == 'O':
				child_blood_types['B'] += 1
				child_blood_types['O'] += 1
	total = sum(child_blood_types.values())
# make it in percentage
	for blood_type in child_blood_types:
		child_blood_types[blood_type] /= total

	return child_blood_types


parent1 = input("What is parent1 allele type?: ")
while len(parent1) < 2:
	print("Please input a valid allele corespinding to a blood type ex: AO, BO, AB or OO")
	parent1 = input("What is parent1 blood type?: ")
parent2 = input("What is parent2 blood type?: ")
while len(parent2) < 2:
	print("Please input a valid allele corespinding to a blood type ex: AO, BO, AB or OO")
	parent2 = input("What is parent2 allele type?: ")
child_blood_types = calculate_child_blood_types(parent1, parent2)
print(child_blood_types)
