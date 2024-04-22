# LearningDjango3

## 建立虛擬工作環境

py -m venv venv

## 啟用虛擬工作環境

venv\Scripts\activate #啟用虛擬工作環境 反斜線

py -m pip install --upgrade pip # 升級pip套件

pip freeze #列出所有已安裝套件
pip install Django
pip install –r requirements.txt #常見相依性套件安裝方法

pip freeze > requirements.txt #相依性套件輸出

## 安裝Django

pip install Django~=3.2.0 # 會自動將其他相依性套件下載下來

## 建立專案

django-admin startproject Django3_learning

## 建立資料庫

py manage.py migrate

## 建立超級使用者

py manage.py createsuperuser

## 啟動伺服器

py manage.py runserver localhost:8000







