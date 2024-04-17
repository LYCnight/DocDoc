import queue

class Content_Queue:
    def __init__(self, headline_list):
        self.queue = queue.Queue()
        for headline in headline_list:
            self.queue.put(headline)

    def top(self):
        """
        获取队列头部元素
        """
        try:
            # 获取队列头部元素
            headline = self.queue.queue[0]
            return headline
        except IndexError:
            print("Queue is empty")
            return None

    def pop(self):
        """
        获取并弹出头部元素
        """
        try:
            headline = self.queue.get_nowait()
            return headline
        except queue.Empty:
            print("Queue is empty")
            return None

    def empty(self):
        return self.queue.empty()

    def push(self, headline):
        self.queue.put(headline)

