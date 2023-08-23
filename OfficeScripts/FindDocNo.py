#####
#####This is for identifying the docList from the MFOL
##### then we'll pick the unique docno and put it in a DocListFile
#####

mfol_file = r"C:\Users\AKHIL\Documents\Testing\Input.txt"
doc_list_file = r"C:\Users\AKHIL\Documents\Testing\DocList.txt"

with open(mfol_file,'r',encoding="utf-8") as inp, open(doc_list_file,'w',encoding='utf-8') as out:
    line_buffer = inp.read()
    lines = line_buffer.split("\n")
    doc_list = []
    for line in lines:
        doc_list.append(line[11:25:])
    
    # inserting the list into a set
    list_set = set(doc_list)
    print("Doc Lis is ")
    print(doc_list)
    print("List Set is:")
    print(list_set)

    #converting the set to list
    unique_doc_list = (list(list_set))
    for doc_no in unique_doc_list:
        if(doc_no != ""):
            out.write(doc_no+"\n")

    
