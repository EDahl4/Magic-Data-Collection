import json
import matplotlib.pyplot as plt



class MagicData:
    def __init__(self, data_file = "data.json"):
        self.data_file = data_file
        self.categories = ["PEOPLE", "COLORPAIRING", "ARCHETYPE", "FIRSTPICK", "LASTPICK"]
    def read_data(self):
        lines = []
        with open(self.data_file, 'r') as data:
            for line in data:
                category_data = json.loads(line.strip())
                lines.append(category_data)
        return lines
    
    def write_data(self, lines):
        with open(self.data_file, 'w') as data:
            for line in lines:
                data.write(json.dumps(line) + "\n")
        
    def input_data(self, category_index, input_name, win_rate):
        lines = self.read_data()
        category_data = lines[category_index]
        win_rate = [win_rate]
        if input_name in category_data:
            category_data[input_name] = category_data.get(input_name) + win_rate
            
        else:
            category_data[input_name] = win_rate
        lines[category_index] = category_data
        self.write_data(lines)
        print("Data succcessfully entered")
        
    def get_index(self, category):
        return self.categories.index(category)  
    
    def get_average(self, category_data, input_name):
            values = category_data[input_name] 
            return round(sum(values) / len(values), 2)
  
    def get_frequency(self, category_data, input_name):
        values = category_data[input_name]
        return sum(values)
    

class menu2():
    def __init__(self):
        self.magicdata = MagicData()

    def get_category_data(self, category):
        lines = self.magicdata.read_data()
        return lines[self.magicdata.get_index(category)]


    def clear_data(self):
        answer = input("Do you want to clear the data? (type 'yes' if yes, press 'enter' if no) ").upper()
        if answer == "YES":
            data_place_holders = []
            for indexes in self.magicdata.categories:
                data_place_holders.append({})

            with open("data.json", 'w') as data:
                for categories in data_place_holders:
                    json.dump(categories, data)
                    data.write("\n")

    def get_option(self):
        while True:
            i = 0
            print("Please enter a number for the option you want to do.\n", "-"*43)
            try:
                i = int(input("Option 1: Input Data\nOption 2: Manipulate Data\nOption 3: Display Data\nOption 4: Undo\nOption 5: Quit\n"))
                if i < 1 or i > 5:
                    print("Please input a valid option number")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
            return i
        
    def input_scenario(self):
        while True:
            print("Input one of the following categories(", ", ".join(self.magicdata.categories), ") or 'stop' to exit")
            category = input("\n").upper()
            if category == "STOP":
                break
            if category not in self.magicdata.categories:
                print(f"{category} is not one of the available categories. Please choose from the available categories.")
                continue
            input_name = input("Enter the name that coressponds with the data (name of person, name of archetype, etc): ").lower()
            while True:
                try:
                    win_rate = float(input("Input the win rate (no percent sign) or frequency: "))
                    if not (0 <= win_rate <= 100):
                        print("Error: Win rate must be between 0 and 100.")
                        continue
                    break
                except ValueError:
                    print("Win rate or frequency must be a number")
            index = self.magicdata.get_index(category)
            self.magicdata.input_data(index, input_name, win_rate)

            return category, input_name
    
    def manipulate_data(self):
        while True:    
            print("Input one of the following categories you want to manipulate(", ", ".join(self.magicdata.categories), ")")
            category = input("\n").upper()
            if category not in self.magicdata.categories:
                print(f"{category} is not one of the available categories. Please choose from the available categories.")
                continue
            input_name = input("Enter the name that coressponds with the data (name of person, name of archetype, etc): ").lower()
            category_data = self.get_category_data(category)
            if input_name not in category_data:
                print(f"{input_name} is not in {category}. Please enter a valid name")
                continue
            try:
                input_num = int(input("would you like to calculate the frequency(1) or average win rate (2)? "))
                if input_num == 1:
                    print(f"\nThe frequency of {input_name} is {self.magicdata.get_frequency(category_data, input_name)}")
                elif input_num == 2:
                    print(f"\nThe win rate of {input_name } is {self.magicdata.get_average(category_data, input_name)}%")
                else:
                    print("Please input a valid choice (1 or 2)")
                    continue
            except ValueError:
                print("Please input a valid number")
            break

    def visualize_data(self):
        while True:
            print("Input one of the following categories you want to visualize(", ", ".join(self.magicdata.categories), ")")
            category = input("\n").upper()
            if category not in self.magicdata.categories:
                print(f"{category} is not one of the available categories. Please choose from the available categories.")
                continue
            category_data = self.get_category_data(category)
            categories = list(category_data.keys())
            ListValues = list(category_data.values())
            values = []
            counter = 0
            sum = 0
            try: 
                type_of_graph = int(input("What type of data do you want to graph, winrate(1) or frequency(2) "))
            
                if type_of_graph == 1:
                    for lists in ListValues:
                        for elem in lists:
                            counter = counter + 1
                            sum = sum + elem
                        values.append(sum/counter)
                    plt.bar(categories, values)
                    plt.xlabel(category)
                    plt.ylabel("Win Rate")
                    plt.show()
                elif type_of_graph == 2:
                    for lists in ListValues:
                        for elem in lists:
                            counter = counter + 1
                            sum = sum + elem
                        values.append(sum)
                    plt.pie(values, labels = categories)
                    plt.title(f"Frequency of {category}", )
                    plt.show()
                else:
                    print("Input a valid numer (1 or 2)")
                    continue
            except ValueError:
                print("Input a valid number")
                continue
            break
    
    def undo(self, undo_options):
        category = undo_options[0]
        name = undo_options[1]

        lines = self.magicdata.read_data()
        category_data = lines[self.magicdata.get_index(category)]
        try:
            if len(category_data.get(name)) > 1:
                category_data.get(name).pop()
                print("Successfully undone")
            else:
                del category_data[name]
                print("Successfully undone")
            lines[self.magicdata.get_index(category)] = category_data
            self.magicdata.write_data(lines)
            
        except TypeError:
            print("Cannot undo any further")
        
    def startup(self):
        self.clear_data()
        while True:
            option = self.get_option()
            if option == 1:
                for_undo = self.input_scenario()
            elif option == 2:
                self.manipulate_data()
            elif option == 3:
                self.visualize_data()
            elif option ==4:
                try: 
                    self.undo(for_undo)
                except UnboundLocalError:
                    print("Input data into a category before using undo")
                    continue

            elif option == 5:
                break





    

menu = menu2()
menu.startup()
print("Successfully stopped")