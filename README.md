# AgriScan App

AgriScan est une application mobile destinée à l'analyse de plantes à partir d'une photo. Ce dépôt contient une application Expo/React Native et une API FastAPI minimale.

## Aperçu

- **Frontend** : application multiplateforme React Native, Expo et Expo Router
- **Backend** : API FastAPI avec endpoint de diagnostic
- **Plateformes prises en charge** : Android, iOS et web
- **Langages** : TypeScript, JavaScript et Python

> Le backend renvoie actuellement une réponse de démonstration (`plant_healthy`) avec une confiance fixée à `0.83`. L'intégration d'un véritable modèle IA reste à implémenter.

## Structure du projet

```text
agriscan-app/
├── agriscan-app-front/    # Application Expo/React Native
│   ├── app/               # Routes et écrans
│   ├── components/        # Composants réutilisables
│   ├── constants/         # Constantes de l'application
│   ├── hooks/             # Hooks React personnalisés
│   └── assets/            # Images et ressources
└── agriscan-app-backend/  # API FastAPI
    ├── main.py            # Endpoints de l'API
    └── fiable.jpg         # Ressource d'exemple
```

## Prérequis

- Node.js et npm
- Expo CLI via `npx` (aucune installation globale nécessaire)
- Python 3.10 ou supérieur
- Android Studio, un émulateur iOS ou Expo Go pour tester l'application mobile

## Installation

### Backend

Depuis la racine du dépôt :

```bash
cd agriscan-app-backend
python -m venv .venv
```

Activez l'environnement virtuel :

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Installez les dépendances nécessaires :

```bash
pip install fastapi uvicorn python-multipart pillow
```

Lancez l'API :

```bash
uvicorn main:app --reload
```

L'API sera disponible sur `http://127.0.0.1:8000`.

### Frontend

Dans un autre terminal :

```bash
cd agriscan-app-front
npm install
npm start
```

Vous pouvez aussi lancer directement une plateforme :

```bash
npm run android
npm run ios
npm run web
```

## API

### Vérifier l'état du service

```http
GET /
```

Réponse :

```json
{
  "ok": true,
  "service": "AgriScan API"
}
```

### Analyser une image

```http
POST /diagnose
Content-Type: multipart/form-data
```

Champ attendu : `image`.

Exemple avec cURL :

```bash
curl -X POST \
  -F "image=@chemin/vers/image.jpg" \
  http://127.0.0.1:8000/diagnose
```

Réponse actuelle :

```json
{
  "diagnosis": "plant_healthy",
  "confidence": 0.83
}
```

## Scripts frontend

| Commande | Description |
|---|---|
| `npm start` | Lance Expo |
| `npm run android` | Lance l'application Android |
| `npm run ios` | Lance l'application iOS |
| `npm run web` | Lance la version web |
| `npm run lint` | Vérifie le code avec ESLint |
| `npm run reset-project` | Réinitialise le projet Expo avec un modèle vierge |

## Développement

- Lancer le backend sur le port `8000`.
- Mettre à jour la configuration réseau du frontend afin qu'elle pointe vers l'adresse du backend depuis l'émulateur ou l'appareil physique.
- Remplacer la réponse simulée de `/diagnose` par l'inférence d'un modèle IA réel.
- Ajouter les dépendances Python dans un fichier `requirements.txt` pour faciliter l'installation.

## Licence

Aucune licence n'est actuellement définie pour ce projet.