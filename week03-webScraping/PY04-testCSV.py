import csv

employee_file = open('emplotee_file.csv', mode = 'w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar ='"',quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['John Smith', 'Accounting','November'])
employee_writer.writerow(['Erica Mayers','IT','Match'])

employee_file.close()