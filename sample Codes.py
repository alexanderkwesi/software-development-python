sample Codes

[form_first_id,form_last_id,items_in_list] = page_item().select_row_id(form_first_id, form_last_id)  

 <!--<a href="{{url_for("nnext")}}" class="next">next ></a>--> 
 #app.add_url_rule('/uploaditems/<nnext>/<previous>', 'uploaditems', nnext, previous)
  #for item_id, item_image, item_detail, item_barcode, item_cost in fetch_items:
         #   count = count + 1
          #  if count == 1 and count < len(fetch_items):
           #     if item_id%5 == 0 :
            #        first_row_id = int(item_id + 1)
             #       last_row_id = int(item_id + 5)
              #      return [first_row_id,last_row_id,fetch_items]
#
 #               count = 0 
  #              continue 

        
         
            #sqll = """ SELECT ltrim(rtrim(substring(CHAR(ItemImage), 1, '(<FileStorage: '), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), '("') AS Item_Image FROM UploadItems WHERE ltrim(rtrim(substring(CHAR(ItemImage), 1, '(<FileStorage: '), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), '("')  = ltrim(rtrim(substring(CHAR(ItemImage), 1, '( <FileStorage: '), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), '("') """
        #sqll = """ SELECT trim(substr((ItemImage,16), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), "(<FileStorage: ") FROM UploadItems WHERE trim(substr((ItemImage,16), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), "(<FileStorage: ") = trim(substr((ItemImage,16), "('image/jpeg')>('image/jpg')>('image/png')>('image/svg+xml')>"), "(<FileStorage: ") """
        #datatuple = (str(fileitem))
        
        
 # list_one = str(databaseretrieval).replace(')','\n')
            #list_two = str(list_one).replace("(",'')
            #list_three = (list_two.replace(",", "").replace("'", "").replace(" ",'').replace('[','').replace(']',''))

            
                    
            #with open("file.csv", newline='') as newfile:
             #       files = csv.reader(newfile)  
              #      for row in files:
               #         rows = str(row).replace("[]", "")
                #        #rows = str(row).replace("<FileStorage: ", "")
                 #       listinfo = {'Keys': rows}
                  #      for keys, valuess in listinfo.items():#valll = str(valuess).lstrip("<FileStorage:").rstrip("\'('image/jpeg')>").replace("('image/jpg')>", "").rstrip("('image/png')>").rstrip("('image/svg+xml')>")
                   #         valll = str(valuess).replace("['", "").replace("']", "").replace('"', "").replace("[","").replace("]","")
                    #    return f"{itemstring}"
                    
                    
                    
                       #files = csv.reader(newfile)  
    #with open("file.csv", newline='') as newfile:
        #for row in files:
            #rows = str(row).replace("[]", " ")
            #listinfo = {'Keys': rows}
            #for keys, valuess in listinfo.items():valll = (valuess).replace("['", "").replace("']", "").replace('"', "").replace("'", "")
            #return render_template('uploaditem.html', date=today, sqlconstring=valll)
            
            
            
              #app.add_url_rule('/uploaditem/<sqlstring>', 'show_item', sqlstring) 



                        
