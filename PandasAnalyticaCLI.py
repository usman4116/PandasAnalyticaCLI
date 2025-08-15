import pandas as pd

class data_Analyt:

    def __init__(self):
        self.df=None
        self.file_name=""

    def load_data(self):

        self.file_name = input("Enter the file name with extension and 0 for exit: ")  

        if self.file_name.endswith('.xlsx'):

            self.df = pd.read_excel(self.file_name)

        elif self.file_name.endswith('.csv'):

            self.df =pd.read_csv(self.file_name)
        elif self.file_name.endswith('.json'):

            self.df = pd.read_json(self.file_name)
        elif self.file_name==0:

            print("Exiting the program.")
            exit()
        else:
            print("Invalid file format. Please provide a valid file.")
            return        
        print("\nDataset loaded successfully!\n")   
    def display_data(self):    
        while True:
            print("1. Display Data")
            print("2. Display Info")
            print("3. Display Missing Values")
            print("4. Display First 5 Rows")
            print("5. Display Summary Statistics")
            print("6. To Covert this file")

            print("7. Exit")

            choice = input("Enter your choice: ")
            
            if choice == '1':
                print(self.df)
            elif choice == '2':
                print(self.df.info())
            elif choice == '3':
                print(self.df.isnull().sum())
            elif choice == '4':
                print(self.df.head())
            elif choice == '5':
                print(self.df.describe())
            elif choice == '6': 
                print("Choose the conversion format:")

                if self.df is not None:
                       print("1. Convert to CSV")
                       print("2. Convert to Excel")
                       print("3. Convert to JSON")
                       print("4. Exit")
                       conversion_choice = input("Enter your choice: ")
                       
                       if conversion_choice == '1':
                           
                           output_file = input("Enter the name for the output CSV file (with .csv extension): ")
                           self.df.to_csv(output_file, index=False)
                           print("Data saved to {output_file}")
                       elif conversion_choice == '2':   
                            
                            output_file = input("Enter the name for the output Excel file (with .xlsx extension): ")
                            self.df.to_excel(output_file, index=False)
                            print("Data saved to {output_file}")
                       elif  conversion_choice == '3':
                           
                           output_file=input("Enter namne for the output Json  file (with .json extension) ")    
                           self.df.to_json(output_file,orient='records')
                           print("Data saved to {output_file}")

            elif choice == '7':
                break
            else:
                print("Invalid choice, please try again.")



tool = data_Analyt()
tool.load_data()
tool.display_data()
