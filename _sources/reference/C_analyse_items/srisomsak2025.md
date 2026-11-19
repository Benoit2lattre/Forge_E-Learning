---
cle: srisomsak2025
reference: "Srisomsak, V., Sitticharoon, C., Keadkraichaiwat, I., Meethes, S. et Inpaen, I. (2026). Detection of flawed multiple-choice questions in preclinical medical education using item difficulty and discrimination indices: A six-year analysis. BMC Medical Education, 26, article 92."
doi: 10.1186/s12909-025-08204-5
axe: [C1]
type_etude: étude rétrospective des corrections d'items sur six ans (236 examens, 14 238 QCM)
public: examens de QCM à 5 options des deux premières années de médecine (faculté de médecine Siriraj, université Mahidol, Thaïlande)
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "signaler en priorité les questions où la réponse attendue n'est pas la plus choisie, ou est choisie autant qu'une autre option : clé erronée ou plusieurs bonnes réponses possibles"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "traiter les seuils (réussite faible, discrimination négative) comme des alertes à vérifier par l'enseignant, pas comme un verdict automatique : ils manquent une partie des questions défectueuses"
    niveau: C
    transferabilite: forte
---

# Seuils statistiques et questions défectueuses (Srisomsak et al., 2025)

Srisomsak, V., Sitticharoon, C., Keadkraichaiwat, I., Meethes, S. et Inpaen, I. (2026). Detection of flawed multiple-choice questions in preclinical medical education using item difficulty and discrimination indices: A six-year analysis. *BMC Medical Education*, 26, article 92. [DOI](https://doi.org/10.1186/s12909-025-08204-5)

**En une phrase.** Sur six ans d'examens de médecine (14 238 QCM), 81 questions ont dû être corrigées, surtout pour plusieurs bonnes réponses ou une clé fausse ; les seuils « réussite < 0,25 ou point-bisériale < 0 » en repèrent 86 %, mais en manquent 14 %, que la répartition des réponses aurait permis de voir.

## La source

| | |
| --- | --- |
| **Équipe** | Département de physiologie et service d'éducation médicale, faculté de médecine Siriraj (université Mahidol, Bangkok). |
| **Nature** | Académique ; fonds de recherche en éducation médicale de la faculté (p. 13). |
| **Support** | *BMC Medical Education* (Springer Nature), libre accès ; publié en ligne fin 2025. |
| **Audience** | 3 citations (OpenAlex, 08/11/2026) ; article récent. |
| **Reproductibilité** | Moyenne : procédure et formules décrites (p. 3-4) ; données sur demande. Pages du fichier PDF. |

## Ce que fait l'étude

- **Données** (p. 3-4) : examens informatisés de 32 cours de première et deuxième années, 2017 à 2022.
- **Procédure de l'établissement** (p. 4) : signalement automatique si réussite < 0,25 et/ou point-bisériale < 0 ; relecture de toutes les questions, en particulier quand la bonne réponse n'est pas l'option la plus choisie ou quand plusieurs options ont des taux proches ; correction validée par le responsable du cours.
- **Analyses** : causes des corrections, indicateurs des questions corrigées et non corrigées (détail pour 2022), part des questions corrigées que les seuils auraient repérées.

## Résultats

- **Fréquence** (p. 5) : 59 examens sur 236 (25 %) ont au moins une correction ; 81 questions sur 14 238 (0,6 %).
- **Causes** : plusieurs bonnes réponses 47 %, clé fausse 41 %, points donnés à tous 7 %, suppression 5 %.
- **Seuils** (p. 11-12) : la réussite < 0,25 repère environ 80 % des questions corrigées, la point-bisériale < 0 environ 50 %, les deux réunies 86 % ; 14 % des questions corrigées passent les deux seuils.
- **Profil** : questions corrigées plus difficiles et moins discriminantes ; avec une clé fausse, la vraie réponse est plus choisie et discrimine mieux que la réponse attendue ; avec plusieurs bonnes réponses, la discrimination de la réponse attendue peut sembler normale (p. 12).
- **Recommandation** (p. 13) : signaler aussi les questions où la réponse attendue a un taux de choix égal ou inférieur à une autre option.

## Avis critique

**Apport.** Montre que les erreurs les plus fréquentes dans un examen réel sont des erreurs de clé ou de bonnes réponses multiples, et qu'elles se voient mieux dans la répartition des réponses que dans les seuils.

**Points forts**
- Grand corpus réel sur six ans, causes vérifiées par les responsables de cours.
- Analyse option par option des questions corrigées.

**Réserves**
1. **Importante** — Les questions défectueuses ne sont connues que si la procédure les a trouvées : le taux de 14 % manquées est une borne basse, le vrai taux de détection est inconnu.
2. **Importante** — Point-bisériale incluant l'item, seuils fixes ; une seule faculté de médecine.
3. **Mineure** — Données détaillées des questions non corrigées pour une seule année.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les seuils seuls manquent une partie des questions défectueuses | C | Un établissement, détection non indépendante |
| Une réponse attendue moins choisie qu'une autre option signale une clé fausse ou plusieurs bonnes réponses | C | Différences nettes sur les questions corrigées |

**Transférabilité** : forte. Le mécanisme (erreur de clé, deux options justes) est le même pour des QCM de mécanique.

**Pour conclure, il faudrait** relire toutes les questions d'une année de quiz et compter combien de défauts DiagForge aurait signalés.

## Pour Forge

- **DiagForge** : alerte « réponse attendue moins choisie (ou autant choisie) qu'une autre option » en tête de liste (niveau C ; DiagForge signale déjà « réponse fausse plus choisie que la bonne »).
- **DiagForge** : présenter les alertes comme des points à vérifier par l'enseignant (niveau C ; voir Moore et al., 2023).
