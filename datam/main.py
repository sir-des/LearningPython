import json

data = """
1. Eld Evans 1000
2. Calvince Ouma 3250
3. Abraham Kwemboi 500
4. Zipporah Mokeira 200
5. Phosa Olive 350
6. Franklin Oigara 500
7. Edgar Kamau 100
8. Pascal Wasau 150
9. Steve Mwathi 350
10. Lauren Dede 350
11. Patience Wasau 250
12. Anthony Mutongori 100
13. Randy Wandollah 300
14. Pascal Chacha 200
15. Dominic Obure 250
16. Deborah Moraa 200
17. Joe Otieno 50
18. Nahashon Ombaso 200
19. Gift Gesimba 150 
20. Trizah Okhonjo 100
21. Michelle Anita 100
22. Ryan Oenga 200
23. Felix Omondi 300
24. John Wesley 200
25. Esther Ouma 600
26. Varsity Irine 350
27. Duncan Ouma 250
28. Charles Ndungu 100
29. Lincoln 200
30. Dee Friends 300
31. Becky Ogola 100
32. Thomas George 100
33. Madam Lidya 100
34. Isanda Clare 150
35. Lucy Daveen 100
36. Mercy Abuya 100
37. paishey K 50
38. Vincent 200
39. Albert 200
40. Daniela Mwamba 150
41. Clinton 100
42. Tr Collo 200
43. Elder Cliff 500
44. Dorca 300
45. Irene 50
46. Cedzy 50
47. Wendy 500
48. Felix 100
49. Ann 100
50. Vanessa 50
51. Elton 200
52. Joseph Keneni 100


"""

# Split the data into separate lines
lines = data.strip().split('\n')

# Create an empty list to store the dictionaries
table = []

# Iterate over the lines
for line in lines:
    # Split each line into components
    components = line.split()
    # print(components)
    number = components[0][:-1]  # Remove the dot at the end of the number
    name = ' '.join(components[1:-1])  # Join the name components
    amount = components[-1]

    # Create a dictionary for the line
    row = {'number': number, 'name': name, 'amount': amount}

    # Append the dictionary to the table
    table.append(row)

# Convert the list of dictionaries to a JSON object
json_table = json.dumps(table)

# Print the resulting JSON table
print(json_table)