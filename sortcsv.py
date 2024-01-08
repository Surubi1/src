


def sort():
    #retorna vector con los nombres de los archivos a los cuales se envia a csv2sql
    
    #Algoritmo de verificacion de arhivos...
    
    
    return vectorsorted
    
    
def main():
    vectorsorted=sort()
    
    for con=1:length(vectorsorted):
        
        resp_csvs2sql=csv2sql(vectorsorted(con))
        if resp_csvs2sql==0
            #todo bien 
            resp_query=query()
            if resp_query==0
                #todo bien
            else 
                #error  
        else
            #error
            
                
    
    print("Terminado!")
        
    
if __name__=="__main__":
    main()