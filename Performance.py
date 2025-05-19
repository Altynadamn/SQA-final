from locust import HttpUser, task, between, constant_pacing
import random
import string

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"
]

def random_text(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class BaseStackOverflowUser(HttpUser):
    abstract = True
    host = "https://api.stackexchange.com/2.3"
    headers = {}

    def on_start(self):
        self.headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _ua_label(self):
        return self.headers["User-Agent"].split()[0]

class ReadUser(BaseStackOverflowUser):
    wait_time = between(2, 5)

    @task(3)
    def list_questions(self):
        self.client.get(
            "/questions?order=desc&sort=activity&site=stackoverflow",
            headers=self.headers,
            name=f"GET /questions [{self._ua_label()}]"
        )

    @task(1)
    def search_questions(self):
        query = random_text(5)
        self.client.get(
            f"/search/advanced?q={query}&site=stackoverflow",
            headers=self.headers,
            name=f"GET /search/advanced [{self._ua_label()}]"
        )

class MixedUser(BaseStackOverflowUser):
    wait_time = constant_pacing(5)

    @task(2)
    def browse_and_search(self):
        self.client.get(
            "/questions?order=desc&sort=activity&site=stackoverflow",
            headers=self.headers,
            name=f"GET /questions [{self._ua_label()}]"
        )
        query = random_text(5)
        self.client.get(
            f"/search/advanced?q={query}&site=stackoverflow",
            headers=self.headers,
            name=f"GET /search/advanced [{self._ua_label()}]"
        )

    @task(1)
    def get_question_details(self):
        # Simulate fetching a specific question
        question_id = random.randint(1, 1000000)  # Random question ID
        self.client.get(
            f"/questions/{question_id}?site=stackoverflow&filter=withbody",
            headers=self.headers,
            name=f"GET /questions/[id] [{self._ua_label()}]"
        )