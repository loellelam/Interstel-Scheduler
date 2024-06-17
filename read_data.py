import csv

def read_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data

# # Usage
# file_path = 'ground_contacts.csv'
# ground_contacts_data = read_ground_contacts(file_path)

# # Print the data to verify
# for contact in ground_contacts_data:
#     print(contact)
