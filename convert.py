import csv
import sys
import os

# Function to convert VCard file to CSV
def vcard_to_csv(vcf_file, csv_file):
    email = ""
    phone = ""
    with open(vcf_file, 'r') as vcf, open(csv_file, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        # Write the header row
        csv_writer.writerow(['Name', 'Email', 'Phone'])
        
        # Iterate over the lines in the VCard file
        for line in vcf:
            if line.startswith('FN:'):
                name = line[3:].strip()
            elif line.startswith('EMAIL;'):
                email = line.split(':')[1].strip()
            elif line.startswith('TEL;'):
                phone = line.split(':')[1].strip()
            elif line == 'END:VCARD\n':
                csv_writer.writerow([name, email, phone])
                name, email, phone = '', '', ''

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python vcf_to_csv.py <vcf_file>")
        sys.exit(1)
    vcf_file = sys.argv[1]
    if not os.path.exists(vcf_file):
        print(f"Error: {vcf_file} does not exist.")
        sys.exit(1)
    csv_file = os.path.splitext(vcf_file)[0] + '.csv'
    vcard_to_csv(vcf_file, csv_file)
    print(f"Your contacts have been saved to {csv_file}.")
