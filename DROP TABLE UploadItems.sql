DROP TABLE UploadItems
DROP TABLE UploadItem_tmp
CREATE TABLE "UploadItems" (
	Item_Id INTEGER NOT NULL,
	ItemImage TEXT,
	ItemDetail TEXT,
	ItemBarCode REAL,
	ItemCost NUMERIC,
	CONSTRAINT Item_Id_PK PRIMARY KEY (Item_Id)
)