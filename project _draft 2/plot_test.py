import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import mysql.connector
from batchDAO import batchDAO

#def do_plot():

    # # here is the trick save your figure into a bytes object and you can afterwards expose it via flas
    # bytes_image = io.BytesIO()
    # plt.savefig(bytes_image, format='png')
    # bytes_image.seek(0)
    # return bytes_image

 
def getAll():
    results = batchDAO.getAll()


    df = pd.DataFrame(results)
    print (df)


    df.plot(x = "id",y="yield", kind ="bar", color = "green", title="Yield per Batch")
    plt.show()


getAll()