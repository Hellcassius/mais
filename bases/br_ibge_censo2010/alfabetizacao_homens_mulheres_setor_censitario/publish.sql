/*

Query para publicar a tabela.

Esse é o lugar para:
    - modificar nomes, ordem e tipos de colunas
    - dar join com outras tabelas
    - criar colunas extras (e.g. logs, proporções, etc.)

Qualquer coluna definida aqui deve também existir em `table_config.yaml`.

# Além disso, sinta-se à vontade para alterar alguns nomes obscuros
# para algo um pouco mais explícito.

TIPOS:
    - Para modificar tipos de colunas, basta substituir STRING por outro tipo válido.
    - Exemplo: `SAFE_CAST(column_name AS NUMERIC) column_name`
    - Mais detalhes: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types

*/
SELECT 
SAFE_CAST(cod_setor AS STRING) cod_setor,
SAFE_CAST(situacao_setor AS STRING) situacao_setor,
SAFE_CAST(sigla_uf AS STRING) sigla_uf,
SAFE_CAST(v086 AS STRING) v086,
SAFE_CAST(v087 AS STRING) v087,
SAFE_CAST(v088 AS STRING) v088,
SAFE_CAST(v089 AS STRING) v089,
SAFE_CAST(v090 AS STRING) v090,
SAFE_CAST(v091 AS STRING) v091,
SAFE_CAST(v092 AS STRING) v092,
SAFE_CAST(v093 AS STRING) v093,
SAFE_CAST(v094 AS STRING) v094,
SAFE_CAST(v095 AS STRING) v095,
SAFE_CAST(v096 AS STRING) v096,
SAFE_CAST(v097 AS STRING) v097,
SAFE_CAST(v098 AS STRING) v098,
SAFE_CAST(v099 AS STRING) v099,
SAFE_CAST(v100 AS STRING) v100,
SAFE_CAST(v101 AS STRING) v101,
SAFE_CAST(v102 AS STRING) v102,
SAFE_CAST(v103 AS STRING) v103,
SAFE_CAST(v104 AS STRING) v104,
SAFE_CAST(v105 AS STRING) v105,
SAFE_CAST(v106 AS STRING) v106,
SAFE_CAST(v107 AS STRING) v107,
SAFE_CAST(v108 AS STRING) v108,
SAFE_CAST(v109 AS STRING) v109,
SAFE_CAST(v110 AS STRING) v110,
SAFE_CAST(v111 AS STRING) v111,
SAFE_CAST(v112 AS STRING) v112,
SAFE_CAST(v113 AS STRING) v113,
SAFE_CAST(v114 AS STRING) v114,
SAFE_CAST(v115 AS STRING) v115,
SAFE_CAST(v116 AS STRING) v116,
SAFE_CAST(v117 AS STRING) v117,
SAFE_CAST(v118 AS STRING) v118,
SAFE_CAST(v119 AS STRING) v119,
SAFE_CAST(v120 AS STRING) v120,
SAFE_CAST(v121 AS STRING) v121,
SAFE_CAST(v122 AS STRING) v122,
SAFE_CAST(v123 AS STRING) v123,
SAFE_CAST(v124 AS STRING) v124,
SAFE_CAST(v125 AS STRING) v125,
SAFE_CAST(v126 AS STRING) v126,
SAFE_CAST(v127 AS STRING) v127,
SAFE_CAST(v128 AS STRING) v128,
SAFE_CAST(v129 AS STRING) v129,
SAFE_CAST(v130 AS STRING) v130,
SAFE_CAST(v131 AS STRING) v131,
SAFE_CAST(v132 AS STRING) v132,
SAFE_CAST(v133 AS STRING) v133,
SAFE_CAST(v134 AS STRING) v134,
SAFE_CAST(v135 AS STRING) v135,
SAFE_CAST(v136 AS STRING) v136,
SAFE_CAST(v137 AS STRING) v137,
SAFE_CAST(v138 AS STRING) v138,
SAFE_CAST(v139 AS STRING) v139,
SAFE_CAST(v140 AS STRING) v140,
SAFE_CAST(v141 AS STRING) v141,
SAFE_CAST(v142 AS STRING) v142,
SAFE_CAST(v143 AS STRING) v143,
SAFE_CAST(v144 AS STRING) v144,
SAFE_CAST(v145 AS STRING) v145,
SAFE_CAST(v146 AS STRING) v146,
SAFE_CAST(v147 AS STRING) v147,
SAFE_CAST(v148 AS STRING) v148,
SAFE_CAST(v149 AS STRING) v149,
SAFE_CAST(v150 AS STRING) v150,
SAFE_CAST(v151 AS STRING) v151,
SAFE_CAST(v152 AS STRING) v152,
SAFE_CAST(v153 AS STRING) v153,
SAFE_CAST(v154 AS STRING) v154,
SAFE_CAST(v155 AS STRING) v155,
SAFE_CAST(v156 AS STRING) v156,
SAFE_CAST(v157 AS STRING) v157,
SAFE_CAST(v158 AS STRING) v158,
SAFE_CAST(v159 AS STRING) v159,
SAFE_CAST(v160 AS STRING) v160,
SAFE_CAST(v161 AS STRING) v161,
SAFE_CAST(v162 AS STRING) v162,
SAFE_CAST(v163 AS STRING) v163,
SAFE_CAST(v164 AS STRING) v164,
SAFE_CAST(v165 AS STRING) v165,
SAFE_CAST(v166 AS STRING) v166,
SAFE_CAST(v167 AS STRING) v167,
SAFE_CAST(v168 AS STRING) v168,
SAFE_CAST(v169 AS STRING) v169,
SAFE_CAST(v170 AS STRING) v170,
SAFE_CAST(v171 AS STRING) v171,
SAFE_CAST(v172 AS STRING) v172,
SAFE_CAST(v173 AS STRING) v173,
SAFE_CAST(v174 AS STRING) v174,
SAFE_CAST(v175 AS STRING) v175,
SAFE_CAST(v176 AS STRING) v176,
SAFE_CAST(v177 AS STRING) v177,
SAFE_CAST(v178 AS STRING) v178,
SAFE_CAST(v179 AS STRING) v179,
SAFE_CAST(v180 AS STRING) v180,
SAFE_CAST(v181 AS STRING) v181,
SAFE_CAST(v182 AS STRING) v182,
SAFE_CAST(v183 AS STRING) v183,
SAFE_CAST(v184 AS STRING) v184,
SAFE_CAST(v185 AS STRING) v185,
SAFE_CAST(v186 AS STRING) v186,
SAFE_CAST(v187 AS STRING) v187,
SAFE_CAST(v188 AS STRING) v188,
SAFE_CAST(v189 AS STRING) v189,
SAFE_CAST(v190 AS STRING) v190,
SAFE_CAST(v191 AS STRING) v191,
SAFE_CAST(v192 AS STRING) v192,
SAFE_CAST(v193 AS STRING) v193,
SAFE_CAST(v194 AS STRING) v194,
SAFE_CAST(v195 AS STRING) v195,
SAFE_CAST(v196 AS STRING) v196,
SAFE_CAST(v197 AS STRING) v197,
SAFE_CAST(v198 AS STRING) v198,
SAFE_CAST(v199 AS STRING) v199,
SAFE_CAST(v200 AS STRING) v200,
SAFE_CAST(v201 AS STRING) v201,
SAFE_CAST(v202 AS STRING) v202,
SAFE_CAST(v203 AS STRING) v203,
SAFE_CAST(v204 AS STRING) v204,
SAFE_CAST(v205 AS STRING) v205,
SAFE_CAST(v206 AS STRING) v206,
SAFE_CAST(v207 AS STRING) v207,
SAFE_CAST(v208 AS STRING) v208,
SAFE_CAST(v209 AS STRING) v209,
SAFE_CAST(v210 AS STRING) v210,
SAFE_CAST(v211 AS STRING) v211,
SAFE_CAST(v212 AS STRING) v212,
SAFE_CAST(v213 AS STRING) v213,
SAFE_CAST(v214 AS STRING) v214,
SAFE_CAST(v215 AS STRING) v215,
SAFE_CAST(v216 AS STRING) v216,
SAFE_CAST(v217 AS STRING) v217,
SAFE_CAST(v218 AS STRING) v218,
SAFE_CAST(v219 AS STRING) v219,
SAFE_CAST(v220 AS STRING) v220,
SAFE_CAST(v221 AS STRING) v221,
SAFE_CAST(v222 AS STRING) v222,
SAFE_CAST(v223 AS STRING) v223,
SAFE_CAST(v224 AS STRING) v224,
SAFE_CAST(v225 AS STRING) v225,
SAFE_CAST(v226 AS STRING) v226,
SAFE_CAST(v227 AS STRING) v227,
SAFE_CAST(v228 AS STRING) v228,
SAFE_CAST(v229 AS STRING) v229,
SAFE_CAST(v230 AS STRING) v230,
SAFE_CAST(v231 AS STRING) v231,
SAFE_CAST(v232 AS STRING) v232,
SAFE_CAST(v233 AS STRING) v233,
SAFE_CAST(v234 AS STRING) v234,
SAFE_CAST(v235 AS STRING) v235,
SAFE_CAST(v236 AS STRING) v236,
SAFE_CAST(v237 AS STRING) v237,
SAFE_CAST(v238 AS STRING) v238,
SAFE_CAST(v239 AS STRING) v239,
SAFE_CAST(v240 AS STRING) v240,
SAFE_CAST(v241 AS STRING) v241,
SAFE_CAST(v242 AS STRING) v242,
SAFE_CAST(v243 AS STRING) v243,
SAFE_CAST(v244 AS STRING) v244,
SAFE_CAST(v245 AS STRING) v245,
SAFE_CAST(v246 AS STRING) v246,
SAFE_CAST(v247 AS STRING) v247,
SAFE_CAST(v248 AS STRING) v248,
SAFE_CAST(v249 AS STRING) v249,
SAFE_CAST(v250 AS STRING) v250,
SAFE_CAST(v251 AS STRING) v251,
SAFE_CAST(v252 AS STRING) v252,
SAFE_CAST(v253 AS STRING) v253,
SAFE_CAST(v254 AS STRING) v254,
SAFE_CAST(v255 AS STRING) v255
from basedosdados-staging.br_ibge_censo2010_staging.alfabetizacao_homens_mulheres_setor_censitario as t
