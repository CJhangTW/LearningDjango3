# LearningDjango3

## 建立虛擬工作環境

py -m venv 虛擬環境名稱

## 啟用虛擬工作環境

Py3Dj3\Scripts\activate #啟用虛擬工作環境

pip freeze #列出所有已安裝套件
pip install Django
pip install –r requirement.txt #常見相依性套件安裝方法

pip freeze > requirement.txt #相依性套件輸出

## 安裝Django

py -m pip install --upgrade pip # 升級pip套件
pip install Django~=3.2.0 # 會自動將其他相依性套件下載下來

## 建立專案

django-admin startproject Django3_learning

## 建立資料庫

py manage.py migrate

## 建立超級使用者

py manage.py createsuperuser

## 啟動伺服器

py manage.py runserver localhost:8000







