
# side effects
def get_holidays():
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')

    if r.status_code == 200:
        return r.json()
    
    return None



class MockedResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return [
            {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
            },
            {
                "userId": 1,
                "id": 2,
                "title": "quis ut nam facilis et officia qui",
                "completed": False
            }
        ]


# replace requests with folllowing object
class MockedRequests:
    def __init__(self):
        pass
    
    @staticmethod
    def get(url):
        return MockedResponse()


requests = MockedRequests


resp = get_holidays()

assert resp is not None, "get_holidays() returns empty response"

# check correct json output

