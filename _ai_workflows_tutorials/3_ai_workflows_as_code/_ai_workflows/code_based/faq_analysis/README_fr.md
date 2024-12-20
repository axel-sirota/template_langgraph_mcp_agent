# Analyse de FAQ : deux façons de travailler avec l'IA 🚀

Vous vous demandez comment rendre vos workflows IA plus puissants ? Cet exemple montre deux façons d'analyser et d'améliorer les FAQs :
1. En utilisant des instructions textuelles avec un assistant IA
2. En utilisant du code structuré qui s'exécute de façon autonome

## Ce que fait cet exemple 🎯

Prend une FAQ existante et l'améliore en :
- trouvant les questions sans réponse
- analysant ce qui manque
- suggérant de nouvelles réponses
- créant un rapport d'amélioration complet

## Essayez les deux approches 🤝

### 1. Version texte : rapide et interactive
Parfaite pour l'exploration et les itérations rapides.

```
_text/
├── run.md         # Quoi exécuter
├── instructions/  # Quoi faire
└── _output/       # Où vont les résultats
```

**Pour essayer :**
1. Ouvrez votre assistant IA
2. Copiez le contenu de `_text/run.md`
3. Regardez l'IA travailler sur les tâches
4. Discutez et affinez si nécessaire

### 2. Version code : structurée et indépendante
Parfaite pour l'automatisation et plus de contrôle.

```
_code/
├── run.py             # Exécuteur Python
├── instructions.yaml  # Tâches structurées
├── config.yaml        # Paramètres IA
└── _output/           # Où vont les résultats
```

**Pour essayer :**
```bash
cd _code
python run.py
```

## Comparez les résultats 📊

Les deux versions créent ces fichiers dans `_output/` :
1. `1_existing_faq.md` : ce qui est dans la FAQ actuelle
2. `2_questions_analysis.md` : ce qui manque
3. `3_suggestions.md` : propositions de nouvelles réponses
4. `4_report.md` : analyse complète

## Quand utiliser chaque approche 🤔

### La version texte est idéale quand vous :
- voulez expérimenter rapidement
- devez discuter des idées avec l'IA
- voulez affiner les choses de façon interactive
- n'avez pas besoin d'automatisation

### La version code est meilleure quand vous :
- voulez exécuter les choses automatiquement
- avez besoin de plus de contrôle sur le processus
- voulez intégrer avec d'autres outils
- voulez l'indépendance des assistants IA

## Comment créer le vôtre 🛠️

### Commencez par le texte
1. Regardez `_text/instructions/instructions_v1.0.0.md`
2. Voyez comment les tâches sont décrites en langage naturel
3. Notez comment les sorties sont clairement spécifiées

### Passez au code quand vous êtes prêt
1. Consultez `_code/instructions.yaml`
2. Voyez comment les mêmes tâches sont structurées
3. Notez comment les entrées et sorties sont explicites

---

<div align="center">
  <sub>Créé avec ❤️ par AI Swiss</sub>
</div>
