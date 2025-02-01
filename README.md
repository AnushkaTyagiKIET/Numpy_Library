# NumPy Learning Journey  

Welcome to my NumPy learning journey! This repository is dedicated to exploring and practicing with the NumPy library, showcasing various examples, exercises, and notes as I progress in understanding this powerful Python library for numerical computing.  

## 📚 Overview  

NumPy (Numerical Python) is the foundational package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with an extensive collection of mathematical functions to operate on these arrays.  

### Goals  
In this repository, I aim to:  
- Understand core functionalities of NumPy.  
- Explore array creation, manipulation, and operations.  
- Learn about NumPy's mathematical functions and utilities.  
- Apply NumPy in real-world scenarios, such as data analysis and scientific computing.  

## Company Productivity Analysis  

### Project Overview  
This project analyzes the productivity of different companies based on their employees' product output. The data used is assumed for practice purposes. The program performs various operations such as reading data from a file, converting it into a NumPy array, and performing statistical analysis like finding the most and least productive companies.  

### Files Included  
- `main.py`: The main script that reads data, processes it, and performs various operations.  
- `Operationclass.py`: Contains the `IntArray` class for handling operations related to company productivity.  
- `company.txt`: The data file containing information about products produced by employees of different companies.  

### Functionalities and Implementations  

1. **Reading Data from a File**  
   - The `file_handling()` function reads data from `company.txt`.  
   - Each line represents a company's employees' production numbers, separated by commas.  
   - The function processes this data and converts it into a NumPy array for further operations.  
   - **Reason for Using NumPy**: Provides efficient array handling and mathematical computations, making data manipulation faster.  

2. **Finding the Most and Least Productive Companies**  
   - The `products_produced_by_each_company()` function calculates the total production of each company using `np.sum()`.  
   - The `max_productivity()` function determines which company has the highest production.  
   - The `min_productivity()` function identifies the least productive company.  
   - **Why Use NumPy's Sum Function?**: It is more efficient than manually looping through arrays.  

3. **Calculating the Mean Productivity**  
   - The `mean_Products()` function calculates the average number of products produced per employee.  
   - Utilizes `np.mean()` for efficiency.  

4. **Handling and Displaying Data Using a Class**  
   - The `IntArray` class in `Operationclass.py` is designed to manage and visualize productivity data.  
   - Functions include:  
     - `display()`: Prints the array.  
     - `salary()`: Calculates salaries based on products produced (assuming 7 units of money per product).  
     - `show_data()`: Generates a line plot for employee productivity.  

5. **Visualization with Matplotlib**  
   - `show_data()` uses Matplotlib to plot the number of products produced by employees.  
   - **Why Use `plt.xticks(X)`?**: Ensures that all worker IDs are displayed for better readability.  
   - Other Matplotlib features used:  
     - `marker='o'` makes data points visible.  
     - `plt.grid()` adds a grid for better visualization.  

### Running the Project  
1. Ensure you have Python installed.  
2. Install dependencies using:  
   ```bash  
   pip install numpy matplotlib