#@app.route('/uploaditem/<itemstring>', methods=['GET', 'POST'])#
#def viewuploaditem(itemstring): 
 #       listinfo, valll = [], []  
        #else:

        #display all images        
  #      if request.method == "GET":
                
     #       with open("file.csv", newline='') as newfile:
   #             for row in files:
                   rows = str(row).replace("[]","")#.replace("<FileStorage: ", "")
    #            files = csv.reader(newfile)  
      #             print(row)
       #¢            listinfo = {'Keys': rows}
         #          for keys, valuess in listinfo.items():#valll = str(valuess).lstrip("<FileStorage:").rstrip("\'('image/jpeg')>").replace("('image/jpg')>", "").rstrip("('image/png')>").rstrip("('image/svg+xml')>")
          #             # valll = str(valuess).replace("['", "").replace("']", "").replace('"', "").replace("[","").replace("]","").replace("'", "")
           # return render_template('uploaditem.html', date=today, sqlstring=valll, string=itemstring) #for value in list_three:
             #   for val in value:
              #      if not val.startswith('"') or not val.__contains__("\""):   
               #            string_value_one = "".join(val)
                    #string_value_one = "+".join(string_value_one)
               # list_four.append(string_value_one)
                       
                #sqlconstruct = (str(list_four).replace('"', "").replace(",", ""))

            #for i in range(0 , len(sqlcursor)):
           
                #string_value = "".join(sqlconstruct).replace("'", " ")
                
                
                
              
                
                #with open('file.csv', 'w', newline='')  as file:
                 #   writer = csv.writer(file)
                  #  for a in string_value:
                   #     if a != "\n":
                    #        #csvv = writer.writerow(['Item'])
                     #       csvv = writer.writerow([testentry])
                      #      continue
                        
                #itemduplicate = pd.read_csv('file.csv')
                #itemduplicate.head()
                #itemduplicate.columns
                #duplicateRowsDF = itemduplicate[itemduplicate.duplicated()]
                #duplicateRowsDF = itemduplicate[itemduplicate.duplicated(keep='last')]
                #duplicateRowsDF = itemduplicate[itemduplicate.duplicated(['Item'])]
                #result = itemduplicate.drop_duplicates(keep=False)        
                
                #with open("file.csv", newline='') as newfile:
                 #   files = csv.reader(newfile)  
                  #  for row in files:
                   #     #rows = str(row).replace("<FileStorage: ", "")
                    #    rows = str(row).replace("[]", "")
                     #   listinfo = {'Keys': rows}
                      #  for keys, valuess in listinfo.items():#valll = str(valuess).lstrip("<FileStorage:").rstrip("\'('image/jpeg')>").replace("('image/jpg')>", "").rstrip("('image/png')>").rstrip("('image/svg+xml')>")
        
                        #.replace("['", "").replace("']", "").replace('"', "").replace("[","").replace("]","")       # list_one = str(databaseretrieval).replace(')','\n')
        #list_two = str(list_one).replace("(",'')
        #list_three = (list_two.replace(",", "").replace("'", "").replace(" ",'').replace('[','').replace(']',''))//setInterval(hidedisplay, 5000);
       //const btn = document.getElementById('uploadbtnclick');
           // btn.addEventListener('click', () => {

                //window.addEventListener('load', () => {
                   // if (documnet.getElementById('pop-up-upload-item-image').style.display.block == "none")
                   // {
                       // document.getElementById('success-message').style.display = "block";
                   // }
                    //setInterval(hidedisplay, 5000);
                //});    
                
        //});
                
        //window.addEventListener('load', () => {
        //if (window.location.href.endsWith("uploaditem"))
       // {
            
            //const btn = document.getElementById('uploadbtnclick');
            //btn.addEventListener('click', () => {

         //   window.addEventListener('load', () => {
           //     document.getElementById('success-message').style.display = "block";
               
            //});    
            
            //});
            //setInterval(hidedisplay, 5000);
        //}
        //setInterval(hidedisplay, 10000);
      //});
      function hidedisplay()
      {
        document.getElementById('success-message').style = 'none';
      }
</script>
<script>

        //const goto_url = {{ url_for('uploaditem')}}
        const form_class = getElementsByClassName('form')
        const form_attribute = getAttribute('id')
        alert(form_attribute)
        fetch(goto_url)
          .then(response => response.text)
         .then(text => form_class.style.display = "none")

</script>  }
      //setInterval(hidedisplay, 5000);
       //const btn = document.getElementById('uploadbtnclick');
           // btn.addEventListener('click', () => {

                //window.addEventListener('load', () => {
                   // if (documnet.getElementById('pop-up-upload-item-image').style.display.block == "none")
                   // {
                       // document.getElementById('success-message').style.display = "block";
                   // }
                    //setInterval(hidedisplay, 5000);
                //});    
                
        //});
                
        //window.addEventListener('load', () => {
        //if (window.location.href.endsWith("uploaditem"))
       // {
            
            //const btn = document.getElementById('uploadbtnclick');
            //btn.addEventListener('click', () => {

         //   window.addEventListener('load', () => {
           //     document.getElementById('success-message').style.display = "block";
               
            //});    
            
            //});
            //setInterval(hidedisplay, 5000);
        //}
        //setInterval(hidedisplay, 10000);
      //});
        
        
        
        <script>

        //const goto_url = {{ url_for('uploaditem')}}
        const form_class = getElementsByClassName('form')
        const form_attribute = getAttribute('id')
        alert(form_attribute)
        fetch(goto_url)
          .then(response => response.text)
         .then(text => form_class.style.display = "none")};
      
</script>