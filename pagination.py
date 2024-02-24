import sqlite3




con = sqlite3.connect("SHELFIE.db", check_same_thread=False)
cursor = con.cursor()
    

class pages():
    def __init__(self, previous:int, nexts:int):
        self.previous = previous + 5
        self.nexts = nexts + 5
    def previous_page(self):
        count, fetch_items = 0, []

        cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 5 """, (self.previous,self.nexts))
        fetch_items =  cursor.fetchall()
        con.commit()
        count = count + 1
        if count == 1:
           return fetch_items
           count = 0  
        exit()
     
    def next_page(self):
        count, fetch_items = 0, []
        if self.previous == self.previous + 1 and self.nexts == self.nexts + 5: 
            self.first_row_id = self.previous + 5
            self.last_row_id = self.nexts + 5
            cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 5 """, (self.first_row_id , self.last_row_id))
            fetch_items =  cursor.fetchall()
            con.commit()
            count = count + 1
            if count == 1:
                return fetch_items
            count = 0  
            exit()
        elif self.previous == self.previous and self.nexts == self.nexts: 
            self.first_row_id = self.previous + 5
            self.last_row_id = self.nexts + 5
            cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 5 """, (self.first_row_id , self.last_row_id))
            fetch_items =  cursor.fetchall()
            con.commit()
            count = count + 1
            if count == 1:
                return fetch_items
            count = 0  
            exit()

class page_default():
    
    def __init__(self, previous:int, nexts:int):
        self.previous = previous
        self.nexts = nexts
    def previous_default_page(self):
        
        count, fetch_items = 0, []

        cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 5 """, (self.previous,self.nexts))
        fetch_items =  cursor.fetchall()
        con.commit()
        count = count + 1
        if count == 1:
           return fetch_items 
           count = 0  
        exit()
           
        
class page_item():
    fetch_items_to_func_get_fetch_items, initial_id, subsequent_id = [], 0, 0
    count, fetch_items, first_row_id, last_row_id = 0, [], 0, 0
    def select_row_id(self, first_row:int, last_row:int):
        
        self.first_row = first_row
        self.last_row = last_row
        self.inital_id = self.first_row
        self.subsequent_id = self.last_row
        cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 5 """, (self.first_row, self.last_row))
        self.fetch_items_to_func_get_fetch_items = fetch_items =  cursor.fetchall()
        con.commit()
        print(fetch_items)
        return [self.first_row, self.last_row]
    def get_fetch_items(self):
        fetch_items = []
        self.fetch_items = self.fetch_items_to_func_get_fetch_items
        return self.fetch_items
        def get_first_last_row_id(self):
            first_row_id, last_row_id = 0, 0
            self.first_row_id = self.initial_id
            self.last_row_id = self.subsequent_id
            
            return self.first_row_id , self.last_row_id
      