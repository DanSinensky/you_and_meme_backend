# You & Meme

## A Social Media App

---

### Quicklinks

- [Frontend Repository](link to frontend GitHub goes here)
- [Deployed App](link to Heroku deployed app goes here)

### Description

- What do you meme? This social media app is fun for everyone! Scroll through hundreds of memes and add your unique comments to them. Or upload your own meme and get your friends to make comments. Who can come up with the most original meme? You or me? It's You & Meme!

### Features

- User Authentication
- Post memes
- Comment on memes
- Like memes

### Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL

### Setup & Install

Prerequisites:<br>

- Python3
- pip
- virtualenvwrapper

Steps<br>

1. Clone this repository

```
git clone https://github.com/YourRepo/You-and-Meme-Backend.git
```

2. Navigate to the project directory

```
cd You-and-Meme-Backend
```

3. Create the virtual environment

```
virtualenv you_and_meme_backend
```

4. If you've just created the virtual environment, it should be activated by default. If not, activate it

```
workon you_and_meme_backend
```

5. Install the dependencies

```
pip install -r requirements.txt
```

6. Run migrations

```
python manage.py migrate
```

7. Create a superuser for the Django admin panel

```
python manage.py createsuperuser
```

8. Run the server

```
python manage.py runserver
```

### Data Models

#### User

- `username`: CharField (max_length=100)
- `email`: EmailField (max_length=100)
- `password`: CharField (max_length=100)

#### Post

- `user`: ForeignKey (User)
- `meme`: TextField
- `likes`: IntegerField (default=0)

#### Comment

- `user`: ForeignKey (User)
- `post`: ForeignKey (Post)
- `body`: TextField

### API Endpoints

- Using Django REST Framework's 'ModelViewSet,' each model is automatically outfitted with CRUD endpoints.

### API Endpoints

| Resource | Method | Endpoint              | Description                |
| -------- | ------ | --------------------- | -------------------------- |
| Users    | GET    | `/api/users/`         | List all users             |
|          | GET    | `/api/users/{id}/`    | Retrieve a single user     |
|          | POST   | `/api/users/`         | Create a new user          |
|          | PUT    | `/api/users/{id}/`    | Update a user              |
|          | PATCH  | `/api/users/{id}/`    | Partially update a user    |
|          | DELETE | `/api/users/{id}/`    | Delete a user              |
| Posts    | GET    | `/api/posts/`         | List all posts             |
|          | GET    | `/api/posts/{id}/`    | Retrieve a single post     |
|          | POST   | `/api/posts/`         | Create a new post          |
|          | PUT    | `/api/posts/{id}/`    | Update a post              |
|          | PATCH  | `/api/posts/{id}/`    | Partially update a post    |
|          | DELETE | `/api/posts/{id}/`    | Delete a post              |
| Comments | GET    | `/api/comments/`      | List all comments          |
|          | GET    | `/api/comments/{id}/` | Retrieve a single comment  |
|          | POST   | `/api/comments/`      | Create a new comment       |
|          | PUT    | `/api/comments/{id}/` | Update a comment           |
|          | PATCH  | `/api/comments/{id}/` | Partially update a comment |
|          | DELETE | `/api/comments/{id}/` | Delete a comment           |

---

#### Contact

- Contributors to this project include: <br>
  [Dan Sinesky](https://www.linkedin.com/in/dansinensky/) | [Manfred Joa](https://www.linkedin.com/in/manfredjoa/) | [Rebekah Gomez](https://www.linkedin.com/in/rebekah-gomez/) | [Alan Malpartida](Alan's LinkedIn) | [Danish Mansoor](https://www.linkedin.com/in/danishhhm/) | [Kyle Harris](https://www.linkedin.com/in/kyleharris007/)
- Please reach out to us via LinkedIn
