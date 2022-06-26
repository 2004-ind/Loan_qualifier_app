# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
    

def save_csv(csvpath_1, qualifying_loans):
    """save the qualifying_loans in CSV file to the path provided.

    Args:
        csvpath (Path): The csv file path.
        qualifying_loans : saves the the list of qualifying loans.
    Returns:
        A list of lists that contains the list of qualifying loan from the CSV file.

    """
    with open(csvpath_1, "w") as csvfile:
        data = qualifying_loans
        csvwriter = csv.writer(csvfile, delimiter=",")
        
       
        # Write the header
        header = ["Lender","Max_Loan_Amount","Max_LTV","Max_DTI","Min_Credit_Score","Interest_Rate"]
        csvwriter.writerow(header)
        
        # Save the CSV data
        for row in data:
            csvwriter.writerow(row)
          
    return
