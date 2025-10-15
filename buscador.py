import requests

def buscar_livros():
  
    print("--- Buscador de Livros da Google ---")


    API_URL = "https://www.googleapis.com/books/v1/volumes"
    

    termo_busca = input("Digite o título ou autor do livro que deseja buscar: ")
    

    if not termo_busca.strip():
        print("O termo de busca não pode estar vazio.")
        return


    parametros = {
        'q': termo_busca,
        'maxResults': 5
    }


    try:
        print(f"\nBuscando livros para '{termo_busca}'...")

        resposta = requests.get(API_URL, params=parametros)


        if resposta.status_code == 200:
        
            dados_json = resposta.json()
        else:
            print(f"Erro na requisição. Código de status: {resposta.status_code}")
            return 

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar à internet: {e}")
        return 


    if dados_json.get('totalItems', 0) > 0 and 'items' in dados_json:
        print("\n--- Resultados Encontrados ---")
        

        for i, item in enumerate(dados_json['items'], 1):
        
            info = item.get('volumeInfo', {})
            
       
            titulo = info.get('title', 'Título indisponível')
            autores = ", ".join(info.get('authors', ['Autor(es) indisponível(is)']))
            editora = info.get('publisher', 'Editora indisponível')
            

            print(f"\n{i}. Título: {titulo}")
            print(f"   Autor(es): {autores}")
            print(f"   Editora: {editora}")

    else:
        print("\nNenhum livro encontrado com o termo de busca.")

    print("\n--- Fim da Busca ---")

if __name__ == "__main__":
    buscar_livros()