# -*- coding: utf-8 -*-
"""multi_classification_on_images.ipynb

@ author: Vishal Dhiman

"""



from __future__ import absolute_import,print_function,division,unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


class fashion_mnist:
  def __init__(self):
    self.epoch=0
    self.class_name=['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot']

  def load_data(self):
    #loading data
    fashion_mnist=keras.datasets.fashion_mnist
    (self.train_img,self.train_lab),(self.test_img,self.test_lab)=fashion_mnist.load_data()
    
    print("\n[Out]: Data Loaded Successfully.")
    
  def preprocessing(self):
    #normalize 0-1
    self.train_img=self.train_img/255.0
    self.test_img=self.test_img/255.0
    print("\n[Out]: Preprocessing done.\n")
    
  def data_info(self):
    
    print("[Out]: Training data shape: ",self.train_img.shape)
    print("[Out]: Training label data shape: ",self.train_lab.shape)
    print("[Out]: Test data shape: ",self.train_img.shape)
    print("[Out]: Training label data shape: ",self.train_lab.shape)
    
  def show_data(self):
    print("[Out]: Plotting images")
    plt.figure(figsize=(10,10))
    for i in range(25):
      plt.subplot(5,5,i+1)
      plt.xticks([])
      plt.yticks([])
      plt.grid(False)
      plt.imshow(self.train_img[i],cmap=plt.cm.binary)
      plt.xlabel(self.class_name[self.train_lab[i]])
    plt.show()
    
  
  def create_model(self):
    
    #define layers
    model=keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation='relu'),
        keras.layers.Dense(10,activation='softmax')
        ])
    #compile
    model.compile(optimizer='Adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    print("[Out]: Model Summary:")
    
    model.summary()
    
    print("[Out]: Model creation and compilation successful. ")
    
    return model
  
  def train_model(self,model,epoch):
    self.epoch=epoch
    model.fit(self.train_img,self.train_lab,epochs=epoch)
    print("[Out]: Model now trained.")
    
  def evaluate_model(self,model):
    
    test_los,test_accu=model.evaluate(self.test_img,self.test_lab)
    
    print("[Out]: Model test loss:{} and  test accuracy:{} ".format(test_los,test_accu))
    
  def model_predict(self,model):
    print("[Out]: choose img:")
    n=int(input("::"))
    img=np.expand_dims(self.train_img[n],0)
    
    d=model.predict(img)
    print("[Out]: predicted label:",np.argmax(d))
    print("[Out]: actual model:",self.train_lab[n])
    
  def save_model(self,model):
    
    model.save("model_classification.h5")
    print("[Out]: Model saved.")
   
    
    
  
 
    
    
    
if __name__=="__main__":
  
  obj=fashion_mnist()
  obj.load_data()
  obj.preprocessing()
  obj.data_info()
  obj.show_data()
  model=obj.create_model()
  obj.train_model(model,10)
  obj.evaluate_model(model)
  obj.model_predict(model)
  #obj.save_model(model)

obj.preprocessing()

fashion_mnist=keras.datasets.fashion_mnist
(train_img,train_lab),(test_img,test_lab)=fashion_mnist.load_data()



print(train_img.shape)
print(train_lab.shape)



train_img=train_img/255.0
test_img=test_img/255.0

plt.figure(figsize=(10,10))
for i in range(25):
  plot_im(train_img[i],i,train_lab[i])

plt.show()

model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='Adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_img,train_lab,epochs=10)

test_los,test_accu=model.evaluate(test_img,test_lab)
print(test_los,test_accu)
