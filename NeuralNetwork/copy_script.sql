COPY (SELECT DISTINCT atr_1, atr_2, atr_3, atr_4, atr_5, atr_6, atr_7, atr_8, atr_9, 
       atr_10, atr_11, atr_12, atr_13, atr_14, atr_15, atr_16, atr_17, 
       atr_18, atr_19, atr_20, atr_21, atr_22 FROM public.train_data) TO '/home/dezhum/Desktop/data_bkp.csv' CSV;

COPY (SELECT DISTINCT * FROM public.train_data) TO '/home/dezhum/Desktop/all_data_bkp.csv' CSV;

COPY (SELECT atr_1, atr_2, atr_3, atr_4, atr_5, atr_6, atr_7, atr_8, atr_9, 
       atr_10, atr_11, atr_12, atr_13, atr_14, atr_15, atr_16, atr_17, 
       atr_18, atr_19, atr_20, atr_21, atr_22 FROM public.train_data) TO '/home/dezhum/WorkSpace/ВКР/NeuralNetwork/data.csv' CSV;

COPY (SELECT opinion FROM public.train_data) TO '/home/dezhum/WorkSpace/ВКР/NeuralNetwork/target.csv' CSV;
