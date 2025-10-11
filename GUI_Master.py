# -*- coding: utf-8 -*-
"""


@author: saurabh
"""

# -*- coding: utf-8 -*-
"""


@author: rahul
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from subprocess import call
import tkinter as tk
import tkinter as tk
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
#from sklearn.ensemble import RandomForestRegressor

#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Machine Learning Based Predicting Student Academic Success")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img3.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Student Performance Prediction System",font=("Times New Roman", 35, 'bold'),
                    background="Maroon", fg="white", width=52, height=1)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#

def RF():
    
    data = pd.read_csv("ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    from sklearn.ensemble import RandomForestClassifier  

    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    #rfclassifier =  RandomForestClassifier(n_estimators= 10, criterion="entropy")  
    #rfclassifier.fit(x_train, y_train)
    
    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    
    
    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    import seaborn as sns
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,y_pred)
    
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')
    
    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()
    
    
   
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"SVM.joblib")
    print("Model saved as SVM.joblib")

def SVM():
    
    data = pd.read_csv("ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=9999)

    from sklearn.ensemble import RandomForestClassifier  

  
    # rfclassifier =  RandomForestClassifier(n_estimators= 10, criterion="entropy")  
    # rfclassifier.fit(x_train, y_train)
    
    # y_pred = rfclassifier.predict(x_test)
    # print(y_pred)
    
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    
    
    
   

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    import seaborn as sns
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,y_pred)
    
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')
    
    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as model.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"model.joblib")
    print("Model saved as model.joblib")
    
#from sklearn.model_selection import train_test_split 
#from sklearn.preprocessing import StandardScaler
#from sklearn.datasets import make_moons, make_circles, make_classification
#from sklearn.neural_network import MLPClassifier
#from sklearn.neighbors import KNeighborsClassifier


    
def graph():
    
    image3 =Image.open('RF.png')
    background_image1=ImageTk.PhotoImage(image3)
    background_label1 = tk.Label(root, image=background_image1)
    background_label1.image = background_image1
    background_label1.place(x=300, y=100)
    
    image4 =Image.open('SVM.png')
    background_image2=ImageTk.PhotoImage(image4)
    background_label2 = tk.Label(root, image=background_image2)
    background_label2.image = background_image2
    background_label2.place(x=700, y=100)



def log():
    from subprocess import call
    call(["python","Check.py"])
    
def window():
  root.destroy()


# button1 = tk.Button(root, text="Model Training SVM", command=SVM, width=15, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button1.place(x=50, y=160)

button2 = tk.Button(root, text="Model Training RF", command=SVM, width=15, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button2.place(x=50, y=250)

button2 = tk.Button(root, text="Check Performance",command=log,width=15, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button2.place(x=50, y=360)

button3 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=50, y=460)

root.mainloop()