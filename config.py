PATHS= {
        "raw_data": r"C:\Users\zakar\OneDrive\Bureau\projects\techreco\data\technopark_startups.json", 

        "embedding_data": r"C:\Users\zakar\OneDrive\Bureau\projects\techreco\data\embedding_data",
        
} 
#r is essential because pandas uses the linux convention for paths. 
#otherwise we get a unicode error (although the problem has nothing to do with encoding.)
