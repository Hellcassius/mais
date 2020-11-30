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
SAFE_CAST(v001 AS STRING) v001,
SAFE_CAST(v002 AS STRING) v002,
SAFE_CAST(v003 AS STRING) v003,
SAFE_CAST(v004 AS STRING) v004,
SAFE_CAST(v005 AS STRING) v005,
SAFE_CAST(v006 AS STRING) v006,
SAFE_CAST(v007 AS STRING) v007,
SAFE_CAST(v008 AS STRING) v008,
SAFE_CAST(v009 AS STRING) v009,
SAFE_CAST(v010 AS STRING) v010,
SAFE_CAST(v011 AS STRING) v011,
SAFE_CAST(v012 AS STRING) v012,
SAFE_CAST(v013 AS STRING) v013,
SAFE_CAST(v014 AS STRING) v014,
SAFE_CAST(v015 AS STRING) v015,
SAFE_CAST(v016 AS STRING) v016,
SAFE_CAST(v017 AS STRING) v017,
SAFE_CAST(v018 AS STRING) v018,
SAFE_CAST(v019 AS STRING) v019,
SAFE_CAST(v020 AS STRING) v020,
SAFE_CAST(v021 AS STRING) v021,
SAFE_CAST(v022 AS STRING) v022,
SAFE_CAST(v023 AS STRING) v023,
SAFE_CAST(v024 AS STRING) v024,
SAFE_CAST(v025 AS STRING) v025,
SAFE_CAST(v026 AS STRING) v026,
SAFE_CAST(v027 AS STRING) v027,
SAFE_CAST(v028 AS STRING) v028,
SAFE_CAST(v029 AS STRING) v029,
SAFE_CAST(v030 AS STRING) v030,
SAFE_CAST(v031 AS STRING) v031,
SAFE_CAST(v032 AS STRING) v032,
SAFE_CAST(v033 AS STRING) v033,
SAFE_CAST(v034 AS STRING) v034,
SAFE_CAST(v035 AS STRING) v035,
SAFE_CAST(v036 AS STRING) v036,
SAFE_CAST(v037 AS STRING) v037,
SAFE_CAST(v038 AS STRING) v038,
SAFE_CAST(v039 AS STRING) v039,
SAFE_CAST(v040 AS STRING) v040,
SAFE_CAST(v041 AS STRING) v041,
SAFE_CAST(v042 AS STRING) v042,
SAFE_CAST(v043 AS STRING) v043,
SAFE_CAST(v044 AS STRING) v044,
SAFE_CAST(v045 AS STRING) v045,
SAFE_CAST(v046 AS STRING) v046,
SAFE_CAST(v047 AS STRING) v047,
SAFE_CAST(v048 AS STRING) v048,
SAFE_CAST(v049 AS STRING) v049,
SAFE_CAST(v050 AS STRING) v050,
SAFE_CAST(v051 AS STRING) v051,
SAFE_CAST(v052 AS STRING) v052,
SAFE_CAST(v053 AS STRING) v053,
SAFE_CAST(v054 AS STRING) v054,
SAFE_CAST(v055 AS STRING) v055,
SAFE_CAST(v056 AS STRING) v056,
SAFE_CAST(v057 AS STRING) v057,
SAFE_CAST(v058 AS STRING) v058,
SAFE_CAST(v059 AS STRING) v059,
SAFE_CAST(v060 AS STRING) v060,
SAFE_CAST(v061 AS STRING) v061,
SAFE_CAST(v062 AS STRING) v062,
SAFE_CAST(v063 AS STRING) v063,
SAFE_CAST(v064 AS STRING) v064,
SAFE_CAST(v065 AS STRING) v065,
SAFE_CAST(v066 AS STRING) v066,
SAFE_CAST(v067 AS STRING) v067,
SAFE_CAST(v068 AS STRING) v068,
SAFE_CAST(v069 AS STRING) v069,
SAFE_CAST(v070 AS STRING) v070,
SAFE_CAST(v071 AS STRING) v071,
SAFE_CAST(v072 AS STRING) v072,
SAFE_CAST(v073 AS STRING) v073,
SAFE_CAST(v074 AS STRING) v074,
SAFE_CAST(v075 AS STRING) v075,
SAFE_CAST(v076 AS STRING) v076,
SAFE_CAST(v077 AS STRING) v077,
SAFE_CAST(v078 AS STRING) v078,
SAFE_CAST(v079 AS STRING) v079,
SAFE_CAST(v080 AS STRING) v080,
SAFE_CAST(v081 AS STRING) v081,
SAFE_CAST(v082 AS STRING) v082,
SAFE_CAST(v083 AS STRING) v083,
SAFE_CAST(v084 AS STRING) v084,
SAFE_CAST(v085 AS STRING) v085,
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
SAFE_CAST(v132 AS STRING) v132
from basedosdados-staging.br_ibge_censo2010_staging.pessoa_renda_setor_censitario as t
