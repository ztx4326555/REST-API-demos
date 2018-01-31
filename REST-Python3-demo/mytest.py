from HuobiServices import *
import datetime
import matplotlib.pyplot as plt
import mpl_finance as mpf
import os
import time
import numpy as np
from matplotlib.pylab import date2num

def filllist(res):
    data_list=[]
    for block in res['data']:
        dt = datetime.datetime.utcfromtimestamp(block['id']) + datetime.timedelta(hours=8)
        # mpf库中要求的顺序是：时间、开盘价、最高价、最低价、收盘价
        data_list.append((date2num(dt), block['open'], block['high'], block['low'], block['close']))
    return data_list
def triggle():

    while(1):
        ans=get_depth('omgusdt','step0')
        ans2=get_depth('btcusdt','step0')
        ans3=get_depth('omgbtc','step0')
        print("%f %f"%(ans3['tick']['bids'][0][0]*ans2['tick']['bids'][0][0]/ans['tick']['asks'][0][0],ans['tick']['bids'][0][0]/(ans3['tick']['asks'][0][0]*ans2['tick']['asks'][0][0])))
        time.sleep(0.1)


def abv(myid):
    #myid='btcusdt'
    while(1):
        ans=get_depth(myid,'step0')
        mid=(ans['tick']['asks'][0][0]+ans['tick']['bids'][0][0])/2
        signalabv=(ans['tick']['bids'][0][1]-ans['tick']['asks'][0][1])/(ans['tick']['bids'][0][1]+ans['tick']['asks'][0][1])
        print("%f %f"%(signalabv,mid))
        fig,ax = plt.subplots()
        ax.xaxis_date()
        ax.set_title('abv-mid')
        
        
        
    

if __name__ == '__main__':
#    print (get_symbols())
#(omg\btc\usdt)(omg\btc\eth)三角好做

    abv('btcusdt')
        
    '''
    res = get_kline('omgusdt', '1min', 500)
    res2= get_kline('btcusdt', '1min', 500)
    res3= get_kline('omgbtc', '1min', 500)
    dataltcusdt_list = []
    databtcusdt_list = []
    dataltcbtc_list = []
    
    # 操作上一步中获取到的data
    
    dataltcusdt_list=filllist(res)
    databtcusdt_list=filllist(res2)
    dataltcbtc_list=filllist(res3)
    for i in range(0,49):
        print('%f %s'%(res3['data'][i]['close']*res2['data'][i]['close']/res['data'][i]['close'],res3['data'][i]['id']))
        

    fig, ax = plt.subplots()
    ax.xaxis_date()
    ax.set_title('BTC/USDT')
    mpf.candlestick_ohlc(ax,databtcusdt_list,colorup='green',colordown='r',width=0.0002)
    plt.grid()
    plt.show()
    '''
