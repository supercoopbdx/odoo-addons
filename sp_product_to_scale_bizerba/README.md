# sp_product_to_scale_bizerba

Attention, ce module a été modifié afin de s'adapter aux besoins métiers de Supercoop.
Pour toute information, utilisez le support :
https://github.com/supercoopbdx/sp_product_to_scale_bizerba/issues

Attention, le first commit corrige un bug sur le module original:
Lorsque plusieurs logs avec images à envoyer, une seule image était uploadé sur le ftp.

Evolutions du module :
- Génération du fichier de touches (KEYS_xxxxxxx.CSV) pour la balance tactile
- Tri par ordre alphabétique les articles et réassigne automatiquement les n° de séquences en fonction du groupe de balance
- Ajoute le groupe "7. Aucun" permettant de retirer proprement l'article des balances
- Efface le n° de séquence lors de la désactivation d'un article ou si groupe = 7. Aucun
