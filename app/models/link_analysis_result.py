class LinkAnalysisResult:
    def __init__(self):
        self.total_links = 0
        self.http_links = 0
        self.https_links = 0
        self.mailto_links = 0
        self.tel_links = 0
        self.links_without_href = 0
        self.utm_links = 0