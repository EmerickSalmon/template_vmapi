class VCenterClient:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def __enter__(self):
        # Initialisez et connectez-vous ici
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Gérez la déconnexion ici
        self.disconnect()

    def connect(self):
        # Logique de connexion
        pass

    def disconnect(self):
        # Logique de déconnexion
        pass