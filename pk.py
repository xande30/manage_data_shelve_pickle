import pickle
from termcolor import colored
import shelve
from colorama import Fore, Back, Style

#colorama.init(autoreset=True)

anItem =['1','Buyer', 'Thing','1', '$180','Excellent', '2022-01-05']
with open('item.pickle', 'wb') as pf:
	pickle.dump(anItem,pf)
with open('item.pickle', 'rb') as pf:
	itemCopy = pickle.load(pf)

print(Fore.CYAN,itemCopy)


# ID, Name, Description, OwnerID, Price, Condition, DateRegistered 

items = [
['1', 'Buyer', 'Thing', '1', '$150', 'Excellent', '2022-01-05'],
['2', 'Buyer', 'Thing', '2', '$350', 'Fair', '2022-01-04'],
['3', 'Bike',  'Vehicle','3', '$200', 'Good', '2023-01-01'],
['4', 'Book',  'Tool', '4', '$50', 'Good', '2019-08-01'],
['5','Car', 'Asset', '5' , '$11000', 'Average', '2023-07-21'],
['6','Home', 'Asset', '6', '$70000', 'Excellent', '2023-06-13'],
]
#ID, Anme, Email

members = [
['1', 'Freddy','fred@test.com'],
['2', 'Mike', 'mike@gmail.com'],
['3', 'John', 'john@hotmail.com'],
['4', 'Sloan', 'sloan@yahoo.com'],
['5', 'Steve', 'steve@dom.com'],
]
# ID, ItemID, BorrowerID, DateBorrowed, DateReturned
loans = [
['1','1','3','4/1/2012','4/26/2022'],
['2','2','5','9/5/2012','1/5/2023'],
['3','3','4','7/3/2013','7/22/2023'],
['4','4','1','11/19/2013','11/29/2013'],
['5','5','2','12/5/2013','None']
]

def createDB(data, shelfname):
	try:
		shelf = shelve.open(shelfname, 'c')
		for datum in data:
			shelf[datum[0]] = datum
	finally:
		shelf.close()
def readDB(shelfname):
	try:
		shelf = shelve.open(shelfname, 'r')
		return [shelf[key] for key in shelf]
	finally:
		shelf.close()


def main():
	print(Fore.BLUE,'Creating data files...')
	createDB(items, 'itemshelf')
	createDB(members, 'membershelf')
	createDB(loans, 'loanshelf')
	print(Fore.MAGENTA,'reading items...')
	print(Fore.YELLOW,readDB('itemshelf'))
	print(Fore.GREEN,'reading members...')
	print(Fore.RED,readDB('membershelf'))
	print(Fore.BLUE,'reading loans...')
	print(Fore.CYAN,readDB('loanshelf'))

if __name__ == "__main__": 
	main()
