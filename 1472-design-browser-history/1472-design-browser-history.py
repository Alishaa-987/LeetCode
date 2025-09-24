class Browser:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Browser(homepage)

    def visit(self, url: str) -> None:
        newBrowser = Browser(url)
        newBrowser.prev = self.head
        self.head.next = newBrowser
        self.head = self.head.next

    def back(self, steps: int) -> str:
        count = 0

        while self.head.prev and count < steps:
            self.head = self.head.prev
            count += 1
	
        return self.head.url

    def forward(self, steps: int) -> str:
        count = 0

        while self.head.next and count < steps:
            self.head = self.head.next
            count += 1
        
        return self.head.url