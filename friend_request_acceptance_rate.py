import pandas as pd

# Start writing code
df = fb_friend_requests

#df.loc[df['date']=='2020-01-04 00:00:00']

#df.groupby(['user_id_sender', ' user_id_receiver'])

#df.drop_duplicates(['user_id_sender' , 'user_id_receiver'])

df['bool'] = 0
df.loc[df['action']=='accepted' , 'bool']=1

#dfi = df.groupby(['date'])['bool'].sum().reset_index()
#dfi = df.groupby(['user_id_sender' , 'user_id_receiver'])['action'].sum().reset_index()

#dfi['new'] = dfi['action']
#dfi.merge(df , how ='outer')
#df['duplicates'] = df.duplicated(['user_id_sender' , 'user_id_receiver'])
dfi = df
df = df.sort_values('action')
df['duplicates'] = df.duplicated(['user_id_sender' , 'user_id_receiver'])
df = df.drop(df[df.duplicates==False] .index)
df['count'] = 1
df =df.groupby('date').sum().reset_index()
#dfi.drop('bool' ,axis =1)

dfi['sum'] = 1
dfi = dfi.groupby('date').sum().reset_index()

dfi

#df['sum'] = 1
dfi =dfi.drop('bool' ,axis =1)
df= df.merge(dfi ,how = 'outer')
#df.groupby('date').sum().reset_index()

dfi['acceptance_rate'] = df['count']/df['sum']
dfi.dropna()
