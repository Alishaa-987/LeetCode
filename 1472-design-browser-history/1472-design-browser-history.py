class BrowserHistory:
    def __init__(self, homepage):
        # Step 1: start on homepage
        self.back_stack = []         # stores pages you can go back to
        self.forward_stack = []      # stores pages you can go forward to
        self.current = homepage      # your current page

    def visit(self, url):
        # Step 2: when visiting a new page
        self.back_stack.append(self.current)  # save current page for "back"
        self.current = url                    # move to new page
        self.forward_stack = []               # clear forward history

    def back(self, steps):
        # Step 3: move back in history
        while steps > 0 and self.back_stack:  # only go back if possible
            self.forward_stack.append(self.current)   # save current to forward stack
            self.current = self.back_stack.pop()      # go to last visited page
            steps -= 1
        return self.current

    def forward(self, steps):
        # Step 4: move forward in history
        while steps > 0 and self.forward_stack:  # only go forward if possible
            self.back_stack.append(self.current)      # save current to back stack
            self.current = self.forward_stack.pop()   # move to next page
            steps -= 1
        return self.current
