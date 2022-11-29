# importing the required modules
import glob
import pandas as pd

# specifying the path to csv files
path = r"E:\Tulajdonos\Desktop\Tomasz diplomamunka\Új inputadatok\_ajánlatok\proba"

# csv files in the path
filenames = glob.glob(path + "/*.csv")

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )

# specified name.
combined_csv.to_csv( "PROBA merged ajanlatok.csv", index=False )
print("Done!")