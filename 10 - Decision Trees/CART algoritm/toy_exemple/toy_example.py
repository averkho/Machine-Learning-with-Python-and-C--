# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:39:06 2022

@author: AVERKHO
"""
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from collections import Counter

decision_tree=DecisionTreeClassifier()




def transform_data():
    
    dat=pd.read_csv('../example/owls15.csv')
    dat.columns=['A','B','C','D','label']
    print(dat['label'].unique())
    dict_to_convert={'LongEaredOwl':'Poor','SnowyOwl':'Moderate','BarnOwl':'Good'}
    dat['label']=dat['label'].map(dict_to_convert)
    
    dat.to_csv('product_quality.csv',index=False)
 
dat=pd.read_csv('./product_quality.csv')

decision_tree=DecisionTreeClassifier()

X=dat[dat.columns[:-1]]
y=dat[dat.columns[-1]]

X_train,X_test,y_train,y_test=train_test_split(X,y,shuffle=True,test_size=0.2)

decision_tree.fit(X_train,y_train)

pred=decision_tree.predict(X_test)

print(accuracy_score(y_test,pred))

class Question(object):
    
    def __init__(self,attr_id,value):
        
        self.attr_id=attr_id
        self.value=value
        self.calc_mode=isinstance(self.value,float) or isinstance(self.value,int)
        
    def __str__(self):
        
        comparator=">=" if self.calc_mode else "=="
        return "Is attribute {} {} {}:".format(self.attr_id+1,comparator,self.value)
    
    def check_answer(self,dat):
        
        if self.calc_mode:
            
            true_instances=dat[dat[dat.columns[self.attr_id]]>=self.value]
            false_instances=dat[dat[dat.columns[self.attr_id]]<self.value]
            true_instances.reset_index(inplace=True,drop=True)
            false_instances.reset_index(inplace=True,drop=True)
            
            return true_instances,false_instances
        
        else:
            
            true_instances=dat[dat[dat.columns[self.attr_id]]==self.value]
            false_instances=dat[dat[dat.columns[self.attr_id]]!=self.value]
            true_instances.reset_index(inplace=True,drop=True)
            false_instances.reset_index(inplace=True,drop=True)
            
            return true_instances,false_instances
        
class Leaf(object):

    def __init__(self,dat):
        
        self.probabilities=self.__class_frequency(dat)
        print(self.probabilities)
        
    def __class_frequency(self,dat):
        
        return Counter(dat['label'])
    
    def pretty_print(self,offset=0):
        
        total_count=sum(self.probabilities.values())
        results={}
        for class_name,count in self.probabilities.items():
            results[class_name]=count*100/total_count
        
        return ",".join(["<{}:{}>".format(r[0],r[1]) for r in results.items()])
        
class Node(object):
    
    def __init__(self,question,true_subtree,false_subtree):
        
        self.question = question
        self.true_subtree=true_subtree
        self.false_subtree=false_subtree
    
    def pretty_print(self,offset=0):
        
        padding="\n"+offset*"\t\t"+"└────"
        q=str(self.question)
        true_path=padding+"Y:  "+self.true_subtree.pretty_print(offset=offset+1)
        false_path=padding+"N:  "+self.false_subtree.pretty_print(offset=offset+1)
        
        return q+true_path+false_path

class Cart(object):
    
    def __init__(self,dat,y):
        
        self.y=y
        
        self.__tree=self.__construct_tree(dat)
    
    def __construct_tree(self,dat):
        
        #find the best way to split the data
        info_gain,question=self.__calc_best_split(dat)
        print('info_gain ',info_gain)
        if info_gain==0:
            
            return Leaf(dat)
        
        true_data,false_data=self.__split_data(dat,question)
        
        true_subtree=self.__construct_tree(true_data)
        false_subtree=self.__construct_tree(false_data)
        
        return Node(question,true_subtree,false_subtree)
    
    def __split_data(self,dat,question):
        
        true_instances,false_instances=question.check_answer(dat)
        
        return true_instances,false_instances
    
    def __calc_info_gain(self,lhs_dat,rhs_dat,cur_uncertainty):
        
        num_instances=lhs_dat.shape[0]+rhs_dat.shape[0]
        weight_rhs=rhs_dat.shape[0]/num_instances
        weight_lhs=lhs_dat.shape[0]/num_instances
        
        uncert_lhs=self.__calc_uncertainty(lhs_dat)
        uncert_rhs=self.__calc_uncertainty(rhs_dat)
        new_uncert=weight_rhs*uncert_rhs+weight_lhs*uncert_lhs
        
        return cur_uncertainty-new_uncert
    
    def __calc_best_split(self,dat):
        
        best_info_gain=0
        best_question=None
        
        current_uncertainty=self.__calc_uncertainty(dat)
        
        dimensionality=dat.shape[1]-1
        
        for attr_id in range(dimensionality):
            
            unique_values=set(dat[dat.columns[attr_id]].unique())
            
            for value in unique_values:
                
                question=Question(attr_id,value)
                true_instances,false_instances=self.__split_data(dat,question)
                
                if max(true_instances.shape[0],false_instances.shape[0])>=dat.shape[0]:
                    
                    continue
                
                info_gain=self.__calc_info_gain(false_instances,true_instances,current_uncertainty)
                
                if info_gain>best_info_gain:
                    
                    best_info_gain=info_gain
                    best_question=question
                    
        
        
        return best_info_gain,best_question
        
    def __calc_uncertainty(self,dat):
        
        '''
        Calculation of Gini uncertainty for a dataset
        
        '''
        
        uncertainty=1
        
        count_of_labels=Counter(list(dat[self.y]))
        num_instances=dat.shape[0]
        
        for label,count in count_of_labels.items():
            
            prob_of_label=count/num_instances
            prob_of_matching=prob_of_label**2
            uncertainty-=prob_of_matching
        
        return uncertainty
    
    def visualize_model(self):
        
        print("")
        print(self.__tree.pretty_print())
    
    
            

cart=Cart(dat,y='label')

Cart(dat,y='label').visualize_model()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        