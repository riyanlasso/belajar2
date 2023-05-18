SELECT table1.Frame, table1.Marker,table1.X_Cordinates, table1.X_Scoring,table1.Y_Cordinates, table1.Y_Scoring,table1.Z_Cordinates, table1.Z_Scoring, 
table2.Frame, table2.Marker,table2.X_Cordinates, table2.X_Scoring,table2.Y_Cordinates, table2.Y_Scoring,table2.Z_Cordinates, table2.Z_Scoring
FROM riyanlasso.agneska AS table1
JOIN riyanlasso.doni AS table2 
ON table1.id = table2.id;