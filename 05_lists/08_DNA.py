#Search through a list of DNA triplets to check whether a specific sequence exists and report if it’s found.
item_to_find = 'TAA'
item_found = False

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

for i in dna_sequence:
  if i == item_to_find:
    item_found = True

if item_found:
  print("Item Found!")
else:
  print("Item not found.")
