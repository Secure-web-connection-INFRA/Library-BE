# Lib API Documentation

List all the api regarding the book and also contain the access role change api but only allowed for ADMIN user and allows upload of book

## All-lib

**Method:** `GET`

**URL:** `localhost:5000/lib/`

**Response:**

```json
{
  "data": [
    {
      "author": "Chetan Bhagat",
      "description": "Coming from two very different cultural backgrounds, Krish and Ananya try to convince their parents to bless their relationship before they get married.",
      "id": "b123",
      "image": "base64Coverimage"
    }
  ]
}
```

## Search

**Method:** `GET`

**URL:** `localhost:5000/lib/search?book=2 states`

**Response:**

```json
{
  "author": "Chetan Bhagat",
  "description": "Coming from two very different cultural backgrounds, Krish and Ananya try to convince their parents to bless their relationship before they get married.",
  "id": "b123",
  "image": "base64Coverimage"
}
```

## Download

**Method:** `GET`

**URL:** `localhost:5000/lib/download?bookId=b123`

**Body:**

```json
{
  "bookdID": "b123"
}
```

**Response:**

```json
{
  "author": "Chetan Bhagat",
  "description": "Coming from two very different cultural backgrounds, Krish and Ananya try to convince their parents to bless their relationship before they get married.",
  "id": "b123",
  "file": "base64Pdf",
  "key": "publicKey of digital signature",
  "publishedOn": "2014",
  "title": "2 states"
}
```

## Role

**Method:** `GET`

**Response:**

```
Successfully updates
```

## Upload

**Method:** `POST`

**URL:** `localhost:5000/lib/upload`

**Body:**

```json
{
  "pdfBase64": "pdfBase64 book",
  "coverBase64": "coverBase64 book",
  "author": "Aswin",
  "title": "try",
  "description": "wasdcafdsfas",
  "publishedOn": "2024-06-28"
}
```

**Response:**

```
Successfully uploaded
```
