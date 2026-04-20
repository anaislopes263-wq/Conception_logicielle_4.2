"""
Pattern de création:Singleton + pattern de comportement: Observer 

ScolariteManager :
  - Singleton : une seule instance dans toute l'application.
  - Observer  : implémente mise_a_jour() appelé automatiquement
                par un Etudiant quand sa moyenne change.
"""


class ScolariteManager:
    """
    Gestionnaire central de la scolarité.
    Unique instance garantie par le pattern Singleton.
    """

    _instance = None   # attribut de classe qui stocke l'unique instance

    def __new__(cls):
        """Surcharge de __new__ pour garantir l'unicité de l'instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialiser()
        return cls._instance

    def __initialiser(self):
        """Initialisation des données internes (appelée une seule fois)."""
        self.__etudiants = []
        self.__statistiques = {}   # {numero_etudiant: moyenne}

    # ------------------------------------------------------------------ #
    #  Gestion des étudiants                                               #
    # ------------------------------------------------------------------ #

    def inscrire_etudiant(self, etudiant):
        """Inscrit un étudiant et l'abonne automatiquement aux notifications."""
        if etudiant not in self.__etudiants:
            self.__etudiants.append(etudiant)
            self.__statistiques[etudiant.numero_etudiant] = etudiant.moyenne
            etudiant.abonner(self)   # l'étudiant nous notifiera à chaque note

    def retirer_etudiant(self, etudiant):
        """Retire un étudiant de la liste."""
        if etudiant in self.__etudiants:
            self.__etudiants.remove(etudiant)
            etudiant.desabonner(self)
            self.__statistiques.pop(etudiant.numero_etudiant, None)

    @property
    def etudiants(self):
        return list(self.__etudiants)

    # ------------------------------------------------------------------ #
    #  Pattern Observer — mise à jour                                      #
    # ------------------------------------------------------------------ #

    def mise_a_jour(self, etudiant):
        """
        Appelé automatiquement par un Etudiant lors de l'ajout d'une note.
        Met à jour les statistiques globales.
        """
        self.__statistiques[etudiant.numero_etudiant] = etudiant.moyenne
        print(
            f"  [ScolariteManager] Mise à jour : {etudiant.nom} "
            f"→ nouvelle moyenne = {etudiant.moyenne:.2f}/20"
        )

    # ------------------------------------------------------------------ #
    #  Statistiques                                                        #
    # ------------------------------------------------------------------ #

    def afficher_statistiques(self):
        """Affiche les statistiques globales de tous les étudiants inscrits."""
        if not self.__statistiques:
            print("Aucun étudiant inscrit.")
            return
        print("Statistiques globales :")
        for num, moy in self.__statistiques.items():
            print(f"  {num} → {moy:.2f}/20")
        moyennes = list(self.__statistiques.values())
        print(f"  Moyenne générale : {sum(moyennes)/len(moyennes):.2f}/20")

    def __str__(self):
        return f"ScolariteManager ({len(self.__etudiants)} étudiant(s) inscrit(s))"
