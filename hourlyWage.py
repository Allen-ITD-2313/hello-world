file_name = input('Enter the file name: ')

print('\n%-15s%-10s%-10s' % ('Name', 'Hours', 'Total Pay'))

for line in open(file_name):
    line = line.strip()

    if line != '':
        (nm, wage, hours) = line.split()

        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

        print('%-15s%-10d%-10.2f' % (nm, hours, pay))
