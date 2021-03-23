"""Utility functions for wrangling data."""

__author__ = "730316345"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    
    # TODO 0.1) Complete the implementation of this function here.
    file_handle = open("data/nc_durham_2015_march_21_to_27.csv", "r", encoding= "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows

def column_values(rows:list[dict[str, str]], title:str) -> list[str]:
  final_list: list[str] = []
  for row in rows:
      final_list.append(str(row[title]))
   
   return final_list

def columnar(original:list[dict[str, str]]) ->dict[str, list[str]]:
    newDict: dict[str,list[str]]= []
    for row in original:
        for column in row:
            newDict[row,column_values]
        
    return newDict 
