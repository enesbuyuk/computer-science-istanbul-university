first_dna = input("Please input the first DNA:")
second_dna =  input("Please input the second DNA:")
matched = []
for i in range(len(first_dna)):
    if first_dna[i] == second_dna[i]:
        matched.append(i+1)
rate=len(matched)*100/len(first_dna)
print(rate)
print(f"The nucleotides at these positions in the two DNAs are identical: {matched}")