# GuardAI — análise do laboratório

Data: 10/11/2026. Revisão realizada pelo assistente nesta sessão, seguindo a especialização. Não é transcrição do Hermes.

## Escopo e autorização
Criação e teste deste laboratório solicitados pelo proprietário do projeto. SQLite em memória, dados sintéticos, sem rede ou sistemas de terceiros.

## Contexto e lacunas
O login existe como função Python para demonstrar um vetor, sem aplicação web exposta. Não há dados reais. Hermes não está instalado neste ambiente; a execução nesse harness não foi realizada. Não houve varredura de servidor.

## Evidência e causa
`lab/app.py`, linhas 5–6: os parâmetros username e password são interpolados na instrução SQL. A entrada `aluno' -- ` encerra o valor e comenta a verificação da senha. O retorno verdadeiro no teste demonstra bypass da autenticação sintética. A conta alvo e a tabela são criadas localmente em `lab/database.py`.

## Impacto, probabilidade e severidade
No laboratório, impacto 1: dados fictícios e nenhuma exposição externa. Probabilidade 1: ambiente isolado e acesso local controlado. Produto 1, severidade baixa na matriz didática adotada. A facilidade técnica está comprovada, mas não equivale à probabilidade de ataque externo neste ambiente. Em aplicação real exposta, o impacto pode ser relevante; faltam contexto e dados para atribuir nota. Esta classificação contextual não reduz a importância da fraqueza SQL Injection e não é CVSS.

## CWE e MITRE ATT&CK
A fraqueza corresponde a CWE-89. T1190 (Exploit Public-Facing Application) é associação condicional caso o vetor seja explorado em aplicação publicamente acessível para acesso inicial. Não se afirma que o laboratório offline demonstra uma intrusão dessa técnica.

Fontes oficiais consultadas em 10/11/2026:
- https://cwe.mitre.org/data/definitions/89.html
- https://attack.mitre.org/techniques/T1190/
- https://docs.python.org/3/library/sqlite3.html

## Correção e nova análise
`lab/app_secure.py`, linhas 5–6: placeholders `?` e parâmetros separados mantêm o texto fornecido como valores, sem alterar a estrutura SQL. Nenhuma entrada é interpolada na consulta corrigida. A inspeção e os testes confirmam mitigação dos bypasses cobertos.

## Validação observada
- `python3 -m lab.demo`: login válido aceito em ambas as versões, senha incorreta rejeitada e bypass aceito só na vulnerável.
- `python3 -m unittest discover -s tests -v`: oito testes aprovados, incluindo tautologia, comentário SQL, usuário com apóstrofo, campos vazios, usuário inexistente e texto destrutivo tratado como dado.
- Saídas integrais: `demo.txt` e `tests.txt` nesta pasta.

## Risco residual e próximo passo
Não é sistema de autenticação de produção. As senhas sintéticas em texto, ausência de limitação de tentativas, sessões e outras proteções devem ser substituídas ao projetar aplicação real. Os testes não certificam ausência de falhas. Próximo passo: reproduzir os cenários no Hermes configurado, conservar a saída real e revisar o comportamento de perguntas de contexto.
