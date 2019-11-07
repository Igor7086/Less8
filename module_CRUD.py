import requests


class CRUD:
    host = 'http://pulse-rest-testing.herokuapp.com/'
    book_url = 'books'

    def create_book(self, body):
        book_response = requests.post(url=self.host + self.book_url, data=body)
        return book_response

    def get_book(self, book_id):
        book_response = requests.get(url=self.host + self.book_url + '/' + str(book_id))
        return book_response

    def update_book(self, book_id, body_updated_book):
        updated_book_response = requests.put(url=self.host + self.book_url + '/' + str(book_id),
                                             data=body_updated_book)
        return updated_book_response

    def delete_book(self, book_id):
        deleted_book_response = requests.delete(url=self.host + self.book_url + '/' + str(book_id))
        return deleted_book_response
