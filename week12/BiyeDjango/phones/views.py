import json

import pandas as pd
from django.shortcuts import render

# Create your views here.
from django_pandas.io import read_frame

from  .models import Phones



querycontent=Phones.objects.all()
# pip install django-pandas
dateframe=read_frame(querycontent)

def index(request):
    """首页"""

    return render(request, 'index.html')

def comments(request):
    """
        评论数据展示页
        """
    data = df_to_json(dateframe)
    return render(request, 'comments.html', data)





def sentiments(request):
    """
    舆情数据分析页
    :param request:
    :return:
    """
    data = analyse_sentiments(dateframe)
    return render(request, 'sentiments.html', data)


def analyse_sentiments(df):
    """
    分析舆情数据, 获取评论总数、正向评价数量及比例
    （由于正负评论处理方法基本相同, 这里只处理正向评论）
    :param DF:
    :return:
    """

    total_num=df['name'].value_counts().rename_axis(
        'name'
    ).reset_index(name='total_num')

    positive_num= df[df['stmscore']>=0.5].value_counts()\
        .rename_axis('name').reset_index(name='positive_num')
    #process
    result=pd.merge(total_num,positive_num,how='outer')
    result['positive_pct']=result['positive_num']/result['total_num']
    result['positive_pct']=result['positive_pct'].apply(
        lambda x:format(x,'.2%')
    )
    return df_to_json(result)

def df_to_json(df):
    """
    df to json
    :param df:
    :return:
    """
    records= df.to_json(orient='records')
    data=json.loads(records)
    result={'data':data}
    return data