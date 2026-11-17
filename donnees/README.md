# donnees/

Données d'exemple suivies par git. **Aucune donnée réelle d'étudiant** : uniquement le bac à sable Moodle
(un étudiant fictif, « Sam Student ») et des promotions fictives générées par `scripts/diagforge/outils/promotion_fictive.py`.

## diagforge/ — exports Moodle pour DiagForge (bilan des résultats)

| Dossier | Contenu | Pour tester |
| --- | --- | --- |
| `bac_a_sable/1_avant_correction/` | Notes et Réponses (sans texte de question), avant correction des questions ouvertes ; export XML des 10 questions | copies « à corriger » |
| `bac_a_sable/2_apres_correction/` | Notes après correction | notes complètes |
| `bac_a_sable/3_reponses_completes/` | Réponses avec texte de la question et bonne réponse ; export Statistiques (interrompu par une erreur Moodle) | questions tirées au hasard, comparaison avec Moodle |
| `promotion_fictive/` | 60 étudiants fictifs, un test, export en français ; `verite.txt` : cas plantés | indicateurs, alertes |
| `promotion_groupes/` | 60 étudiants fictifs, deux tests (Quizz1_SMA, Quizz1_SMB), `roster.csv`, XML avec tags de thème | groupes, réussite par thème |

```
python scripts/diagforge/diagforge.py donnees/diagforge/promotion_groupes -p Ecole1
python scripts/diagforge/diagforge.py donnees/diagforge/bac_a_sable/3_reponses_completes donnees/diagforge/bac_a_sable/2_apres_correction -q donnees/diagforge/bac_a_sable/1_avant_correction
```

Les sorties du bilan (`bilan_*.xlsx`, `*_fiche_prof.html`, `*_images/`) sont générées à côté des exports et ne sont pas suivies.
