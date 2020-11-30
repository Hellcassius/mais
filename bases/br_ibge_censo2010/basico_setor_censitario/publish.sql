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
SAFE_CAST(cod_grandes_regioes AS STRING) cod_grandes_regioes,
SAFE_CAST(nome_grande_regiao AS STRING) nome_grande_regiao,
SAFE_CAST(cod_uf AS STRING) cod_uf,
SAFE_CAST(nome_da_uf AS STRING) nome_da_uf,
SAFE_CAST(sigla_uf AS STRING) sigla_uf,
SAFE_CAST(cod_meso AS STRING) cod_meso,
SAFE_CAST(nome_da_meso AS STRING) nome_da_meso,
SAFE_CAST(cod_micro AS STRING) cod_micro,
SAFE_CAST(nome_da_micro AS STRING) nome_da_micro,
SAFE_CAST(cod_rm AS STRING) cod_rm,
SAFE_CAST(nome_da_rm AS STRING) nome_da_rm,
SAFE_CAST(cod_municipio AS STRING) cod_municipio,
SAFE_CAST(nome_do_municipio AS STRING) nome_do_municipio,
SAFE_CAST(cod_distrito AS STRING) cod_distrito,
SAFE_CAST(nome_do_distrito AS STRING) nome_do_distrito,
SAFE_CAST(cod_subdistrito AS STRING) cod_subdistrito,
SAFE_CAST(nome_do_subdistrito AS STRING) nome_do_subdistrito,
SAFE_CAST(cod_bairro AS STRING) cod_bairro,
SAFE_CAST(nome_do_bairro AS STRING) nome_do_bairro,
SAFE_CAST(situacao_setor AS STRING) situacao_setor,
SAFE_CAST(tipo_setor AS STRING) tipo_setor,
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
SAFE_CAST(v012 AS STRING) v012
from basedosdados-staging.br_ibge_censo2010_staging.basico_setor_censitario as t
