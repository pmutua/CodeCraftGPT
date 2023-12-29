class Config:
    API_KEY = None  # Placeholder for the API key, initially set to None

    @classmethod
    def set_api_key(cls, api_key):
        cls.API_KEY = api_key

    @classmethod
    def get_api_key(cls):
        return cls.API_KEY
