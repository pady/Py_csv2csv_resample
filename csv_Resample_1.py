#
#
# 1) 
df = pd.read_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\Striker_F_Runs2_3_4.csv',header=1)
#
# 2) 
t5e6n30001=pd.date_range(start='1/1/1 0:0:2',periods=30001, freq='5U')
t5e6n_end_2p1_end=pd.date_range(start='1/1/1 0:0:2',end='1/1/1 0:0:2.1', freq='5U')
#
# 3) 
df['datetime']=t5e6n30001
df['datetime']=t5e6n_end_2p1_end
#
# 4)  
df_re_750r=df.resample('200U',on='datetime').first()
df_re_200mks=df.resample('200U',on='datetime').first() # 200001 raws
#
# 5)  
df_re_750r.to_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\F_resample_200mks.csv', index=False)
df_re_200mks.to_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\F_resample_200mks.csv', index=False)
#  ValueErrodfr: Length of values (20001) does not match length of index (30001)
#


df = pd.read_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\Test100.csv',header=0)
df['datetime']=t5e6n30001
df_re_750r=df.resample('200U',on='datetime').first()
print(df)
           Time     Cell1Z  ...     Cell6X                   datetime
0      4.379430  -3.059172  ...   0.669773 2001-01-01 00:00:02.000000
1      4.379435  -0.307361  ...   0.423862 2001-01-01 00:00:02.000005
2      4.379440   2.444449  ...   1.407507 2001-01-01 00:00:02.000010
3      4.379445  -7.186888  ...  -0.805694 2001-01-01 00:00:02.000015
4      4.379450   5.196260  ...   1.653418 2001-01-01 00:00:02.000020
...         ...        ...  ...        ...                        ...
29996  4.529410 -36.080897  ...  35.589162 2001-01-01 00:00:02.149980
29997  4.529415 -23.697750  ...  39.031918 2001-01-01 00:00:02.149985
29998  4.529420 -30.577276  ...  37.310540 2001-01-01 00:00:02.149990
29999  4.529425 -31.953182  ...  36.818718 2001-01-01 00:00:02.149995
30000  4.529430 -23.697750  ...  38.786007 2001-01-01 00:00:02.150000

[30001 rows x 21 columns]
print(t5e6n30001)
DatetimeIndex([       '2001-01-01 00:00:02', '2001-01-01 00:00:02.000005',
               '2001-01-01 00:00:02.000010', '2001-01-01 00:00:02.000015',
               '2001-01-01 00:00:02.000020', '2001-01-01 00:00:02.000025',
               '2001-01-01 00:00:02.000030', '2001-01-01 00:00:02.000035',
               '2001-01-01 00:00:02.000040', '2001-01-01 00:00:02.000045',
               ...
               '2001-01-01 00:00:02.149955', '2001-01-01 00:00:02.149960',
               '2001-01-01 00:00:02.149965', '2001-01-01 00:00:02.149970',
               '2001-01-01 00:00:02.149975', '2001-01-01 00:00:02.149980',
               '2001-01-01 00:00:02.149985', '2001-01-01 00:00:02.149990',
               '2001-01-01 00:00:02.149995', '2001-01-01 00:00:02.150000'],
              dtype='datetime64[ns]', length=30001, freq='5U')
df_re_750r.to_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\Test100_200mks.csv', index=False)
df_re_300r=df.resample('500U',on='datetime').first()
print(df_re_300r)
                               Time     Cell1Z  ...     Cell5X     Cell6X
datetime                                        ...                      
2001-01-01 00:00:02.000000  4.37943  -3.059172  ...   0.349465   0.669773
2001-01-01 00:00:02.000500  4.37993  -3.059172  ...  -0.145951   0.669773
2001-01-01 00:00:02.001000  4.38043   3.820355  ...   0.597172   0.669773
2001-01-01 00:00:02.001500  4.38093   1.068544  ...   0.349465   0.177951
2001-01-01 00:00:02.002000  4.38143  -1.683266  ...  -0.145951   0.915684
...                             ...        ...  ...        ...        ...
2001-01-01 00:00:02.148000  4.52743 -47.088139  ...  27.101887  10.752132
2001-01-01 00:00:02.148500  4.52793 -40.208613  ...  30.817501  17.637645
2001-01-01 00:00:02.149000  4.52843 -31.953182  ...  30.817501  25.998625
2001-01-01 00:00:02.149500  4.52893 -37.456803  ...  33.294577  30.916849
2001-01-01 00:00:02.150000  4.52943 -23.697750  ...  38.248729  38.786007

[301 rows x 20 columns]
df_re_300r.to_csv('C:\\Users\\pdybskiy\\Documents\\Python\\Proj_xls_reduction1\\Test100_500mks.csv', index=False)

