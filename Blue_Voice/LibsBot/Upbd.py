import git
import pymysql
import time

def PullGit(caminho_repo,caminho_clone):

    try:
        git.Repo.clone_from(caminho_repo, caminho_clone)
        resposta='Repositório clonado para a máquina'
    except:
        g=git.cmd.Git(caminho_clone)
        g.pull()
    return caminho_clone
    
def PushGit(caminho_repo,caminho_clone):
    try:
        repo = git.Repo(caminho_clone)
        files = repo.git.diff(None, name_only=True)
        print(files)
        for f in files.split('\n'):
            caminho=caminho_clone + '\\' + f
            repo.git.add(caminho)
        repo.git.commit('-m','TDC', author='email usuário')
        repo.git.push()
        return 'Repositório atualizado. Em que mais posso ajudar?'
    except:
        return 'Repositório atualizado. Em que mais posso ajudar?'
    
    
def ApplyScript(caminho_script,nome_script, nome_banco):

	# Abrimos uma conexão com o banco de dados:
    conexao = pymysql.connect(db='NOME_BASE', user='root', passwd='senha')
    cursor = conexao.cursor()
    cursor.execute("Select schema_name from schemata where schema_name='" + nome_banco + "'")
    linha=cursor.fetchone()
    cursor.close
    arquivo=caminho_script + "\\" + nome_script
    if linha==None:
        with open(arquivo,'r') as abre_sql: 
            arq_sql=abre_sql.read()
            arq_quebrado=arq_sql.split('GO')
            for parte in arq_quebrado:
                if parte!='':
                    cursor.execute(parte)
    else:
        conexao.close
        conexao = pymysql.connect(db=nome_banco, user='usuario', passwd='senha')
        with open(arquivo,'r') as abre_sql: 
            arq_sql=abre_sql.read()
            arq_quebrado=arq_sql.split('GO')
            for parte in arq_quebrado:
                if parte!='':
                    cursor.execute(parte)
