odoo.define('sp_pos_search.sp_pos_search', function (require) {
"use strict";

    var PosDB = require('point_of_sale.DB');

    PosDB.include({
        /**
        ** @Override
        ** retourne la chaine en remplacant les caracteres speciaux
        */
        _product_search_string: function(product){
            var self = this;
            var str = this._super(product);
            return this.accentsTidy(str);
        },
        /**
        ** Remplace tout les caracteres speciaux
        ** Attention, fonctionne qu'en utf-8
        ** @see https://stackoverflow.com/a/990922
        */
        accentsTidy: function(s){
            var r=s.toLowerCase();
            r = r.replace(new RegExp("[àáâãäå]", 'g'),"a");
            r = r.replace(new RegExp("æ", 'g'),"ae");
            r = r.replace(new RegExp("ç", 'g'),"c");
            r = r.replace(new RegExp("[èéêë]", 'g'),"e");
            r = r.replace(new RegExp("[ìíîï]", 'g'),"i");
            r = r.replace(new RegExp("ñ", 'g'),"n");
            r = r.replace(new RegExp("[òóôõö]", 'g'),"o");
            r = r.replace(new RegExp("œ", 'g'),"oe");
            r = r.replace(new RegExp("[ùúûü]", 'g'),"u");
            r = r.replace(new RegExp("[ýÿ]", 'g'),"y");
            return r;
        },
        /**
        ** @Override
        ** Recherche en remplacant les caracteres speciaux
        **/
        search_product_in_category: function(category_id, query){
            try {
                query = query.replace(/[\[\]\(\)\+\*\?\.\-\!\&\^\$\|\~\_\{\}\:\,\\\/]/g,'.');
                query = query.replace(/ /g,'.+');
                query = this.accentsTidy(query);
                var re = RegExp("([0-9]+):.*?"+query,"gi");
            }catch(e){
                return [];
            }
            var results = [];
            for(var i = 0; i < this.limit; i++){
                var r = re.exec(this.category_search_string[category_id]);
                if(r){
                    var id = Number(r[1]);
                    results.push(this.get_product_by_id(id));
                }else{
                    break;
                }
            }
            return results;
        },
    });
});
