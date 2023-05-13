import matplotlib.pyplot as plt
import pandas as pd

url = 'https://drive.google.com/file/d/1bayMcfy2Iw_SqyeWTmyscAMzPGx2JBaf/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)
    
    
    
column_name = "Which crop(s) are present in the field?"
ax = data[column_name].value_counts().plot(kind='pie')
ax.set_xlabel("Field types")
ax.set_ylabel("Number of points")
plt.show()
