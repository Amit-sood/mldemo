class MatchingPinning():
    def __init__(self) -> None:
        pass

    def makePrediction(self, searchText):
        from sentence_transformers import SentenceTransformer, util
        from flask import jsonify
        import numpy as np
        #import csv
        modelPath="./models/"
        model = SentenceTransformer(modelPath)

        searchSentenceArray=[]
        sentences=[
            'Steven Bailey 39 Addison Crescent Manchester M16 0WN (0161) 000 0058',
            'Stephen Mount 39 Addison Crescent Manchester M16 0WN (0161) 000 0058',
            'Steven Baile 39 Adison Crecent Manchester M16 0WN (0161) 000 0058',
            'Steve B. 39 Addison Crescent Manchester M16 0WN (0161) 000 0058',
            'Bailey Steven Manchester Addison Crescent 39 M16 0WN (0161) 000 0058',
            'Steven Baile 39 Adison Crecent ',
            'Steven Bailey 39 Addison cre  MN M16 0WN (0161) 000 0058',
            'James Abercrombie 8 Hanbury Drive, Calcot RG31 7EJ (0118) 602 4786',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Manchester M16 0WN (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Manchester M16 0WN (01933) 127372',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443']

        
        """
        # Open file 
        with open('./fakeData.csv') as file_obj:
            
            # Create reader object by passing the file 
            # object to reader method
            reader_obj = csv.reader(file_obj)
            
            # Iterate over each row in the csv 
            # file using reader object
            for row in reader_obj:
                sentences.append(row[0])
                #print(row[0])

        """
        print(len(sentences))
        for i in range(len(sentences)):    
            searchSentenceArray.append(searchText)
        

        #Compute embeddings
        print('a')
        searchEmbeddings = model.encode(searchSentenceArray, convert_to_tensor=True)
        print(len(searchEmbeddings))
        
        print('b')
        #embeddings = model.encode(sentences, convert_to_tensor=True)
        embeddings=np.load('./models/embeddings.npy')

        
        print('-----------------')

        #Compute cosine-similarities for each sentence with each other sentence
        cosine_scores = util.cos_sim(searchEmbeddings, embeddings)
        #print(len(cosine_scores))

        returnCosineScore=[]    
        #Output the pairs with their score
        for i in range(len(sentences)):            
            returnCosineScore.append("{:.4f}".format( cosine_scores[i][i]))
            #print("{} \t\t {} \t\t Score: {:.4f}".format(sentences[i], searchSentenceArray[i], cosine_scores[i][i]))
        returnData = jsonify({'results': sentences, 'score':returnCosineScore})
        
        return returnData
