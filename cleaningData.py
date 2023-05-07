"https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file"
from more_itertools import unique_everseen
with open('Data/dataUpdated.tsv', 'r') as f, open('Data/newDataUpdated.tsv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))
    
"https://towardsdatascience.com/data-cleaning-how-to-handle-missing-values-in-pandas-cc8570c446ec"