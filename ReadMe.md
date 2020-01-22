# Data Collection App

A base app for images and videos data collection.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Clone the repo

```
git clone https://github.com/faizankarim/Data_Collection_Web_App.git
```

install python requirements

```
pip install -r requirements
```


## Deployment

Pre commands django server
```
python manage.py makemigration
python manage.py migrate
```
Create Super User
```
python manage.py createsuper user
```
Run django server
```
python manage.py runserver
```

Client Side:
```
http://127.0.0.1:8000/dc/
```

Admin Side:
```
http://127.0.0.1:8000/admin/
```

## Built With

* [Python](https://www.python.org/) - Programming Language
* [Django](https://www.djangoproject.com/) - Web Framework

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Faizan Karim** - [Github](https://github.com/faizankarim)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
